from pyecharts import Pie


attr = ["语文", "数学", "英语", "物理", "化学", "生物"]
score = [20, 30, 40, 25, 10, 15]
pie = Pie('图书销量饼图')
pie.add('', attr, score, is_label_show=True)
pie.render('D:\\pye\\pie.html')
