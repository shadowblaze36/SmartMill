#!/bin/bash
cd /etc/cron.d/
chmod -R 755 tarea1
chmod -R 755 tarea2
cd /etc/init.d/
./cron restart
