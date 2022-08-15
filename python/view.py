import PySimpleGUI as sg
import threading
import cv2
from tools import indexToBird


from model import bird_finder

class a_gui():
    def __init__(self,):

        sg.theme('Light Brown 3')

        layout = [
                  [sg.Text('Machine learning model (.H5 file): '), sg.In(size=(25,1), enable_events=True ,key='-FILE_ECHO-'), sg.FileBrowse(key="COMPUTER_VISION_MODEL_H5", 
                                                                                                                                            file_types=[("Model save", "*.H5")])],
                  [sg.Text('Choose cropped bird photo folder'), sg.In(size=(25,1), enable_events=True ,key='-FILE_ECHO-'), sg.FolderBrowse(key="-PATH2SNAPS-")],                 
                  [sg.Button('Classify birds', size=(50, 1))],
                  [sg.Text('Have fun dad! - Love, Mark')]
        ]
      
        self.window = sg.Window('Bird Classifier', layout)
        

    def life_support(self,):
        while True:
            event, values = self.window.read()
            
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            
            elif event.startswith('Classify birds'):
                model_path = values["COMPUTER_VISION_MODEL_H5"]
                snap_path = values["-PATH2SNAPS-"]
                bird_net = bird_finder(path_to_model=model_path, path_to_snapshots=snap_path)
                bird_net.check_for_images()
                predictions, _ = bird_net.predict()
                for idx, img in enumerate(bird_net.imgz):
                    # Build a result for the user
                    prediction_string = 'Species (EN): ' + indexToBird(predictions[idx])
                    print(prediction_string)
                    imgTxt = cv2.putText(img,
                                         text=prediction_string, 
                                         org = (200,100), 
                                         fontFace = cv2.FONT_HERSHEY_PLAIN, 
                                         fontScale=1, 
                                         color=(255,255,255),
                                         thickness=3,
                                         lineType= cv2.LINE_AA,
                                         bottomLeftOrigin=True
                                         )
                    cv2.namedWindow(prediction_string,cv2.WINDOW_NORMAL)
                    cv2.resizeWindow(prediction_string, 400,400)
                    cv2.imshow(prediction_string, imgTxt)
                    cv2.waitKey()
                    
        self.window.close()