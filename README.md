# Snusbase CLI

A simple CLI wrapper for interacting with the Snusbase API to search breach data, hashes, and IP information.

---

## Prerequisites

To access the Snusbase database (a collection of data leaks), you must have an API key.

1. Obtain an API key from the official Snusbase customer portal:  
   https://snusbase.sell.app/#customer-portal  
   *(This project is not selling anything. Keys are purchased directly from Snusbase via Sell.app.)*

2. Create a `.env` file and add your API key:
   ~~~env
   SNUSBASE_API_KEY=your_key_here
   ~~~

3. Install dependencies:
   ~~~bash
   pip install -r requirements.txt
   ~~~

4. Run the examples below.

**COMING SOON**  
Check out the Snusbase web app repository to deploy this on your own domain.  
Link: **TBA**

---

## Usage

All commands follow this format:

~~~bash
python3 snusbase_cli.py <command> [options]
~~~

### Quick Search Example

To perform a quick search for a specific term (e.g., "teste"):

~~~bash
python3 search_teste.py
~~~

Or use the CLI directly:

~~~bash
python3 snusbase_cli.py search "teste" --types username email
~~~

---

## Examples

### Basic email search
~~~bash
python3 snusbase_cli.py search "user@example.com" --types email
~~~

### Multiple search terms and types
~~~bash
python3 snusbase_cli.py search "user@example.com" "another@example.net" --types email username
~~~

### Wildcard search (prefix / suffix matching)
~~~bash
python3 snusbase_cli.py search "john" --types username --wildcard
~~~

### Group results by a specific column
~~~bash
python3 snusbase_cli.py search "example.com" --types _domain --group-by _domain
~~~

### Limit search to specific breach tables
~~~bash
python3 snusbase_cli.py search "user@example.com" --types email --tables adobe linkedin
~~~

### Disable grouping entirely
~~~bash
python3 snusbase_cli.py search "user@example.com" --types email --group-by false
~~~

### Hash or password lookup
~~~bash
python3 snusbase_cli.py hash "5f4dcc3b5aa765d61d8327deb882cf99" --types hash
~~~

### Hash lookup with wildcard and table scoping
~~~bash
python3 snusbase_cli.py hash "abc123" --types password --wildcard --tables some_hash_db
~~~

### IP WHOIS lookup (single or multiple IPs)
~~~bash
python3 snusbase_cli.py ipwhois 1.1.1.1 8.8.8.8
~~~

### Database statistics
~~~bash
python3 snusbase_cli.py stats
~~~

---

## Notes

- Wildcard searches enable partial matching.
- Table scoping restricts searches to specific breach datasets.
- Grouping can be customized or disabled depending on output needs.
