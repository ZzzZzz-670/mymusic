import requests


url = "https://music.163.com/"

headers = {
    'referer': 'https://cn.bing.com/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
}

# Cookies 字典
# cookies = {
#     '_iuqxldmzr_': '32',
#     '_ntes_nnid': 'a823a47c6f9ac9c848cecd5eeed983d4,1751350617046',
#     '_ntes_nuid': 'a823a47c6f9ac9c848cecd5eeed983d4',
#     'NMTID': '00O_Zvx-FzuzUtedUzzsSI6oh2y2MoAAAGXxJ8LDw',
#     'WEVNSM': '1.0.0',
#     'WNMCID': 'ajbrxp.1751350619110.01.0',
#     'WM_NI': 'U/GGlzh3x6taCBspZJUzxkwVMeB53spt/8C81jwe1YpT0ykjd3Rq3HW1fCRTsglTxzGfJcneIwfLmKnIbH6ljwoYH1MRR3pzjeuY86c5ifttaWDApcQ30nTNbFHEGsy/QmU=',
#     'WM_NIKE': '9ca17ae2e6ffcda170e2e6eea5cc6af8ac8296ce3ea79e8ba2d44b939b9facd26bb38a008daa4081b69f87cc2af0fea7c3b92a97f189a8ef72acedb8d7f76b819ebd91d94297a6b88cf65e8fbb8ed6b279b4ace1d9c234f3b6b986b453b48c009aea62a8ed9e92b24495efaaa4d160b1b9a4b5fb7285ba8684ed6f8ba9aaadf041ae97aea9b568aaa9a1bacb3b8f8e9ed4f372aabbbbbabb3ea1eba787f780a3898ca2f36993ed008fd746a29a88a6c679bbf19f8ed837e2a3',
#     'WM_TID': 'hsXGgINJSsRAEBURVFeTP+BB0l+8HzQac',
#     'ntes_utid': 'tid._.Qx5zPvBR3YZBQxFUARbSf6Eggu5Hp0U6._.0',
#     'sDeviceId': 'YD-lM1i+2vuDFpAR1AVVQPCKuUk0rtS4gVv',
#     'JSESSIONID-WYYY': 'vuzZY3WT9Qn8Y692XRBkvZoHG4f/ljfyQpFWk2e9ucWt28tspBguSOKYiJEVdtR+FI1RjWoTdKQzzNIrBG3cjMvrAWgMR85PdgM3Z64Do9k1zz0g0RYK1REHZR%5Cl175yru/M7Y4t1A3Ho6XmquFJ6a1caMoSdOY/eIT9%5Ct1Izof8fSRK%3A1751370734098'
# }

# 发送 GET 请求
response = requests.get('https://music.163.com/', headers=headers, cookies=None)

# 打印响应内容
print(response.status_code)
# print(response.text)

response.text
