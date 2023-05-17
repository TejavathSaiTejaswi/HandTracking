import screen_brightness_control as sbc


##############################################
wCam, hCam = 640, 480

###############################################


# cap = cv2.VideoCapture(0)
# cap.set(3, wCam)
# cap.set(4, hCam)


# get the brightness
brightness = sbc.get_brightness()
print(brightness)
# get the brightness for the primary monitor
primary = sbc.get_brightness(display=0)
print(primary)
# set the brightness to 100%
sbc.set_brightness(100)
# set the brightness to 100% for the primary monitor
sbc.set_brightness(100, display=0)

# show the current brightness for each detected monitor
for monitor in sbc.list_monitors():
    print(monitor, ':', sbc.get_brightness(display=monitor), '%')
