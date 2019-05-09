from pyecharts import Funnel

attr = ['认知', '了解', '认可', '考虑', '意向', '购买']
value = [120, 100, 80, 60, 40, 20]
funnel = Funnel('客户购买分析图')
funnel.add('买车', attr, value, is_label_show=True, label_pos='inside', label_text_color='#fff')
funnel.render('D:\\pye\\funel.html')    # 在指定目录下生成文件
