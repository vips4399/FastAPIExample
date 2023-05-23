# FastAPI Example
### Python Version : 3.9

# Included Routes
    /health
    /v1/route/echo_params/{path_param}?url_param={url_param}
    /v1/route/dependency
    /v1/route/echo_header

# Static www

    /www/index.html

## Running Locally as Container

**Note : You must have docker installed for this to work, Pipenv is also generally suggested for local development**

``$docker build -t fastapiexample .``

After the container is built

``$docker run --rm -p 8079:80 fastapiexample``

When the container is running, you should now be able to test that the health route works. You can either use your browser and naviate to `localhost:8079/health` or `$curl localhost:8079/health | jq`

## Environment Setup
** Highly recommeneded to use pipenv and pyenv to manage python environments and python verions respectively **

``$ pipenv shell``

``$ pipenv install --dev``

# Running Tests

After settting up the environment, running local tests would be a good first tests that everything is setup correctly.

To run the unit tests after the dependencies are install and the environment is setup.

`$ pytest tests/ -v --cov=src`



## Running Locally No Container

To run locally with no container
`$ gunicorn -c gunicorn_config.py src.main:app`

## FAQ

1. **Q:** Something went wrong in my containerized app, all I see is internal server error, how do I see what happened?

    **A:** The logs are stored in `error_log` in the working directory of the container. First find the container_id with `$docker ps` , once you have that, start a terminal in that container with `$docker exec -it <container_id> /bin/bash` , lastly you can check the log with `$cat error_log`