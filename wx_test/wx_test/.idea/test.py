#coding=utf-8


result = {"emotion":{"robotEmotion":{"a":0,"d":0,"emotionId":0,"p":0},"userEmotion":{"a":0,"d":0,"emotionId":0,"p":0}},"intent":{"actionName":"","code":10004,"intentName":""},"results":[{"groupType":1,"resultType":"text","values":{"text":"能再说具体点吗"}}]}


print (type(result))

result1 = result['results'][0]['values']['text']

print (result1)



