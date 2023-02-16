import cv2
import os 
import numpy as np
import json
import codecs

# Change these variables to your desired values #i olarak variable ismi degisecek

counter=0
out_folder = 'P:/USERDATA/Desktop/labeled_photos/' # Folder to save the video 
with open(r"P:\USERDATA\Desktop\videolarin_adlari.txt", 'r') as f:
    for img_no in f: 
        mp = ".avi"
        precise_extension = "result" + str(img_no) + str(mp)
        precise_extension= ''.join(precise_extension.splitlines())        
        path = "P:/USERDATA/Desktop/cut_frames/" + precise_extension        
        print(path)
        counter = counter +1
        print(counter)
        if counter<186:
            continue

#in_folder = 'P:\USERDATA\Desktop\cut_frames\' # Folder where the video is
#in_file = "result" + 1569992340 # Name of the video (without extension)
#in_path = in_folder + str(in_file) + '.mp4' 
#out_comeback = '../..' # Folder to go after finish the labeling (optional)
## You do not need to change from here on

        y = np.empty (0, np.int8)
        i = int(0)
        last_label = 1
        delay = 25  # waitKey delay, interframes (at delay 1 it runs ~2x the speed)
        jump_step = 50 # frames to jump in return/advance

        cap = cv2.VideoCapture(path) 
        if (cap.isOpened()== False): 
            print("Error opening video file")

        print("Video acildi")
        os.chdir(out_folder)
        while(cap.isOpened()): 
            #print("video devam edior ve acildi")
            y = np.insert(y, i, last_label)
            ret, frame = cap.read()
            i+=1

            if ret == True: 
                #print("sorunsuz isleme")
                cv2.putText(frame, "Label: {}".format(last_label), (500, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                cv2.imshow('Frame', frame) 
        
            # To the meaning of each class, read the documentation
            # You can also rewind, advance or pause 
                c = cv2.waitKey(delay) & 0xFF
        
                if c == ord(' '): # pause
                    while True:
                        c = cv2.waitKey(delay) & 0xFF
                        if c!=255: 
                            print("255")
                            break  
                if c == ord('0'): last_label = 0 #for drinking
                elif c == ord('1'): last_label = 1 #for not drinking
                elif c == ord('3'): last_label = 3 #for unknown
                elif c == ord('a'): # back
                    i = int(cap.get(cv2.CAP_PROP_POS_FRAMES) - jump_step)
                    if i<0: i=0
                    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
                elif c == ord('d'):  # avance
                    last_label = -1
                    for i in range(i, i+jump_step): y = np.insert(y, i, last_label)
                    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
                elif c == ord('q'): # exit 
                    break
            else: break # end of video, so break the loop 

        print('-----------------------------------------------------')
        print ('Labeled video: ', str(img_no))
        print('Number of frames: ', cap.get(cv2.CAP_PROP_POS_FRAMES))           
        y = y[:int(cap.get(cv2.CAP_PROP_POS_FRAMES))] # workaround

        # close
        #%cd $out_comeback
        cap.release() # release the video capture object 
        cv2.destroyAllWindows() # Closes all the frames 

# print stats
        print ('File duration: %d frames = %f seconds' % (len(y), float(len(y))/25))
        unique, counts = np.unique(y, return_counts=True)
        print(dict(zip(unique, counts)))
        print('-----------------------------------------------------')
        out_path = out_folder + str(img_no) + '.json'
        out_path=''.join(out_path.splitlines())  #DUN SON EKLEDIGIM KODDDDDDDDDDDDDDDDDDDDDDDD
        print(out_path)
        json.dump(y.tolist(), codecs.open(out_path, 'w', encoding='utf-8')) # saves the array in .json format

print("finished!!!!!!!!!!!!!!!!!!!")