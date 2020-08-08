import easyocr
reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
result = reader.readtext('chinese.jpg')

print(result)

# UserWarning: page-1 is image-based, camelot only works on text-based pages. [lattice.py:394]
import camelot
tables = camelot.read_pdf('0002514084.pdf')
tables.export('0002514084.csv', f='csv', compress=False)