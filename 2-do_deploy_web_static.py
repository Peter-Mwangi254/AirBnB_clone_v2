#!/usr/bin/python3
"""Distributes an archive to your web servers, using the function do_deploy
"""

from os import path
from fabric.api import put, env, run, task


env.hosts = ['100.26.49.195', '54.152.70.222']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


@task
def do_deploy(archive_path):
    """Distributes an archive to your web servers,
    using the function do_deploy
    """
    try:
        if (path.exists(archive_path)):
            archive = archive_path.split('/')[1]
            arch_path = "/tmp/{}".format(archive)
            folder = archive.split('.')[0]
            f_path = "/data/web_static/releases/{}/".format(folder)

        put(archive_path, arch_path)
        run("mkdir -p {}".format(f_path))
        run("tar -xzf {} -C {}".format(arch_path, f_path))
        run("rm {}".format(arch_path))
        run("mv -f {}web_static/* {}".format(f_path, f_path))
        run("rm -rf {}web_static".format(f_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(f_path))
        print("New version deployed!")
        return True
    except FileNotFoundError:
        return False
