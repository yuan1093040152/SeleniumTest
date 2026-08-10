import requests
import json

url = "https://zero-ai-test.leyoujia.com/zero-ai-api/v1/wop/execute"

# ============ 请将Cookie更新为您最新的值 ============
cookie_string = "jjshome_uuid=aa682b3f-a02e-71dc-60a8-e63ccf824bbf; login-mac=; JSESSIONID=9BF3C2407FE07CB954793A2E35984ED0; proLEYOUJIA=MzhhMWQwY2UtMTRkMS00MzhiLWE3MDUtNTY5NTRkZDY1MDdj; jjshome_sid=513deaf4-abab-dc65-3fe1-8341aa437bbc; fatLEYOUJIA=NjA4N2VlMDQtMzA5NS00YjljLWExYmQtYjEzZjA1YTBmZmU4; login-workerid=77835581"
# ===================================================

headers = {
    'Accept': 'text/event-stream',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    'Cookie': cookie_string,
    'DNT': '1',
    'Origin': 'https://zero-ai-test.leyoujia.com',
    'Pragma': 'no-cache',
    'Referer': 'https://zero-ai-test.leyoujia.com/?page=intents&package=0cb5f7da-6654-4e69-8e7d-545711172d00&tab=recipes',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
    'X-ZAI-INTERNAL-KEY': 'lyj.123456',      # 关键内部认证Key
    'X-ZAI-Trace-ID': 'trace-1784871663329-xsb57js', # 建议每次生成唯一值
    'X-ZAI-User': '092992',                  # 关键用户标识
    'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"'
}

payload = {
    "intent_id": "modify_user_role",
    "tenant_id": "tenant_default",
    "user_id": "admin_01",
    "target_system": "iam",
    "operation_type": "MODIFY",
    "entity_type": "user_role",
    "entity_id": "usr_772",
    "payload": {
        "new_role": "super_admin"
    },
    "idempotency_key": "b6a7114c-1234-4567-89ab-cdef01234567",
    "human_confirmed": False
}

try:
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    print(f"HTTP状态码: {response.status_code}")
    print("响应内容:")
    print(json.dumps(response.json(), ensure_ascii=False, indent=2))
except Exception as e:
    print(f"请求异常: {e}")