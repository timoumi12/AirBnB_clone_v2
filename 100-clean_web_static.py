#!/usr/bin/python3
'''a Fabric script deletes out-of-date archives, using the function do_clean'''
from fabric.api import env, put, run, local
import os
from datetime import datetime
env.hosts = ['52.86.164.135', '100.25.0.108']
env.user = 'ubuntu'


def do_clean(number=0):
    '''deletes out-of-date archives'''

    number = int(number)
    if number == 0 or number == 1:
        number = 2
    else:
        number += 1

    local('cd versions; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {}; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
