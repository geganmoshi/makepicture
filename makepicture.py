from PIL import Image,ImageDraw
import random
import numpy as np
import cv2
import math

def make_picture(bg,word,degree):
    bg = Image.open(bg)
    bg_width = bg.size[0]
    bg_height = bg.size[1]

    word = Image.open(word)
    word_width = word.size[0]
    word_height = word.size[1]
    word = word.rotate(degree)

    i = 2
    index = 1
    while bg_width < word_width or bg_height < word_height:
        word = word.resize((int(word_width/(i * index)), int(word_height/(i * index))), Image.ANTIALIAS)
        word_width = word.size[0]
        word_height = word.size[1]
        index += 1
    range_width = bg_width - word_width
    range_height = bg_height - word_height

    width_x = random.randint(0, range_width)
    height_y = random.randint(0, range_height)

    box = (width_x, height_y, width_x + word_width, height_y + word_height)
    region = word
    region = region.resize((box[2] - box[0], box[3] - box[1]))
    bg.paste(region, box)
    bg.save('./out.png')

    x_1, y_1 = Nrotate(degree,int(word_width/4),int(word_height/4),int(word_width/2),int(word_height/2),word_height)
    x_2, y_2 = Nrotate(degree, int(word_width/4*3), int(word_height / 4),int(word_width/2),int(word_height/2),word_height)
    x_3, y_3 = Nrotate(degree, int(word_width/4*3), int(word_height/4*3),int(word_width/2),int(word_height/2),word_height)
    x_4, y_4 = Nrotate(degree, int(word_width/4), int(word_height/4*3),int(word_width/2),int(word_height/2),word_height)

    new_img = Image.new('RGBA', (bg_width, bg_height), color=(0, 0, 0, 255))
    # draw = ImageDraw.Draw(new_img)
    # draw.rectangle(box, fill=(255, 255, 255))
    new_img.save('./label.png')

    img = cv2.imread('./label.png')
    mask = np.zeros(img.shape, np.uint8)

    # 不规则图形生成方法
    # pts = np.array([[width_x,height_y],[width_x+word_width,height_y],[width_x + word_width,height_y + word_height],[width_x ,height_y + word_height]], np.int32)
    # pts = pts.reshape((-1, 1, 2))
    # mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
    # mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))
    # cv2.imwrite('./label_1.png', mask2)

    pts = np.array([[width_x + x_1, height_y + y_1], [width_x + x_2, height_y + y_2], [width_x + x_3, height_y + y_3], [width_x + x_4, height_y + y_4]], np.int32)
    print(width_x + x_1, height_y + y_1)
    pts = pts.reshape((-1, 1, 2))
    mask = cv2.polylines(mask, [pts], True, (255, 255, 255))
    mask2 = cv2.fillPoly(mask, [pts], (255, 255, 255))
    cv2.imwrite('./label_2.png', mask2)

def make_bigger_picture(path):
    word = Image.open(path)
    word_width = word.size[0]
    word_height = word.size[1]
    region = word
    new_img_bg = Image.new('RGBA', (word_width * 2, word_height * 2), color=(0, 255, 0, 255))
    new_img_bg.paste(region, (int(word_width/2),int(word_height/2),int(word_width/2*3),int(word_height/2*3)))
    new_img_bg.save('./new_ing.png')

def make_picture_cv2(bg,word):
    bg = cv2.imread(bg)
    bg_width,bg_height, channels = bg.shape

    word = cv2.imread(word)
    word_width,word_height,channels = word.shape
    print(word_width,word_height)

    M = cv2.getRotationMatrix2D(((word_width - 1) / 2.0, (word_height - 1) / 2.0), 90, 1)
    dst = cv2.warpAffine(word, M, (word_width ,word_height ))
    cv2.imwrite('./label_3.png', dst)

# 逆时针
def Nrotate(angle,valuex,valuey,pointx,pointy,row):
    x1 = valuex
    y1 = row - valuey
    x2 = pointx
    y2 = row - pointy
    x = (x1 - x2) * math.cos(3.14 / 180.0 * angle) - (y1 - y2) * math.sin(3.14 / 180.0 * angle) + x2
    y = (x1 - x2) * math.sin(3.14 / 180.0 * angle) + (y1 - y2) * math.cos(3.14 / 180.0 * angle) + y2
    x = x
    y = row - y
    return x,y

def test(path):
    im = Image.open(path)
    im.show()
    im_rotate = im.rotate(90)
    im_rotate.show()

crop_image = lambda img, x0, y0, w, h: img[y0:y0 + h, x0:x0 + w]

# test('./new_ing.png')
# make_bigger_picture('C:\\Users\\sunxufeng\\Desktop\\word.jpg')
make_picture('C:\\Users\\sunxufeng\\Desktop\\bg.jpg','./new_ing.png',60)
# make_picture('C:\\Users\\sunxufeng\\Desktop\\bg.jpg','C:\\Users\\sunxufeng\\Desktop\\word.jpg')
# make_picture_cv2('C:\\Users\\sunxufeng\\Desktop\\bg.jpg','C:\\Users\\sunxufeng\\Desktop\\word.jpg')