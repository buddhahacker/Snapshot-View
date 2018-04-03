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

' pipenv run "python Valhalla/valhalla.py <command> <--project=PROJECT>"'

*command* is list, start, or stop
*project* is optional
