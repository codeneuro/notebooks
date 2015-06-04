setup:
	sudo yum update -y
	sudo yum install -y httpd24 php56 mysql55-server php56-mysqlnd gcc
	git clone https://github.com/andrewosh/tmpnb-redirector.git tmpnb-redirector
	sudo pip install -r tmpnb-redirector/requirements.txt

deploy:
	sudo service httpd start
	sudo rm -rf /var/www/html/
	sudo cp -a site/. /var/www/html/
	# Query the workers for their availability every 10s (default 60s) 
	python tmpnb-redirector/redirector.py --stats_period=10

clean:
	sudo rm -rf /var/www/html/


