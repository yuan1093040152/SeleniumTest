# coding=utf-8
"""
@Author  : Yuan Meng
@File    : T_018.py
@Time    : 2026/2/11 11:59
@Software: PyCharm
Ctrl+shift+v 历史粘贴版
ctrl+alt+空格 自动补全
ctrl+alt+D   分屏
Ctrl+/       快速注释

"""
import fitz
import os,time
timestamp = int(time.time())
# 修复后的最简单版本
pdf_path = r"C:\Users\Administrator\Desktop\发票\深圳象鲜科技有限公司_发票金额154元.pdf"
output_dir = r"C:\Users\Administrator\Desktop\发票\output_images"

# 确保输出目录存在
os.makedirs(output_dir, exist_ok=True)

# 打开PDF文件
pdf = fitz.open(pdf_path)

# 先获取总页数（在关闭前）
total_pages = len(pdf)

print(f"开始转换 {total_pages} 页...")

# 逐页转换
for i in range(total_pages):
    page = pdf[i]
    pix = page.get_pixmap(dpi=300)  # 设置分辨率
    pix.save(f"{output_dir}/{timestamp}-{i+1}.png")
    print(f"已转换第 {i+1} 页")

# 关闭文件
pdf.close()

print(f"✅ 转换完成！图片保存在: {output_dir}")