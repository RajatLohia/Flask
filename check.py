print('#Hello from python#')  
import cv2
# aise python file run hoti hai js se hena
#han kal check.py hogayi thi run aur camera bhi khul gya tha browser se aj kyunis
print("not reached here")
# define a video capture object 
vid = cv2.VideoCapture(0) 
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read() 
    # Display the resulting frame 
    cv2.imshow('frame', frame) 
    #   kya dikhaun ?
    #    kha hai python env?
    #    matlab ? 
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 