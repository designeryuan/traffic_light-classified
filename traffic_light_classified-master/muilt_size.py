import cv2
import os
def rebuild(dir):
    for root,dirs,files in os.walk(dir):
        for file in files:
            filepath=os.path.join(root,file)
            try:
                img = cv2.imread(filepath)
                x = img.shape[0]
                y = img.shape[1]
                bili = 0.2
                x1 = int(bili * x)
                x2 = int(x - x1)
                y1 = int(bili * y)
                y2 = int(y - y1)
                crop = img[x1:x2, y1:y2]
                path = "E:/Geogle Download/traffic_light_classified-master/traffic_light_classified-master/image/yellow/"+file
                #path = 'C:/Users/lenovo/Desktop/image/' + file
                cv2.imwrite(path,crop)
            except:
                print(filepath)
                #os.remove(filepath)
dir = "E:/Geogle Download/traffic_light_classified-master/traffic_light_classified-master/image/yellow"
#dir = 'C:/Users/lenovo/Desktop/images'
rebuild(dir)
print("end")


