Hi! This is my solution to the Shopify technical challenge for backend/infrastructure developers.
It runs using python (Flask) and mongodb. The easiest way to get it up and running for your system will be to use the docker
stuff that I set up for you in the build folder. There, there is a script (rebuild_restart.sh) that will set up and run the docker container
for you. Then, just navigate to localhost, and the site should be there for you!

If you don't have docker on your machine, you can install it and set it up by following the instructions on docker.com, or you can install
python3 on your machine (find it at python.org). After this, follow the instructions at https://docs.mongodb.com/manual/installation/#std-label-tutorial-installation
to install mongodb on your machine. Finally, using pip install both flask and pymongo, and you will be good to go. Simply navigate to the top level
directory of this project and run the command "python3 -m flask run" (although the command you use to invoke python may change depending on your setup).

The controls for the app itself are fairly self explanatory. The one thing I will point out is the paging, simply click the links at the bottom to navigate to that page
just like any other site with pagin implemented. 

Thanks so much for taking the time to look this over. I'm super excited to work at Shopify and I hope to get the chance!