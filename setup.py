# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2017 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from setuptools import setup, find_packages

import risks_mgmt
import os

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if on_rtd:
    shapely_dep = "Shapely<1.5.13"
else:
    shapely_dep = "Shapely>=1.5.13"

with open('README.md') as f:
    readme = f.read()

setup(
    name='geonode-risk_management_tools',
    version='.'.join(str(i) for i in risks_mgmt.__version__),
    description='geonode-risk_management_tools is a GeoNode Extension built by WorldBanck GFDRR '
                'which adds the capability of extracting and managing '
                'Hazard Risks on geographical areas.',
    long_description=readme,
    author='Alessio Fabiani',
    author_email='alessio.fabiani@geo-solutions.it',
    maintainer='geonode-risk_management_tools contributors and GeoSolutions S.A.S. (http://www.geo-solutions.it)',
    url='https://github.com/GeoNode/geonode-risk_management_tools',
    # see MANIFEST for packaging exclusions
    packages=find_packages('.'),
    license='GPLv3+',
    classifiers=[
        'Development Status :: 0.1',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later'
        ' (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Framework :: Django :: 1.8',
    ],
    install_requires=[
        'django-tastypie>=0.12.2,<0.14',
        'python-dateutil>=2.5.3,<2.7',
        'numpy>=1.11.2,<1.12',
        'geonode>=2.5.9,<2.6',
        'Django>=1.8,<1.9',
    ],
    include_package_data=True,
    zip_safe=False,
)
