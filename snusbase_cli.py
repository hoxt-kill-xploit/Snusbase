#!/usr/bin/env python3
"""
Standalone CLI for querying the Snusbase API.
Author: https://github.com/hoxt-kill-xploit
Organization home: https://hoxt.pro

Usage examples:
  snusbase search email@example.com --types email
  snusbase ipwhois 1.1.1.1 8.8.8.8
  snusbase stats
"""

import argparse
import sys
from snusbase_client import SnusbaseAPI

def main():
    parser = argparse.ArgumentParser(description="Snusbase CLI - Query 16B+ leaked records")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Search
    search = subparsers.add_parser("search")
    search.add_argument("terms", nargs="+")
    search.add_argument("--types", required=True, nargs="+")
    search.add_argument("--wildcard", action="store_true")
    search.add_argument("--tables", nargs="*")
    search.add_argument("--group-by", default="db")

    # Hash lookup
    hash_cmd = subparsers.add_parser("hash")
    hash_cmd.add_argument("terms", nargs="+")
    hash_cmd.add_argument("--types", required=True, nargs="+")
    hash_cmd.add_argument("--wildcard", action="store_true")
    hash_cmd.add_argument("--tables", nargs="*")
    hash_cmd.add_argument("--group-by", default="db")

    # IP WHOIS
    ipwhois = subparsers.add_parser("ipwhois")
    ipwhois.add_argument("ips", nargs="+")

    # Stats
    subparsers.add_parser("stats")

    args = parser.parse_args()

    try:
        api = SnusbaseAPI()
        
        if args.command == "search":
            result = api.search(
                args.terms, args.types,
                wildcard=args.wildcard,
                tables=args.tables,
                group_by=args.group_by
            )
        elif args.command == "hash":
            result = api.hash_lookup(
                args.terms, args.types,
                wildcard=args.wildcard,
                tables=args.tables,
                group_by=args.group_by
            )
        elif args.command == "ipwhois":
            result = api.ip_whois(args.ips)
        elif args.command == "stats":
            result = api.stats()
        
        print(SnusbaseAPI.format_results(result))
    
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
