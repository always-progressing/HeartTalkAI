# 心语桥——AI心理论坛（持续更新中）
这是一个基于 微调后的Qwen-7b 模型的心理咨询论坛，旨在为用户提供情感支持和心理辅导。用户可以通过简单的界面与 AI 聊天，获得个性化的建议和反馈。
## 功能特点
- 用户可以通过网页与 AI 进行对话。
- 支持情感倾诉、心理咨询、生活困扰等内容的交流。
- 使用微调的 AI 模型进行对话和情感共情，模拟真实且更温暖的论坛氛围。

### 1. 安装依赖
确保您已安装 Python 3 和 pip。然后，安装所需的 Python 包。
安装Flask、websocket-client
```bash
pip install flask
pip install websocket-client
```
我的版本如下：
Flask==3.0.3
websocket-client==1.8.0

### 2. 将项目下载到本地
在bash中进入项目根目录

3. 启动 Flask 服务
运行 app.py 启动本地服务器：

```bash
python app.py
```
Flask 默认会在 http://127.0.0.1:5000/ 启动服务。您可以通过浏览器访问该 URL，开始体验心理论坛。
如下图，在文本框中尽情倾诉，随后点击发送即可。
![屏幕截图 2024-12-20 224502](https://github.com/user-attachments/assets/c8fb1522-e2a5-4e45-9fbb-ea2df45882de)

