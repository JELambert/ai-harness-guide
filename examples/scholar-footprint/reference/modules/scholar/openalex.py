"""Minimal OpenAlex client shared by the scholar scripts."""

import json
import os
import urllib.parse
import urllib.request

BASE = "https://api.openalex.org"


def get(path, **params):
    key = os.environ.get("OPENALEX_API_KEY")
    if key:
        params["api_key"] = key
    url = f"{BASE}/{path}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": "scholar-module/0.1"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def short_id(url):
    return url.rsplit("/", 1)[-1] if url else None
