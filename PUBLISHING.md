# lema001 发布指南

本指南将帮助你将 lema001 项目发布到 PyPI。

## 📋 准备工作

### 1. 安装必要的工具

```bash
pip install build twine
```

### 2. 修改配置信息

在发布之前，请确保修改以下文件中的占位符信息：

#### pyproject.toml
- 将 `Your Name` 替换为你的真实姓名
- 将 `your.email@example.com` 替换为你的邮箱
- 将 GitHub URL 替换为你的实际仓库地址

#### setup.py
- 同样修改作者信息和 GitHub URL

#### README.md
- 将 `yourusername` 替换为你的 GitHub 用户名
- 将联系方式替换为你的实际信息

## 🏗️ 构建项目

### 1. 清理旧的构建文件

```bash
# Windows PowerShell
Remove-Item -Recurse -Force build, dist, *.egg-info

# Linux/Mac
rm -rf build dist *.egg-info
```

### 2. 构建分发包

```bash
python -m build
```

这会在 `dist/` 目录下生成两个文件：
- `lema001-0.1.0.tar.gz` - 源码分发包
- `lema001-0.1.0-py3-none-any.whl` - Wheel 包

### 3. 检查构建结果

```bash
twine check dist/*
```

确保没有错误提示。

## 🧪 测试上传（TestPyPI）

在正式发布前，建议先上传到 TestPyPI 进行测试。

### 1. 注册 TestPyPI 账号

访问 https://test.pypi.org/account/register/ 注册账号

### 2. 创建 API token

在 TestPyPI 网站设置中创建 API token

### 3. 配置 ~/.pypirc 文件

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

### 4. 上传到 TestPyPI

```bash
twine upload --repository testpypi dist/*
```

### 5. 测试安装

```bash
pip install --index-url testpypi lema001
```

## 🚀 正式发布到 PyPI

### 1. 注册 PyPI 账号

访问 https://pypi.org/account/register/ 注册账号

### 2. 验证邮箱

检查邮箱并验证账户

### 3. 创建 API token

在 PyPI 网站设置中创建 API token

### 4. 保存 token

将 token 保存到 `~/.pypirc` 文件（见上方配置）

### 5. 上传到 PyPI

```bash
twine upload dist/*
```

### 6. 验证发布

访问 https://pypi.org/project/lema001/ 查看你的项目

## 📦 从 PyPI 安装

发布后，用户可以通过以下方式安装：

```bash
pip install lema001
```

## 🔄 更新版本

### 1. 更新版本号

修改以下文件中的版本号：

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

### 2. 重新构建和发布

```bash
# 清理
Remove-Item -Recurse -Force build, dist, *.egg-info

# 构建
python -m build

# 上传
twine upload dist/*
```

## 📝 版本号规范

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

## ⚠️ 注意事项

1. **不要删除已发布的版本** - PyPI 不允许删除已发布的版本
2. **不要重复使用版本号** - 每个版本号只能使用一次
3. **谨慎上传** - 上传前务必在 TestPyPI 测试
4. **保护 token** - 不要将 API token 提交到代码仓库
5. **阅读官方文档** - https://packaging.python.org/

## 🔗 相关链接

- PyPI 官方文档：https://pypi.org/help/
- Python 打包指南：https://packaging.python.org/
- TestPyPI: https://test.pypi.org/
- 语义化版本：https://semver.org/

## 💡 常见问题

### Q: 上传时提示"File already exists"
A: 版本号重复，需要修改版本号后重新构建

### Q: 如何删除已上传的包？
A: PyPI 不允许删除包，但可以发布新版本覆盖

### Q: 忘记添加某个文件怎么办？
A: 修改版本号，补充文件后重新发布

---

祝你发布顺利！🎉
