#! /usr/bin/env python2.6
# -*- coding: utf-8 -*-


__author__ = 'Justin Bayer, bayer.justin@googlemail.com'


from setuptools import setup, find_packages


setup(
    name="chopmunk",
    version="pre-0.1",
    author="Justin Bayer",
    author_email="bayer.justin@googlemail.com",
    description="minimalist python logging",
    license="BSD",
    keywords="Log logging",
    packages=find_packages(exclude=['examples', 'docs']),
    include_package_data=True,
)

