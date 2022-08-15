import PySimpleGUI as sg
import threading
import cv2
from tools import indexToBird


from model import bird_finder

class a_gui():
    def __init__(self,):

        sg.theme('Light Brown 3')
        layout = [[sg.Text('Navigate to the bird snapshots folder')],
                  [sg.FolderBrowse(key="-PATH2SNAPS-")],
                  [sg.Button('Classify birds', size=(50, 1))],
                  [sg.Text('Have fun dad!')]
        ]
      
        self.window = sg.Window('Bird Classifier', layout)
        

    def life_support(self,):
        while True:
            event, values = self.window.read()
            
            if event in (sg.WIN_CLOSED, 'Exit'):
                break
            
            elif event.startswith('Go'):
                snap_path = values["-PATH2SNAPS-"]
                bird_net = bird_finder(path_to_snapshots=snap_path)
                bird_net.check_for_images()
                predictions, _ = bird_net.predict()
                for idx, img in enumerate(self.bird_net.imgz):
                    # Build a result for the user
                    human_words = indexToBird(predictions[idx])
                    prediction_string = 'Species: ' + human_words
                    print(prediction_string)
                    cv2.imshow(prediction_string, img)
                    cv2.waitKey()
                    
        self.window.close()