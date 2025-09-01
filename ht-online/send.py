# coding=utf-8
"""
@Author  : Yuan Meng
@File    : send.py
@Time    : 2025/9/1 20:43
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import time,smtplib,ssl
from email.mime.text import MIMEText
from email.utils import formataddr



class Send:
    def __init__(self):
        self.sender_email = "1093040152@qq.com"
        self.receiver_email = "1093040152@qq.com"
        self.auth_code = "bqqrnagvnxgefecf"

    def send_qq_email(self,title,info):
        # 邮件内容（简化编码，避免冗余格式问题）
        message = MIMEText(info, "plain", "utf-8")
        # 用formataddr确保From/To格式符合RFC标准，避免之前的Header编码问题
        message["From"] = formataddr(("发送者",self.sender_email))
        message["To"] = formataddr(("接收者", self.receiver_email))
        message["Subject"] = title  # 避免复杂编码，减少服务器解析压力

        try:
            # 创建SSL上下文（兼容不同版本服务器）
            context = ssl.create_default_context()

            # 连接服务器并发送（用with自动管理连接，减少手动关闭问题）
            with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as server:
                server.set_debuglevel(1)  # 保留调试日志，方便排查其他问题

                # 1. 登录（已验证成功，无需修改）
                server.login(self.sender_email, self.auth_code)
                print("✅ 邮箱登录成功")

                # 2. 发送邮件（核心逻辑，已验证能入队）
                server.sendmail(self.sender_email, self.receiver_email, message.as_string())
                print("✅ 邮件已成功提交到服务器队列，等待送达")

                # 3. 手动关闭连接（增加容错，避免with自动关闭时的异常）
                try:
                    server.quit()
                    print("✅ 连接正常关闭")
                except smtplib.SMTPServerDisconnected as e:
                    # 忽略“QUIT阶段的异常响应”（非关键错误，邮件已发送）
                    if str(e) in ("(-1, b'\\x00\\x00\\x00')", "Connection unexpectedly closed"):
                        print("ℹ️ 连接关闭时出现非关键异常，已忽略（邮件已正常发送）")
                    else:
                        raise  # 其他关闭异常仍抛出，便于排查

        # 捕获核心错误（仅处理影响发送的关键问题）
        except smtplib.SMTPAuthenticationError:
            print("❌ 登录失败：请检查授权码是否正确（需重新生成并立即使用）")
        except smtplib.SMTPConnectError:
            print("❌ 连接失败：请检查网络是否屏蔽465端口（尝试切换手机热点）")
        except Exception as e:
            # 仅提示关键错误，跳过关闭阶段的非关键异常
            if "(-1, b'\\x00\\x00\\x00')" not in str(e):
                print(f"❌ 核心错误：{str(e)}")
            else:
                print("ℹ️ 非关键异常已忽略，邮件已正常发送")


if __name__ == "__main__":
    Send().send_qq_email(title='标题',info='正文')
