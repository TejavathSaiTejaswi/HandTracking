import cv2
import mediapipe as mp
import time #to check the frame rate

mpHands = mp.solutions.hands
hands = mpHands.Hands() #because of the default parameters. We do not have to change
mpDraw = mp.solutions.drawing_utils # between each point if you draw a line

# to calculate the fps. (to calculate frame rate)
pTime = 0
cTime = 0
# ctrl and click on Hands to know more about the parameters
#static_image_mode by default is False(sometimes it detects and sometimes it tracks) so that it detects and track when there is confidence level
#-> if it is true then it detects the whole time which makes it quite slow so we will keep it as false(good tracking confidence, it keeps tracking otherwise no)
#max_num_hands=2,
#min_detection_confidence=0.5(50%)(If it goes below 50%, it does detection)
#min_tracking_confidence=0.5
#to create a video object

cap = cv2.VideoCapture(0)


while True:
    success, img = cap.read()
    #In the loop we are going to send RGB image to hands object
    # first convert it
    # hands object only uses RGB images
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results) #<class 'mediapipe.python.solution_base.SolutionOutputs'>
    #to check whether something is detected or not
    #print(results.multi_hand_landmarks) #-> we get some results when our hand is pplaced
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                print(id,lm) # index of the point position like from 0 to 20 and coordinates
                h, w, c = img.shape #height, width and channels of the image
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy) # to print coordinates for respective indexes instead of printing all of them
                if id == 0:
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

                #cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)


            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)