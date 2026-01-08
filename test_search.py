#!/usr/bin/env python3
"""
Test script for Snusbase search query functionality.
Demonstrates various search operations without requiring a real API key.
"""

import sys
from snusbase_client import SnusbaseAPI


def test_search_initialization():
    """Test API client initialization with mock data"""
    print("=" * 60)
    print("TEST 1: API Client Initialization")
    print("=" * 60)
    
    try:
        # Use the template API key for testing
        api = SnusbaseAPI(api_key="sbo9ldwlaaz65ba6te4rkw9vzrfkmd")
        print("✓ API client initialized successfully")
        print(f"✓ Base URL: {api.BASE_URL}")
        print(f"✓ API key configured: {api.api_key[:10]}...")
        return api
    except Exception as e:
        print(f"✗ Failed to initialize API client: {e}")
        return None


def test_search_basic(api):
    """Test basic email search"""
    print("\n" + "=" * 60)
    print("TEST 2: Basic Email Search")
    print("=" * 60)
    
    try:
        print("Searching for: user@example.com")
        print("Type: email")
        
        result = api.search(
            terms=["user@example.com"],
            types=["email"]
        )
        
        print("\nResponse received:")
        print(SnusbaseAPI.format_results(result))
        print("✓ Basic search executed")
        
    except Exception as e:
        print(f"✗ Basic search failed: {e}")


def test_search_multiple_terms(api):
    """Test search with multiple terms"""
    print("\n" + "=" * 60)
    print("TEST 3: Multiple Search Terms")
    print("=" * 60)
    
    try:
        print("Searching for: user@example.com, john_doe")
        print("Types: email, username")
        
        result = api.search(
            terms=["user@example.com", "john_doe"],
            types=["email", "username"]
        )
        
        print("\nResponse received:")
        print(SnusbaseAPI.format_results(result))
        print("✓ Multiple terms search executed")
        
    except Exception as e:
        print(f"✗ Multiple terms search failed: {e}")


def test_search_wildcard(api):
    """Test wildcard search"""
    print("\n" + "=" * 60)
    print("TEST 4: Wildcard Search")
    print("=" * 60)
    
    try:
        print("Searching for: john (with wildcard)")
        print("Type: username")
        
        result = api.search(
            terms=["john"],
            types=["username"],
            wildcard=True
        )
        
        print("\nResponse received:")
        print(SnusbaseAPI.format_results(result))
        print("✓ Wildcard search executed")
        
    except Exception as e:
        print(f"✗ Wildcard search failed: {e}")


def test_search_domain_grouping(api):
    """Test domain search with custom grouping"""
    print("\n" + "=" * 60)
    print("TEST 5: Domain Search with Grouping")
    print("=" * 60)
    
    try:
        print("Searching for: example.com")
        print("Type: _domain")
        print("Group by: _domain")
        
        result = api.search(
            terms=["example.com"],
            types=["_domain"],
            group_by="_domain"
        )
        
        print("\nResponse received:")
        print(SnusbaseAPI.format_results(result))
        print("✓ Domain search with grouping executed")
        
    except Exception as e:
        print(f"✗ Domain search failed: {e}")


def test_search_table_scoping(api):
    """Test search with table scoping"""
    print("\n" + "=" * 60)
    print("TEST 6: Search with Table Scoping")
    print("=" * 60)
    
    try:
        print("Searching for: user@example.com")
        print("Type: email")
        print("Tables: adobe, linkedin")
        
        result = api.search(
            terms=["user@example.com"],
            types=["email"],
            tables=["adobe", "linkedin"]
        )
        
        print("\nResponse received:")
        print(SnusbaseAPI.format_results(result))
        print("✓ Table scoping search executed")
        
    except Exception as e:
        print(f"✗ Table scoping search failed: {e}")


def test_search_no_grouping(api):
    """Test search with grouping disabled"""
    print("\n" + "=" * 60)
    print("TEST 7: Search with No Grouping")
    print("=" * 60)
    
    try:
        print("Searching for: user@example.com")
        print("Type: email")
        print("Group by: false")
        
        result = api.search(
            terms=["user@example.com"],
            types=["email"],
            group_by="false"
        )
        
        print("\nResponse received:")
        print(SnusbaseAPI.format_results(result))
        print("✓ No grouping search executed")
        
    except Exception as e:
        print(f"✗ No grouping search failed: {e}")


def main():
    """Run all search query tests"""
    print("\n")
    print("*" * 60)
    print("*" + " " * 58 + "*")
    print("*" + "  SNUSBASE SEARCH QUERY TEST SUITE".center(58) + "*")
    print("*" + " " * 58 + "*")
    print("*" * 60)
    print("\nThis script demonstrates various search query capabilities")
    print("of the Snusbase API client.\n")
    
    # Initialize API
    api = test_search_initialization()
    
    if not api:
        print("\n✗ Cannot proceed without API client")
        sys.exit(1)
    
    # Run all search tests
    test_search_basic(api)
    test_search_multiple_terms(api)
    test_search_wildcard(api)
    test_search_domain_grouping(api)
    test_search_table_scoping(api)
    test_search_no_grouping(api)
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    print("All search query tests have been executed.")
    print("Note: Actual results depend on API key validity and")
    print("      Snusbase service availability.")
    print("\nTo use with a real API key, set SNUSBASE_API_KEY in .env file")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
