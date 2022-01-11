import streamlit as st
import cv2
from collections import deque
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
#from collections import deque
import streamlit.components.v1 as components


st.title("Air Canvas Using OpenCV")


app_mode = st.sidebar.selectbox("Select the App Mode", ("Home","About Us", "Project"))

if app_mode == "Home":
    
    html_temp = """
        <body style="background-color:red;">
        <div style="background-color:teal ;padding:10px">
        <h2 style="color:white;text-align:center;">EXPLORE THE VIRTUAL PAINTER</h2>
        </div>
        </body>
        """
    h_t ="""
    <head>
    <link rel="stylesheet" type="text/css" href="E:\Sadhu_Final_OpenCV\style_home.css" media=”screen” />
    </head>
    <img src="https://miro.medium.com/max/1400/1*1Vo8FRSa5TAeOirIKa92fQ.png"  width="600" height="450"/>
        <h2>Introduction </h2>
        <p> One of the oldest fascinations of humankind has
        always been the desire to write in air and in the recent years, this
        has turned into a competitive research field. Existence of such a
        system can ameliorate the user-system interface in multiple
        applications</p>
        <h2>Description</h2>
        <p></p>
        <h2>Features</h2>
        <div>
    <ul>
        <li>User Friendly</li>
        <li>Robust</li>
        <li>Efficient</li>
    </ul>
    </div>
            <h2>Benefits</h2>
            <p>The proposed system has the capability to eliminate
    conventional ways of writing. With the use of this system,
    one wouldn’t need notebooks or cell phones in order to
    write down important notes. This system also has the
    potential to serve people with hearing impairment or
    people with difficulty using keyboards. Extended version
    of this project can be used as an OCR. The generated text
    can be sent as an email, text message or a simple word
    document. </p>
    """
    st.markdown(h_t, unsafe_allow_html=True)

if app_mode == "About Us":
    # bootstrap 4 collapse example
    # components.html(
    # """
    # </div>

    #     <h1>Welcome home</h1>
    # </div>
    # """,
    # height=600,
    # )
    
    html_t = """
    <body style="background-color:red;">
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;">EXPLORE THE VIRTUAL PAINTER</h2>
    
    </div>
    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQsKc6FPQh_56dcMzgOkl-ADoIGMnF_Fw8TYw&usqp=CAU" />
    
    """
    st.markdown(html_t, unsafe_allow_html=True)

    st.markdown('In this Application, we are using *OpenCV* for creating a Virtual Painter App. *StreamLit* is used for creating the Graphical User Interface.')
    st.image("data:image/jpeg;base64,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")

    components.html(
    """
       <head>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
        
            <style>
            html {
            box-sizing: border-box;
            }

            *, *:before, *:after {
            box-sizing: inherit;
            }

            .column {
            float: left;
            width: 33.3%;
            margin-bottom: 16px;
            padding: 0 8px;
            }

            @media screen and (max-width: 650px) {
            .column {
                width: 100%;
                display: block;
            }
            }

            .card {
            box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
            }

            .container {
            padding: 0 16px;
            }

            .container::after, .row::after {
            content: "";
            clear: both;
            display: table;
            }

            .title {
            color: grey;
            }

            .button {
            border: none;
            outline: 0;
            display: inline-block;
            padding: 8px;
            color: white;
            background-color: #000;
            text-align: center;
            cursor: pointer;
            width: 100%;
            }

            .button:hover {
            background-color: #555;
            }
            </style>
            </head>
            <body>

            <h2>Meet The Team</h2>
            <div class="row">
            <div class="column">
                <div class="card">
                <img src="https://cdn1.iconfinder.com/data/icons/website-internet/48/website_-_female_user-512.png"  alt="Jane" style="width:100%">
                <div class="container">
                    <h2>Ruchika Agrawal</h2>
                    <p class="title">Content Writer and Design Lead</p>
                    <p>18ETCS002101</p>
                    <p>Some text that describes me lorem ipsum ipsum lorem.</p>
                    <p>ruchikaagrawal@gmail.com</p>
                    <p><button class="button">Contact</button></p>
                </div>
                </div>
            </div>

            <div class="column">
                <div class="card">
                <img src="https://cdn1.iconfinder.com/data/icons/website-internet/48/website_-_female_user-512.png" alt="Mike" style="width:100%">
                <div class="container">
                    <h2>S Sadhana</h2>
                    <p class="title">Team Lead & Schedule Manager</p>
                    <p>18ETCS002102</p>
                    <p>Some text that describes me lorem ipsum ipsum lorem.</p>
                    <p>sadhana1058@gmail.com</p>
                    <p><button class="button">Contact</button></p>
                </div>
                </div>
            </div>
            
            <div class="column">
                <div class="card">
                <img src="https://cdn1.iconfinder.com/data/icons/website-internet/48/website_-_female_user-512.png" alt="John" style="width:100%">
                <div class="container">
                    <h2>Sunidhi V</h2>
                    <p class="title">Design Lead </p>
                    <p>18ETCS002125</p>
                    <p>Some text that describes me lorem ipsum ipsum lorem.</p>
                    <p>sunidhivenkatesh2000@gmail.com</p>
                    <p><button class="button">Contact</button></p>
                </div>
                </div>
            </div>
            </div>

            </body>
    """,
        height=800,
    )

