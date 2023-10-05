#!/usr/bin/python3
'''a Fabric script that distributes an archive to your web servers'''
from fabric.api import env, put, run, sudo
from os.path import exists, basename, splitext
# Define the remote servers
env.hosts = ['52.86.164.135', '100.25.0.108']


def do_deploy(archive_path):
    '''distributes an archive to your web servers'''

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
