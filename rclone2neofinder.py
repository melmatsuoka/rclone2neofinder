#!/usr/bin/env python3

""" 
rclone2neofinder

Dumps a recursive listing of an rclone remote to a CSV file, then converts it to a Yoyotta CSV for importing into NeoFinder.

"""

__author__ = "Mel Matsuoka"
__contact__ = "mel@postproductive.tv"
__copyright__ = "Copyright 2023, Melvin H Matsuoka"
__date__ = "2023/11/13"
__license__ = "MIT"
__version__ = "1.0.0"

import os
import argparse
import subprocess
import csv

parser = argparse.ArgumentParser(
					prog='rclone2neofinder',
					description='Dumps a recursive listing of an S3 rclone remote to a CSV file, then converts it to a Yoyotta CSV for importing into NeoFinder')
parser.add_argument('-r', '--remote', type=str, required=True, help="The name of your rclone remote")
parser.add_argument('-b', '--bucket', type=str, required=True, help="Name of remote S3 bucket")
args = parser.parse_args()

rclone_remote = args.remote
s3_bucket = args.bucket
 
rclone_csv = s3_bucket + '_rclone' + '.csv'
new_csv = s3_bucket + '_yoyotta.csv'

# Dump csv listing of rclone remote

with open (rclone_csv,'w') as fd:
	subprocess.run(['rclone', 'lsf', '-R', '--csv', '--absolute', '--format', 'ps', '--fast-list', '--exclude', '.DS_Store', rclone_remote + ':/' + s3_bucket], stdout=fd)
  
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
			writer.writerow([s3_bucket, base_path, str(file_name), file_size])
		
		line_count += 1

print("\nConversion complete! Import the \"" + new_csv + "\" file into NeoFinder via the \"Import Catalogs…\" menu, using \"Yoyotta CSV text file\" as the Format.")
