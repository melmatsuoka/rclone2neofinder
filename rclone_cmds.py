# rclone_cmds.py
# Created by Mel on 11/14/23.

import subprocess

def run_cmd(fd, remote, bucket=None):
	match remote:
		case "dropbox":
			return run_dropbox(fd, remote)
		case "s3":
			run_s3(fd, remote, bucket)
		case _:
			return "Unknown remote type."


def run_dropbox(fd, remote):
	return "Remote is " + remote

def run_s3(fd, remote, bucket):
	#return "Remote is " + remote + ", Bucketname is " + bucket
	subprocess.run(['rclone', 'lsf', '-R', '--csv', '--absolute', '--format', 'ps', '--fast-list', '--exclude', '.DS_Store', remote + ':/' + bucket], stdout=fd)

