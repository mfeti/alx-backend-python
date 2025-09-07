#!/usr/bin/env python3
"""
Project verification script for Python Generators project.
This script tests the basic functionality of all modules.
"""

import sys
import os

def test_imports():
    """Test that all modules can be imported successfully"""
    print("🔍 Testing module imports...")
    
    try:
        import seed
        print("✅ seed.py imported successfully")
        
        # Import the generator modules
        stream_users_module = __import__('0-stream_users')
        print("✅ 0-stream_users.py imported successfully")
        
        batch_module = __import__('1-batch_processing')
        print("✅ 1-batch_processing.py imported successfully")
        
        paginate_module = __import__('2-lazy_paginate')
        print("✅ 2-lazy_paginate.py imported successfully")
        
        ages_module = __import__('4-stream_ages')
        print("✅ 4-stream_ages.py imported successfully")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_functions_exist():
    """Test that all required functions exist"""
    print("\n🔍 Testing function definitions...")
    
    try:
        import seed
        
        # Test seed.py functions
        assert hasattr(seed, 'connect_db'), "connect_db function missing"
        assert hasattr(seed, 'create_database'), "create_database function missing"
        assert hasattr(seed, 'connect_to_prodev'), "connect_to_prodev function missing"
        assert hasattr(seed, 'create_table'), "create_table function missing"
        assert hasattr(seed, 'insert_data'), "insert_data function missing"
        print("✅ All seed.py functions defined")
        
        # Test stream_users functions
        stream_module = __import__('0-stream_users')
        assert hasattr(stream_module, 'stream_users'), "stream_users function missing"
        print("✅ stream_users function defined")
        
        # Test batch processing functions
        batch_module = __import__('1-batch_processing')
        assert hasattr(batch_module, 'stream_users_in_batches'), "stream_users_in_batches function missing"
        assert hasattr(batch_module, 'batch_processing'), "batch_processing function missing"
        print("✅ batch processing functions defined")
        
        # Test pagination functions
        paginate_module = __import__('2-lazy_paginate')
        assert hasattr(paginate_module, 'paginate_users'), "paginate_users function missing"
        assert hasattr(paginate_module, 'lazy_pagination'), "lazy_pagination function missing"
        print("✅ pagination functions defined")
        
        # Test aggregation functions
        ages_module = __import__('4-stream_ages')
        assert hasattr(ages_module, 'stream_user_ages'), "stream_user_ages function missing"
        assert hasattr(ages_module, 'calculate_average_age'), "calculate_average_age function missing"
        print("✅ aggregation functions defined")
        
        return True
        
    except (ImportError, AssertionError) as e:
        print(f"❌ Function definition error: {e}")
        return False

def test_files_exist():
    """Test that all required files exist"""
    print("\n🔍 Testing file existence...")
    
    required_files = [
        'seed.py',
        '0-stream_users.py',
        '1-batch_processing.py', 
        '2-lazy_paginate.py',
        '4-stream_ages.py',
        'user_data.csv',
        'README.md'
    ]
    
    all_exist = True
    for filename in required_files:
        if os.path.exists(filename):
            print(f"✅ {filename} exists")
        else:
            print(f"❌ {filename} missing")
            all_exist = False
    
    return all_exist

def test_csv_format():
    """Test that CSV file has correct format"""
    print("\n🔍 Testing CSV file format...")
    
    try:
        with open('user_data.csv', 'r') as file:
            first_line = file.readline().strip()
            expected_header = "user_id,name,email,age"
            
            if first_line == expected_header:
                print("✅ CSV header format is correct")
                
                # Count rows
                lines = file.readlines()
                print(f"✅ CSV contains {len(lines)} data rows")
                return True
            else:
                print(f"❌ CSV header incorrect. Expected: {expected_header}, Got: {first_line}")
                return False
                
    except FileNotFoundError:
        print("❌ user_data.csv file not found")
        return False

def main():
    """Run all tests"""
    print("🚀 Python Generators Project Verification")
    print("=" * 50)
    
    tests = [
        test_files_exist,
        test_csv_format,
        test_imports,
        test_functions_exist
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Project is ready for submission.")
        return 0
    else:
        print("⚠️  Some tests failed. Please check the issues above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
