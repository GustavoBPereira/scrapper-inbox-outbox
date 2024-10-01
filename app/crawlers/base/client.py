from typing import Optional, Dict
from smart_url import SmartPath, SmartUrl
import requests

class HttpClient:
    def __init__(self, base_url=None):
        self.base_url = base_url

    def get(self, endpoint, params : Optional[Dict] = None, headers : Optional[Dict] = None):
        url = self._build_url(endpoint, params)
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, params : Optional[Dict] = None, data : Optional[Dict] = None, headers : Optional[Dict] = None):
        url = self._build_url(endpoint, params)
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()
        return response.json()

    def _build_url(self, endpoint, params : Optional[Dict] = None):
        url = SmartUrl(self.base_url)
        url.append_path(endpoint)
        url.update_query(params)
        return str(url)
