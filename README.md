# lema001

[![PyPI version](https://badge.fury.io/py/lema001.svg)](https://badge.fury.io/py/lema001)
[![Python Versions](https://img.shields.io/pypi/pyversions/lema001.svg)](https://pypi.org/project/lema001/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## 1. Summary
lema是一组AI相关项目的集合，所有项目都以 lema 打头后面加序号，本项目是第一个项目。
本项目命名为lema001，是一组AI Agent Runtime 所需的基础功能。
本项目构建成python模块，并发布到PyPI上，其他系统可以通过 PIP install 安装，并在自身的 Agent应用中通过 import lema001 导入相关功能。

📖 功能特性： 

**注意**: 当前本项目还处在实验期，可能存在未知的安全问题。



### 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

### 🤝 贡献

欢迎提交 Issue 和 Pull Request！

### 📬 联系方式

- Author: jingyu.yang
- Email: 15801554959@aliyun.com


###############################################################################################
###############################################################################################


## 2. 使用者：如何安装和使用lema001模块

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

### 如何快速使用lema001

#### 作为 Python 模块使用

```python
import lema001 #或from lema001 import hello, main

# 调用 hello 函数
result = lema001.hello()
print(result)  # 输出：Hello from lema001!

# 查看版本
print(lema001.__version__)  # 输出：0.1.0

# 运行主函数
main()
```

#### 使用命令行工具

安装后，你可以在终端中直接运行：

```bash
lema001
```

或者作为模块运行：

```bash
python -m lema001
```



##############################################################
## 3. 项目贡献者：如何开发?

### 设置开发环境

```bash
# 克隆仓库
git clone https://github.com/yang2978/lema001.git
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


### 📁 项目结构及关键文件用途说明

```
lema001/
├── lema001/                    # Python 包主目录
│   ├── __init__.py             # 包初始化，包含版本号和 API
│   └── __main__.py             # 命令行入口
|   |__ xxx.py                  # 模块文件
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

#### pyproject.toml（主要配置文件）
- 使用现代 Python 打包标准 (PEP 517/518)
- 定义了项目元数据、依赖、分类等
- 配置了命令行工具入口 `lema001`
- 包含开发依赖和工具配置

#### setup.py（兼容性配置）
- 用于兼容旧的构建工具
- 与 pyproject.toml 保持一致的配置
- 支持传统的 `pip install .` 安装方式

#### lema001/__init__.py（包核心）
- 定义了版本号 `__version__ = "0.1.0"`


######################################################################
######################################################################
# 4. PyPI 发布指南🚀 

## 📋 准备工作

#### 注册并配置

注册两个账号：

- 注册测试账号：访问 https://test.pypi.org/account/register/ 
- 在 PyPI 网站设置中创建测试账号下的API token：pypi-test-token
- 注册正式账号：访问 https://pypi.org/account/register/ 并验证邮箱
- 在 PyPI 网站设置中创建正式账号下的 API token：pypi-token
- 
- 配置 `~/.pypirc` 文件，将 token 保存到该文件中:

```ini
[distutils]
index-servers =
    testpypi
    pypi

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-test-token

[pypi]
repository = https://upload.pypi.org/legacy/
username = __token__
password = pypi-token
```


#### 安装必要的工具

```bash
pip install build twine
```

## **每次发布需要做的事情：**

### 更新版本号

#### 📝 版本号规范

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

#### 需要同时修改以下三个文件中的版本号：

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

###  构建项目

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


### ✅ 发布前检查清单

**在发布到 PyPI 之前，请确保完成以下检查：**⚠️ 
- [ ] **版本号正确** - pyproject.toml、setup.py 和 lema001/__init__.py 中的版本号一致
- [ ] **不要重复使用版本号**: PyPI 不允许删除已发布的包，每个版本号只能用一次
- [ ] **不要删除已发布的版本** - PyPI 不允许删除已发布的版本
  
- [ ] **作者信息已更新** - pyproject.toml、setup.py 和 README.md 中的作者信息都已修改为你的真实信息
- [ ] **GitHub 链接已更新** - 所有 GitHub URL 都已替换为你的实际仓库地址
- [ ] **联系方式已更新** - README.md 中的联系方式是你的真实邮箱
- [ ] **本地测试通过** - 能够成功构建并安装
- [ ] **功能测试通过** - test_install.py 所有测试通过
- [ ] **单元测试通过** - pytest 运行所有测试通过
- [ ] **命令行工具正常** - `lema001` 命令可以正常执行
- [ ] **文件编码**: 确保所有文件都使用 UTF-8 编码
- [ ] **保护 API Token**: 不要将 API token 提交到 Git 仓库
- [ ] **谨慎上传,先在 TestPyPI 测试**: 避免直接发布到正式环境
   

** 🔍 验证命令汇总**

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



### 🧪 测试上传（TestPyPI）

在正式发布前，建议先上传到 TestPyPI 进行测试。

```bash
twine upload --repository testpypi dist/*
pip install --index-url testpypi lema001
```

### 🚀 正式发布到 PyPI

```bash
twine upload dist/*
```

**验证发布**: 访问 https://pypi.org/project/lema001/ 查看你的项目


### 💡 常见问题

**Q: 上传时提示"File already exists"**  
A: 版本号重复，需要修改版本号后重新构建

**Q: 如何删除已上传的包？**  
A: PyPI 不允许删除包，但可以发布新版本覆盖

**Q: 忘记添加某个文件怎么办？**  
A: 修改版本号，补充文件后重新发布

**相关链接：**
- **阅读官方文档**: https://packaging.python.org/
- **PyPI 官方文档**：https://pypi.org/help/
- **Python 打包指南**：https://packaging.python.org/
- **TestPyPI**: https://test.pypi.org/
- **语义化版本**：https://semver.org/

本项目完全符合 PyPI 标准，并已经发布到PyPI上！ 🎉 
自2026年3月会不定期的发布本项目最新版本到PyPI上，并预祝未来每次发布顺利！🎉。