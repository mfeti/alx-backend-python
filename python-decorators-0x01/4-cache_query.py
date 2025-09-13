import time
import sqlite3 
import functools

def with_db_connection(func):
    """Decorator that handles database connection opening and closing"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect('users.db')
        try:
            # Pass the connection as the first argument to the decorated function
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
    return wrapper

query_cache = {}

def cache_query(func):
    """Decorator that caches query results based on the SQL query string"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Extract query from function arguments
        query = kwargs.get('query') or (args[1] if len(args) > 1 else None)
        
        if query:
            # Check if query result is already cached
            if query in query_cache:
                print(f"Cache hit for query: {query}")
                return query_cache[query]
            else:
                print(f"Cache miss for query: {query}")
                # Execute the function and cache the result
                result = func(*args, **kwargs)
                query_cache[query] = result
                return result
        else:
            # If no query found, execute without caching
            return func(*args, **kwargs)
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

#### First call will cache the result
if __name__ == "__main__":
    print("=== First call (should cache the result) ===")
    users = fetch_users_with_cache(query="SELECT * FROM users")
    print(f"Retrieved {len(users)} users")
    
    print("\n=== Second call (should use cached result) ===")
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
    print(f"Retrieved {len(users_again)} users")
    
    print(f"\n=== Cache contents ===")
    print(f"Cached queries: {list(query_cache.keys())}")
    print(f"Number of cached results: {len(query_cache)}")
    
    print("\n=== Third call with different query (should cache new result) ===")
    specific_user = fetch_users_with_cache(query="SELECT * FROM users WHERE id = 1")
    print(f"Retrieved specific user: {specific_user}")
    
    print(f"\n=== Updated cache contents ===")
    print(f"Cached queries: {list(query_cache.keys())}")
    print(f"Number of cached results: {len(query_cache)}")