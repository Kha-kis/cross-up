#!/bin/python3

import datetime
import logging
import os
import subprocess
import sys

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
)

# Load config from file
with open('config.cfg') as f:
    config = {}
    for line in f:
        if not line.strip().startswith('#') and '=' in line:
            key, val = line.strip().split('=', 1)
            config[key.strip()] = val.strip()

# Set up logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler('cross-up.log'))
logger.setLevel(logging.INFO)

# Print start message
logger.info(datetime.datetime.utcnow())
logger.info('')
logger.info('Starting L4G Upload Assistant for %s at filepath %s', sys.argv[3], sys.argv[1])
logger.info('')

if sys.argv[2] == config['cat']:
    try:
        # Run L4G Upload Assistant
        upload_cmd = [
            'python3',
            config['l4g'],
            sys.argv[1],
            '-ua',
            '-tk',
            config['trackers'],
            '--anon',
        ]
        logger.info('Running L4G Upload Assistant: %s', ' '.join(upload_cmd))
        upload_result = subprocess.run(upload_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        logger.info('L4G Upload Assistant output: %s', upload_result.stdout.decode('utf-8').strip())

        # Trigger cross-seed
        cs_cmd = [
            'curl',
            '--no-progress-meter',
            '-XPOST',
            config['csurl'],
            '--data-urlencode',
            'name=' + sys.argv[3],
        ]
        logger.info('Triggering cross-seed: %s', ' '.join(cs_cmd))
        cs_result = subprocess.run(cs_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        logger.info('Cross-seed output: %s', cs_result.stdout.decode('utf-8').strip())
    except subprocess.CalledProcessError as e:
        logger.error('Error running command: %s', e)
        print('Error running command:', e)
else:
    logger.error('Unknown error')
    print('Unknown error')
