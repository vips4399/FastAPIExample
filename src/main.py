from fastapi import FastAPI
from fastapi.responses import JSONResponse
from src.middleware.logging import LogMiddleware
from starlette.staticfiles import StaticFiles

app = FastAPI()

#  An Example of Simple Application Level Route
#  This Example listens for GET requests on <host>/health
#  and returns a JSONResponse with status_code 200 OK!
@app.get("/health")
def healtcheck() -> JSONResponse:
    return JSONResponse(status_code=200, content={"message": "health check OK!"})


# Add the logging middleware to the app
# This is optional and just an example of how
# to use middlewares in FastAPI
app.add_middleware(LogMiddleware)


# This is an example of how to serve static
# content like non-templated HTML
# When the app is running this should be viewable at http://localhost:<port>/www/
app.mount("/www", StaticFiles(directory="www", html = True), name="www")