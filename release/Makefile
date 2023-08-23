versionfile := version.txt
VERSION := $(shell cat ${versionfile})
IMAGE := karethio/dst-docker-base
BUILD_DIR := ../build/
.PHONY: build

build:
	docker build -t $(IMAGE):$(VERSION) $(BUILD_DIR) --no-cache
shell:
	docker run -it --rm $(IMAGE):$(VERSION) /bin/bash
push:
	docker tag $(IMAGE):$(VERSION) $(IMAGE):latest
	docker image push $(IMAGE):$(VERSION)
	docker image push $(IMAGE):latest
