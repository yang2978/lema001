# lema001

[![PyPI version](https://badge.fury.io/py/lema001.svg)](https://badge.fury.io/py/lema001)
[![Python Versions](https://img.shields.io/pypi/pyversions/lema001.svg)](https://pypi.org/project/lema001/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## 1. Summary description
lema是一组AI相关项目的集合，所有项目都以 lema 打头后面加序号，本项目是第一个项目。本项目的核心目的是构建一组AI Agent Runtime 所需的基础功能，其他系统可以通过 PIP install 安装，并在自身的 Agent 应用中通过 import lema001 导入相关功能。


**注意**: 当前本项目还处在实验期，大部分代码逻辑仍处在，用于存放各种实验性代码。

## 2. 📬 联系方式

- Author: jingyu.yang
- Email: 15801554959@aliyun.com

## 3. 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

## 4. 🤝 贡献

欢迎提交 Issue 和 Pull Request！



###############################################################################################
###############################################################################################
## 5. 📦 如何安装并使用

### 5.1 从 PyPI 安装（推荐）

```bash
pip install lema001
```

### 5.2 从源码安装

```bash
# 克隆或下载源码后
cd lema001
pip install .

# 或者开发模式安装
pip install -e .
```

### 5.3 安装开发依赖

```bash
pip install lema001[dev]
```

## 6. 🚀 快速开始

### 6.1 作为 Python 模块使用

```python
import lema001

# 调用 hello 函数
result = lema001.hello()
print(result)  # 输出：Hello from lema001!

# 查看版本
print(lema001.__version__)  # 输出：0.1.0
```

### 6.2 使用命令行工具

安装后，你可以在终端中直接运行：

```bash
lema001
```

或者作为模块运行：

```bash
python -m lema001
```

## 7. 📖 功能特性

- ✨ 简单易用的 API
- 🔧 可扩展的实验框架
- 📝 完整的类型注解
- 🧪 包含单元测试

## 8. 📁 项目结构

```
lema001/
├── lema001/                    # Python 包主目录
│   ├── __init__.py             # 包初始化，包含版本号和 API
│   └── __main__.py             # 命令行入口
├── tests/                      # 测试目录
│   ├── __init__.py             # 测试包初始化
│   └── test_lema001.py         # 单元测试
├── .gitignore                  # Git 忽略配置
├── MANIFEST.in                 # 打包清单
├── pyproject.toml              # 现代项目配置（PEP 517/518）
├── setup.py                    # 传统安装配置（向后兼容）
├── requirements.txt            # 项目依赖列表
├── README.md                   # 项目说明文档，含快速开始和验证指南（本文件）
├── LICENSE                     # MIT 许可证
└── test_install.py             # 功能测试脚本
```

### 8.1 🔍 关键配置文件说明

#### 8.1.1 pyproject.toml（主要配置文件）
- 使用现代 Python 打包标准 (PEP 517/518)
- 定义了项目元数据、依赖、分类等
- 配置了命令行工具入口 `lema001`
- 包含开发依赖和工具配置

#### 8.1.2 setup.py（兼容性配置）
- 用于兼容旧的构建工具
- 与 pyproject.toml 保持一致的配置
- 支持传统的 `pip install .` 安装方式

#### 8.1.3 lema001/__init__.py（包核心）
- 定义了版本号 `__version__ = "0.1.0"`
- 提供了示例函数 `hello()`
- 提供了命令行入口函数 `main()`

## 9. 📝 示例

```python
from lema001 import hello, main

# 使用 hello 函数
print(hello())

# 运行主函数
main()
```

## 10. 🔧 开发

### 10.1 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/jingyu-yang/lema001.git
cd lema001

# 创建虚拟环境
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 安装开发依赖
pip install -e .[dev]
```

### 10.2 运行测试

```bash
pytest
```

### 10.3 代码格式化

```bash
# 使用 black 格式化代码
black lema001

# 使用 flake8 检查代码风格
flake8 lema001

# 使用 mypy 进行类型检查
mypy lema001
```

######################################################################
######################################################################
# 3. PyPI 发布指南🚀 

## 3.1 📋 准备工作

#### 安装必要的工具

```bash
pip install build twine
```

####  构建项目

```bash
# 清理旧的构建文件（Windows PowerShell）
Remove-Item -Recurse -Force build, dist, *.egg-info

# 构建分发包
python -m build

# 检查构建结果
twine check dist/*
```

这会生成两个文件：
- `lema001-0.1.0.tar.gz` - 源码分发包
- `lema001-0.1.0-py3-none-any.whl` - Wheel 包



#### 11.2.1 注册并配置

- 访问 https://test.pypi.org/account/register/ 注册账号
- 创建 API token
- 配置 `~/.pypirc` 文件：

```ini
[distutils]
index-servers =
    testpypi
    pypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-你的-token

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-你的-token
```

### 11.2 🧪 测试上传（TestPyPI）

在正式发布前，建议先上传到 TestPyPI 进行测试。

```bash
twine upload --repository testpypi dist/*
```

#### 11.3 测试安装

```bash
pip install --index-url testpypi lema001
```

### 11.3 🚀 正式发布到 PyPI

#### 11.3.1 注册 PyPI 账号

访问 https://pypi.org/account/register/ 注册账号并验证邮箱

#### 11.3.2 创建并配置 API token

- 在 PyPI 网站设置中创建 API token
- 将 token 保存到 `~/.pypirc` 文件（见上方配置）

#### 11.3.3 上传到 PyPI

```bash
twine upload dist/*
```

#### 11.3.4 验证发布

访问 https://pypi.org/project/lema001/ 查看你的项目

### 11.4 🔄 更新版本

#### 11.4.1 更新版本号

需要同时修改以下三个文件：

**pyproject.toml**:
```toml
version = "0.1.1"  # 递增版本号
```

**lema001/__init__.py**:
```python
__version__ = "0.1.1"
```

**setup.py**:
```python
version="0.1.1"
```

#### 11.4.2 重新构建和发布

```bash
# 清理
Remove-Item -Recurse -Force build, dist, *.egg-info

# 构建
python -m build

# 上传
twine upload dist/*
```

### 11.5 📝 版本号规范

遵循语义化版本控制 (Semantic Versioning)：

- **MAJOR.MINOR.PATCH** (主版本号。次版本号。修订号)
- **MAJOR**: 不兼容的 API 变更
- **MINOR**: 向后兼容的功能新增
- **PATCH**: 向后兼容的问题修正

示例：
- 0.1.0 - 初始发布
- 0.1.1 - 修复 bug
- 0.2.0 - 新增功能
- 1.0.0 - 稳定版本

### 11.6 ⚠️ 注意事项

1. **不要删除已发布的版本** - PyPI 不允许删除已发布的版本
2. **不要重复使用版本号** - 每个版本号只能使用一次
3. **谨慎上传** - 上传前务必在 TestPyPI 测试
4. **保护 token** - 不要将 API token 提交到代码仓库
5. **阅读官方文档** - https://packaging.python.org/

### 11.7 🔗 相关链接

- PyPI 官方文档：https://pypi.org/help/
- Python 打包指南：https://packaging.python.org/
- TestPyPI: https://test.pypi.org/
- 语义化版本：https://semver.org/

### 11.8 💡 常见问题

**Q: 上传时提示"File already exists"**  
A: 版本号重复，需要修改版本号后重新构建

**Q: 如何删除已上传的包？**  
A: PyPI 不允许删除包，但可以发布新版本覆盖

**Q: 忘记添加某个文件怎么办？**  
A: 修改版本号，补充文件后重新发布



## 12. ✅ 发布前检查清单

在发布到 PyPI 之前，请确保完成以下检查：

### 12.1 ⚠️ 必须确认的项目

- [ ] **作者信息已更新** - pyproject.toml、setup.py 和 README.md 中的作者信息都已修改为你的真实信息
- [ ] **GitHub 链接已更新** - 所有 GitHub URL 都已替换为你的实际仓库地址
- [ ] **联系方式已更新** - README.md 中的联系方式是你的真实邮箱
- [ ] **版本号正确** - pyproject.toml、setup.py 和 lema001/__init__.py 中的版本号一致
- [ ] **本地测试通过** - 能够成功构建并安装
- [ ] **功能测试通过** - test_install.py 所有测试通过
- [ ] **单元测试通过** - pytest 运行所有测试通过
- [ ] **命令行工具正常** - `lema001` 命令可以正常执行

### 12.2 🧪 本地测试步骤

```bash
# 1. 安装必要的工具
pip install build twine pytest

# 2. 清理并构建
Remove-Item -Recurse -Force build, dist, *.egg-info
python -m build

# 3. 检查构建结果
twine check dist/*

# 4. 本地安装测试
pip install .

# 5. 运行功能测试
python test_install.py

# 6. 测试命令行工具
lema001
```

### 12.3 🔍 验证命令汇总

```bash
# 查看项目结构
tree /F /A

# 检查 Python 语法
python -m py_compile lema001/__init__.py
python -m py_compile lema001/__main__.py

# 运行所有测试
pytest -v

# 构建包
python -m build

# 检查包
twine check dist/*

# 查看生成的文件
ls dist/
```

## 13. 💡 重要提示

1. **版本号管理**: 版本号在三个地方定义
   - `pyproject.toml` 
   - `setup.py`
   - `lema001/__init__.py`
   
   确保同步更新！

2. **不要重复使用版本号**: PyPI 不允许删除已发布的包，每个版本号只能用一次

3. **先在 TestPyPI 测试**: 避免直接发布到正式环境

4. **保护 API Token**: 不要将 API token 提交到 Git 仓库

5. **阅读官方文档**: https://packaging.python.org/

6. **文件编码**: 确保所有文件都使用 UTF-8 编码

## 14. 📚 参考资源

- **Python 打包官方指南**: https://packaging.python.org/
- **PyPI 帮助文档**: https://pypi.org/help/
- **TestPyPI**: https://test.pypi.org/
- **语义化版本**: https://semver.org/

---

本项目完全符合 PyPI 标准，并已经发布到PyPI上！ 🎉 
自2026年3月会不定期的发布本项目最新版本到PyPI上，并预祝未来每次发布顺利！🎉。