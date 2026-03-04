# lema001

[![PyPI version](https://badge.fury.io/py/lema001.svg)](https://badge.fury.io/py/lema001)
[![Python Versions](https://img.shields.io/pypi/pyversions/lema001.svg)](https://pypi.org/project/lema001/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

实验项目库 - 所有的实验项目都以 lema 打头后面加序号，这个是第一个项目

## 📦 安装

### 从 PyPI 安装（推荐）

```bash
pip install lema001
```

### 从源码安装

```bash
# 克隆或下载源码后
cd lema001
pip install .

# 或者开发模式安装
pip install -e .
```

### 安装开发依赖

```bash
pip install lema001[dev]
```

## 🚀 快速开始

### 作为 Python 模块使用

```python
import lema001

# 调用 hello 函数
result = lema001.hello()
print(result)  # 输出：Hello from lema001!

# 查看版本
print(lema001.__version__)  # 输出：0.1.0
```

### 使用命令行工具

安装后，你可以在终端中直接运行：

```bash
lema001
```

或者作为模块运行：

```bash
python -m lema001
```

## 📖 功能特性

- ✨ 简单易用的 API
- 🔧 可扩展的实验框架
- 📝 完整的类型注解
- 🧪 包含单元测试

## 📝 示例

```python
from lema001 import hello, main

# 使用 hello 函数
print(hello())

# 运行主函数
main()
```

## 🔧 开发

### 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/yourusername/lema001.git
cd lema001

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -e .[dev]
```

### 运行测试

```bash
pytest
```

### 代码格式化

```bash
# 使用 black 格式化代码
black lema001

# 使用 flake8 检查代码风格
flake8 lema001

# 使用 mypy 进行类型检查
mypy lema001
```

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📬 联系方式

- Author: Your Name
- Email: your.email@example.com

---

**注意**: 这是一个实验项目库，用于存放各种实验性代码。
