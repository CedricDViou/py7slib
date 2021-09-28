import os
import glob
from setuptools import setup, find_packages

packages = find_packages()

# Also want to replicate what install.sh is doing as a separate install script.
#  The module wr_len.py and the script hera_wr_redis_monitor.py moved to node_control.

setup_args = dict(name="py7slib",
                  maintainer="HERA Team",
                  description="Library for interfacing to Seven Solutions libraries",
                  url="https://github.com/HERA-Team/py7slib",
                  use_scm_version=True,
                  setup_requires=["setuptools_scm"],
                  install_requires=["redis"],
                  packages=packages,
                  package_data={'py7slib': [so.lstrip('py7slib') for so in glob.glob('py7slib/lib/*')]},
                  )
