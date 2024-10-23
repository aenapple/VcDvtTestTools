
import os
import sys
from InterfaceVIP import *
from InterfaceVIP50 import *
import keyboard
import json

sys.stdout.flush()


MOTOR_MIX_FWD = 0
MOTOR_MIX_BCK = 1


def mainMotorCw():
    print('Main Motor')
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_MAIN, 10, 0)
    time.sleep(5.0)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_MAIN, 0, 0)
  
def mainMotorCcw():
    print('Main Motor')
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_MAIN, 10, 1)
    time.sleep(5.0)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_MAIN, 0, 1)
  
def stopAll():
    print("Stopping all")
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, 0, MOTOR_MIX_FWD)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, 0, MOTOR_MIX_BCK)

    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, 0, MOTOR_MIX_FWD)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, 0, MOTOR_MIX_BCK)

    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_MAIN, 0, MOTOR_MIX_FWD)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_MAIN, 0, MOTOR_MIX_BCK)

    padHeatersOff()
    PtcBlowerOff()
    PtcIntakeOff()
    intakeFanOff()
    BlowerOff()

def leftMotorFwd():
    print("left_fwd")
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, 0, MOTOR_MIX_FWD)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, 0, MOTOR_MIX_BCK)
    time.sleep(0.5)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, MOTOR_PWM, MOTOR_MIX_FWD)

def leftMotorBck():
    print("left_bck")
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, 0, MOTOR_MIX_FWD)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, 0, MOTOR_MIX_BCK)
    time.sleep(0.5)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, MOTOR_PWM, MOTOR_MIX_BCK)

def rightMotorFwd():
    print("right_fwd")
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, 0, MOTOR_MIX_FWD)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, 0, MOTOR_MIX_BCK)
    time.sleep(0.5)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, MOTOR_PWM, MOTOR_MIX_FWD)
    
def rightMotorBck():
    print("right_bck")
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, 0, MOTOR_MIX_FWD)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, 0, MOTOR_MIX_BCK)
    time.sleep(0.5)
    pvtIntefaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, MOTOR_PWM, MOTOR_MIX_BCK)

def padHeatersOn():
    print("Pad Heaters On")
    pvtIntefaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_RIGHT, 100)
    pvtIntefaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_LEFT, 100)

def padHeatersOff():
    print("Pad Heaters Off")
    pvtIntefaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_RIGHT, 0)
    pvtIntefaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_LEFT, 0)

def PtcBlowerOn():
    print("Blower Ptc On")
    pvtIntefaceVIP.cmd_control_heater(IFC_VIP_HEATER_PTC_BLOWER, 30)

def PtcBlowerOff():
    print("Blower Ptc Off")
    pvtIntefaceVIP.cmd_control_heater(IFC_VIP_HEATER_PTC_BLOWER, 0)

def PtcIntakeOn():
    print("Intake Ptc On")
    pvtIntefaceVIP.cmd_control_heater(IFC_VIP_HEATER_PTC_INTAKE, 30)

def PtcIntakeOff():
    print("Intake Ptc Off")
    pvtIntefaceVIP.cmd_control_heater(IFC_VIP_HEATER_PTC_INTAKE, 0)
  
def intakeFanOn():
    print("intake Fan On")
    pvtIntefaceVIP.cmd_control_fan(   IFC_VIP_FAN_INTAKE,    FAN_PWM)

def intakeFanOff():
    print("intake Fan Off")
    pvtIntefaceVIP.cmd_control_fan(IFC_VIP_FAN_INTAKE, 0)

def getNTCTemperatures():
    pad_l_result, pad_l     = pvtIntefaceVIP.get_temperature(IFC_VIP_T_PAD_HEATER_LEFT)
    pad_r_result, pad_r     = pvtIntefaceVIP.get_temperature(IFC_VIP_T_PAD_HEATER_RIGHT)
    intake_result, intake   = pvtIntefaceVIP.get_temperature(IFC_VIP_T_PTC_HEATER_INTAKE)
    main_result,   main     = pvtIntefaceVIP.get_temperature(IFC_VIP_T_PTC_HEATER_BLOWER)

    try:
        print("Pad Left temperature: ", pad_l[2])
    except:
        print(pad_l)

    try:
        print("Pad Right temperature: ", pad_r[2])
    except:
        print(pad_r)

    try:
        print("Intake temperature: ", intake[2])
    except:
        print(intake)

    try:
        print("Main temperature: ", main[2])
    except:
        print(main)

def BlowerOn():
    print("Blower On")
    pvtIntefaceVIP.cmd_control_fan(   IFC_VIP_FAN_BLOWER,    FAN_PWM)

def BlowerOff():
    print("BlowerOff")
    pvtIntefaceVIP.cmd_control_fan(   IFC_VIP_FAN_BLOWER,    0)

