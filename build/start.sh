#!/usr/bin/env bash

#start the mongodb service
systemctl enable --now mongod

#make everything editable
chmod a+rwx /srv

#lets get the app up and goind
cd /srv/flask_app

service nginx start

#notice the touch-reload arg so that we can hot reload the backend
uwsgi --touch-reload=build/uwsgi.ini --enable-threads --ini build/uwsgi.ini