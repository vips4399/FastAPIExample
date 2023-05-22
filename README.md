# FastAPI Example
### Python Version : 3.9

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




## Running Locally No Container
**WIP**
