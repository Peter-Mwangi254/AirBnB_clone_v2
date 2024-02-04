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
        if not (path.exists(archive_path)):
            return False

        # upload archive
        put(archive_path, '/tmp/')

        # create target dir
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/\
releases/web_static_{}/'.format(timestamp))

        # uncompress archive and delete .tgz
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/'
            .format(timestamp, timestamp))

        # remove archive
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # remove extraneous web_static dir
        run('sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static'
            .format(timestamp))

        # delete pre-existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # re-establish symbolic link
        run(' ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current'.format(timestamp))
    except FileNotFoundError:
        return False

    # return True on success
    return True
