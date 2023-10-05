#!/usr/bin/python3
from fabric.api import env, put, run, local
from os.path import exists, basename, splitext
from datetime import datetime
# full deploy
env.hosts = ['100.25.188.65', '34.204.61.68']


def do_pack():
    """
    Compress the contents of the web_static folder into a .tgz archive.
    """

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    archive_name = "web_static_" + timestamp + ".tgz"
    local("mkdir -p versions")
    result = local("tar -czvf versions/{} web_static".format(archive_name))
    if result.return_code == 0:
        return "versions/{}".format(archive_name)
    else:
        return None


def do_deploy(archive_path):
    """
    Deploy the archive to the web servers.
    """
    if not exists(archive_path):
        return False

    try:
        filename = splitext(basename(archive_path))[0]
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'.format(filename))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.
            format(filename + '.tgz', filename))
        run('rm /tmp/{}'.format(filename + '.tgz'))
        run('mv /data/web_static/releases/{}/web_static/* '
            '/data/web_static/releases/{}/'.format(filename, filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        run('rm -rf /data/web_static/current')
        run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.
            format(filename))
        return True

    except Exception as e:
        print(e)
        return False


def deploy():
    """ creates and distributes an archive to your web servers
    """
    new_archive_path = do_pack()
    if exists(new_archive_path) is False:
        return False
    result = do_deploy(new_archive_path)
    return result
