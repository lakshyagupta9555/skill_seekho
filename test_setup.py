"""
Run this script after setup to test the platform
"""
import os
import sys

def run_tests():
    print("🧪 Testing Skill Swap Platform...")
    print()
    
    tests = [
        ("Django installation", "import django"),
        ("Channels installation", "import channels"),
        ("Pillow installation", "from PIL import Image"),
        ("Settings module", "from skill_swap import settings"),
    ]
    
    passed = 0
    failed = 0
    
    for test_name, test_code in tests:
        try:
            exec(test_code)
            print(f"✅ {test_name}: PASSED")
            passed += 1
        except Exception as e:
            print(f"❌ {test_name}: FAILED - {str(e)}")
            failed += 1
    
    print()
    print(f"Results: {passed} passed, {failed} failed")
    print()
    
    if failed == 0:
        print("🎉 All tests passed! Platform is ready to use.")
        print()
        print("Next steps:")
        print("1. python manage.py createsuperuser")
        print("2. python manage.py runserver")
    else:
        print("⚠️ Some tests failed. Please check the installation.")

if __name__ == '__main__':
    run_tests()
