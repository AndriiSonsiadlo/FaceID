# Copyright (С) 2021 Andrii Sonsiadlo

from os.path import dirname, abspath

#person
folder_persons_data = "person_data"
folder_temp = "temp"
path_temp = f"{folder_persons_data}//{folder_temp}"
folder_person_photo = "photos"

file_person_json = "person_data.json"
file_person_list_pkl = "person_list.pkl"
dir_person_data = dirname(dirname(abspath(__file__))) + f"\\{folder_persons_data}\\"  # 'Kivy/person_data' directory path

#model
folder_models_data = "model_data"
file_plot = 'plot.png'
file_model_json = 'model_data.json'
filename_model_list_pkl = 'model_list.pkl'
filename_knn_model = 'knn_model.clf'
filename_svm_model = 'svm_model.clf'
dir_model_data = dirname(dirname(abspath(__file__))) + f"\\{folder_models_data}\\"

#statistics
path_file_stats = "statistics//basic_data.csv"
path_plt_facescreen_stats = "statistics//result.png"


# image
camera_off_path_image = "Graphics/Images/camera_off_2.png"
default_user_image = "Graphics/Images/default-user.png"


