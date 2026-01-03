#!/usr/bin/env python3
"""
Author: https://github.com/hoxt-kill-xploit
Organization home: https://hoxt.pro
Snusbase API helper - CLI + web app(TBA)
"""
from typing import Any, Dict, List, Optional
import requests
import os
from dotenv import load_dotenv


class SnusbaseAPI:
    BASE_URL = "https://api.snusbase.com"

    def __init__(self, api_key: str = None):
        if not api_key:
            load_dotenv()
            api_key = os.getenv("SNUSBASE_API_KEY")
        if not api_key:
            raise ValueError("SNUSBASE_API_KEY required")
        
        self.api_key = api_key
        self.session = requests.Session()
        self.session.headers.update({
            "Auth": self.api_key,
            "Content-Type": "application/json",
            "User-Agent": "Snusbase-CLI/1.0",
        })

    def _request(self, method: str, endpoint: str, payload: Dict = None) -> Dict[str, Any]:
        try:
            if method == "GET":
                resp = self.session.get(f"{self.BASE_URL}{endpoint}", timeout=30)
            else:
                resp = self.session.post(f"{self.BASE_URL}{endpoint}", json=payload, timeout=30)
            resp.raise_for_status()
            return resp.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def search(self, terms: List[str], types: List[str], wildcard=False, group_by="db", tables=None) -> Dict[str, Any]:
        payload = {"terms": terms, "types": types, "wildcard": wildcard, "group_by": group_by}
        if tables: payload["tables"] = tables
        return self._request("POST", "/data/search", payload)

    def stats(self) -> Dict[str, Any]:
        return self._request("GET", "/data/stats")

    def ip_whois(self, ips: List[str]) -> Dict[str, Any]:
        return self._request("POST", "/tools/ip-whois", {"terms": ips})

    def hash_lookup(self, terms: List[str], types: List[str], wildcard=False, group_by="db", tables=None) -> Dict[str, Any]:
        payload = {"terms": terms, "types": types, "wildcard": wildcard, "group_by": group_by}
        if tables: payload["tables"] = tables
        return self._request("POST", "/tools/hash-lookup", payload)

    @staticmethod
    def format_results(results: Dict[str, Any]) -> str:
        if "error" in results:
            return f"❌ Error: {results['error']}"

        if not results.get("results"):
            return "ℹ️ No results found."

        lines = []
        for db, data in results.get("results", {}).items():
            lines.append(f"🗄️ Database: {db}")
            if isinstance(data, list):
                for item in data:
                    lines.append("  ---")
                    if isinstance(item, dict):
                        for k, v in item.items():
                            lines.append(f"  {k}: {v}")
                    else:
                        lines.append(f"  {item}")
            else:
                lines.append(f"  {data}")
            lines.append("")

        if results.get("errors"):
            lines.append("⚠️ Errors:")
            for term, err in results["errors"].items():
                lines.append(f"  {term}: {err}")

        return "
".join(lines)
