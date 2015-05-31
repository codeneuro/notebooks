images: base-image notebooks-image

base-image:
	docker build -t codeneuro/base base/

notebooks-image: base-image
	[ -d notebooks ] || cp -r ../notebooks .
	docker build -t codeneuro/notebooks .
	rm -rf notebooks/

# Cleanup with fangs
nuke:
	-docker stop `docker ps -aq`
	-docker rm -fv `docker ps -aq`
	-docker images -q --filter "dangling=true" | xargs docker rmi

.PHONY: nuke