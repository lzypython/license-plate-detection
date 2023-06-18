# 测试百度在线图片文本识别包
# 导入百度的OCR包

from aip import AipOcr

def Ocr(image):
    # 此处填入在百度云控制台处获得的appId, apiKey, secretKey的实际值
    appId, apiKey, secretKey = ['28509942', 'HbB3GChFwWENkXEI7uCuNG5V', 'IRnFhizLzlXnYFiNoq3VcyLxRHaj2dZU']
    # 创建ocr对象
    ocr = AipOcr(appId, apiKey, secretKey)
    with open(image, 'rb') as fin:
        img = fin.read()
        res = ocr.basicGeneral(img)
        return res['words_result'][0]["words"]


# print(Ocr("1.png"))