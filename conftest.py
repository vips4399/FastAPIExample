from tests.fakes import FakeSettings
from src.deps import get_config
from src.main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture()
def test_client() -> TestClient:
    # override the dependency in the app to use our test fake
    # instead of using the real thing
    app.dependency_overrides[get_config] = lambda : FakeSettings()
    
    # you could use a generator here, but I'm keeping this example fixture simple
    return TestClient(app)

