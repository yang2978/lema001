"""
测试模块示例
"""

import pytest
from lema001 import hello, __version__


def test_hello():
    """测试 hello 函数"""
    result = hello()
    assert result == "Hello from lema001!"
    assert isinstance(result, str)


def test_version():
    """测试版本号"""
    version = __version__
    assert isinstance(version, str)
    assert version == "0.1.0"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
