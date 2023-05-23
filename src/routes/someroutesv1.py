from typing import Optional, Annotated, Union, Tuple
from fastapi import APIRouter, Depends, Header
from fastapi.responses import JSONResponse
from src.deps import get_config, Config

# to do routing in FastAPI, you need to use the fastAPI
# router object
router = APIRouter(prefix="/v1/route")


@router.get("/echo_path_param/{path_param}")
def echo(
    path_param: Optional[str],
    url_param: Optional[str],
) -> JSONResponse:
    """
    This example shows how to set a endpoint on a route
    as well as how to deal with path and url parameters in FastAPI
    Example : http://localhost/v1/route/echo_path_param/helloworld?url_param=hello
    """
    return JSONResponse(
        status_code=200, content={"path_param": path_param, "url_param": url_param}
    )


@router.get("/echo_header")
def echo_header(Echo_Header: Annotated[Optional[str], Header()] = None):
    """
    this example shows how to deal with headers
    in fast API using the Header object
    Example : curl http://localhost/v1/route/echo_header -H "ECHO-HEADER:Yarp"
    """
    return JSONResponse(status_code=200, content={"ECHO-HEADER": Echo_Header})


@router.get("/dependency")
def print_deps(config: Config = Depends(get_config)):
    """
    this example shows how to use dependencies in
    fastAPI without introducing tight coupling, notice
    that the Depends constructor takes a getter as an
    argument, requires ENVAR1 and ENVAR2 to be set.
    """
    return JSONResponse(
        status_code=200,
        content={"ENVAR1": config.SOME_ENVAR1, "ENVAR2": config.SOME_ENVAR2},
    )
