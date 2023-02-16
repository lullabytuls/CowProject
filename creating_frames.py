
# Importing all necessary libraries
from re import U
import cv2
import os
import time
# Read the video from specified path

counter=0

with open(r"P:\USERDATA\Desktop\videolarin_adlari.txt", 'r') as f: #videos_names.txt
    for img_no in f: 
        
        mp = ".avi"
        precise_extension = "result" + str(img_no) + str(mp)
        precise_extension= ''.join(precise_extension.splitlines())        
        path = "P:/USERDATA/Desktop/cut_frames/" + precise_extension        
        print(path)
        counter = counter +1
        if counter < 66:
            continue
        
        print(counter)
        print(img_no)
        printsp
        #time.sleep(7)
        
        cam = cv2.VideoCapture(path)
  
        try:
      
            # creating a folder named data
            if not os.path.exists('C:/Users/zeynep22000/cow_frames'):
                os.makedirs('C:/Users/zeynep22000/cow_frames')
            img_path = "C:/Users/zeynep22000/cow_frames" + img_no
            img_path = ''.join(img_path.splitlines())   

            if not os.path.exists(img_path):
                os.makedirs(img_path)
  
            # if not created then raise error
        except OSError:
            print ('Error: Creating directory of data')
  
# frame
        currentframe = 0
  
        while(True):
      
            # reading from frame
            ret,frame = cam.read()
  
            if ret:
                # if video is still left continue creating images
                
                name = img_path + "/" + img_no + "(" + str(currentframe) + ")" + '.jpg'
                name =  ''.join(name.splitlines())   
                print ('Creating...' + name)
  
               # writing the extracted images
                cv2.imwrite(name, frame)
    
                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
            else:
                break
  
        # Release all space and windows once done
        cam.release()
        cv2.destroyAllWindows()