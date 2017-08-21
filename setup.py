#!/usr/bin/env python3

from setuptools import setup, find_packages

setup(name='stormbot-role',
      version='1.2',
      description='role plugin for stormbot',
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://git.paulfariello.fr/Stormbot/stormbot-role',
      packages=find_packages(),
      install_requires=['stormbot', 'isodate'],
      entry_points={'stormbot.plugins': ['role = stormbot_role:VolunteerPicker']},
      classifiers=['Environment :: Console',
                   'Intended Audience :: System Administrators',
                   'Operating System :: POSIX',
                   'Programming Language :: Python'])
