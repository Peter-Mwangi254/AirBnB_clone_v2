#!/usr/bin/python3
"""A Fabric script (based on the file 2-do_deploy_web_static.py) that
creates and distributes an archive to your web servers
"""

from os import path
from datetime import datetime
from fabric.api import put, env, run, local


env.hosts = ['100.26.49.195', '54.152.70.222']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """Generates a .tgz archive from the contents of
    the web_static folder
    """
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = 'versions/web_static_' + timestamp + '.tgz'

    # create the versions folder if it doesn't exist
    local("mkdir -p versions")

    # create the .tgz archive
    result = local(f"tar -cvzf {archive_path} web_static/")

    if result.succeeded:
        return archive_path
    return None


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


def deploy():
    """Deploys web static
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success
