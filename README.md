# 心语桥——AI心理论坛
这是一个基于在讯飞星辰Maas平台上微调的Qwen-7b模型的心理咨询论坛，旨在为用户提供情感支持和心理辅导。用户可以通过简单的界面与 AI 聊天，获得个性化的建议和反馈。（持续完善中）
## 功能特点
- 用户可以通过网页与 AI 进行对话。
- 支持情感倾诉、心理咨询、生活困扰等内容的交流。
- 使用微调的 AI 模型进行对话和情感共情，模拟真实且更温暖的论坛氛围。

## 架构
```
my_project/
├── app.py                   # Flask 后端主程序
├── SparkApi.py              # 调用 API 和处理 WebSocket 请求的 Python 脚本
├── index.html               # 前端 HTML 页面
├── test.py                  # 调用api体验模型，直接运行即可体验
├── README.md                # 项目说明文档
```

## 如何体验？
### **在网站上直接体验！**
https://hearttalkai-2.onrender.com/
![image](https://github.com/user-attachments/assets/93052738-692e-4272-b1e8-620117d019c8)

### 1. 运行python脚本体验
1. 下载项目代码
2. 运行test.py
比如在git bash，进入项目根目录，运行test.py
```bash
python test.py
```
4. 在控制台的“我：”后输入想说的话后回车即可（若在终端或命令行运行同理）
![屏幕截图 2024-12-20 184157](https://github.com/user-attachments/assets/7bb76cfb-0b14-45f3-b803-54facb33f8b9)

### 2. 在本机html网页上体验
#### 1. 安装依赖
确保您已安装 Python 3 和 pip。然后，安装所需的 Python 包。
安装Flask、websocket-client
```bash
pip install flask
pip install websocket-client
```
我的版本如下：
Flask==3.0.3
websocket-client==1.8.0

#### 2. 将项目下载到本地
在bash中进入项目根目录

#### 3. 启动 Flask 服务
运行 app.py 启动本地服务器：

```bash
python app.py
```
Flask 默认会在 http://127.0.0.1:5000/ 启动服务。您可以通过浏览器访问该 URL，开始体验心理论坛。
如下图，在文本框中尽情倾诉，随后点击发送即可。
![屏幕截图 2024-12-20 224502](https://github.com/user-attachments/assets/c8fb1522-e2a5-4e45-9fbb-ea2df45882de)

