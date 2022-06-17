#-----------------------------------------------------------------------#

#-----------------------------------------------------------------------#
from PIL import Image
import time

from yolo import YOLO

if __name__ == "__main__":
    yolo = YOLO()

    # mode = "predict"
    #
    #
    # if mode == "predict":
    '''
        1、如果想要进行检测完的图片的保存，利用r_image.save("img.jpg")即可保存，直接在predict.py里进行修改即可。 
        2、如果想要获得预测框的坐标，可以进入yolo.detect_image函数，在绘图部分读取top，left，bottom，right这四个值。
        3、如果想要利用预测框截取下目标，可以进入yolo.detect_image函数，在绘图部分利用获取到的top，left，bottom，right这四个值
        在原图上利用矩阵的方式进行截取。
        4、如果想要在预测图上写额外的字，比如检测到的特定目标的数量，可以进入yolo.detect_image函数，在绘图部分对predicted_class进行判断，
        比如判断if predicted_class == 'car': 即可判断当前目标是否为车，然后记录数量即可。利用draw.text即可写字。
    '''
    img = r'D:\Users\Aider\Desktop\Learn\data\exmple.jpg'

    image = Image.open(img)
    t1=time.time()

    r_image = yolo.detect_image(image)
    r_image.show()
    t2=time.time()
    print(f'{t2-t1}')
    r_image.save("img/exmple_yolo.jpg")
