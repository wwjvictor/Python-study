from PIL import Image, ImageFilter, ImageOps

def dodge(a, b, alpha):          # 图像组成：红绿蓝（RGB）三原色组成
    return min(int(a * 255 / (256 - b * alpha)), 255)


def draw(img, blur=25, alpha=1.0):
    img1 = img.convert('L')                     # 图片转换成灰色
    img2 = img1.copy()                          # 拷贝图片
    img2 = ImageOps.invert(img2)                # 将输入图像转换为反色图像
    for i in range(blur):                       # 模糊度
        img2 = img2.filter(ImageFilter.BLUR)    # 模糊滤波
    width, height = img1.size
    for x in range(width):
        for y in range(height):
            a = img1.getpixel((x, y))           # 换算,得到灰度值
            b = img2.getpixel((x, y))
            img1.putpixel((x, y), dodge(a, b, alpha))   # rgb转化为像素
    img1.show()
    img1.save('D:\\Backup\\桌面\\p4.jpg')    # 保存素描图片的路径，需要改成你自己的


img = Image.open('D:\\Backup\\桌面\\p3.jpg')      # 打开需要素描的图片，使用Image模块中的open函数打开一张图片，路径改成你自己的。
draw(img)
