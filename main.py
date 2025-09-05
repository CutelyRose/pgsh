import requests
import time
from jsonpath import jsonpath

token='' # 填自己获取的token

print('此程序仅供学习，切勿用于非法用途')
try:
    t=str(int(time.time()*1000))

    headers={'Authorization':token,
             'Version':'1.59.3',
             'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
             'User-Agent':'okhttp/3.14.9',
             'timestamp':t,
             'Host':'userapi.qiekj.com',
             'channel':'channel',
             'phoneBrand':'Redmi'}
    data1={'categoryCode':'5','token':token}
    response_list=requests.post(url='https://userapi.qiekj.com/goods/latestUsed',headers=headers,data=data1)
    result_name=jsonpath(response_list.json(),'$..goodsName')
    result_goodsId=jsonpath(response_list.json(),'$..goodsId')
    for i,name in enumerate(result_name):
        print(f"{i+1}:{name}")
    choice=int(input('请输入你的选择\n'))
    data2={'goodsId':result_goodsId[choice-1],'token':token}
    response_skuId=requests.post(url='https://userapi.qiekj.com/goods/normal/skus',headers=headers,data=data2)
    result_skuId=jsonpath(response_skuId.json(),'$.data[0].skuId')
    print(result_skuId[0]) # 获取skuid
    data3={'skuId':result_skuId[0],'promotions':'[{"assetId":"0","oldPromotionId":"","orgId":"0","promotionId":"0","promotionType":"-6"},{"assetId":"0","oldPromotionId":"","orgId":"0","promotionId":"0","promotionType":"-7"},{"assetId":"0","oldPromotionId":"0","orgId":"0","promotionId":"0","promotionType":"8"}]','token':token}
    response=requests.post(url='https://userapi.qiekj.com/goods/water/unlock',headers=headers,data=data3)
    print(response.json())
except:
    print('请仔细检查token或者输入是否合法\n')
