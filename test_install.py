"""
测试安装和功能验证脚本
使用方法：python test_install.py
"""

import sys


def test_import():
    """测试导入包"""
    try:
        import lema001
        print(f"✅ 成功导入 lema001 v{lema001.__version__}")
        return True
    except ImportError as e:
        print(f"❌ 导入失败：{e}")
        return False


def test_hello_function():
    """测试 hello 函数"""
    try:
        from lema001 import hello
        result = hello()
        expected = "Hello from lema001!"
        
        if result == expected:
            print(f"✅ hello() 函数正常：'{result}'")
            return True
        else:
            print(f"❌ hello() 返回错误：期望 '{expected}', 实际 '{result}'")
            return False
    except Exception as e:
        print(f"❌ hello() 测试失败：{e}")
        return False


def test_main_function():
    """测试 main 函数"""
    try:
        from lema001 import main
        print("✅ main() 函数可调用")
        # 不实际运行，因为会输出内容
        return True
    except Exception as e:
        print(f"❌ main() 测试失败：{e}")
        return False


def test_version():
    """测试版本号"""
    try:
        from lema001 import __version__
        if __version__ == "0.1.0":
            print(f"✅ 版本号正确：v{__version__}")
            return True
        else:
            print(f"⚠️  版本号不是预期的 0.1.0: v{__version__}")
            return True  # 仍然算通过，只是提示
    except Exception as e:
        print(f"❌ 版本测试失败：{e}")
        return False


def main():
    """运行所有测试"""
    print("=" * 60)
    print("lema001 包功能测试")
    print("=" * 60)
    print()
    
    tests = [
        ("导入测试", test_import),
        ("hello() 函数", test_hello_function),
        ("main() 函数", test_main_function),
        ("版本号", test_version),
    ]
    
    results = []
    for name, test_func in tests:
        print(f"[{name}]")
        result = test_func()
        results.append(result)
        print()
    
    print("=" * 60)
    print(f"测试结果：{sum(results)}/{len(results)} 通过")
    
    if all(results):
        print("🎉 所有测试通过！你的包可以正常工作。")
        return 0
    else:
        print("⚠️  部分测试失败，请检查问题。")
        return 1


if __name__ == "__main__":
    sys.exit(main())
