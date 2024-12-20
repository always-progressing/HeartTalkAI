from flask import Flask, request, jsonify, send_from_directory
import threading
import SparkApi  # 根据您的代码修改

app = Flask(__name__)

# 启动 WebSocket 和对话处理的线程
def start_chat_thread(question, ws_url, appid, api_key, api_secret, domain):
    SparkApi.main(appid, api_key, api_secret, ws_url, domain, question)

@app.route('/')
def index():
    # 返回 index.html 文件
    return send_from_directory('.', 'index.html')

@app.route('/get_reply', methods=['POST'])
def get_reply():
    user_message = request.json.get('message')

    # 启动一个线程来处理 WebSocket 和生成对话
    # threading.Thread(target=start_chat_thread, args=(
    #     user_message,
    #     "wss://maas-api.cn-huabei-1.xf-yun.com/v1.1/chat",
    #     '916751a0',
    #     '509c5399bb1c8606ed210aa9c0d67bac',
    #     'MzBiN2M2ZTU1NjQ2MWRkMWRmZDc3ZmVk',
    #     'xqwen257bchat'
    # )).start()
    # # 启动对话处理
    SparkApi.answer = ""  # 清空上一次的回答
    SparkApi.main(
        '916751a0',
        '509c5399bb1c8606ed210aa9c0d67bac',
        'MzBiN2M2ZTU1NjQ2MWRkMWRmZDc3ZmVk',
        "wss://maas-api.cn-huabei-1.xf-yun.com/v1.1/chat",
        "xqwen257bchat",
        user_message
    )

    # return jsonify({"reply": "正在处理您的请求..."})  # 占位符
    # 返回生成的回答给前端
    return jsonify({"reply": SparkApi.answer})

if __name__ == '__main__':
    app.run(debug=True)
