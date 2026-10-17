本项目是一个基于 Python + Pytest + Requests 搭建的接口自动化测试框架，用于验证 JSONPlaceholder 开放 API 的功能与稳定性。
项目采用分层设计，支持配置分离、参数化测试，并能生成可视化的 HTML 测试报告。

📂 项目结构
text
├── config/                 # 配置文件目录
│   └── settings.py         # 存放基础 URL 等全局配置，实现环境隔离
├── test_cases/             # 测试用例目录
│   └── test_posts.py       # 核心接口测试脚本
├── run_test.bat            # 一键执行脚本（自动跑测试并生成报告）
├── report.html             # 自动化生成的 HTML 测试报告
└── README.md               # 项目说明文档

🧪 测试覆盖范围
1. 正向测试 (Happy Path)：请求存在的资源（ID=1），断言状态码为 200，且返回数据 ID 匹配。
2. 逆向测试 (Negative Testing)：请求不存在的资源（ID=9999），断言系统能正确返回 404 状态码。
3. 数据交互测试 (POST)：构造 JSON 数据发送 POST 请求创建文章，断言返回 201 (Created) 且数据一致。
4. 参数化测试 (Data-Driven)：使用 @pytest.mark.parametrize，用一套代码覆盖多条不同 ID 的并发验证逻辑。
   
🛠️ 技术栈
· Python 3.x
· Requests (HTTP 请求库)
· Pytest (单元测试框架)
· Pytest-HTML (测试报告生成插件)

🚀 如何运行
1. 安装依赖：pip install requests pytest pytest-html
2. 运行测试：
   · 方式一：在终端执行 pytest test_cases/ --html=report.html
   · 方式二（推荐）：直接双击运行根目录下的 run_test.bat 脚本
3. 查看报告：在浏览器中打开生成的 report.html 文件。
