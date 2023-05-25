from fastapi.testclient import TestClient


def test_healthcheck(test_client: TestClient):
    resp = test_client.get("/health")

    assert resp.status_code == 200
    assert resp.json() == {"message": "health check OK!"}


def test_envars_dependency(test_client: TestClient):
    resp = test_client.get("/v1/route/dependency")

    assert resp.status_code == 200
    assert resp.json() == {"ENVAR1": "TEST_ENVAR1", "ENVAR2": "TEST_ENVAR2"}


def test_non_existant_route_returns_404(test_client: TestClient):
    resp = test_client.get("/v1/fakeroute")

    assert resp.status_code == 404


def test_url_and_path_params(test_client: TestClient):
    resp = test_client.get("v1/route/echo_path_param/p1?url_param=p2")

    assert resp.status_code == 200
    assert resp.json() == {"path_param": "p1", "url_param": "p2"}


def test_headers(test_client: TestClient):
    headers = {"Echo-Header": "HELLO WORLD!"}
    resp = test_client.get("v1/route/echo_header", headers=headers)

    assert resp.status_code == 200
    assert resp.json() == {"ECHO-HEADER": "HELLO WORLD!"}

def test_redirect(test_client: TestClient):
    # test client automatically follows redirects so we aren't looking for a 300 response.
    resp = test_client.get("/")

    assert resp.status_code == 200
    assert resp.url == "http://testserver/www/"