import imageio
import cv2

'''
作者：pk哥
公众号：brucepk
日期：2018/11/4
代码解析详见微信公众号「brucepk」。

如有疑问或需转载，请加微信号：dyw520520，备注来意，谢谢。
如需加入python技术交流群，请加我微信，备注「进群」，我拉你进群，一起讨论交流，共同成长。
'''

originalPic = 'D:\\Buckup\\桌面\\y1.jpg'      # 原始动态图存放路径
dealPic = 'D:\\Buckup\\桌面\\y2.jpg'            # 处理后的字符动态图存放路径和名称

string = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "'''    # 灰度与字符的映射
pics = imageio.mimread(originalPic)    # 读取动态图，把动态图转化为一帧一帧的图片

A = []
# 把上面的每帧图片转化为字符画，并保存在A列表里
for img in pics:
    u, v, _ = img.shape
    c = img * 0 + 255
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    for i in range(0, u, 6):
        for j in range(0, v, 6):
            pix = gray[i, j]
            b, g, r, _ = img[i, j]
            zifu = string[int(((len(string)-1)*pix)/256)]
            cv2.putText(c, zifu, (j, i), cv2.FONT_HERSHEY_COMPLEX, 0.3, (int(b), int(g), int(r)), 1)
    A.append(c)

imageio.mimsave(dealPic, A, 'GIF', duration=0.1)   # 把A列表里的字符画组合起来，变成动态图
print('转化完成，请到你保存的路径下查看')