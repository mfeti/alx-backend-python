# Python Context Managers and Async Operations

This project implements custom Python context managers and asynchronous database operations using modern Python features.

## Project Structure

```
python-context-async-perations-0x02/
├── 0-databaseconnection.py    # Task 0: Class-based context manager for DB connections
├── 1-execute.py              # Task 1: Reusable query context manager
├── 3-concurrent.py           # Task 2: Concurrent async database queries
├── setup_database.py         # Database setup with sample data
├── database.db              # SQLite database file
└── README.md                # This file
```

## Tasks Overview

### Task 0: Custom Class-based Context Manager for Database Connection
- **File**: `0-databaseconnection.py`
- **Objective**: Create a class-based context manager to handle opening and closing database connections automatically
- **Features**:
  - Implements `__enter__` and `__exit__` methods
  - Automatic connection management
  - Works with `with` statement
  - Performs `SELECT * FROM users` query

### Task 1: Reusable Query Context Manager
- **File**: `1-execute.py`
- **Objective**: Create a reusable context manager that takes a query as input and executes it
- **Features**:
  - Handles both connection and query execution
  - Supports parameterized queries
  - Executes `SELECT * FROM users WHERE age > ?` with parameter 25
  - Returns query results automatically

### Task 2: Concurrent Asynchronous Database Queries
- **File**: `3-concurrent.py`
- **Objective**: Run multiple database queries concurrently using asyncio.gather
- **Features**:
  - Uses `aiosqlite` library for async SQLite operations
  - Two async functions: `async_fetch_users()` and `async_fetch_older_users()`
  - Concurrent execution with `asyncio.gather()`
  - Performance timing to demonstrate concurrency benefits
  - Uses `asyncio.run(fetch_concurrently())` to run the concurrent fetch

## Database Setup

Run the setup script to create the test database:

```bash
python3 setup_database.py
```

This creates `database.db` with:
- A `users` table with columns: `id`, `name`, `age`
- Sample data with 10 users of various ages for testing

## Usage Examples

### Task 0: Database Connection Context Manager

```python
with DatabaseConnection('database.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    print(results)
```

### Task 1: Reusable Query Context Manager

```python
query = "SELECT * FROM users WHERE age > ?"
param = (25,)

with ExecuteQuery('database.db', query, param) as results:
    for row in results:
        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
```

### Task 2: Concurrent Async Queries

```python
# Both queries run concurrently
all_users, older_users = await asyncio.gather(
    async_fetch_users(),
    async_fetch_older_users()
)
```

## Running the Examples

Each file can be run independently:

```bash
# Test database connection context manager
python3 0-databaseconnection.py

# Test reusable query context manager
python3 1-execute.py

# Test concurrent async queries
python3 3-concurrent.py
```

## Key Features

1. **Context Managers**: Proper resource management with automatic cleanup
2. **Parameterized Queries**: Safe SQL execution with parameter binding
3. **Async Operations**: Non-blocking database queries using aiosqlite
4. **Concurrent Execution**: Multiple queries running simultaneously
5. **Error Handling**: Proper exception propagation and resource cleanup

## Dependencies

- **Python 3.7+**: Required for async context managers
- **aiosqlite**: For asynchronous SQLite operations
  ```bash
  pip install aiosqlite
  ```

## Learning Objectives

This project demonstrates:
- **Context Manager Protocol**: Implementing `__enter__` and `__exit__` methods
- **Resource Management**: Automatic cleanup of database connections
- **Async Programming**: Using `async`/`await` with database operations
- **Concurrent Programming**: Running multiple operations simultaneously
- **Modern Python Features**: Context managers, async context managers, and asyncio

## Performance Benefits

The concurrent implementation shows significant performance improvements when dealing with multiple database operations, as demonstrated by the timing measurements in the async task.

Each implementation follows Python best practices for resource management and provides clean, maintainable code for database operations.