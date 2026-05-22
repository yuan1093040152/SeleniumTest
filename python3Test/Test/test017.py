# -*- coding: utf-8 -*-
# pip install requests pycryptodome

import base64
import json
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

URL = "https://i.leyoujia.com/jjscj-deal/index/cjIndexList"
COOKIE = "jjshome_uuid=17ba35ec-9032-5667-970e-762d7bcd3496; prefs={}; fhListCookies=; gr_user_id=cff45c57-2c71-4a02-8138-82e7894de66c; cookiesId=7f2b44a078c34dc18d6ac70f44aa728f; userInfoCookie=bC3nvfu4XquEcf2F5XZgdZxuWGLDRydSQSX3co-BZr2o6tzvjPURDw-gIvl04w22AoLfMCGX781Z-J67PDeksPRcrWB8upERzxkwT0cJV1I=1; agentCardhd_time=1; token=t.RgsYudEC8r4CuGfqPXtA; Hm_lvt_1851e6f08c8180e1e7b5e33fb40c4b08=1774527206,1776391025; Hm_lvt_728857c2e6b321292b2eb422213d1609=1774527206,1776391025; login-workerid=06045224; login-mac=dc02f04c52b58e4751f9223b9d2fe776; __session:0.05605370019726297:_dgHidden=false; connect.sid=s%3AAR8rzj-SH3k7KBDmqWjDX2BVaiZpc7Fy.vq0sIcJDSeEccceNpIwLaD2Stdjp4dNzHbM%2FXjG3ERE; JSESSIONID=CA9B9392568AE411459C5BC8467EBFA3; accTyp=1; proLEYOUJIA=YTNjMTRhZGQtMWRiNi00MTM1LTkxMTktYmVlNzkzMzcwOTFm; jjshome_sid=b0cd93a4-bde3-2e4f-5de3-ead96ba99710; lyj_pc_token=242dae9c-f807-4a37-b49f-749dd2384d43"

AES_KEY = b"ODcyYTUxNGM1N2M2"

HEADERS = {
    "content-type": "application/json;charset=UTF-8",
    "encrypt": "true",
    "referer": "https://i.leyoujia.com/lyj-menu/cj/CJ_NEW?showTab=true&submenu=CJCX",
    "cookie": COOKIE,
}


def build_query(gzdh: str, **overrides) -> dict:
    query = {
        "pageSize": 100,
        "currPage": 1,
        "workerType": 0,
        "managerTypeVal": 3,
        "dateType": 1,
        "orderTab": 1,
        "managerType": 3,
        "gzdh": gzdh,
        "zlsqType": 1,
    }
    query.update(overrides)
    return query


def _encrypt(plain: dict) -> str:
    text = json.dumps(plain, ensure_ascii=False, separators=(",", ":"))
    ct = AES.new(AES_KEY, AES.MODE_ECB).encrypt(pad(text.encode(), 16))
    return base64.b64encode(ct).decode()


def _decrypt(cipher: str) -> dict:
    raw = base64.b64decode(cipher.strip())
    plain = unpad(AES.new(AES_KEY, AES.MODE_ECB).decrypt(raw), 16)
    return json.loads(plain.decode())


def cj_index_list(query: dict) -> dict:
    resp = requests.post(URL, json={"key": _encrypt(query)}, headers=HEADERS, timeout=60)
    resp.raise_for_status()
    return _decrypt(resp.text)


def check_jdzt(gzdh: str, result: dict) -> list:
    """jdzt 不符合规则时，将传参的 gzdh 加入 cj_error。"""
    cj_error = []
    if not gzdh:
        return cj_error

    prefix = gzdh[0].upper()
    for item in (result.get("data")).get("list"):
        jyzt = item.get("jyzt")
        print("jyzt",jyzt)
        if prefix == "M" and jyzt != 1:
            cj_error.append(gzdh)
            break
        if prefix == "Z" and jyzt != 4:
            cj_error.append(gzdh)
            break
    return cj_error


if __name__ == "__main__":
    gzdh = "M3062605-4631"
    result = cj_index_list(build_query(gzdh=gzdh))
    cj_error = check_jdzt(gzdh, result)

    # print(json.dumps(result, ensure_ascii=False, indent=2))
    print("--- cj_error ---")
    print(json.dumps(cj_error, ensure_ascii=False, indent=2))
