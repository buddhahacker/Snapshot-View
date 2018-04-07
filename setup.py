from setuptools import setup

setup(
    name='Valhalla',
    version='0.1',
    author="Buddhahacker",
    author_email="buddhahacker@outlook.com",
    description="Valhalla is a majestic hall containing tools to manage your AWS EC2 snapshots",
    license="GPLv3+",
    packages=['valhalla'],
    url="https://github.com/buddhahacker/Snapshot-View",
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        valhalla=valhalla.valhalla:cli
    ''',



)
