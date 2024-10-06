def test_get_assignments(client):
    response = client.get('/principal/assignments', headers={
        'X-Principal': json.dumps({"user_id": 5, "principal_id": 1})
    })
    assert response.status_code == 200
    assert 'data' in response.json

def test_get_teachers(client):
    response = client.get('/principal/teachers', headers={
        'X-Principal': json.dumps({"user_id": 5, "principal_id": 1})
    })
    assert response.status_code == 200
    assert 'data' in response.json

def test_grade_assignment(client):
    response = client.post('/principal/assignments/grade', headers={
        'X-Principal': json.dumps({"user_id": 5, "principal_id": 1})
    }, json={
        "id": 1,
        "grade": "A"
    })
    assert response.status_code == 200
    assert response.json['data']['grade'] == "A"
