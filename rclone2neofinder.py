#!/usr/bin/env python3

""" 
rclone2neofinder

Dumps a recursive listing of an rclone remote to a CSV file, then converts it to a Yoyotta CSV for importing into NeoFinder.

"""

__author__ = "Mel Matsuoka"
__contact__ = "mel@postproductive.tv"
__copyright__ = "Copyright 2023, Melvin H Matsuoka"
__date__ = "2023/11/14"
__license__ = "MIT"
__version__ = "1.1.0"

import os
import argparse
import csv
import rclone_cmds 

parser = argparse.ArgumentParser(
			prog='rclone2neofinder',
			description='Dumps a recursive listing of an S3 rclone remote to a CSV file, then converts it to a Yoyotta CSV for importing into NeoFinder')
parser.add_argument('-r', '--remote', type=str, required=True, help="The name of your rclone remote")
parser.add_argument('-b', '--bucket', type=str, required=False, help="Name of remote S3 bucket")
args = parser.parse_args()

rclone_remote = args.remote
remote_bucket = args.bucket

# Build CSV filenames. Uses join() & filter() to avoid redundant underscores in filenames if 'remote_bucket' arg is null

rclone_csv = '_'.join(filter(None, [rclone_remote, remote_bucket, 'rclone'])) + '.csv'
new_csv = '_'.join(filter(None, [rclone_remote, remote_bucket, 'yoyotta'])) + '.csv'

# Dump csv listing of rclone remote
 
with open (rclone_csv,'w') as fd:
	rclone_cmds.run_cmd(fd, rclone_remote, remote_bucket)
  
# Write column headers to Yoyotta CSV

fields = ['Media', 'Path', 'Name', 'Size']

with open(new_csv, 'w', newline='') as file: 
	writer = csv.DictWriter(file, fieldnames = fields)	
	writer.writeheader() 

# Convert rclone CSV to Yoyotta compatible CSV format
	
with open(rclone_csv, 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter=',')
	line_count = 0

	for line in csv_reader:
		file_path = line[0]
		file_path_dequoted = file_path.strip('"').rsplit('/', 1)
		base_path = file_path_dequoted[0]
		file_name = file_path_dequoted[1]
		file_size = line[1]
		
		with open(new_csv, 'a', newline='') as file: 
			writer = csv.writer(file) 
			if remote_bucket:				
				writer.writerow([remote_bucket, base_path, str(file_name), file_size])
			else:
				# Make the "Media" data the same name as the rclone remote name if no bucket is defined (e.g. Dropbox)
				writer.writerow([rclone_remote, base_path, str(file_name), file_size])
			line_count += 1

print("\nConversion complete! Import the \"" + new_csv + "\" file into NeoFinder via the \"Import Catalogs…\" menu, using \"Yoyotta CSV text file\" as the Format.")
