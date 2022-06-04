# # Container's default name
# NAME=pytest-api-booking
#
# .PHONY: test
# start:
#     docker image rm --force $(NAME)
#     docker build -t $(NAME) .



# Container's default name
NAME=pytest-api-booking

# Docker image default name
IMAGE=test/$(NAME)

# Stop container
.PHONY: rm
rm:
	@echo "--> Removing image $(NAME)"
	docker image rm --force $(NAME)

# Start container
.PHONY: start
start:
	@echo "--> Starting $(NAME)"
	docker build -t $(NAME) .

# Start container
.PHONY: run
run:
	@echo "--> Running $(NAME)"
	docker run -ti $(NAME) pytest tests

# testing
.PHONY: test
test: rm start run
