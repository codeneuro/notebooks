# notebooks

[![Join the chat at https://gitter.im/CodeNeuro/notebooks](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/CodeNeuro/notebooks?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

Interactive notebooks for trying analyses and exploring datasets

## How it works

We're using the [tmpnb](http://github.com/jupyter/tmpnb) service to launch docker containers on demand. Each user who launches from [notebooks.codeneuro.org](http://notebooks.codeneuro.org) gets their own temporary interactive environment, preloaded with a variety of executable notebooks. The environments will be deleted after an hour of inactivity, so *this is not intended for real work!* But it is a great way to experiment with new tools and explore data sets. And [public data repositories](http://datasets.codeneuro.org) can link directly to these notebooks, making this a great way to interactively examine public data sets.

## How to deploy

We deploy this infrastructure on Amazon Web Services, but using other environments should be easy as well. To deploy on AWS, we deploy a master service on a single instance and worker services on additional instances. The master runs the Apache web server and the load balancer (based on [tmpnb-redirector](http://github.com/jupyter/tmpnb-redirector), while the workers each run an instance of [tmpnb](http://github.com/jupyter/tmpnb).  

### General 
```
git clone http://github.com/codeneuro/notebooks
cd notebooks
```

### Master-specific

In the master directory, first run the setup scripts
```
cd master
make setup 
```

Deploy the Apache web server and start the `screen`ed `redirector.py` process: 
```
make deploy
```

### Worker-specific

In the worker directory, first run the setup scripts and edit `conf.yml`: 
```
cd worker
make setup 
```
Each worker contains a `conf.yml` file which specifies: 
* The hostname of the master node 
* The port on the master node that handles registration commands (typically 9001) 
* The hostname of the worker (so that the redirector redirects to readable URLs) 
* The port of the worker's main tmpnb service (typically 8000)

To deploy the worker, run 
```
make launch 
```


We deploy this infrastructure on Amazon Web Services, but using other environments should be easy as well. To deploy on AWS, create an EC2 instance, and make sure ports 80, 8000, and 43 are open. Then ssh into the instance and run:

```
git clone http://github.com/codeneuro/notebooks
```
```
cd notebooks
make setup
make launch
```

If you want to build your own version, start with this repo and just modify the website content and docker images accordingly. We will work on simpler strategies for customization in the future.

## The docker images

This repo contains images for `codeneuro/base` and [`codeneuro/notebooks`](https://registry.hub.docker.com/u/codeneuro/notebooks/). The base image is based on [`jupyter/minimal`](https://github.com/jupyter/docker-demo-images/tree/master/common), and the notebooks image sets up a custom scientific computing environment with local versions of tools like [Spark](http://spark.apache.org) and [Thunder](http://thunder-project.org).
