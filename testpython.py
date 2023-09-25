#!/usr/bin/env python3

#import http.client as http_client
#http_client.HTTPConnection.debuglevel = 1

import os
import sys
import hcl
import glob
import json
import yaml
import hvac
from datetime import datetime
import requests
import inspect
import argparse
import tempfile
from pathlib import Path
from pprint import pprint
from string import Template

def arguments():
    parser = argparse.ArgumentParser(description='Vault operations')
    parser.add_argument('--namespace')
    parser.add_argument('--approle_mount', default='approle',
                        help='mount point used for approle, default: approle')
    parser.add_argument('--identity_mount', default='identity',
                        help='mount point used for identity, default: identity')
    parser.add_argument('--engine_name')
    parser.add_argument('--engine_type', help='[kv | ssh | aws]')
    parser.add_argument('--role_name')
    parser.add_argument('--policy_name')
    parser.add_argument('--username')
    parser.add_argument('--role_id')
    parser.add_argument('--secret_id')
    parser.add_argument('--ssh_public_key_path')
    parser.add_argument('--scope')
    parser.add_argument('--group_name')
    parser.add_argument('--child_namespace')
    parser.add_argument('--template')
    args = parser.parse_args()

    return vars(args)


if __name__ == '__main__':
    args = arguments()
    sys.exit(0)