else:
    st.sidebar.markdown("---")

    mode = st.sidebar.selectbox("Select the Mode", ("Draw", "Clear All"))
    if mode == "Draw":
        st.sidebar.markdown("---")
        color_name = st.sidebar.selectbox("Select Color", ("Red", "Green", "Blue"))
        st.write(f"Color : {color_name}")
                

        if st.button("Web Camera"):
            #set to defaults
            def setValues(x):
                print("")


            # selecting the colour of the pointer(RED)
            cv2.namedWindow("Color detectors")
            cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180,setValues)
            cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255,setValues)
            cv2.createTrackbar("Upper Value", "Color detectors", 255, 255,setValues)
            cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180,setValues)
            cv2.createTrackbar("Lower Saturation", "Color detectors", 120, 255,setValues)
            cv2.createTrackbar("Lower Value", "Color detectors", 176, 255,setValues)


            # Providing colour options
            bpoints = [deque(maxlen=1024)]
            gpoints = [deque(maxlen=1024)]
            rpoints = [deque(maxlen=1024)]
            ypoints = [deque(maxlen=1024)]

            blue_index = 0
            green_index = 0
            red_index = 0
            yellow_index = 0

            #The kernel to be used for dilation
            kernel = np.ones((5,5),np.uint8)

            colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255)]
            colorIndex = 0

            # Paint/Air Canvas setup
            paintWindow = np.zeros((471,636,3)) + 255
            paintWindow = cv2.rectangle(paintWindow, (40,1), (140,65), (0,0,0), 2)
            # paintWindow = cv2.rectangle(paintWindow, (145,1), (158,65),(0,0,0), 2)
            paintWindow = cv2.rectangle(paintWindow, (160,1), (255,65), colors[0], -1)
            paintWindow = cv2.rectangle(paintWindow, (275,1), (370,65), colors[1], -1)
            paintWindow = cv2.rectangle(paintWindow, (390,1), (485,65), colors[2], -1)
            paintWindow = cv2.rectangle(paintWindow, (505,1), (600,65), colors[3], -1)
            


            cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            # cv2.putText(paintWindow, "print", (152, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
            cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
            cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)   
            vid = cv2.VideoCapture(0)

            while(True):
                ret, frame = vid.read()
                frame = cv2.flip(frame, 1)
                hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

                u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
                u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
                u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
                l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
                l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
                l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
                Upper_hsv = np.array([u_hue,u_saturation,u_value])
                Lower_hsv = np.array([l_hue,l_saturation,l_value])


                # Adding the colour buttons to the camera frame for colour access
                frame = cv2.rectangle(frame, (40,1), (140,65), (122,122,122), -1)
                frame = cv2.rectangle(frame, (160,1), (255,65), colors[0], -1)
                frame = cv2.rectangle(frame, (275,1), (370,65), colors[1], -1)
                frame = cv2.rectangle(frame, (390,1), (485,65), colors[2], -1)
                frame = cv2.rectangle(frame, (505,1), (600,65), colors[3], -1)
                cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)

                # masking the pointer so that it can be identified easily
                Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
                Mask = cv2.erode(Mask, kernel, iterations=1)
                Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
                Mask = cv2.dilate(Mask, kernel, iterations=1)

                # Contours for the pointer after identifying it, using numpy
                cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,
                    cv2.CHAIN_APPROX_SIMPLE)
                center = None

                # contours are formed
                if len(cnts) > 0:
                    # to find the biggest contour
                    cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
                    ((x, y), radius) = cv2.minEnclosingCircle(cnt)
                    # Draw the circle around the contour
                    cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                    # Calculating the center of the detected contour
                    M = cv2.moments(cnt)
                    center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']))

                    # to chekc if the user wants to click on any button above the screen
                    if center[1] <= 65:
                        if 40 <= center[0] <= 140: # Clear Button
                            bpoints = [deque(maxlen=512)]
                            gpoints = [deque(maxlen=512)]
                            rpoints = [deque(maxlen=512)]
                            ypoints = [deque(maxlen=512)]

                            blue_index = 0
                            green_index = 0
                            red_index = 0
                            yellow_index = 0

                            paintWindow[67:,:,:] = 255
                        elif 160 <= center[0] <= 255:
                                colorIndex = 0 # Blue
                        elif 275 <= center[0] <= 370:
                                colorIndex = 1 # Green
                        elif 390 <= center[0] <= 485:
                                colorIndex = 2 # Red
                        elif 505 <= center[0] <= 600:
                                colorIndex = 3 # Yellow
                    else :
                        if colorIndex == 0:
                            bpoints[blue_index].appendleft(center)
                        elif colorIndex == 1:
                            gpoints[green_index].appendleft(center)
                        elif colorIndex == 2:
                            rpoints[red_index].appendleft(center)
                        elif colorIndex == 3:
                            ypoints[yellow_index].appendleft(center)

                else:
                    bpoints.append(deque(maxlen=512))
                    blue_index += 1
                    gpoints.append(deque(maxlen=512))
                    green_index += 1
                    rpoints.append(deque(maxlen=512))
                    red_index += 1
                    ypoints.append(deque(maxlen=512))
                    yellow_index += 1

                # To draw lines
                points = [bpoints, gpoints, rpoints, ypoints]
                for i in range(len(points)):
                    for j in range(len(points[i])):
                        for k in range(1, len(points[i][j])):
                            if points[i][j][k - 1] is None or points[i][j][k] is None:
                                continue
                            cv2.line(frame, points[i][j][k - 1], points[i][j][k], colors[i], 2) #to display on camera screen
                            cv2.line(paintWindow, points[i][j][k - 1], points[i][j][k], colors[i], 2) #to display on paint

                # Show all the windows
                cv2.imshow("Air Canvas", frame)
                cv2.imshow("Virtual White Board", paintWindow)
                cv2.imshow("mask",Mask)


                # cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
