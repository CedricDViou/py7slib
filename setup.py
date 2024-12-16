from setuptools import setup, find_packages

setup(
    name='py7slib_py3',
    version='0.0.1',
    description='Python3 version of py7slib',
    author='Cedric Viou',
    packages=find_packages(
        include=['py7slib_py3', 'py7slib_py3.*'],
        exclude=['tests*']),
    include_package_data=True,
    package_data={
        'py7slib_py3.data': ['*.so.*', 'eb-discover_*'],
    },
    python_requires='>=3.6',
    install_requires=[
        'serial',
    ],
    entry_points={
        'console_scripts': [
            'eb_sw_loader=py7slib_py3.eb_sw_loader:main',
            'sdb_tool=py7slib_py3.sdb_tool:main',
            'shell=py7slib_py3.shell:main',
            'spiflash_update=py7slib_py3.spiflash_update:main',
            'write_calibration=py7slib_py3.write_calibration:main',
        ],
    },
)
