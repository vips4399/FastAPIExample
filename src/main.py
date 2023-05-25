from fastapi import FastAPI
from fastapi.responses import JSONResponse, RedirectResponse
from src.middleware.logging import LogMiddleware
from starlette.staticfiles import StaticFiles
from src.routes.someroutesv1 import router

app = FastAPI(title="FastAPI Example", version=1.0)


@app.get("/health")
async def healtcheck() -> JSONResponse:
    """
    An Example of Simple Application Level Route
    This Example listens for GET requests on <host>/health
    and returns a JSONResponse with status_code 200 OK!
    """
    return JSONResponse(status_code=200, content={"message": "health check OK!"})

@app.get("/")
async def re_route_to_static() -> RedirectResponse:
    """
    Redirect traffic on root to correct mount for static files.
    """
    return RedirectResponse("/www/")

# Add the logging middleware to the app
# This is optional and just an example of how
# to use middlewares in FastAPI
app.add_middleware(LogMiddleware)


# This is an example of how to serve static
# content like non-templated HTML
# When the app is running this should be viewable at http://localhost:<port>/www/
app.mount("/www", StaticFiles(directory="www", html=True), name="www")


# This example adds routes defined in a router
# These routes are in src/routes/someroutesv1.py
app.include_router(router=router)
