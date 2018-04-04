# Snapshot-View
A snapshot of current AWS EC2 instances

## About

This project is a demo, and uses boto3 to manage
AWS EC2 instance snapshots.

## Configuring

valhalla uses the configuration file created by the
AWS cli. e.g.

'aws configure --profile Valhalla'

## Running

' pipenv run "python Valhalla/valhalla.py <command> <subcommand> <--project=PROJECT>"'

*command* is instances, volumes, or snapshots
*subcommand* - depends on command
*instances* - list, stop or start
*volumes* - list
*snapshots* - list and create  

*project* is optional
