import os
import sys
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from Interfaces.InterfaceVIP50 import *
import random
from TASKSYS import *
from dataClasses import *

MOTOR_MIX_FWD = 0
MOTOR_MIX_BCK = 1

def MixingCycle(interfaceVIP, motor, mix_phase, mixIntervalTime, mix_fwd, mix_bck):  
    match mix_phase:
        case 0:
            interfaceVIP.cmd_control_motor(motor, 100, MOTOR_MIX_FWD)
            mixPhase = 1
            mixingCounter = mix_fwd
        case 1:
            interfaceVIP.cmd_control_motor(motor, 0, MOTOR_MIX_FWD)
            time.sleep(1)
            interfaceVIP.cmd_control_motor(motor, 100, MOTOR_MIX_BCK)
            mixPhase = 2
            mixingCounter = mix_bck
        case 2:
            interfaceVIP.cmd_control_motor(motor, 0, MOTOR_MIX_BCK)
            time.sleep(1)
            interfaceVIP.cmd_control_motor(motor, 100, MOTOR_MIX_FWD)
            mixPhase = 3
            mixingCounter = mix_fwd
        case 3:
            interfaceVIP.cmd_control_motor(motor, 0, MOTOR_MIX_FWD)
            time.sleep(1)
            interfaceVIP.cmd_control_motor(motor, 100, MOTOR_MIX_BCK)
            mixPhase = 4
            mixingCounter = mix_bck*0.8
        case 4:
            interfaceVIP.cmd_control_motor(motor, 0, MOTOR_MIX_BCK)
            interfaceVIP.cmd_control_motor(motor, 0, MOTOR_MIX_FWD)
            mixPhase = 0
            mixingCounter = mixIntervalTime
        
    return mixPhase, mixingCounter

def GetBmeData(interfaceVIP, location):
    result, read_data = interfaceVIP.get_bme688(location, 0)
    try:
        bmeNumSensor, bmeTemperature, bmeHumidity, bmePressure, bmeGasResistance = struct.unpack('<xbhHIIxx', read_data)
    except:
        bmeNumSensor = -1 
        bmeTemperature = 0 
        bmeHumidity = 0 
        bmePressure = 0 
        bmeGasResistance = 0
        
    if (bmeNumSensor == -1):
        result = 1

    
    return  result, TBme688Sensor(temperature=bmeTemperature, humidity=bmeHumidity, pressure=bmePressure, gasResistance=bmeGasResistance)


# def GetPTCTemperature(interfaceVIP):
#     intake_result, left = interfaceVIP.get_temperature(IFC_VIP_T_PTC_HEATER_LEFT)
#     main_result,  right  = interfaceVIP.get_temperature(IFC_VIP_T_PTC_HEATER_RIGHT)


#     if  intake_result:
#         left = -1
#     else:
#         try:
#             left = left[2]
#         except:
#             left = -2


#     if  main_result:
#         right = -1
#     else:
#         try:
#             right = right[2]
#         except:
#             right = -2

#     return left, right


def GetPTCTemperatureP50(interfaceVIP):
    main_result,  main  = interfaceVIP.get_temperature(IFC_VIP_T_PTC_HEATER_BLOWER)
    intake_result, intake = interfaceVIP.get_temperature(IFC_VIP_T_PTC_HEATER_INTAKE)

    if  main_result:
        main = -1
    else:
        try:
            main = main[2]
        except:
            main = -2

    if  intake_result:
        intake = -1
    else:
        try:
            intake = intake[2]
        except:
            intake = -2

    return main, intake

def GetPadTemperature(interfaceVIP):
    right_result, right = interfaceVIP.get_temperature(IFC_VIP_T_PAD_HEATER_RIGHT)
    left_result,  left = interfaceVIP.get_temperature(IFC_VIP_T_PAD_HEATER_LEFT)

    if  right_result:
        right = -1
    else:
        try:
            right = right[2]
        except:
            right = -2


    if  left_result:
        left = -1
    else:
        try:
            left = left[2]
        except: 
            left = -2

    return left, right


def GetMotorCurrent(interfaceVIP, motor):

    result, read_data = interfaceVIP.get_state_motor(motor)


    if result == 0:
        try:
            sens_num, current  = struct.unpack('<xbxxxxHxxxxxxxx', read_data)

        except:
            current = -2
    else:
        current = -1

    return current

    

def GetWeightData(interfaceVIP):

    left_result,    left = interfaceVIP.get_weight(IFC_VIP_WEIGHT_LEFT)
    right_result,   right  = interfaceVIP.get_weight(IFC_VIP_WEIGHT_RIGHT)
    try:
        sens_num,front = struct.unpack('<xbIxxxxxxxxxx', right)
        sens_num, back  = struct.unpack('<xbIxxxxxxxxxx', right)
    except:
        front = -2
        back  = -2
    
    right = [front, back]

    try:
        sens_num,front = struct.unpack('<xbIxxxxxxxxxx', left)
        sens_num,back  = struct.unpack('<xbIxxxxxxxxxx', left)
    except:
        front = -2
        back  = -2

    left = [front, back]

    return left, right  




# def ActivatePtc(interfaceVIP, ptcFanPwm):
#     interfaceVIP.cmd_control_fan(   IFC_VIP_FAN_PTC_RIGHT,    ptcFanPwm)
#     interfaceVIP.cmd_control_fan(   IFC_VIP_FAN_PTC_LEFT,     ptcFanPwm)    
#     interfaceVIP.cmd_control_fan(   IFC_VIP_FAN_MAIN,    0)    
    

def ActivateIntakeFan(interfaceVIP, intakeFanPwm):
    interfaceVIP.cmd_control_fan(   IFC_VIP_FAN_INTAKE,    intakeFanPwm)
    LogActuators.LOG_Intake_Fan_PWM = intakeFanPwm

def ActivateIntakePTC(interfaceVIP, intakePtcPwm):
    interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PTC_INTAKE, intakePtcPwm)
    LogActuators.LOG_Intake_PTC_PWM = intakePtcPwm

def ActivateBlower(interfaceVIP, blowerPwm):
    interfaceVIP.cmd_control_fan(   IFC_VIP_FAN_BLOWER,    blowerPwm)
    LogActuators.LOG_Blower_Fan_PWM = blowerPwm

def ActivateBlowerPTC(interfaceVIP, blowerPtcPwm):
    interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PTC_BLOWER, blowerPtcPwm)
    LogActuators.LOG_Blower_PTC_PWM = blowerPtcPwm


# def TurnOffActuators(interfaceVIP):
#     interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_RIGHT, 0)
#     interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PTC_RIGHT, 0)
#     interfaceVIP.cmd_control_fan(   IFC_VIP_FAN_PTC_RIGHT, 0)
    
#     interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_LEFT, 0)
#     interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PTC_LEFT, 0)
#     interfaceVIP.cmd_control_fan(   IFC_VIP_FAN_PTC_LEFT, 0)

#     interfaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, 0, 0)
#     interfaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_RIGHT, 0, 1)
#     interfaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, 0, 0)
#     interfaceVIP.cmd_control_motor(IFC_VIP_MOTOR_CHAMBER_LEFT, 0, 1)

#     interfaceVIP.cmd_control_fan(  IFC_VIP_FAN_MAIN, 0)
