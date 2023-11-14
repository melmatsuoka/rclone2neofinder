# rclone2neofinder
Dumps a recursive listing of an [rclone](https://rclone.org) remote, and converts it to a YoYotta CSV file that can be imported into [NeoFinder](https://cdfinder.de). 

This allows you to store offline indexes of your rclone remotes in a searchable NeoFinder database!

This script assumes that you have already configured an rclone remote on your system.

## Usage

```
rclone2neofinder --remote rclone_remote_name --bucket remote_bucket_name
```

## Importing info NeoFinder

The resulting Yoyotta CSV file can then be imported into NeoFinder, via the _File/Import Catalogs…_ menu, then selecting "Yoyotta CSV text file" as the catalog format.

![neofinder1](https://github.com/melmatsuoka/rclone2neofinder/assets/3419536/bedb3006-bbb2-4165-98bf-65f49f6f5e3b)
![neofinder2](https://github.com/melmatsuoka/rclone2neofinder/assets/3419536/3027874d-a8a8-41ba-a059-9350c71c2304)

The CSV will be imported into NeoFinder using the name of the bucket as the catalog name. From there, you can move it into a NeoFinder folder, if desired.

![neofinder3](https://github.com/melmatsuoka/rclone2neofinder/assets/3419536/8f57a6ab-3a3c-4278-aee9-61f0d2e818a2)




