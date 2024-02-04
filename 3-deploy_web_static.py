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


def deploy():
    """Deploys web static
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    success = do_deploy(archive_path)
    return success
