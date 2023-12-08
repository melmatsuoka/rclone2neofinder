# rclone2neofinder
Dumps a recursive listing of an [rclone](https://rclone.org) remote, and converts it to a YoYotta CSV file that can be imported into [NeoFinder](https://cdfinder.de). 

This allows you to store offline indexes of your rclone remotes in a searchable NeoFinder database!

This script assumes that you have already configured an rclone remote on your system.

Currently the script only supports Google Drive, Amazon S3 and Dropbox as remotes. But you can add your own remotes in the `rclone_cmds.py` file, modifying the rclone commands where appropriate.

## Usage Notes

```
rclone2neofinder -r remote -b bucket

-r/--remote: (required) Rclone remote name (as it appears in your 'rclone config' list).
-b/--bucket: (optional) Name of remote bucket, if applicable.
```
If your remote doesn't reference any buckets, the rclone remote name will be used as the Volume/catalog name that appears when you import the converted CSV into NeoFinder. Otherwise, the bucket name will be used as the Volume name.

A caveat to using rclone to retrieve remote directory listings is that some cloud storage providers don't support the `--fast-list` (ListR) feature, which can cause file listings to seemingly take _forever_ if you're indexing a remote that has a lot of files in it (e.g. Dropbox). 

Please reference rclone's [list of supported cloud providers](https://rclone.org/overview/#optional-features) to check if your provider supports `--fast-list` (ListR).

## Importing into NeoFinder

The resulting Yoyotta CSV file can then be imported into NeoFinder, via the _File/Import Catalogs…_ menu, then selecting "Yoyotta CSV text file" as the catalog format.

![neofinder1](https://github.com/melmatsuoka/rclone2neofinder/assets/3419536/bedb3006-bbb2-4165-98bf-65f49f6f5e3b)
![neofinder2](https://github.com/melmatsuoka/rclone2neofinder/assets/3419536/3027874d-a8a8-41ba-a059-9350c71c2304)

The CSV will be imported into NeoFinder using the name of the bucket (or remote) as the catalog name. From there, you can move it into a NeoFinder folder, if desired.

![neofinder-bucketlist](https://github.com/melmatsuoka/rclone2neofinder/assets/3419536/a3cf281b-6495-403a-b08f-d5830d25edb7)





