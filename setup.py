# Copyright 2009 Shikhar Bhushan
# Copyright 2011 Leonidas Poulopoulos
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(name='ncclient',
      version='0.1a',
      description="Python library for NETCONF clients",
      author="Shikhar Bhushan, Leonidas Poulopoulos, Ebben Aries",
      author_email="shikhar@schmizz.net, leopoul@noc.grnet.gr, earies@juniper.net",
      url="http://schmizz.net/ncclient/",
      packages=[
          "ncclient",
          "ncclient/transport",
          "ncclient/operations",
          "ncclient/operations/third_party",
          "ncclient/operations/third_party/juniper"],
      install_requires=[
          "Paramiko > 1.7",
          "lxml > 3.0"],
      license="Apache License 2.0",
      platforms=["Posix; OS X; Windows"],
      #classifiers=[]
      )
