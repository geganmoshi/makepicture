# makepicture

python合成训练图片用于fnc模型或者deeplab v3模型训练，该算法自动压缩图片至合适大小，并可以标记完整图片旋转后的位置

执行顺序：
1. make_bigger_picture，输入参数为上层图片的路径
2. make_picture，输入参数为背景图片路径，make_bigger_picture生成的图片路径，旋转角度
