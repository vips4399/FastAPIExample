from pydantic import BaseSettings


# this is a pydantic settings class, it automagically
# fills in these values from ENVARS
# These envars themselves are set in the Dockerfile
class Config(BaseSettings):
    SOME_ENVAR1: str
    SOME_ENVAR2: str


get_config = lambda: Config()
