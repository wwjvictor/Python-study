from pyecharts import Pie


attr = ["语文", "数学", "英语", "物理", "化学", "生物"]
score = [20, 30, 40, 25, 10, 15]
pie = Pie('图书销量圆环图', title_pos='center')
pie.add('', attr, score, radius=[40, 75], label_text_color=None, is_label_show=True,
        legend_orient='vertical', legend_pos='left')
pie.render('D:\\pye\\pieround.html')   # 在指定目录下生成文件
