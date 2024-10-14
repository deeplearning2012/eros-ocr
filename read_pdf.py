import easyocr
reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory

'''
pdf_path     文件路径
dpi          生成图片的像素
output_folder   生成图片的存储路径
first_page     第一页允许pdftoppm处理
last_page      最后一页允许pdftoppm处理
fmt           JPEG
output_file    存储文件的名字
thread_count   如果文档里面有多张图片命名后面多加几个数字
'''
from pdf2image import convert_from_path
convert_from_path('0002514084.pdf', 500, "output", fmt="JPEG", output_file="0002514084", thread_count=4)

'''
from pdf2image import convert_from_path
pages = convert_from_path('pdf_file', 500)
for page in pages:
    page.save('out.jpg', 'JPEG')
'''

filename = 'output/00025140840001-1.jpg'
#result = reader.readtext(filename)
result = reader.readtext(filename, detail = 0)
print(result)
