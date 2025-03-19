import requests
from cache import cache
from cachetools import cached

@cached(cache)
def fetch_vulnerabilities(package_name: str, version: str):
  url="https://api.osv.dev/v1/query"
  payload={
    "package":{"name": package_name,"ecosystem": "PyPI"},
    "version": version
  }
  response = requests.post(url, json=payload)

  if response.status_code ==200:
    return response.json()
  else:
    return{"error":f"Failed to fetch vulnerabilities (status{response.status_code})"}
