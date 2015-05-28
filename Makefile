setup-docker:
	sudo yum update -y
	sudo yum update -y
	sudo yum install -y docker
	sudo usermod -a -G docker ec2-user
	sudo service docker start
	docker pull codeneuro/notebooks

setup-server:
	sudo yum install -y httpd24 php56 mysql55-server php56-mysqlnd
	sudo service httpd start

site: setup-server
	cp -r site /var/www/html

notebooks: setup-docker
	export TOKEN=$( head -c 30 /dev/urandom | xxd -p )
	docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN --name=proxy jupyter/configurable-http-proxy --default-target http://127.0.0.1:9999
	docker run --net=host -d -e CONFIGPROXY_AUTH_TOKEN=$TOKEN -v /var/run/docker.sock:/docker.sock jupyter/tmpnb python orchestrate.py --image='codeneuro/notebooks' --command="/bin/bash -c 'source activate /opt/conda/envs/python2.7-env/ && thunder -n --notebook-opts='--NotebookApp.base_url={base_path} --ip=0.0.0.0 --port={port}''" --pool_size=25

kill-docker:
	docker stop $(docker ps -a -q)
	docker rm $(docker ps -a -q)



