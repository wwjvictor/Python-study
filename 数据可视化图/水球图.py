from pyecharts import Liquid

liquid = Liquid("水球图")
liquid.add("Liquid", [0.8])
liquid.show_config()
liquid.render('D:\\pye\\sq.html')    # 在指定目录下生成文件
