#!/bin/sh
service cron start
chmod +x clean.sh 
(crontab -l ; echo "*/5 * * * * /usr/src/pdfexport/clean.sh >/devnull 2>&1") | crontab - 
python index.py