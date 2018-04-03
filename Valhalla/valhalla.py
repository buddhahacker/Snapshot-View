import boto3
import click   #this installs the click module

session = boto3.Session(profile_name='Valhalla')
ec2 = session.resource('ec2')

@click.command()
def list_instance():
    "List EC2 instances"
    for i in ec2.instances.all():
        print (','.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return


if __name__ == '__main__':
    list_instance()
