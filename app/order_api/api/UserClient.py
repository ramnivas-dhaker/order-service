from flask import session
import requests

# host_url = 'http://0.0.0.0:5556'
host_url = 'http://user-service.default.svc.cluster.local:5556'
# host_url = 'http://host.docker.internal:5556'

class UserClient:

    @staticmethod
    def get_user(api_key):
        headers = {
            'Authorization': api_key
        }

        response = requests.request(method="GET", url=f'{host_url}/api/user', headers=headers)
        if response.status_code == 401:
            return False

        user = response.json()
        return user