def getBmeSensors():
    for i in range(4):
        result, read_data = pvtIntefaceVIP.get_bme688(i, 0)
        if result == 0:
            string_data  = "numSensor = "           + str(pvtIntefaceVIP.get_bme_num_sensor())
            string_data += ", Temperature = "       + str(pvtIntefaceVIP.get_bme_temperature())
            string_data += ", Humidity = "          + str(pvtIntefaceVIP.get_bme_humidity())
            string_data += ", Pressure = "          + str(pvtIntefaceVIP.get_bme_pressure())
            string_data += ", Gas Resistance = "    + str(pvtIntefaceVIP.get_bme_gas_resistance())
            print(string_data)
        else:
            print(result)

def getWeightSensors():
    for i in range(1, 3):
        result, read_data = pvtIntefaceVIP.get_weight(i)
        
        if result == 0:
            sens_num, weight  = struct.unpack('<xbIxxxxxxxxxx', read_data)
            print(f"Weight Sensor {sens_num} Values:", weight)
        else:
            print(result)
    pass

def getMotorCurrent():
    for i in range(2, 4):
        result, read_data = pvtIntefaceVIP.get_state_motor(i)

        if result == 0:
            sens_num, current  = struct.unpack('<xbxxxxHxxxxxxxx', read_data)
            print(f"Motor {i} Current:", current)
        else:
            print(result)

    pass

def ReadState():
    print()
    print("ReadState")
    result, data = pvtIntefaceVIP.read_state()
    state_sensors = pvtIntefaceVIP.get_sensor_state()

    print("Switches Lock:", state_sensors & IFC_VIP_STATE_SWITCHES_LOCK)
    print("Front Lid Open:", state_sensors & IFC_VIP_STATE_SWITCH_FRONT_LID_OPEN)
    print("Back Lid Open:", state_sensors & IFC_VIP_STATE_SWITCH_BACK_LID_OPEN)
    print("Switch Left:", state_sensors & IFC_VIP_STATE_SWITCH_PRESENT_CH_LEFT)
    print("Switch Right:",state_sensors & IFC_VIP_STATE_SWITCH_PRESENT_CH_RIGHT)


def GetSerial():
    result, result = pvtIntefaceVIP.get_serial(1)
    part_1, ser_part2  = struct.unpack('<xbQxxxxxx', result)

    result, result = pvtIntefaceVIP.get_serial(2)
    part_2, ser_part2  = struct.unpack('<xbQxxxxxx', result)


if __name__ == '__main__':


    PVT_COMPORT = "COM7"
        
    pvtIntefaceVIP = InterfaceVIP50()
    result = pvtIntefaceVIP.open(PVT_COMPORT, 115200)
    if result != 0:
        SystemExit(1)

    print("running")
    MOTOR_PWM     = 100
    FAN_PWM       = 50

    # keyboard.add_hotkey('-',     main_motor_cw)
    # keyboard.add_hotkey('=',     main_motor_ccw)

    keyboard.add_hotkey('shift+q', ReadState)


    keyboard.add_hotkey('q', stopAll)

    keyboard.add_hotkey('w', leftMotorFwd)
    keyboard.add_hotkey('s', leftMotorBck)
    
    keyboard.add_hotkey('r', rightMotorFwd)
    keyboard.add_hotkey('f', rightMotorBck)


    keyboard.add_hotkey('b', getBmeSensors)
    keyboard.add_hotkey('m', getWeightSensors)

    keyboard.add_hotkey('c', getMotorCurrent)




    keyboard.add_hotkey('t', getNTCTemperatures)

    keyboard.add_hotkey('shift+P', padHeatersOn)

    keyboard.add_hotkey('i', intakeFanOn)
    keyboard.add_hotkey('k', intakeFanOff)
    keyboard.add_hotkey('shift+I', PtcIntakeOn)
    keyboard.add_hotkey('shift+k', PtcIntakeOff)


    keyboard.add_hotkey('o', BlowerOn)
    keyboard.add_hotkey('l', BlowerOff)
    keyboard.add_hotkey('shift+o', PtcBlowerOn)
    keyboard.add_hotkey('shift+l', PtcBlowerOff)



    # keyboard.add_hotkey('up',   lambda: (FAN_PWM += 1))
    # keyboard.add_hotkey('down', lambda: (FAN_PWM -= 1))

    
    while True:
        
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN and event.name == 'z':
            FAN_PWM += 1
            if FAN_PWM >= 100:
                FAN_PWM = 100
            print("FAN PWM: ", FAN_PWM)
        if event.event_type == keyboard.KEY_DOWN and event.name == 'x':
            FAN_PWM -= 1
            if FAN_PWM <= 0:
                FAN_PWM = 0
            print("FAN PWM: ", FAN_PWM)
        # getMotorCurrent()
        # dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # print(dt)
