# 测试百度在线图片文本识别包
# 导入百度的OCR包

from aip import AipOcr

def Ocr(image):
    # 此处填入在百度云控制台处获得的appId, apiKey, secretKey的实际值
    #不能开梯子
    appId, apiKey, secretKey = ['32401483', 'tbjxGjB5ejZCG2ICad08Qh9l', 'mGC8IqjRMaY6V5phGqdBgq3cLw0oSzXE']
    # 创建ocr对象
    client = AipOcr(appId, apiKey, secretKey)
    with open(image, 'rb') as fin:
        img = fin.read()
        # print('okk1')
        res = client.basicGeneral(img)
        # print('okk2')
        str = res['words_result']
        # print('okk')
        ans = ""
        for x in str:
            ans = ans + x['words']
        if ans == "":
            return ""
        return "车牌为：" + ans
        #return "车牌为："+str[0]["words"]
# print(Ocr('1.png'))