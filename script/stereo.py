#!/usr/bin/env python3
import hardware
import argparse
import cv2
import time 
import smbus
import signal
import sys
def sigterm_handler(_signo, _stack_frame):
    # Raises SystemExit(0):
    sys.exit(0)
signal.signal(signal.SIGINT, sigterm_handler)
signal.signal(signal.SIGTERM, sigterm_handler)
def parse_cmdline():
    parser = argparse.ArgumentParser(description='Arducam Stereo Controller.')
    parser.add_argument('-i', '--i2c-bus', type=int, nargs=None, required=True,
                        help='Set i2c bus, for Jetson Nano it is 1, for Jetson Xavier NX it is 8.')
    parser.add_argument('-lp', '--left-port', type=str, nargs=None, required=True,
                        help='Set left port Name. Port Name has to be between { A, B, C, D}')
    parser.add_argument('-rp', '--right-port', type=str, nargs=None, required=True,
                        help='Set left port Name. Port Name has to be between { A, B, C, D}')
    parser.add_argument('-d', '--window-name', type=str, nargs=None, required=True,
                        help='Set window header name.')
    parser.add_argument('-f', '--framerate', type=int, nargs=None, required=True,
                        help='Capture framerate not specified Default 20Hz will be used.')
    parser.add_argument('-w', '--width', type=int, nargs=None, required=True,
                        help='Set capture width with argument -w.')
    parser.add_argument('-he', '--height', type=int, nargs=None, required=True,
                        help='Set capture height with argument -he.')
    return parser.parse_args()
                    
def capture_loop(i2c_bus,left_port,right_port,window_name,framerate,capture):
    left_frame_rgb,right_frame_rgb = None,None
    if capture.isOpened() :
        hardware.activate_port(left_port,i2c_bus)
        cv2.waitKey(int((1/framerate)*500))
        if capture.grab():
            left_ret,left_frame = capture.retrieve()
            if left_ret :
                #left_frame_rgb = cv2.cvtColor(left_frame, cv2.COLOR_YUV2BGR_I420)
                cv2.imshow(window_name+"_left",left_frame)
        hardware.activate_port(right_port,i2c_bus)
        cv2.waitKey(int((1/framerate)*500))
        if capture.grab() :
            right_ret,right_frame = capture.retrieve()
            if right_ret :
                #right_frame_rgb = cv2.cvtColor(right_frame, cv2.COLOR_YUV2BGR_I420)
                cv2.imshow(window_name+"_right",right_frame)
        return True,left_frame_rgb,right_frame_rgb
    return False, None,None

args = parse_cmdline()
hardware.setup_gpio()
print("i2c bus is",args.i2c_bus)
print("Left port : ",args.left_port)
print("Right port : ",args.right_port)
print("Window name : ",args.window_name)
print("Framerate  : ",args.framerate)
print("Image width : ",args.width)
print("Image height : ",args.height)
i2c = smbus.SMBus(args.i2c_bus)
hardware.setup_gpio()
hardware.activate_port(args.left_port,i2c)
#cap = cv2.VideoCapture(hardware.gstreamer_pipeline2(args.width,args.height,args.framerate,0,0),cv2.CAP_GSTREAMER)
cap = cv2.VideoCapture(hardware.gstreamer_pipeline(args.width,args.height,args.width,args.height,args.framerate,0),cv2.CAP_GSTREAMER)
cv2.waitKey(1000)
if __name__ == "__main__":
    while True :
        capture_loop(i2c,args.left_port,args.right_port,args.window_name,args.framerate,cap)
gp.output(7, False)
gp.output(11, False)
gp.output(12, True)
    