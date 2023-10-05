#!/usr/bin/python3
'''a Fabric script that generates a .tgz archive'''
from fabric.api import local
from datetime import datetime


def do_pack():
    '''a .tgz archive from the web_static folder of your repo'''

    _date = datetime.now()
    date = _date.strftime("%Y%m%d%H%M%S")
    _file = f"web_static_{date}.tgz"
    local('mkdir -p versions')
    res = local(f"tar czf versions/{_file} web_static")
    if res.return_code == 0:
        return f"versions/{_file}"
    else:
        return None
