# makepicture

python合成训练图片用于fnc模型或者deeplab v3模型训练，该算法自动压缩图片至合适大小，并可以标记完整图片旋转后的位置

执行顺序：
1. make_bigger_picture，输入参数为上层图片的路径
2. make_picture，输入参数为背景图片路径，make_bigger_picture生成的图片路径，旋转角度

![image text](https://github.com/geganmoshi/makepicture/blob/master/%E5%9B%BE%E7%89%87/bg.jpg)
![image text](https://github.com/geganmoshi/makepicture/blob/master/%E5%9B%BE%E7%89%87/picture.jpg)
![image text](https://github.com/geganmoshi/makepicture/blob/master/%E5%9B%BE%E7%89%87/new_ing.jpg)
![image text](https://github.com/geganmoshi/makepicture/blob/master/%E5%9B%BE%E7%89%87/label.jpg)
![image text](https://github.com/geganmoshi/makepicture/blob/master/%E5%9B%BE%E7%89%87/label_2.jpg)
![image text](https://github.com/geganmoshi/makepicture/blob/master/%E5%9B%BE%E7%89%87/label_3.jpg)
![image text](https://github.com/geganmoshi/makepicture/blob/master/%E5%9B%BE%E7%89%87/out.jpg)
