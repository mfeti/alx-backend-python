# Python Decorators for Database Operations

This project implements custom Python decorators to enhance database operations with logging, connection management, transaction handling, retry mechanisms, and caching.

## Project Structure

```
python-decorators-0x01/
├── 0-log_queries.py          # Task 0: Query logging decorator
├── 1-with_db_connection.py   # Task 1: Connection management decorator  
├── 2-transactional.py        # Task 2: Transaction management decorator
├── 3-retry_on_failure.py     # Task 3: Retry mechanism decorator
├── 4-cache_query.py          # Task 4: Query caching decorator
├── setup_database.py         # Database setup with sample data
├── users.db                  # SQLite database file
└── README.md                 # This file
```

## Tasks Overview

### Task 0: `log_queries` Decorator
- **File**: `0-log_queries.py`
- **Purpose**: Logs SQL queries before execution
- **Features**: 
  - Intercepts function calls to log SQL statements
  - Enhances observability of database operations

### Task 1: `with_db_connection` Decorator
- **File**: `1-with_db_connection.py`
- **Purpose**: Automates database connection handling
- **Features**:
  - Automatically opens database connection
  - Passes connection to decorated function
  - Ensures connection is closed after use
  - Eliminates boilerplate connection code

### Task 2: `transactional` Decorator
- **File**: `2-transactional.py`
- **Purpose**: Manages database transactions
- **Features**:
  - Automatically commits successful operations
  - Rolls back on exceptions
  - Ensures data integrity
  - Works with `with_db_connection` decorator

### Task 3: `retry_on_failure` Decorator
- **File**: `3-retry_on_failure.py`
- **Purpose**: Retries failed database operations
- **Features**:
  - Configurable retry attempts (default: 3)
  - Configurable delay between retries (default: 2 seconds)
  - Handles transient database errors
  - Provides resilience for database operations

### Task 4: `cache_query` Decorator
- **File**: `4-cache_query.py`
- **Purpose**: Caches database query results
- **Features**:
  - Caches results based on SQL query string
  - Avoids redundant database calls
  - Improves performance for repeated queries
  - Thread-safe implementation

## Database Setup

Run the setup script to create the test database:

```bash
python3 setup_database.py
```

This creates `users.db` with:
- A `users` table with columns: `id`, `name`, `email`
- Sample data with 5 users for testing

## Usage Examples

### Task 0: Logging Queries
```python
@log_queries
def fetch_all_users(query):
    # Database operation
    pass

users = fetch_all_users(query="SELECT * FROM users")
# Output: Executing query: SELECT * FROM users
```

### Task 1: Connection Management
```python
@with_db_connection
def get_user_by_id(conn, user_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
    return cursor.fetchone()

user = get_user_by_id(user_id=1)  # Connection handled automatically
```

### Task 2: Transaction Management
```python
@with_db_connection
@transactional
def update_user_email(conn, user_id, new_email):
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET email = ? WHERE id = ?", (new_email, user_id))

update_user_email(user_id=1, new_email='new@email.com')  # Auto commit/rollback
```

### Task 3: Retry on Failure
```python
@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

users = fetch_users_with_retry()  # Will retry up to 3 times on failure
```

### Task 4: Query Caching
```python
@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

# First call executes query and caches result
users1 = fetch_users_with_cache(query="SELECT * FROM users")

# Second call returns cached result
users2 = fetch_users_with_cache(query="SELECT * FROM users")
```

## Running the Tests

Each file can be run independently to test its functionality:

```bash
# Test logging decorator
python3 0-log_queries.py

# Test connection management
python3 1-with_db_connection.py

# Test transaction management
python3 2-transactional.py

# Test retry mechanism
python3 3-retry_on_failure.py

# Test query caching
python3 4-cache_query.py
```

## Key Features

1. **Production Ready**: All decorators include proper error handling
2. **Composable**: Decorators can be combined (e.g., `@with_db_connection` + `@transactional`)
3. **Configurable**: Parameters like retry count and cache behavior can be customized
4. **Thread Safe**: Implementations consider concurrent access patterns
5. **Observable**: Comprehensive logging for debugging and monitoring

## Requirements

- Python 3.8 or higher
- SQLite3 (included with Python)
- No external dependencies required

## Project Highlights

This project demonstrates advanced Python concepts:
- Decorator patterns and composition
- Context managers for resource handling
- Exception handling and error recovery
- Caching strategies for performance optimization
- Database transaction management
- Functional programming principles

Each decorator solves real-world database operation challenges while maintaining clean, reusable code.