from pyecharts import Line3D

data = [[1, 2, 3, 4], [1, 2, 3, 4], [0, 4, 8, 16]]
Line3D = Line3D("3D 折线图示例", width=1200, height=600)
Line3D.add("", data, is_visualmap=True)
Line3D.render('D:\\pye\\3D折线图.html')    # 在指定目录下生成文件
