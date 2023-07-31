import requests
# permission.94wan.fun
# card.94wan.fun
# 根据实际情况修改即可！
# cron: 10 20 * * *
# const $ = new Env('叼虎网络连通性测试');

url = 'http://permission.94wan.fun:53334'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
try:
    response = requests.get(url, headers=headers)
    response.raise_for_status() 
    data = response.json() 
    print('\n调试成功:',data['message'],'\n\n')

except requests.exceptions.RequestException as e:
    print('请求错误:', response.text,e)

url = 'http://fn.syyx.com/my_ip'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}
try:
    response = requests.get(url, headers=headers)
    print('调试成功: 你的IP是 『',response.text,'』')

except requests.exceptions.RequestException as e:
    print('请求错误:', response.text,e)
