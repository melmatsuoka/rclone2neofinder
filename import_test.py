#!/usr/bin/env python3

# https://blog.finxter.com/how-to-import-external-code-in-python/
# https://www.mygreatlearning.com/blog/python-init/

import rclone_cmds 

print(rclone_cmds.run_cmd("s3", "melmatsuoka"))
