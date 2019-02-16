import imageio
import cv2

originalPic = 'D:\\Buckup\\桌面\\y1.jpg'      #
dealPic = 'D:\\Buckup\\桌面\\y2.jpg'            # 

string = '''$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "'''   
pics = imageio.mimread(originalPic)    #

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
