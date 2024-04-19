from core.libs import helpers
from flask import jsonify
from core import app
def test_server_running(client):
    response=client.get('/')
    assert response.status_code==200
    assert response.json["status"]=="ready"
    with app.app_context():
        curr_time_json=jsonify({'time':helpers.get_utc_now()})
    assert response.json["time"]==curr_time_json.json['time']

    