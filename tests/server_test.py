def test_server(client):
    response = client.get(
        "/"
    )

    assert response.status_code == 200
    
    status = response.json["status"]
    assert status == "ready"

def test_invalid_route(client):
    response = client.get(
        "/sfsdfsd/fsdfs"
    )

    assert response.status_code == 404
    
    error = response.json["error"]
    assert error == "NotFound"

def test_principal_authentication(client):
    response = client.get(
        "teacher/assignments"
    )

    assert response.status_code == 401

    error = response.json["error"]
    message = response.json["message"]

    assert error == "FyleError"
    assert message == "principal not found"

