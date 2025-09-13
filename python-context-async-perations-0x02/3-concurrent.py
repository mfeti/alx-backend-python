import asyncio
import aiosqlite
import time

async def async_fetch_users():
    """Async function to fetch all users from the database"""
    async with aiosqlite.connect('database.db') as db:
        cursor = await db.execute("SELECT * FROM users")
        results = await cursor.fetchall()
        return results

async def async_fetch_older_users():
    """Async function to fetch users older than 40 from the database"""
    async with aiosqlite.connect('database.db') as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        results = await cursor.fetchall()
        return results

async def fetch_concurrently():
    """Execute both queries concurrently using asyncio.gather"""
    print("Starting concurrent database queries...")
    
    start_time = time.time()
    
    # Use asyncio.gather to run both queries concurrently
    all_users, older_users = await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )
    
    end_time = time.time()
    print(f"\nConcurrent execution completed in {end_time - start_time:.4f} seconds")
    
    # Display results
    print("\n=== All Users ===")
    for user in all_users:
        print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
    
    print(f"\nTotal users: {len(all_users)}")
    
    print("\n=== Users Older Than 40 ===")
    for user in older_users:
        print(f"ID: {user[0]}, Name: {user[1]}, Age: {user[2]}")
    
    print(f"\nUsers older than 40: {len(older_users)}")

# Run the concurrent fetch
if __name__ == "__main__":
    # Use asyncio.run to run the concurrent fetch
    asyncio.run(fetch_concurrently())