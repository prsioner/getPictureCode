#使用tensenflow图片识别
#参考文档：https://juejin.im/post/5b5445495188251acc230ac9
# resnet50_coco_best_v2.0.1.h5 需要预先下载
from imageai.Detection import ObjectDetection
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
execution_path = os.getcwd()

detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew1.jpg"))


for eachObject in detections:
 print(str(eachObject["name"]) + " : " + str(eachObject["percentage_probability"]) )

