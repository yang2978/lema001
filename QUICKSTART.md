# 快速验证你的 Python 包

## ✅ 检查清单

在发布到 PyPI 之前，请完成以下检查：

### 1. 更新个人信息

- [ ] 修改 `pyproject.toml` 中的作者信息
  - 将 `Your Name` 改为你的真实姓名
  - 将 `your.email@example.com` 改为你的邮箱
  - 更新 GitHub URL

- [ ] 修改 `setup.py` 中的相同信息

- [ ] 修改 `README.md` 中的链接
  - 将 `yourusername` 改为你的 GitHub 用户名
  - 更新联系方式

### 2. 本地测试

```bash
# 安装必要的工具
pip install build twine pytest

# 清理旧的构建文件（PowerShell）
Remove-Item -Recurse -Force build, dist, *.egg-info

# 或者使用命令提示符
rmdir /s /q build dist *.egg-info

# 构建项目
python -m build

# 检查构建结果
twine check dist/*

# 本地安装测试
pip install .

# 运行测试
pytest
```

### 3. 功能测试

创建测试脚本 `test_install.py`:

```python
import lema001

# 测试导入
print(f"成功导入 lema001 v{lema001.__version__}")

# 测试函数
result = lema001.hello()
print(f"hello() 返回：{result}")

# 测试主函数
print("运行 main():")
lema001.main()
```

运行测试：
```bash
python test_install.py
```

### 4. 命令行工具测试

安装后测试命令行工具：
```bash
lema001
```

或者：
```bash
python -m lema001
```

## 📦 项目结构说明

```
lema001/
├── lema001/              # 主要 Python 包
│   ├── __init__.py       # 包初始化，包含版本号和主要函数
│   └── __main__.py       # 命令行入口
├── tests/                # 测试目录
│   ├── __init__.py
│   └── test_lema001.py
├── .gitignore            # Git 忽略文件
├── MANIFEST.in           # 打包清单
├── pyproject.toml        # 现代 Python 项目配置（推荐）
├── setup.py              # 传统安装配置（兼容旧工具）
├── requirements.txt      # 项目依赖
├── README.md             # 项目说明（会显示在 PyPI）
├── LICENSE               # 许可证
└── PUBLISHING.md         # 发布指南
```

## 🎯 下一步

1. 完成上述检查和修改
2. 阅读 [PUBLISHING.md](PUBLISHING.md) 了解如何发布到 PyPI
3. 先在 TestPyPI 测试发布
4. 正式发布到 PyPI

## 🔍 验证命令汇总

```bash
# 1. 查看项目结构
tree /F /A

# 2. 检查 Python 语法
python -m py_compile lema001/__init__.py
python -m py_compile lema001/__main__.py

# 3. 运行所有测试
pytest -v

# 4. 构建包
python -m build

# 5. 检查包
twine check dist/*

# 6. 查看生成的文件
ls dist/
```

## 💡 提示

- 确保所有文件都使用 UTF-8 编码
- 版本号在三个地方需要同步更新：
  - `pyproject.toml`
  - `setup.py`
  - `lema001/__init__.py`
- 每次发布使用新的版本号
- 先在 TestPyPI 测试，再正式发布

祝你好运！🚀
