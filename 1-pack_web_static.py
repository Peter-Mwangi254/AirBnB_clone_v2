#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of
the web_static folder
"""
from datetime import datetime
from fabric.api import *


@task
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
    else:
        return None
