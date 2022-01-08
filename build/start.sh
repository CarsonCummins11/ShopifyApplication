#!/usr/bin/env bash
systemctl enable --now mongod

chmod a+rwx /srv

cd /srv/flask_app

service nginx start
uwsgi --touch-reload=build/uwsgi.ini --enable-threads --ini build/uwsgi.ini