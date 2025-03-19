import requests
from cachetools import TTLCache, cached

#cache results for 10 mins
cache=TTLCache(maxsize=100, ttl=600)

@cached(cache)
def fetch_vulnerabilities(package_name: str, version: str):
  url="https://api.osv.dev/v1/query"
  payload={
    "package":{"name": package_name,"ecosystem": "PyPI"},
    "version": version
  }
  response = requests.post(url, json=payload)
  return response.json() if response.status_code ==200
else{"vulns":[]}
