#!/usr/bin/env python3
import hardware
import argparse
import cv2
import time 
import smbus

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
                        help='Set window header name.')
    parser.add_argument('-h', '--height', type=int, nargs=None, required=True,
                        help='Set window header name.')
                    
def main(i2c_bus,left_port,right_port,window_name,framerate,capture):
    if capture.isOpened() :
        hardware.activate_port(left_port,i2c_bus)
        ret,left_frame = capture.read()
        hardware.activate_port(right_port,i2c_bus)
        ret,right_frame = capture.read()
        cv2.imshow(window_name+"_left",left_frame)
        cv2.imshow(window_name+"_right",right_frame)
        time.sleep(1/framerate)
        return left_frame,right_frame


if __name__ == "__main__":
    args = parse_cmdline()
    hardware.setup_gpio()
    print("i2c bus is",args.i2c_bus)
    print("left port : ",args.left_port)
    print("Right port : ",args.right_port)
    print("Window name : ",args.window_name)
    print("Framerate  : ",args.framerate)
    print("Image width : ",args.width)
    print("Image height : ",args.height)
    cap = cv2.VideoCapture(hardware.gstreamer_pipeline(args.widht,args.height,args.width,args.height,args.framerate,0),cv2.CAP_GSTREAMER)
    i2c = smbus.SMBus(args.i2c_bus)
    
    while True :
        main(i2c,args.left_port,args.right_port,args.window_name,args.framerate,cap)
    gp.output(7, False)
    gp.output(11, False)
    gp.output(12, True)
    