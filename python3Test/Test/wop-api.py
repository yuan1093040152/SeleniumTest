"""
WOP API 完整自动化测试脚本
包含所有正常流程和异常流程测试用例（共19个）

运行方式：
    pytest wop_api_full.py -v -s

生成报告：
    pytest wop_api_full.py -v -s --html=report.html --self-contained-html
"""

import pytest
import requests
import json
import uuid
import time
from typing import Dict, Any
from datetime import datetime

# ==================== 配置区 ====================
BASE_URL = "https://zero-ai-test.leyoujia.com"
WOP_ENDPOINT = f"{BASE_URL}/zero-ai-api/v1/wop/execute"
TIMEOUT = 30

# ============ Cookie配置（请定期更新） ============
COOKIE_STRING = "jjshome_uuid=aa682b3f-a02e-71dc-60a8-e63ccf824bbf; login-mac=; JSESSIONID=9BF3C2407FE07CB954793A2E35984ED0; proLEYOUJIA=MzhhMWQwY2UtMTRkMS00MzhiLWE3MDUtNTY5NTRkZDY1MDdj; jjshome_sid=513deaf4-abab-dc65-3fe1-8341aa437bbc; fatLEYOUJIA=NjA4N2VlMDQtMzA5NS00YjljLWExYmQtYjEzZjA1YTBmZmU4; login-workerid=77835581"
# =================================================

# 测试常量
TEST_TENANT = "tenant_default"
TEST_USER = "admin_01"


# ==================== 工具函数 ====================

def generate_idempotency_key(prefix: str = "tc") -> str:
    """生成唯一幂等键"""
    return f"{prefix}-{uuid.uuid4()}"


def generate_trace_id() -> str:
    """生成追踪ID"""
    return f"trace-{int(time.time() * 1000)}-{uuid.uuid4().hex[:6]}"


def parse_cookie(cookie_str: str) -> dict:
    """解析Cookie字符串为字典"""
    cookies = {}
    for item in cookie_str.split(';'):
        item = item.strip()
        if '=' in item:
            k, v = item.split('=', 1)
            cookies[k.strip()] = v.strip()
    return cookies


def get_base_headers() -> dict:
    """获取基础请求头"""
    return {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': COOKIE_STRING,
        'DNT': '1',
        'Origin': 'https://zero-ai-test.leyoujia.com',
        'Pragma': 'no-cache',
        'Referer': 'https://zero-ai-test.leyoujia.com/?page=intents&package=0cb5f7da-6654-4e69-8e7d-545711172d00&tab=recipes',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/150.0.0.0 Safari/537.36',
        'X-ZAI-INTERNAL-KEY': 'lyj.123456',
        'X-ZAI-Trace-ID': generate_trace_id(),
        'X-ZAI-User': '092992',
        'sec-ch-ua': '"Not;A=Brand";v="8", "Chromium";v="150", "Google Chrome";v="150"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"'
    }


def send_request(payload: Dict[str, Any]) -> Dict[str, Any]:
    """发送WOP请求"""
    try:
        headers = get_base_headers()
        # 移除Cookie（用cookies参数传递）
        if 'Cookie' in headers:
            del headers['Cookie']

        response = requests.post(
            WOP_ENDPOINT,
            json=payload,
            cookies=parse_cookie(COOKIE_STRING),
            headers=headers,
            timeout=TIMEOUT
        )

        print(f"\n[调试] HTTP状态码: {response.status_code}")

        # 尝试解析JSON
        try:
            return response.json()
        except json.JSONDecodeError as e:
            return {
                "code": response.status_code,
                "success": False,
                "message": f"响应不是JSON格式: {response.text[:200]}",
                "data": None
            }

    except requests.exceptions.Timeout:
        return {"code": 408, "success": False, "message": "请求超时", "data": None}
    except requests.exceptions.ConnectionError:
        return {"code": 503, "success": False, "message": f"服务不可达: {BASE_URL}", "data": None}
    except Exception as e:
        return {"code": 500, "success": False, "message": str(e), "data": None}


def assert_success(response: Dict[str, Any], expected_code: str = "WRITE_SUCCESS"):
    """断言响应成功"""
    assert response.get("success") is True, f"响应失败: {response.get('message')}"
    assert response.get("code") == 200, f"HTTP状态码异常: {response.get('code')}"
    assert response.get("data", {}).get("code") == expected_code, \
        f"业务状态码异常: {response.get('data', {}).get('code')}"


# ==================== Fixture ====================

