import os
import sys
import subprocess
from os import name, system

#! UNSTABLE! MIGHT DELETE YOUR USER ENVIRONMENT VARIABLES! BACK THEM UP BEFORE USE!

if not sys.argv[1]:
	pass
else:
	addPath = sys.argv[1]


if name == "nt":
	os.system("cargo build --release")
	os.rename("./target/release/ae-plus-plus.exe", "./aepp.exe")

	subprocess.run(["powershell", "-Command", "Copy-Item .\\aepp.exe \"C:\\Users\\$env:USERNAME\"; Write-Host \"File moved to C:\\Users\\$env:USERNAME\" -f Green"])

	if addPath == "-addpath":
		subprocess.run(["powershell", "-Command", "[Environment]::SetEnvironmentvariable(\"Path\", \";C:\\Users\\$env:USERNAME\\aepp.exe\", \"User\"); Write-Host \"Program added to PATH\" -f DarkRed"])
else:
	# Add support for Linux and MacOS later
	os.system("")
