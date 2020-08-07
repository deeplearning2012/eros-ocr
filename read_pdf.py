import easyocr
reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory

from pdf2image import convert_from_path
convert_from_path('0002514084.pdf', 500, "output", fmt="JPEG", output_file="ok", thread_count=4)

'''
from pdf2image import convert_from_path
pages = convert_from_path('pdf_file', 500)
for page in pages:
    page.save('out.jpg', 'JPEG')
'''

#result = reader.readtext('0002514084.pdf')
#print(result)