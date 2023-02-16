from operator import iadd
import numpy as np
import cv2

# Open the video
with open(r"P:\USERDATA\Desktop\videolarin_adlari.txt", 'r') as f:
    for i in f: 
        mp = ".mp4"
        precise_extension = str(i) + str(mp)

        precise_extension= ''.join(precise_extension.splitlines())
        
        path = "P:/USERDATA/Desktop/video data/" + precise_extension        
        #print(path)
        
        
    

        #cap = cv2.VideoCapture('P:/USERDATA/Desktop/video data/1569135540.mp4')
        cap = cv2.VideoCapture(path)


    # Initialize frame counter
        cnt = 0

    # Some characteristics from the original video
        w_frame, h_frame = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps, frames = cap.get(cv2.CAP_PROP_FPS), cap.get(cv2.CAP_PROP_FRAME_COUNT)

    # Here you can define your croping values
        x,y,h,w = 1200,0,304,700

    # output
        

        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        first_part = "P:/USERDATA/Desktop/ayiklama/"  
        video_path = "result" + str(i) + ".avi"
        actual_path = first_part + video_path
        actual_path = ''.join(actual_path.splitlines())
        #print(actual_path)


        out = cv2.VideoWriter(actual_path, fourcc, fps, (w, h))

    # Now we start
        while(cap.isOpened()):
            ret, frame = cap.read()

            cnt += 1 # Counting frames

            # Avoid problems when video finish
            if ret==True:
            # Croping the frame
                crop_frame = frame[y:y+h, x:x+w]

            # Percentage
                xx = cnt *100/frames
                print(int(xx),'%')

            # Saving from the desired frames
            #if 15 <= cnt <= 90:
            #    out.write(crop_frame)

            # I see the answer now. Here you save all the video
                out.write(crop_frame)

            # Just to see the video in real time          
                cv2.imshow('frame',frame)
                cv2.imshow('croped',crop_frame)

                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break


        cap.release()
        out.release()
        cv2.destroyAllWindows()

