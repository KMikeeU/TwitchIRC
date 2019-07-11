#!/usr/bin/env python

from distutils.core import setup

setup(name='TwitchIRC',
      version='1.0',
      description='Python module for connecting and interacting with Twitch Chat',
      author='KMikeeU',
      author_email='mikeeu@pm.me',
      url='https://github.com/KMikeeU/TwitchIRC',
      packages=['TwitchIRC'],
      install_requires=["re", "socket", "ssl", "_thread"]
     )