import cv2
import os
def rebuild(dir):
    for root,dirs,files in os.walk(dir):
        for file in files:
            filepath=os.path.join(root,file)
            try:
                image = cv2.imread(filepath)
                dim=(64,64)
                resized=cv2.resize(image,dim)
                path = "E:/Geogle Download/traffic_light_classified-master/traffic_light_classified-master/image/yellow/"+file
                #path = 'C:/Users/lenovo/Desktop/image/' + file
                cv2.imwrite(path,resized)
            except:
                print(filepath)
                #os.remove(filepath)
dir = "E:/Geogle Download/traffic_light_classified-master/traffic_light_classified-master/image/yellow"
#dir = 'C:/Users/lenovo/Desktop/images'
rebuild(dir)
print("end")