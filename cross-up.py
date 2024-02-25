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

# Get the directory of the current script
script_dir = os.path.dirname(os.path.realpath(__file__))

# Construct the path to the config file
config_file_path = os.path.join(script_dir, 'config.cfg')

# Load config from file
with open(config_file_path) as f:
    config = {}
    for line in f:
        if not line.strip().startswith('#') and '=' in line:
            key, val = line.strip().split('=', 1)
            config[key.strip()] = val.strip()

# Set up logger
logger = logging.getLogger(__name__)
logger.addHandler(logging.FileHandler(os.path.join(script_dir, 'cross-up.log')))
logger.setLevel(logging.INFO)

# Print start message
logger.info(datetime.datetime.utcnow())
logger.info('')
logger.info('Starting L4G Upload Assistant for %s at filepath %s', sys.argv[3], sys.argv[1])
logger.info('')

baseupload_cmd = ['python3', os.path.join(script_dir, config['l4g']), sys.argv[1], '-ua', '-tk', config['trackers']]

# Inside the conditional block for handling the upload
if config['torrent_client'] == 'qbittorrent':
    if sys.argv[2] == config['cat']:
        try:
            # Run L4G Upload Assistant when sys.argv[2] matches config['cat']
            upload_cmd = baseupload_cmd + [config['upload_args']]
            logger.info('Running L4G Upload Assistant for qBittorrent: %s', ' '.join(upload_cmd))
            upload_result = subprocess.run(upload_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            logger.info('L4G Upload Assistant output: %s', upload_result.stdout.decode('utf-8').strip())
        except subprocess.CalledProcessError as e:
            logger.error('Error running command: %s', e)
            print('Error running command:', e)
    else:
        logger.error('Unknown error')
        print('Unknown error')
elif config['torrent_client'] == 'rtorrent':
    if sys.argv[2] == config['label']:
        try:
            # Run L4G Upload Assistant when sys.argv[2] matches config['label']
            upload_cmd = baseupload_cmd + [config['upload_args']]
            logger.info('Running L4G Upload Assistant for rTorrent: %s', ' '.join(upload_cmd))
            upload_result = subprocess.run(upload_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            logger.info('L4G Upload Assistant output: %s', upload_result.stdout.decode('utf-8').strip())
        except subprocess.CalledProcessError as e:
            logger.error('Error running command: %s', e)
            print('Error running command:', e)
    else:
        logger.error('Unknown error')
        print('Unknown error')
else:
    logger.error('Unknown torrent client specified in config')
    print('Unknown torrent client specified in config')

# Trigger cross-seed (outside of the if block)
cs_cmd = [
    'curl',
    '--no-progress-meter',
    '-XPOST',
    config['csurl'],
    '--data-urlencode',
    'infoHash=' + sys.argv[3],
]
logger.info('Triggering cross-seed: %s', ' '.join(cs_cmd))
cs_result = subprocess.run(cs_cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
logger.info('Cross-seed output: %s', cs_result.stdout.decode('utf-8').strip())
