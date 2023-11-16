""" 
rclone_cmds



"""

__author__ = "Mel Matsuoka"
__contact__ = "mel@postproductive.tv"
__copyright__ = "Copyright 2023, Melvin H Matsuoka"
__date__ = "2023/11/14"
__license__ = "MIT"
__version__ = "1.0.0"

import configparser
import subprocess

def remote_type(remote):
    # Retrieve the rclone remote "type" from rclone config
	rclone_config = subprocess.run(['rclone', 'config', 'show', remote], capture_output=True).stdout.decode()
	config = configparser.ConfigParser()
	config.read_string(rclone_config)
	return config[remote]['type']

def run_cmd(fd, remote, bucket=None):
	match remote_type(remote):
		case "drive":
			run_gdrive(fd, remote, bucket)
		case "dropbox":
			run_dropbox(fd, remote)
		case "s3":
			run_s3(fd, remote, bucket)
		case _:
			return "Unknown remote type."

def run_dropbox(fd, remote):
    # Dropbox
    # Note: Requires a --tpslimit of 12 to avoid rate-limiting errors, and recursive Dropbox listings take a bloody long time!
	subprocess.run(['rclone', 'lsf', '-R', '--csv', '--absolute', '--format', 'ps', '--files-only', '--fast-list', '--exclude', '.DS_Store', '--tpslimit', '12', remote + ':/'], stdout=fd)

def run_gdrive(fd, remote, bucket):
    # Google Drive
	subprocess.run(['rclone', 'lsf', '-R', '--csv', '--absolute', '--format', 'ps', '--files-only', '--fast-list', '--exclude', '.DS_Store', remote + ':/'], stdout=fd)

def run_s3(fd, remote, bucket):
    # Amazon S3
	subprocess.run(['rclone', 'lsf', '-R', '--csv', '--absolute', '--format', 'ps', '--files-only', '--fast-list', '--exclude', '.DS_Store', remote + ':/' + bucket], stdout=fd)

