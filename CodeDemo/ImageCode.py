# -*- coding:utf-8 -*-
from aip import AipOcr
class ImageCode():
    def GetImageCode(self,name):
        APP_ID = '16947930'
        API_KEY = '0ynD0BGPC6QtrPWs68i4sQO9'
        SECRET_KEY = 'fKsckEf41jUtTDBwFIeHYkhnYyvNaViz'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        print (11)
        with open('.//'+name+'.png','rb') as f:
            image = f.read()
        image1 = client.basicAccurate(image)
        print (image1)
        return image1['words_result'][0]['words']