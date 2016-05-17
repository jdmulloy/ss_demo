#!/bin/sh

. ./aws_keys

ansible-playbook -i ./ec2.py -u centos playbook.yml $@
