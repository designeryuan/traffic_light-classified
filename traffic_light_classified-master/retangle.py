import cv2
image_path = 'E:/Geogle Download/traffic_light_classified-master/traffic_light_classified-master/image/re_green/966.jpg'
image = cv2.imread(image_path)
first_point = (430,80)
last_point = (480,250)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.rectangle(image, first_point, last_point, (0, 255, 0), 2)
cv2.putText(image, '0.99', (500, 150), font, 1.0, (0, 255, 0), 2)
store_path = 'E:/Geogle Download/traffic_light_classified-master/traffic_light_classified-master/image/7.jpg'
cv2.imwrite(store_path, image)