from pyecharts import Gauge

gauge = Gauge('项目完成进度')
gauge.add('进度表', '完成率', 88.88)
gauge.render('D:\\pye\\gauge.html')    # 在指定目录下生成文件