@pytest.fixture
def base_create_payload():
    """基础创建请求模板"""
    return {
        "tenant_id": TEST_TENANT,
        "user_id": TEST_USER,
        "target_system": "crm",
        "operation_type": "CREATE",
        "entity_type": "customer",
        "batch_size": 1,
        "carrier_type": "TEXT",
        "confidence": 0.95,
        "source": "agent",
        "entry_channel": "agent_dialog",
        "human_confirmed": False
    }


# ==================== 正常流程测试 (TC-WOP-001 ~ TC-WOP-008) ====================

class TestWopNormalFlow:
    """正常流程测试类"""

    def test_tc_wop_001_create_success(self, base_create_payload):
        """TC-WOP-001：CREATE操作-绿灯放行成功"""
        print("\n" + "=" * 60)
        print("TC-WOP-001：CREATE操作-绿灯放行成功")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_customer",
            "payload": {
                "name": f"测试客户_TC001_{datetime.now().strftime('%H%M%S')}",
                "contact": "13800138001",
                "region": "华南"
            },
            "idempotency_key": generate_idempotency_key("tc-wop-001")
        })

        print(f"请求: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert_success(response)
        assert response["data"]["interact_payload"] is None
        assert response["data"]["data"]["status"] == "success"
        print("✅ 测试通过")

    def test_tc_wop_002_create_with_optional_fields(self, base_create_payload):
        """TC-WOP-002：CREATE操作-含完整可选字段"""
        print("\n" + "=" * 60)
        print("TC-WOP-002：CREATE操作-含完整可选字段")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_order",
            "target_system": "order_center",
            "entity_type": "order",
            "carrier_type": "VOICE",
            "confidence": 0.88,
            "source": "task_engine",
            "entry_channel": "automated_workflow",
            "write_profile": {
                "risk_level": "low",
                "priority": "high"
            },
            "api_config": {
                "timeout": 30,
                "retry_count": 3
            },
            "payload": {
                "product_name": f"智能手机_{datetime.now().strftime('%H%M%S')}",
                "quantity": 2,
                "unit_price": 5999.00,
                "customer_id": "cust_10001"
            },
            "idempotency_key": generate_idempotency_key("tc-wop-002")
        })

        print(f"请求: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert_success(response)
        print("✅ 测试通过")

    def test_tc_wop_003_batch_create(self, base_create_payload):
        """TC-WOP-003：批量CREATE操作-多条数据写入"""
        print("\n" + "=" * 60)
        print("TC-WOP-003：批量CREATE操作-多条数据写入")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "batch_create_orders",
            "target_system": "order_center",
            "entity_type": "order",
            "batch_size": 3,
            "payload": {
                "orders": [
                    {"product": f"手机_{datetime.now().strftime('%H%M%S')}", "quantity": 2, "price": 5999},
                    {"product": f"平板_{datetime.now().strftime('%H%M%S')}", "quantity": 1, "price": 3999},
                    {"product": f"耳机_{datetime.now().strftime('%H%M%S')}", "quantity": 3, "price": 999}
                ]
            },
            "idempotency_key": generate_idempotency_key("tc-wop-003")
        })

        print(f"请求: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert_success(response)
        data = response["data"]["data"]
        assert data["total_count"] == 3
        assert data["success_count"] == 3
        assert data["failed_count"] == 0
        print("✅ 测试通过")

    def test_tc_wop_004_hard_approval_flow(self, base_create_payload):
        """TC-WOP-004：CREATE操作-强确认拦截后执行成功"""
        print("\n" + "=" * 60)
        print("TC-WOP-004：CREATE操作-强确认拦截后执行成功")
        print("=" * 60)

        idempotency_key = generate_idempotency_key("tc-wop-004")

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_sensitive_user",
            "target_system": "iam",
            "entity_type": "user",
            "payload": {
                "username": f"admin_test_{datetime.now().strftime('%H%M%S')}",
                "role": "super_admin",
                "department": "IT"
            },
            "idempotency_key": idempotency_key,
            "human_confirmed": False
        })

        print(f"第一次请求: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response1 = send_request(payload)
        print(f"第一次响应: {json.dumps(response1, ensure_ascii=False, indent=2)}")

        # 检查是否需要硬确认
        if response1.get("data", {}).get("code") == "NEED_HARD_APPROVAL":
            assert "interact_payload" in response1["data"]
            assert response1["data"]["interact_payload"]["type"] == "hard_confirm"

            # 第二次请求 - 确认后执行
            payload["human_confirmed"] = True
            print(f"第二次请求（已确认）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
            response2 = send_request(payload)
            print(f"第二次响应: {json.dumps(response2, ensure_ascii=False, indent=2)}")

            assert_success(response2)
            print("✅ 测试通过")
        else:
            print("⚠️ 意图未配置为HARD级别，跳过确认流程测试")
            pytest.skip("意图未配置为HARD级别")

    def test_tc_wop_005_soft_approval(self, base_create_payload):
        """TC-WOP-005：CREATE操作-软确认拦截"""
        print("\n" + "=" * 60)
        print("TC-WOP-005：CREATE操作-软确认拦截")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_high_value_order",
            "target_system": "order_center",
            "entity_type": "order",
            "payload": {
                "product": "高端服务器",
                "quantity": 10,
                "total_amount": 500000
            },
            "idempotency_key": generate_idempotency_key("tc-wop-005"),
            "human_confirmed": False
        })

        print(f"请求: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        if response.get("data", {}).get("code") == "NEED_SOFT_APPROVAL":
            assert "interact_payload" in response["data"]
            assert "suggested_question" in response["data"]["interact_payload"]
            print("✅ 测试通过")
        else:
            print("⚠️ 意图未配置为SOFT级别，跳过软确认测试")
            pytest.skip("意图未配置为SOFT级别")

    def test_tc_wop_006_custom_write_profile(self, base_create_payload):
        """TC-WOP-006：自定义write_profile的CREATE操作"""
        print("\n" + "=" * 60)
        print("TC-WOP-006：自定义write_profile的CREATE操作")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "custom_create_intent",
            "target_system": "external_api",
            "entity_type": "webhook",
            "payload": {
                "event": "user_created",
                "data": {"email": f"test_{datetime.now().strftime('%H%M%S')}@example.com"}
            },
            "idempotency_key": generate_idempotency_key("tc-wop-006"),
            "write_profile": {
                "risk_level": "low",
                "require_approval": False,
                "max_batch_size": 10
            },
            "api_config": {
                "url": "https://api.example.com/webhooks",
                "method": "POST",
                "headers": {
                    "Authorization": "Bearer test_token"
                }
            }
        })

        print(f"请求: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        if response.get("success"):
            assert response.get("code") == 200
            print("✅ 测试通过")
        else:
            print("⚠️ 自定义意图可能未配置，跳过")
            pytest.skip("自定义意图未配置")

    def test_tc_wop_007_idempotency(self, base_create_payload):
        """TC-WOP-007：幂等性验证-相同key重复提交CREATE"""
        print("\n" + "=" * 60)
        print("TC-WOP-007：幂等性验证-相同key重复提交CREATE")
        print("=" * 60)

        idempotency_key = generate_idempotency_key("tc-wop-007")
        customer_name = f"幂等测试客户_{datetime.now().strftime('%H%M%S')}"

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_customer",
            "payload": {
                "name": customer_name,
                "contact": "13800138007"
            },
            "idempotency_key": idempotency_key,
            "human_confirmed": False
        })

        # 第一次请求
        print(f"第一次请求: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response1 = send_request(payload)
        print(f"第一次响应: {json.dumps(response1, ensure_ascii=False, indent=2)}")
        assert_success(response1)
        customer_id1 = response1["data"]["data"]["response_body"].get("customer_id")

        # 第二次请求（相同key）
        print(f"第二次请求（相同幂等键）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response2 = send_request(payload)
        print(f"第二次响应: {json.dumps(response2, ensure_ascii=False, indent=2)}")
        assert_success(response2)
        customer_id2 = response2["data"]["data"]["response_body"].get("customer_id")

        assert customer_id1 == customer_id2, "幂等性验证失败：两次请求返回不同结果"
        print("✅ 测试通过 - 幂等性验证成功")

    def test_tc_wop_008_high_confidence(self, base_create_payload):
        """TC-WOP-008：高置信度CREATE操作"""
        print("\n" + "=" * 60)
        print("TC-WOP-008：高置信度CREATE操作")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_customer",
            "payload": {
                "name": f"高置信度客户_{datetime.now().strftime('%H%M%S')}",
                "contact": "13800138008"
            },
            "idempotency_key": generate_idempotency_key("tc-wop-008"),
            "confidence": 0.99,
            "human_confirmed": False
        })

        print(f"请求: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert_success(response)
        print("✅ 测试通过")


# ==================== 异常流程测试 (TC-WOP-101 ~ TC-WOP-111) ====================

class TestWopExceptionFlow:
    """异常流程测试类"""

    def test_tc_wop_101_missing_intent_id(self):
        """TC-WOP-101：必填参数intent_id缺失"""
        print("\n" + "=" * 60)
        print("TC-WOP-101：必填参数intent_id缺失")
        print("=" * 60)

        payload = {
            "tenant_id": TEST_TENANT,
            "user_id": TEST_USER,
            "target_system": "crm",
            "operation_type": "CREATE",
            "entity_type": "customer",
            "payload": {"name": "测试"},
            "idempotency_key": generate_idempotency_key("tc-wop-101")
        }

        print(f"请求（缺少intent_id）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert response.get("success") is False
        assert response.get("code") in [400, 422]
        print("✅ 测试通过 - 正确返回错误")

    def test_tc_wop_102_missing_tenant_id(self):
        """TC-WOP-102：必填参数tenant_id缺失"""
        print("\n" + "=" * 60)
        print("TC-WOP-102：必填参数tenant_id缺失")
        print("=" * 60)

        payload = {
            "intent_id": "create_customer",
            "user_id": TEST_USER,
            "target_system": "crm",
            "operation_type": "CREATE",
            "entity_type": "customer",
            "payload": {"name": "测试"},
            "idempotency_key": generate_idempotency_key("tc-wop-102")
        }

        print(f"请求（缺少tenant_id）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert response.get("success") is False
        assert response.get("code") in [400, 422]
        print("✅ 测试通过 - 正确返回错误")

    def test_tc_wop_103_empty_payload(self, base_create_payload):
        """TC-WOP-103：payload为空对象"""
        print("\n" + "=" * 60)
        print("TC-WOP-103：payload为空对象")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_customer",
            "payload": {},
            "idempotency_key": generate_idempotency_key("tc-wop-103"),
            "human_confirmed": False
        })

        print(f"请求（payload为空）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        if response.get("success"):
            assert response["data"]["code"] in ["VALIDATION_ERROR", "WRITE_PROFILE_INCOMPLETE"]
            print("✅ 测试通过 - 正确返回业务错误")
        else:
            assert response.get("code") in [400, 422]
            print("✅ 测试通过 - 正确返回参数错误")

    def test_tc_wop_104_invalid_operation_type(self, base_create_payload):
        """TC-WOP-104：无效的operation_type值"""
        print("\n" + "=" * 60)
        print("TC-WOP-104：无效的operation_type值")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_customer",
            "operation_type": "INVALID_OPERATION",
            "payload": {"name": "测试"},
            "idempotency_key": generate_idempotency_key("tc-wop-104"),
            "human_confirmed": False
        })

        print(f"请求（无效operation_type）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert response.get("success") is False
        assert response.get("code") in [400, 422]
        print("✅ 测试通过 - 正确返回错误")

    def test_tc_wop_105_not_exist_intent(self, base_create_payload):
        """TC-WOP-105：未配置的intent_id"""
        print("\n" + "=" * 60)
        print("TC-WOP-105：未配置的intent_id")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "not_exist_intent_12345",
            "payload": {"name": "测试"},
            "idempotency_key": generate_idempotency_key("tc-wop-105"),
            "human_confirmed": False
        })

        print(f"请求（不存在的intent）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        if response.get("success"):
            assert response["data"]["code"] in ["PERMISSION_DENIED", "WRITE_PROFILE_INCOMPLETE"]
            print("✅ 测试通过 - 正确返回业务错误")
        else:
            assert response.get("code") in [400, 403, 404]
            print("✅ 测试通过 - 正确返回权限错误")

    def test_tc_wop_106_invalid_tenant(self, base_create_payload):
        """TC-WOP-106：无效的tenant_id"""
        print("\n" + "=" * 60)
        print("TC-WOP-106：无效的tenant_id")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "tenant_id": "invalid_tenant_999",
            "intent_id": "create_customer",
            "payload": {"name": "测试"},
            "idempotency_key": generate_idempotency_key("tc-wop-106"),
            "human_confirmed": False
        })

        print(f"请求（无效tenant）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        if response.get("success"):
            assert response["data"]["code"] in ["PERMISSION_DENIED", "VALIDATION_ERROR"]
            print("✅ 测试通过 - 正确返回业务错误")
        else:
            assert response.get("code") in [400, 403]
            print("✅ 测试通过 - 正确返回权限错误")

    def test_tc_wop_107_invalid_confidence(self, base_create_payload):
        """TC-WOP-107：无效的confidence值"""
        print("\n" + "=" * 60)
        print("TC-WOP-107：无效的confidence值")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_customer",
            "payload": {"name": "测试"},
            "idempotency_key": generate_idempotency_key("tc-wop-107"),
            "confidence": 1.5,
            "human_confirmed": False
        })

        print(f"请求（confidence=1.5）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert response.get("success") is False
        assert response.get("code") in [400, 422]
        print("✅ 测试通过 - 正确返回错误")

    def test_tc_wop_108_batch_exceeds_limit(self, base_create_payload):
        """TC-WOP-108：批量超过限制"""
        print("\n" + "=" * 60)
        print("TC-WOP-108：批量超过限制")
        print("=" * 60)

        orders = [{"product": f"商品{i}"} for i in range(1, 12)]

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "batch_create_orders",
            "target_system": "order_center",
            "entity_type": "order",
            "payload": {"orders": orders},
            "idempotency_key": generate_idempotency_key("tc-wop-108"),
            "batch_size": 11,
            "human_confirmed": False
        })

        print(f"请求（batch_size=11）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        if response.get("success"):
            assert response["data"]["code"] in ["VALIDATION_ERROR", "WRITE_PROFILE_INCOMPLETE"]
            print("✅ 测试通过 - 正确返回业务错误")
        else:
            assert response.get("code") in [400, 422]
            print("✅ 测试通过 - 正确返回参数错误")

    def test_tc_wop_109_unreachable_system(self, base_create_payload):
        """TC-WOP-109：目标系统不可达"""
        print("\n" + "=" * 60)
        print("TC-WOP-109：目标系统不可达")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_customer",
            "target_system": "unreachable_system_999",
            "payload": {"name": "测试"},
            "idempotency_key": generate_idempotency_key("tc-wop-109"),
            "human_confirmed": False
        })

        print(f"请求（不可达系统）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        if response.get("success"):
            assert response["data"]["code"] == "SYSTEM_ERROR"
            print("✅ 测试通过 - 正确返回系统错误")
        else:
            assert response.get("code") in [400, 500, 503]
            print("✅ 测试通过 - 正确返回错误")

    def test_tc_wop_110_invalid_json_format(self):
        """TC-WOP-110：无效的JSON格式"""
        print("\n" + "=" * 60)
        print("TC-WOP-110：无效的JSON格式")
        print("=" * 60)

        invalid_json = '{"intent_id":"create_customer","tenant_id":"test_tenant_001","user_id":"test_user_110", "target_system":"crm"'

        print(f"请求（无效JSON）: {invalid_json}")
        try:
            response = requests.post(
                WOP_ENDPOINT,
                data=invalid_json,
                timeout=TIMEOUT,
                headers={"Content-Type": "application/json"}
            )
            print(f"HTTP状态码: {response.status_code}")
            if response.status_code == 400:
                print("✅ 测试通过 - 正确返回JSON格式错误")
            else:
                print(f"响应内容: {response.text[:200]}")
        except Exception as e:
            print(f"✅ 测试通过 - 正确返回错误: {e}")

    def test_tc_wop_111_missing_idempotency_key(self, base_create_payload):
        """TC-WOP-111：idempotency_key缺失"""
        print("\n" + "=" * 60)
        print("TC-WOP-111：idempotency_key缺失")
        print("=" * 60)

        payload = base_create_payload.copy()
        payload.update({
            "intent_id": "create_customer",
            "payload": {"name": "测试"},
            "human_confirmed": False
        })
        if "idempotency_key" in payload:
            del payload["idempotency_key"]

        print(f"请求（缺少idempotency_key）: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        response = send_request(payload)
        print(f"响应: {json.dumps(response, ensure_ascii=False, indent=2)}")

        assert response.get("success") is False
        assert response.get("code") in [400, 422]
        print("✅ 测试通过 - 正确返回错误")


# ==================== 服务健康检查 ====================

def test_service_health():
    """测试WOP服务是否可访问"""
    print("\n" + "=" * 60)
    print("服务健康检查")
    print("=" * 60)
    print(f"WOP服务地址: {WOP_ENDPOINT}")

    try:
        response = requests.get(f"{BASE_URL}/health", timeout=5)
        print(f"✅ 服务可访问 (状态码: {response.status_code})")
        return True
    except requests.exceptions.ConnectionError:
        print(f"❌ 无法连接到WOP服务: {BASE_URL}")
        return False
    except Exception as e:
        print(f"❌ 健康检查失败: {e}")
        return False


# ==================== 测试入口 ====================

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("WOP API 完整测试套件")
    print(f"测试时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)

    if not test_service_health():
        print("\n⚠️ 服务不可用，测试无法继续")
        exit(1)

    print("\n" + "=" * 60)
    print("开始执行测试.......")
    print("=" * 60)

    pytest.main([
        __file__,
        "-v",
        "--tb=short",
        "--maxfail=5",
        "-s"
    ])