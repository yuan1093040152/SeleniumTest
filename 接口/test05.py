#utf-8
import requests,json

url = "http://172.16.3.100/aicp/mainremote"

payload = "msgBody=%7B%0A%20%20%22mac%22%20%3A%20%2238%3A97%3Ad6%3Ad4%3A4f%3Aa0%22%2C%0A%20%20%22mobileNo%22%20%3A%20%22%22%2C%0A%20%20%22appVer%22%20%3A%20%224.2.5.1%22%2C%0A%20%20%22phoneBrand%22%20%3A%20%22iPhone%20(3)%22%2C%0A%20%20%22appType%22%20%3A%20%222%22%2C%0A%20%20%22loginAddr%22%20%3A%20%22%E5%B9%BF%E4%B8%9C%E7%9C%81%E6%B7%B1%E5%9C%B3%E5%B8%82%E7%A6%8F%E7%94%B0%E5%8C%BA%E5%85%AB%E5%8D%A6%E8%B7%AF51%22%2C%0A%20%20%22password%22%20%3A%20%22e10adc3949ba59abbe56e057f20f883e%22%2C%0A%20%20%22imei%22%20%3A%20%22218abe7ae5194942bc38f5b1e42a71983fae6e4a%22%2C%0A%20%20%22lat%22%20%3A%20%2222.57021%22%2C%0A%20%20%22username%22%20%3A%20%22H6HQ013219GI%22%2C%0A%20%20%22mobileInfo%22%20%3A%20%22218abe7ae5194942bc38f5b1e42a71983fae6e4a%22%2C%0A%20%20%22phoneModel%22%20%3A%20%22iPhone%208%20Plus%22%2C%0A%20%20%22lng%22%20%3A%20%22114.1057%22%2C%0A%20%20%22ipStr%22%20%3A%20%22172.16.15.2%22%0A%7D&methodCode=login"
headers = {
    'app_name': "JJSOA",
    'appname': "ios-jjr",
    'bundle_identifier': "com.jjshome.oa.test",
    'cit': "000002",
    'clientid': "iOS",
    'empno': "000012",
    'idfa': "6AA3C989-73B8-4ABC-8015-54C5F5546E98",
    'imei': "218abe7ae5194942bc38f5b1e42a71983fae6e4a",
    'latitude': "22.57021",
    'longitude': "114.1057",
    'methodcode': "login",
    'phoneos': "ios",
    'servicecode': "40006",
    'source': "from_self",
    'ssid': "506F7BF2-692C-480E-88B0-99840AC6AABA",
    'uuid': "49246DBE-E8DE-3D5E-8EC1-8C04DAD8E630",
    'content-type': "application/x-www-form-urlencoded",
    'cache-control': "no-cache",
    'postman-token': "d90c16a3-1ac0-227e-6656-ec4a029aa0f0"
    }

response = requests.request("POST", url, data=payload, headers=headers)

a = response.text
print(a)


# "4e313c38e6364d34dada0cb3e019e45c"
# "551a8e7a96dce3a011b551e6e692ebf8"
