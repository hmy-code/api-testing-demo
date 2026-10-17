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
   
 📝 开发与排错记录 (Troubleshooting)

在开发本项目过程中，我遇到并解决了以下真实环境问题，记录了宝贵的实战经验：

1. **接口路径 404 异常排查**
   - **问题**：测试用例报错 `404 != 200。
   - **解决**：排查发现请求 URL 路径拼写错误，修正为正确的 `/posts/1` 后测试通过。体会到看日志排查网络请求的基础重要性。

2. **断言 KeyError 异常**
   - **问题**：获取数据时报错，数据解析失败。
   - **解决**：排查发现向服务器发送的 `POST` 数据字典中，字段名 `title` 被误拼写为 `titile`，修正后接口正确返回。

3. **Pytest 参数化插件兼容问题**
   - **问题**：运行参数化用例时，报错 `UnknownMarkWarning` 且无法识别 `parametrize`。
   - **解决**：排查确认是环境缺少相关依赖，通过终端执行 `pip install pytest-parametrize` 安装插件解决；同时修正了单词拼写错误。

4. **跨目录导包 ModuleNotFoundError**
   - **问题**：将配置抽离到 `config` 文件夹后，测试用例无法正常导入 `settings.py` 中的变量。
   - **解决**：在测试脚本顶部引入 `sys` 和 `os`，通过 `sys.path.append` 动态添加系统路径，实现配置分离架构。

5. **Git 上传与认证问题**
   - **问题**：执行 `git push` 时提示 `src refspec main does not match any`，且弹窗提示证书不受信任。
   - **解决**：发现是未配置全局邮箱及未执行 `git commit` 导致；通过 `git config --global` 配置身份信息，并在推送时正确通过浏览器授权解决。
