#!/usr/bin/env python3
import smbus
import RPi.GPIO as gp # sudo pip install Jetson.GPIO #https://pypi.org/project/Jetson.GPIO/#description
import os

def activate_port(port_name : str, bus : smbus):
    device_address = 0x70
    if port_name == "A" :
        gp.output(7, False)
        gp.output(11, False)
        gp.output(12, True)
        bus.write_byte_data(device_address,0x00,0x04)
        return True 
    elif port_name == "B" :
        gp.output(7, True)
        gp.output(11, False)
        gp.output(12, True)
        bus.write_byte_data(device_address,0x00,0x05)
        return True
    elif port_name == "C":
        gp.output(7, False)
        gp.output(11, True)
        gp.output(12, False)
        bus.write_byte_data(device_address,0x00,0x06)
        return True
    elif port_name == "D" :
        gp.output(7, True)
        gp.output(11, True)
        gp.output(12, False)
        bus.write_byte_data(device_address,0x00,0x07)
        return True
    else :
        print("Wrong port name. Port Name has to be between { A, B, C, D}")
        return False
def setup_gpio():
    gp.setwarnings(False)
    gp.setmode(gp.BOARD)
    gp.setup(7, gp.OUT)
    gp.setup(11, gp.OUT)
    gp.setup(12, gp.OUT)

def gstreamer_pipeline (capture_width : int,capture_height : int ,display_width : int,display_height : int ,framerate : int, flip_method : int):

    return "nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)" + std::to_string(capture_width) + ", height=(int)" +
           std::to_string(capture_height) + ", format=(string)NV12, framerate=(fraction)" + std::to_string(framerate) +
           "/1 ! nvvidconv flip-method=" + std::to_string(flip_method) + " ! video/x-raw, width=(int)" + std::to_string(display_width) + ", height=(int)" +
           std::to_string(display_height) + ", format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink"
    


