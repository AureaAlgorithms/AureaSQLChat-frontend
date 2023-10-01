#File used only during development

docker_compose = docker-compose -f docker_compose.yml
docker_web = docker exec -it streamlit

.PHONY: up
up: # Builds, (re)creates, starts, and attaches to containers for a service. Deletes all previously created contianer images
	@$(docker_compose) up -d --build; docker images -q |xargs docker rmi;

.PHONY: logs
logs: # View the logs of streamlit activity
	@$(docker_compose) logs -f --tail=100

.PHONY: stop
stop: # Stop all containers
	@$(docker_compose) stop

.PHONY: down
down: # Stops containers and removes containers, networks, volumes, and images created by `make up`
	@$(docker_compose) down

.PHONY: shell
shell: # Enter the shell of the docker contianer where streamlit is running
	@$(docker_web) sh -c "export COLUMNS=`tput cols`; export LINES=`tput lines`; exec bash";


.PHONY: install-requirements
install-requirements: # Execute migrate command in streamlit container
	@$(docker_web) pip install -r /app/requirements.txt