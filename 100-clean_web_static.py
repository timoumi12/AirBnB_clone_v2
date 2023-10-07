#!/usr/bin/python3
'''a Fabric script deletes out-of-date archives, using the function do_clean'''
from fabric.api import env, put, run, local
from os.path import exists, basename, splitext
from datetime import datetime
env.hosts = ['52.86.164.135', '100.25.0.108']


def do_clean(number=0):
    # deletes out-of-date archives

    if int(number) == 0 or int(number) == 1:
        run('ls -t | tail -n +2 | xargs rm')
    else:
        run(f'ls -t | tail -n +{number + 1} | xargs rm')
