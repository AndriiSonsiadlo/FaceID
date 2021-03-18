# Copyright (С) 2021 Andrii Sonsiadlo

#algortihm
algorithm_knn = "KNN Classification"
algorithm_svm = "SVM Classification"
algorithms_values = [algorithm_knn, algorithm_svm]

uniform = "uniform"
distance = "distance"
weights_values = [distance, uniform]    #KNN

auto = "auto"
scale = "scale"
gamma_values = [auto, scale] #SVN

threshold_default = 0.5
#default is a 5 frames to identificate person
default_count_frame = 5
default_count_photos = 1

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'JPG', 'JPEG', 'PNG'}

port_0 = "Port 0"
port_1 = "Port 1"
port_2 = "Port 2"
port_3 = "Port 3"
port_4 = "Port 4"
camera_values = [port_0, port_1, port_2, port_3, port_4]

start_webcam_text = "Turn on"
stop_webcam_text = "Turn off"