docker container stop inventory_container
docker rm inventory_container --force
docker build . -t inventory_image
docker run --name inventory_container -p 80:80 --mount type=bind,source="$(pwd)"/..,target=/srv/flask_app --restart always inventory_image