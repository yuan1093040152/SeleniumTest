#coding=utf-8
import requests

response = requests.get('http://pcvideogs.titan.mgtv.com/c1/2018/07/18_0/BC84F0C5776F228F8E9B833E0EFCDDB1_20180718_1_1_1167.mp4?arange=0&pm=JKKvKzSrY3h0Z_5AfVi1EKyRjexfEqs3QoD~WyZfNaPiFePI6xnWsASF839MBlKegd9GppQlPsH568xoEdNtiwi1YqK9qOkLHgRvIYiFt1525w8WpoKWVLBe_MoBh8nIeDotTuAlQvtcLFz7oGBFr9aEveO03LJqWknk13kHdpNW31dchUHinW7m8n31xX8n860N0bwX0CqV2kmA5SQA5UJdTVmeoQA9eTVOkc3AOQ715UXtVVwxdZOD96iHGJ1SnG7nob87KR53~zkElMML9XjCT4ePpZM6IkVx_Ieb2DZr766JS~OVh810ZcEF1g645l6qpoKIuYzUgteKEvoPAEcOXoAjnA7n3EdQkMz1uaANnnDsIZS455r_hmkjtuuP28RVuySdfFrFKjxQElhJDg--&vcdn=0&scid=25012&wsiphost=local')
print (response.status_code)
print (response.text)





