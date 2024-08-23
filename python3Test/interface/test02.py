#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2023/6/13 9:55
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import json

a = {
    "data": {
        "task_status": "SUCCESS",
        "task_progress": 1,
        "sub_task_result_list": [
            {
                "final_image_list": [
                    {
                        "width": 1024,
                        "img_approve_conclusion": "pass",
                        "height": 1024,
                        "img_url": "http://aigc-t2p.bj.bcebos.com/artist-long/26850628_0_final.png?authorization=bce-auth-v1%2F174bf5e9a7a84f55a8e85b1cc5d62b1d%2F2023-06-13T01%3A28%3A53Z%2F1800%2Fhost%2F5ef58eb9c7c8b5e80b29bcda6b1da0e4acb038c5777e251b4506e2e291883ed4"
                    }
                ],
                "sub_task_error_code": 0,
                "sub_task_status": "SUCCESS",
                "sub_task_progress": 1
            },
            {
                "final_image_list": [
                    {
                        "width": 1024,
                        "img_approve_conclusion": "pass",
                        "height": 1024,
                        "img_url": "http://aigc-t2p.bj.bcebos.com/artist-long/26850629_0_final.png?authorization=bce-auth-v1%2F174bf5e9a7a84f55a8e85b1cc5d62b1d%2F2023-06-13T01%3A28%3A53Z%2F1800%2Fhost%2Fbd92bddead045578eab66d9a77d22f5ceef45dee8a54e3f88028884f1b0acae7"
                    }
                ],
                "sub_task_error_code": 0,
                "sub_task_status": "SUCCESS",
                "sub_task_progress": 1
            }
        ],
        "task_id": 0
    },
    "log_id": "1668430320868924424"
}
print(type(a))
for i in a["data"]["sub_task_result_list"]:
    print(i["final_image_list"][0]["img_url"])