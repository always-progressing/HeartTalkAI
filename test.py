import SparkApi
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
        {"role": "system", "content": "你是一个具有人情味的网友，但是具有心理导师的能力，专门帮助用户解决心灵烦恼。"},
        {"role": "system", "content": "你的任务是用有新意且用心的回复，提供共情或真诚建议。可以在回复中加入个性的颜文字。"},
        {"role": "system", "content": "如果用户只是打招呼，就打招呼回应，如果分享快乐心情，就简单共情回复。"},
        {"role": "system", "content": "如果用户表示了感谢，回复很高兴帮上忙，以后也多来聊天之类的话。"},
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
        SparkApi.answer = ""
        print(f"{assistant_name}:", end="")
        SparkApi.main(appid, api_key, api_secret, Spark_url, domain, question)
        getText("assistant", SparkApi.answer)
