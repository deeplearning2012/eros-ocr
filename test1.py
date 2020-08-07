import easyocr
reader = easyocr.Reader(['ch_sim','en']) # need to run only once to load model into memory
result = reader.readtext('WechatIMG7.png')

print(result)

'''
[([[396, 12], [450, 12], [450, 42], [396, 42]], '臼中', 0.1095949187874794), ([[517, 23], [535, 23], [535, 35], [517, 35]], '凼', 0.3831235468387604), ([[121, 47], [179, 47], [179, 67], [121, 67]], '国家电网', 0.9757893085479736), ([[839, 59], [933, 59], [933, 79], [839, 79]], 'OGGOR', 0.10727843642234802), ([[121, 63], [179, 63], [179, 75], [121, 75]], 'STITC CrD', 0.0253871101886034), ([[121, 83], [227, 83], [227, 103], [121, 103]], '国网北京市电力公司', 0.48115742206573486), ([[349, 89], [731, 89], [731, 133], [349, 133]], '用电客户电费交费通知单', 0.8893185257911682), ([[815, 93], [1021, 93], [1021, 135], [815, 135]], 'N0. 0291407', 0.38869234919548035), ([[28, 184], [106, 184], [106, 212], [28, 212]], '增值税:', 0.10132688283920288), ([[134, 184], [310, 184], [310, 210], [134, 210]], '9111000031015531}', 0.3580009341239929), ([[317, 213], [755, 213], [755, 249], [317, 249]], '用户名称:中国铁塔股份有限公司北京市分公司', 0.12192957103252411), ([[30, 216], [128, 216], [128, 246], [30, 246]], '用户编导:', 0.7842770218849182), ([[134, 218], [240, 218], [240, 242], [134, 242]], '0002514084', 0.5982268452644348), ([[762, 218], [950, 218], [950, 246], [762, 246]], '电压等级:交[380', 0.0030011096969246864), ([[316, 248], [754, 248], [754, 280], [316, 280]], '缴费户名:中国铁堵股份有限公司北京市外公司', 0.006452282890677452), ([[34, 250], [104, 250], [104, 274], [34, 274]], '戴费导:', 0.022086523473262787), ([[134, 250], [240, 250], [240, 274], [134, 274]], '1045009184', 0.5728453993797302), ([[28, 282], [124, 282], [124, 308], [28, 308]],
'用户地址:', 0.4739329218864441), ([[134, 282], [614, 282], [614, 310], [134, 310]], '北I币朝阳区一八里店地区办毒处西直涧村西苴涧村路()', 1.4358028010974522e-06), ([[644, 282], [742, 282], [742, 312], [644, 312]], '电蔑类型:', 0.023575343191623688), ([[762, 282], [852, 282], [852, 312], [762, 312]], '正常电葬', 0.1325071007013321), ([[28, 314], [128, 314], [128, 346], [28, 346]], '应收年月{', 0.22716113924980164), ([[134, 316], [244, 316], [244, 340], [134, 340]], '2019年01月', 0.222647562623024), ([[24, 346], [120, 346], [120, 372], [24, 372]], '计昼虑编舄', 0.004952008370310068), ([[172, 348], [280, 348], [280, 372], [172, 372]], '50311224076', 0.9039778113365173), ([[540, 348], [612, 348], [612, 372], [540, 372]], '定比定圜', 0.13631471991539001), ([[762, 348], [872, 348], [872, 374], [762, 374]], '见计量点偏导', 0.011162853799760342), ([[26, 374], [104, 374], [104, 400], [26, 400]], '电`焚别', 0.005968088284134865), ([[18, 402], [119, 402], [119, 428], [18, 428]], '堡卢地址', 0.022098740562796593), ([[172, 402], [616, 402], [616, 428], [172, 428]], '徕区+II甩店色而亩洄村(IOOOI-朝阳新凯=a沛D[G)', 2.588414313954763e-15), ([[28, 436], [120, 436], [120, 462], [28, 462]], '计鬃点电篑', 0.0013304627500474453), ([[172, 436], [330,
436], [330, 462], [172, 462]], '电度电冀4383.OI元', 0.008726316504180431), ([[200, 470], [276, 470], [276, 494], [200, 494]], '抄表示数', 0.280072420835495), ([[326, 470], [398, 470], [398, 494], [326, 494]], '上欧抄丧', 0.0030726774130016565), ([[436, 470], [512, 470], [512, 494], [436, 494]], '本次抄定', 0.12668073177337646), ([[548, 470], [624, 470], [624, 494], [548, 494]], 'J酯抄r', 1.4889980775478762e-05), ([[800, 470], [876, 470], [876, 496], [800, 496]], '
加减电量', 0.12275383621454239), ([[944, 470], [1018, 470], [1018, 494], [944, 494]], '沙见电虽', 0.1641767919063568), ([[55, 477], [130, 477], [130, 505],
[55, 505]], '电能袤号', 0.4420781135559082), ([[225, 495], [257, 495], [257, 509], [225, 509]], '', 0.7216272354125977), ([[807, 495], [873, 495], [873, 509], [807, 509]], '(', 0.31470587849617004), ([[949, 495], [1017, 495], [1017, 511], [949, 511]], '瓦R', 0.011684250086545944), ([[64, 518], [258, 518], [258, 546], [64, 546]], '3400541509_有1(总)', 0.014026512391865253), ([[349, 521], [407, 521], [407, 539], [349, 539]], '178841', 0.28788435459136963), ([[469, 521], [529, 521], [529, 541], [469, 541]], '184105', 0.39507415890693665), ([[993, 521], [1037, 521], [1037, 541], [993, 541]], '5265', 0.48927822709083557), ([[64, 546], [274, 546], [274, 574], [64, 574]], '3400541509有功(尖峰)', 0.04431971162557602), ([[367, 549], [409, 549], [409, 567], [367, 567]], '5013', 0.6936013698577881), ([[487, 549], [529, 549], [529, 567], [487, 567]], '5013', 0.6684660315513611), ([[170, 574], [256, 574], [256, 598], [170, 598]], '无功
(总)', 0.4258991777896881), ([[65, 575], [163, 575], [163, 595], [65, 595]], '3400541509', 0.6411547660827637), ([[359, 575], [409, 575], [409, 595], [359,
595]], '20493', 0.2714916467666626), ([[479, 575], [527, 575], [527, 595], [479, 595]], '20791', 0.9101943969726562), ([[1003, 577], [1035, 577], [1035, 595], [1003, 595]], '?!9', 0.2901111841201782), ([[64, 600], [162, 600], [162, 620], [64, 620]], '3400041509', 0.18615524470806122), ([[170, 600], [256, 600], [256, 626], [170, 626]], '有功C蝗)', 0.012713253498077393), ([[359, 603], [407, 603], [407, 623], [359, 623]], '57071', 0.5377072095870972), ([[479, 603], [529, 603], [529, 623], [479, 623]], '58846', 0.8094317317008972), ([[993, 603], [1037, 603], [1037, 623], [993, 623]], '1775', 0.9445050358772278), ([[64, 628], [256, 628], [256, 652], [64, 652]], '3400541509_直功(E)', 0.006804827135056257), ([[359, 631], [409, 631], [409, 649], [359, 649]], '58380', 0.6411157846450806), ([[479, 631], [529, 631], [529, 649], [479, 649]], 'GOO99', 0.17357715964317322), ([[993, 631], [1037, 631], [1037, 651], [993, 651]], '1719', 0.8187922835350037), ([[803, 655], [877, 655], [877, 673], [803, 673]], '由碍电h', 0.0011572971707209945), ([[945, 655], [1017, 655], [1017, 673], [945, 673]], '电断电a', 0.0012699115322902799), ([[203, 657], [271, 657], [271, 673], [203, 673]], '掴酩由4', 3.102212576777674e-05), ([[327, 657], [397, 657], [397, 673], [327, 673]], 'pI电4', 6.919971383467782e-06), ([[439, 657], [507, 657], [507, 673], [439, 673]], '纬珉电臼', 0.0003000618307851255), ([[663, 657], [727, 657], [727, 671], [663, 671]], '站', 0.0032570301555097103), ([[200, 676], [274, 676], [274, 700], [200, 700]], '(主瓦时)', 0.24881014227867126), ([[436, 
'''