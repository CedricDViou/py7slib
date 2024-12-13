from setuptools import setup, find_packages

setup(
    name='py7slib-py3',
    version='0.0.1',
    description='Python3 version of py7slib',
    author='Cedric Viou',
    packages=find_packages(exclude=['tests*']),
    package_dir={'': 'src'},
    python_requires='>=3.6',
    install_requires=[
        'serial',
    ],
    entry_points={
        'console_scripts': [
            'eb_sw_loader=py7slib-py3.eb_sw_loader:main',
            'sdb_tool=py7slib-py3.sdb_tool:main',
            'shell=py7slib-py3.shell:main',
            'spiflash_update=py7slib-py3.spiflash_update:main',
            'write_calibration=py7slib-py3.write_calibration:main',
        ],
    },
)
