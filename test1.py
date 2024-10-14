import easyocr
reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
filename = 'WechatIMG7.png'
#result = reader.readtext(filename)
result = reader.readtext(filename, detail = 0)

print(result)

