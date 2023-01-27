import os
import sys
import subprocess
from os import name, system

cmd = "Copy-Item .\\aepp.exe \"C:\\Users\\$env:USERNAME\";"
cmd2 = "$env:Path += \";C:\\Users\\env:USERNAME\\.\\aepp.exe\""

if name == "nt":
	os.system("cargo build --release")
	os.rename("./target/release/ae-plus-plus.exe", "./aepp.exe")
	completed = subprocess.run(["powershell", "-Command", cmd])
	if sys.argv[1] == "-addpath":
		completed = subprocess.run(["powershell", "-Command", cmd2])
else:
	# ggdfgfdg
	os.system("")
