import SparkApi
import json

# 读取配置文件
def load_config():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config

# 加载配置
config = load_config()

# 获取配置中的值
appid = config["APP_ID"]
api_key = config["API_KEY"]
api_secret = config["API_SECRET"]
Spark_url = "wss://maas-api.cn-huabei-1.xf-yun.com/v1.1/chat"  # 微调v1.5环境的地址
# Spark_url = "wss://spark-api-n.xf-yun.com/v3.1/chat"  # 微调v3.0环境的地址

# 调用微调大模型时，设置为“patch”
domain = "xqwen257bchat"  # 你可以根据需要修改这个值

text =[]

# length = 0

def getText(role,content):
    jsoncon = {}
    jsoncon["role"] = role
    jsoncon["content"] = content
    text.append(jsoncon)
    return text

def getlength(text):
    length = 0
    for content in text:
        temp = content["content"]
        leng = len(temp)
        length += leng
    return length

def checklen(text):
    while (getlength(text) > 8000):
        del text[0]
    return text
    


if __name__ == '__main__':
    text.clear
    while(1):
        Input = input("\n" +"我:")
        question = checklen(getText("user",Input))
        SparkApi.answer =""
        print("星火:",end = "")
        SparkApi.main(appid,api_key,api_secret,Spark_url,domain,question)
        getText("assistant",SparkApi.answer)
        # print(str(text))

