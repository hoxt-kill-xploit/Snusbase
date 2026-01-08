#!/usr/bin/env python3
"""
Search example script for 'teste' term
Demonstrates how to search for a specific term using the Snusbase API
"""

from snusbase_client import SnusbaseAPI
import sys

def main():
    """
    Perform a search for the term 'teste' across common search types.
    This example searches for 'teste' as:
    - username
    - email
    - name
    """
    try:
        # Initialize the Snusbase API client
        api = SnusbaseAPI()
        
        print("🔍 Performing search for 'teste'...")
        print("=" * 50)
        
        # Search for 'teste' across multiple types
        result = api.search(
            terms=["teste"],
            types=["username", "email", "name"],
            wildcard=False,
            group_by="db"
        )
        
        # Format and display results
        formatted_results = SnusbaseAPI.format_results(result)
        print(formatted_results)
        
        print("=" * 50)
        print("✅ Search completed successfully")
        
    except Exception as e:
        print(f"❌ Error during search: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
