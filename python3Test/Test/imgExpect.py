#coding=utf-8
"""
@Author  : Yuan Meng
@Time    : 2025/3/27 19:51
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""

from PIL import Image  # 导入PIL图像处理库

def is_valid_image(path):
    """检查图片文件是否有效且未损坏"""
    try:
        bValid = True  # 初始化有效性标志
        with open(path, 'rb') as fileObj:  # 以二进制模式打开文件(自动管理文件关闭)
            buf = fileObj.read()  # 读取整个文件内容

            # 检查JPEG文件头标记(0xFFD8)
            if not buf.startswith(b'\xff\xd8'):
                bValid = False
            # 检查JFIF或Exif标识
            elif buf[6:10] in (b'JFIF', b'Exif'):
                # 检查JPEG文件结束标记(0xFFD9)
                # 先去除末尾可能存在的填充字符(\0,\r,\n)
                if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                    bValid = False
            else:
                try:
                    # 使用PIL库验证图片完整性
                    Image.open(fileObj).verify()
                except Exception as e:
                    bValid = False
                    print(e)  # 打印验证错误信息
    except Exception as e:
        return False  # 文件打开或其他操作异常时返回False
    return bValid  # 返回最终验证结果



def is_valid_image(path):

    """检查图片文件是否有效且未损坏"""
    try:
        with open(path, 'rb') as fileObj:
            buf = fileObj.read()
            print('1')

            # 检查文件是否足够大（防止越界访问）
            if len(buf) < 10:
                print('2')
                return False


            # 检查JPEG文件头标记（0xFFD8）
            if not buf.startswith(b'\xff\xd8'):
                print('3')
                return False


            # 检查JFIF或Exif标识
            if buf[6:10] in (b'JFIF', b'Exif'):
                # 检查JPEG文件结束标记（0xFFD9）
                if not buf.rstrip(b'\0\r\n').endswith(b'\xff\xd9'):
                    print('4')
                    return False


            # 使用PIL库验证图片完整性
            try:
                img = Image.open(fileObj)
                img.verify()  # 验证图片
                img.close()  # 关闭图片对象
                print('2222')
            except Exception as e:
                print(f"图片验证失败: {e}")
                return False

    except Exception as e:
        print(f"文件访问错误: {e}")
        return False

    return True  # 所有检查通过，图片有效


# 测试代码
flag = is_valid_image(r'E:/test/123.jpg')  # 测试正常图片
print('1111111',flag)

