from turtle import backward
import serial
import datetime
import time
import busio
import board import SCL, SDA
import argparse

from adafruit_pca9685 import PCA9685

def logging(filename):
    i2c_bus = busio.I2C(SCL, SDA)

    pca = PCA9685(i2c_bus)

    pca.frequency = 63

    left = 0x0b00           # 1100 / 
    sleft = 0x0e00          # 1200 / 
    mleft = 0x000f          # 1300 / 
    center = 0x1050         # 1408 / 
    right = 0x1500          # 1900 / 
    sright = 0x1200         # 1800 / 
    mright = 0x2000         # 1600 / 
    forward = 0x19f0        # 1408 / 
    stop = 0x1000           # 1408 / 
    backward = 0x1A70       # 1408 / 

    pca.channels[0].duty_cycle = center
    pca.channels[1].duty_cycle = stop

    f = open(filename, 'w')

    with serial.Serial('/dev/ttyACM0', 9600, timeout = 10) as ser:
        start = input('Do you want to start logging? [y,n] ') [0]
        if start in 'yY':
            ser.write(bytes("YES\n", "utf-8"))
            while True:
                ser_in = ser.readline()
                if(len(ser_in) != 8):
                    continue
                dyn = ser_in.decode('utf-8')

                print(dyn)

                # 아두이노 값 불러오기
                code = dyn[0:5]
                R1 = int(dyn[0])
                C1 = int(dyn[1])
                L1 = int(dyn[2])
                R2 = int(dyn[3])
                C2 = int(dyn[4])
                L2 = int(dyn[5])

                pca.channels[0].duty_cycle = center
                pca.channels[1].duty_cycle = stop
                
                if code == "001100" or code == "011110":
                    pca.channels[0].duty_cycle = center
                    pca.channels[1].duty_cycle = forward
                elif code == "011000" or code == "011100" or code == "111100":
                    pca.channels[0].duty_cycle = sleft
                    pca.channels[1].duty_cycle = forward
                elif code == "111000" or code == "010000":
                    pca.channels[0].duty_cycle = left
                    pca.channels[1].duty_cycle = forward
                elif code == "001110" or code == "000110" or code == "001111":
                    pca.channels[0].duty_cycle = sright
                    pca.channels[1].duty_cycle = forward
                elif code == "000111" or code == "000010":
                    pca.channels[0].duty_cycle = right
                    pca.channels[1].duty_cycle = forward
                elif code == "100000" or code == "110000":
                    pca.channels[0].duty_cycle = mleft
                    pca.channels[1].duty_cycle = forward
                elif code == "000001" or code == "000011":
                    pca.channels[0].duty_cycle = mright
                    pca.channels[1].duty_cycle = forward
                elif code == "000000":
                    pca.channels[1].duty_cycle = forward
                elif code == "101010":
                    # 정지선
                    pca.channels[0].duty_cycle = center
                    time.sleep(2)
                    pca.channels[1].duty_cycle = stop
                


    f.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="")
    parser.add_argument('log_file_name', metavar='F', type=str, nargs=1, help="log file's name")
    args = parser.parse_args()
    logging(args.log_file_name)