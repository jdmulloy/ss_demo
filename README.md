# ss_demo
Automated AWS VM to give user IP

# Dependencies
1. epel
2. ansible
3. python2-boto

# SSH Source IP
You will need to change the SSH source IP in the ingresshome object to be the
external IP of the machine running ansible. This is to prevent anyone else from
accessing the SSH port.

# AWS Credentials
You will need to put your AWS credentials in the file aws_key. You can copy the
aws_key.example file

# Keypair
The default keypair name is centos. If your keypair name is different you must change it in the cloud formation template located at files/cf.json.

# Running Ansible

You will need to run the script ./run_ansible.sh twice or more. The first pass
sets up the AWS instance. You will then need to run it again when the instance
is up to configure the instance. If the instance is not accessible via ssh yet
when you rerun the script you will need to run it again, until it works.

# Sources #
## Ansible EC2 Dynamic Inventory ##
* http://docs.ansible.com/ansible/intro_dynamic_inventory.html#example-aws-ec2-external-inventory-script
* https://raw.github.com/ansible/ansible/devel/contrib/inventory/ec2.py
* https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.ini
