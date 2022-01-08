#docker commands that allow us to test the docker system rapidly, notice that it sets the container to always restart to ensure
#that the server doesn't just stop if the system is randomly restarted
#basically here we stop a running container (expect but ignore an error message if one is not currently running)
#then we remove said container (again expect an error if there is not one to remove)
#we then rebuild the image and run it with a bind mount to the directory with our code so we can hot edit code in production
docker container stop inventory_container
docker rm inventory_container --force
docker build . -t inventory_image
docker run --name inventory_container -p 80:80 --mount type=bind,source="$(pwd)"/..,target=/srv/flask_app --restart always inventory_image