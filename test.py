import SparkApi_fortest
import json
import random

# 读取配置文件
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config

# 随机生成一个名字
def generate_random_name():
    names = ["星光", "晨曦", "微光", "曙光", "明辉"]  # 可根据需要添加更多名字
    return random.choice(names)

# 加载配置
config = load_config()

# 获取配置中的值
appid = "916751a0"
api_key = "509c5399bb1c8606ed210aa9c0d67bac"
api_secret = "MzBiN2M2ZTU1NjQ2MWRkMWRmZDc3ZmVk"
Spark_url = "wss://maas-api.cn-huabei-1.xf-yun.com/v1.1/chat"  # 微调v1.5环境的地址
# Spark_url = "wss://spark-api-n.xf-yun.com/v3.1/chat"  # 微调v3.0环境的地址

# 调用微调大模型时，设置为“patch”
domain = "xqwen257bchat"  # 你可以根据需要修改这个值

# 初始化对话
text = []

# 向对话中添加初始化的提示
def add_initial_prompt():
    initial_prompts = [
        {
            "role": "system",
            "content": "你是一个友善且理解他人的网络助手，擅长倾听并提供心理支持，帮助用户解决内心困扰。"
        },
        {
            "role": "system",
            "content": "请用真诚和富有创意的回复，提供共情、支持和建议。你可以加入一些个性的颜文字，让对话更温暖。"
        },
        {
            "role": "system",
            "content": "如果用户只是打招呼，回应时简单而友好；如果用户分享快乐心情，提供积极的共情回复。"
        },
        {
            "role": "system",
            "content": "当用户表示感谢时，回复带有温暖的感谢，鼓励他们以后继续聊天。"
        }

    ]
    for prompt in initial_prompts:
        text.append(prompt)

# 计算对话长度
def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

# 检查对话长度，避免超过最大长度
def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text

# 添加用户输入到对话中
def getText(role, content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

if __name__ == '__main__':
    text.clear()
    add_initial_prompt()  # 添加初始化的提示信息
    assistant_name = generate_random_name()  # 随机生成助手名字
    while True:
        Input = input("\n" + "我:")
        question = checklen(getText("user", Input))
        SparkApi_fortest.answer = ""
        print(f"{assistant_name}:", end="")
        SparkApi_fortest.main(appid, api_key, api_secret, Spark_url, domain, question)
        getText("assistant", SparkApi_fortest.answer)
