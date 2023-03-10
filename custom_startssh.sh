#!/bin/bash

/usr/bin/autossh -M 10000 -NT -R 2023:localhost:22 sysadmin@unraid.wickedtribe.org -p 8336
