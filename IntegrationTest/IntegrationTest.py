import os
from os import path
from os import mkdir
import sys
import pandas as pd
import numpy as np
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)
from Interfaces.InterfaceVIP50 import *
from TASKSYS import *
from TASKHAL import *
from dataClasses import *
from strings import *


class IntegrationTest():
    def __init__(self, interfaceVIP) -> None:
        self.interfaceVIP = interfaceVIP

        self.blowerPtc   = TPTCControl(intervalTime=0,  counterWorkTime=0, 
                                     fanPwm=60, 
                                     dutyCycle=ptcDutyCycleMode_0, 
                                     tempRange=[73,75])
        
        self.intakePtc = TPTCControl(intervalTime=0,counterWorkTime=0, 
                                     fanPwm=50, 
                                     dutyCycle=ptcDutyCycleMode_0, 
                                     tempRange=[33,35])
        

        self.filterAi  = TFilterAI(isOdorFlag=False, 
                                   plasmaLampCounter= TASK_SYS_1_HOUR, plasmaOnFlag=False, 
                                   mlWindowCounter=TFilterAI.mlWindow)

        self.intakeAi  = TIntakeAI(mlWindowCounter=TIntakeAI.mlWindow)

        self.AiRight  = TChamberAI(mixingCounter=-1, 
                                   mlWindowCounter=TChamberAI.mlWindow, 
                                   taskRegion=TaskRegionRightChamber)
        
        self.AiRight.padTempRange = [73,75]
        
        self.AiRight.mixIntervalTime        =  TASK_SYS_60_MINUTES
        self.AiRight.increasingPadTempFlag   =  True
      
        
        self.AiLeft   = TChamberAI(mixingCounter=-1, 
                                   mlWindowCounter=TChamberAI.mlWindow, 
                                   taskRegion=TaskRegionLeftChamber)
        
        self.AiLeft.padTempRange = [33, 35]

        self.AiLeft.mixIntervalTime         =  TASK_SYS_60_MINUTES
        self.AiLeft.increasingPadTempFlag   =  True


        TChamberAI.tempRange            = [3300, 3500]
        TChamberAI.tempRangeCounter     = TASK_SYS_90_MINUTES
        TChamberAI.padTempRangeCounter  = TASK_SYS_30_MINUTES
        TChamberAI.increasingChamberTempFlag = True




        self.blowerPtc   = TPTCControl(intervalTime=0,  counterWorkTime=0, 
                                     fanPwm=60, 
                                     dutyCycle=ptcDutyCycleMode_0, 
                                     tempRange=[73,75])

        self.blowerPtc.fanPwmCounter              = TASK_SYS_15_MINUTES
        self.blowerPtc.fanPwm                     = 0    
        self.blowerPtc.increasingFanPwmFlag       = True
        self.blowerPtc.tempRangeCounter           = TASK_SYS_10_MINUTES
        self.blowerPtc.increasingTempRangeFlag    = False

        self.intakePtc = TPTCControl(intervalTime=0,counterWorkTime=0, 
                                     fanPwm=50, 
                                     dutyCycle=ptcDutyCycleMode_0, 
                                     tempRange=[33,35])
        


        self.intakePtc.fanPwmCounter            = TASK_SYS_15_MINUTES
        self.intakePtc.fanPwm                   = 0   
        self.intakePtc.increasingFanPwmFlag     = False 

        self.filterAi                   = TFilterAI(isOdorFlag=False, 
                                                    plasmaLampCounter= TASK_SYS_1_HOUR, plasmaOnFlag=False, 
                                                    mlWindowCounter=TFilterAI.mlWindow)

        self.filterAi.plasmaOnFlag               = 0
        self.filterAi.depletionTime              = TASK_SYS_2_HOURS # TODO; GOtta get this depletion time stuff sorted out too
        self.filterAi.depletionFlag              = False 

        self.incrementCounter           = TASK_PROC_INCREMENT
        # self.incrementCounter           = 5
        self.increment                  = self.incrementCounter


    def QueryAllData(self):
        self.left_bme_result,    self.AiLeft.bmeData.currBme    = GetBmeData(self.interfaceVIP, 0)
        self.right_bme_result,   self.AiRight.bmeData.currBme   = GetBmeData(self.interfaceVIP, 1)
        self.intake_bme_result,  self.intakeAi.bmeData.currBme  = GetBmeData(self.interfaceVIP, 2)
        self.filter_bme_result,  self.filterAi.bmeData.currBme   = GetBmeData(self.interfaceVIP, 3)

        self.AiLeft.currMass, self.AiRight.currMass  = GetWeightData(self.interfaceVIP)


        try:
            self.AiLeft.currPadTemp, self.AiRight.currPadTemp = GetPadTemperature(self.interfaceVIP)
            blowerPtc_t, intakePtc_T = GetPTCTemperatureP50(self.interfaceVIP)
        except:
            self.AiLeft.currPadTemp, self.AiRight.currPadTemp = -2, -2
            blowerPtc_t, intakePtc_T = -2, -2

        
        self.blowerPtc.currPtcTemp = blowerPtc_t
        self.intakePtc.currPtcTemp = intakePtc_T


    def Run(self):
        if (self.incrementCounter > 0):
            self.incrementCounter -= 1
            self.ModulateHeatersUsingNTC(self.blowerPtc.tempRange[0], self.blowerPtc.tempRange[1], 
                                         self.AiLeft.padTempRange[0], self.AiLeft.padTempRange[1],
                                         self.AiRight.padTempRange[0], self.AiRight.padTempRange[1])
            

            if self.AiRight.mixingCounter <= 0:
                if self.AiLeft.mixPhase == 0:
                    self.AiRight.mixPhase, self.AiRight.mixingCounter = MixingCycle(self.interfaceVIP, IFC_VIP_MOTOR_CHAMBER_RIGHT, 
                                                                                    self.AiRight.mixPhase, self.AiRight.mixIntervalTime, 
                                                                                    self.AiRight.mixDuration[0], self.AiRight.mixDuration[1])
            else:
                self.AiRight.mixingCounter -= 1
                


            if self.AiLeft.mixingCounter <= 0:
                if self.AiRight.mixPhase == 0:
                    self.AiLeft.mixPhase, self.AiLeft.mixingCounter   = MixingCycle(self.interfaceVIP, IFC_VIP_MOTOR_CHAMBER_LEFT, 
                                                                                                    self.AiLeft.mixPhase, self.AiLeft.mixIntervalTime, 
                                                                                                    self.AiLeft.mixDuration[0], self.AiLeft.mixDuration[1])
            else:
                self.AiLeft.mixingCounter -= 1

            return 1
        else:
            self.incrementCounter = self.increment

        self.QueryAllData()

        if self.filterAi.depletionFlag: 
            if self.filterAi.depletionTime <= 0:
                self.filterAi.depletionFlag = False
            else:
                self.filterAi.depletionTime -= TASK_PROC_INCREMENT
                self.intakePtc.fanPwm = 0
                return 0



        if self.blowerPtc.fanPwmCounter <= 0:
            self.ModifyBlowerPWM(self.blowerPtc.increasingFanPwmFlag)
            self.blowerPtc.fanPwmCounter = TASK_SYS_15_MINUTES
            
            if (self.blowerPtc.fanPwm >= 85):
                self.blowerPtc.increasingFanPwmFlag = False
                ActivateBlower(self.interfaceVIP, self.blowerPtc.fanPwm)

                self.filterAi.depletionFlag = True
                self.filterAi.depletionTime = TASK_SYS_2_HOURS

            elif (self.blowerPtc.fanPwm <= 10):
                self.blowerPtc.increasingFanPwmFlag = True
                ActivateBlower(self.interfaceVIP, self.blowerPtc.fanPwm)

                self.filterAi.depletionFlag = True
                self.filterAi.depletionTime = TASK_SYS_2_HOURS

        else:
            self.blowerPtc.fanPwmCounter  -= TASK_PROC_INCREMENT



        if self.intakePtc.fanPwmCounter <= 0:
            ActivateIntakeFan(self.interfaceVIP, self.intakePtc.fanPwm)
            self.intakePtc.fanPwmCounter = TASK_SYS_2_HOURS

            if (self.intakePtc.increasingFanPwmFlag):
                self.intakePtc.fanPwm = 0
                self.intakePtc.increasingFanPwmFlag = False
            else:
                self.intakePtc.fanPwm = 100
                self.intakePtc.increasingFanPwmFlag = True
        else:
            self.intakePtc.fanPwmCounter -= TASK_PROC_INCREMENT



        if TChamberAI.tempRangeCounter <= 0:
            self.ModifyChamberTemperature(TChamberAI.increasingChamberTempFlag)
            TChamberAI.tempRangeCounter = TASK_SYS_90_MINUTES

            if (TChamberAI.tempRange[0]   >= TCompostParameters.MAX_TEMP):
                TChamberAI.increasingChamberTempFlag = False

            elif (TChamberAI.tempRange[0] <= TCompostParameters.MIN_TEMP):
                TChamberAI.increasingChamberTempFlag = True

        else:
            TChamberAI.tempRangeCounter -= TASK_PROC_INCREMENT


        if self.blowerPtc.tempRangeCounter <= 0:
            self.ModifyPTCPWM(self.blowerPtc.increasingTempRangeFlag)
            self.blowerPtc.tempRangeCounter = TASK_SYS_25_MINUTES  

            if (self.blowerPtc.tempRange[0]   >= TSafetyParameters.MAX_NTC_TEMP):
                self.blowerPtc.increasingTempRangeFlag = False

            elif (self.blowerPtc.tempRange[0] <= TSafetyParameters.MIN_NTC_TEMP):
                self.blowerPtc.increasingTempRangeFlag = True

        else:
            self.blowerPtc.tempRangeCounter -= TASK_PROC_INCREMENT



        if TChamberAI.padTempRangeCounter <= 0:

            self.ModifyPadTemperature(self.AiLeft.increasingPadTempFlag, self.AiRight.increasingPadTempFlag)
            
            TChamberAI.padTempRangeCounter = TASK_SYS_20_MINUTES + TASK_SYS_5_MINUTES

            if (self.AiRight.padTempRange[0]   >= TSafetyParameters.MAX_NTC_TEMP):
                self.AiRight.increasingPadTempFlag = False

            elif (self.AiRight.padTempRange[0] <= TSafetyParameters.MIN_NTC_TEMP):
                self.AiRight.increasingPadTempFlag = True


            if (self.AiLeft.padTempRange[0]   >= TSafetyParameters.MAX_NTC_TEMP):
                self.AiLeft.increasingPadTempFlag = False

            elif (self.AiLeft.padTempRange[0] <= TSafetyParameters.MIN_NTC_TEMP):
                self.AiLeft.increasingPadTempFlag = True

        else:
            TChamberAI.padTempRangeCounter -= TASK_PROC_INCREMENT

        return 0

    def ModifyChamberTemperature(self, increase=False):
        if increase:
            TChamberAI.tempRange             = [TChamberAI.tempRange[0]      + 500,  TChamberAI.tempRange[1]        + 500]
        else:
            TChamberAI.tempRange             = [TChamberAI.tempRange[0]      - 500,  TChamberAI.tempRange[1]        - 500]


    def ModifyPadTemperature(self, increase_left=False, increase_right=False):
        if increase_right:
            self.AiRight.padTempRange    = [self.AiRight.padTempRange[0] + 5,  self.AiRight.padTempRange[1] + 5]
        else:
            self.AiRight.padTempRange    = [self.AiRight.padTempRange[0] - 5,  self.AiRight.padTempRange[1] - 5]

        if increase_left:
            self.AiLeft.padTempRange    = [self.AiLeft.padTempRange[0] + 5,  self.AiLeft.padTempRange[1] + 5]
        else:
            self.AiLeft.padTempRange    = [self.AiLeft.padTempRange[0] - 5,  self.AiLeft.padTempRange[1] - 5]

    def ModifyBlowerPWM(self, increase=False):
        if increase:
            self.blowerPtc.fanPwm    += 10
        else:
            self.blowerPtc.fanPwm    -= 10 
            
    def ModifyPTCPWM(self, increase= False):
        if increase:
            self.blowerPtc.tempRange    = [self.blowerPtc.tempRange[0] + 2,  self.blowerPtc.tempRange[1]    + 2]
        else:
            self.blowerPtc.tempRange    = [self.blowerPtc.tempRange[0] - 2,  self.blowerPtc.tempRange[1]    - 2]

    def ModulateHeatersUsingNTC(self, localMinPtcTemp: int, localMaxPtcTemp: int, leftLocalMinPadTemp: int, leftLocalMaxPadTemp: int, rightLocalMinPadTemp: int, rightLocalMaxPadTemp: int):
        
        # Intake PTC

        blowerPtc_T, intakePtc_T = GetPTCTemperatureP50(self.interfaceVIP)

        if not self.filterAi.depletionFlag: 
            # print(intakePtc_T, self.intakePtc.dutyCycleOnFlag)
            if (intakePtc_T >= TSafetyParameters.MAX_INTAKE_TEMP):

                ActivateIntakePTC(self.interfaceVIP, 0)
                ActivateIntakeFan(self.interfaceVIP, 100)
                
            elif (intakePtc_T <= TSafetyParameters.MIN_INTAKE_TEMP):
                
                # if not depletion, then activate PTC............

                ActivateIntakePTC(self.interfaceVIP, TSafetyParameters.INTAKE_PTC_PWM)
                ActivateIntakeFan(self.interfaceVIP, self.intakePtc.fanPwm)

        else:
            ActivateIntakePTC(self.interfaceVIP, 0)
            ActivateIntakeFan(self.interfaceVIP, 0)

    

        # Blower PTC Temperature
        if (blowerPtc_T >= TSafetyParameters.MAX_NTC_TEMP or blowerPtc_T >= localMaxPtcTemp):
            
            ActivateBlowerPTC(self.interfaceVIP, 0)

            if (self.blowerPtc.fanPwm <= TCompostParameters.MIN_BLOWER_PWM):
                self.blowerPtc.fanPwm = TCompostParameters.MIN_BLOWER_PWM
            ActivateBlower(self.interfaceVIP, self.blowerPtc.fanPwm)

        elif (blowerPtc_T <= localMinPtcTemp):

            ActivateBlowerPTC(self.interfaceVIP, TSafetyParameters.BLOWER_PTC_PWM)
            ActivateBlower(self.interfaceVIP, 6)


        

        # Pad Heater Temperature
        leftPad_T, rightPad_T = GetPadTemperature(self.interfaceVIP)
        if (rightPad_T >= rightLocalMaxPadTemp):
            
            self.interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_RIGHT, 0)
            LogActuators.LOG_Pad_Heater_R = 0
            
        elif (rightPad_T <= rightLocalMinPadTemp):

            self.interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_RIGHT, TSafetyParameters.PAD_PWM)
            LogActuators.LOG_Pad_Heater_R = TSafetyParameters.PAD_PWM
        
        if (leftPad_T >= leftLocalMaxPadTemp):
            
            self.interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_LEFT,  0)
            LogActuators.LOG_Pad_Heater_L = 0
            
        elif (leftPad_T <= leftLocalMinPadTemp):

            self.interfaceVIP.cmd_control_heater(IFC_VIP_HEATER_PAD_LEFT,  TSafetyParameters.PAD_PWM)
            LogActuators.LOG_Pad_Heater_L = TSafetyParameters.PAD_PWM
        
    def GetAirStateAndParams(self):
        return  self.filterAi.bmeData.currBme, self.blowerPtc.fanPwm, self.blowerPtc.tempRange, self.blowerPtc.currPtcTemp, \
                        self.blowerPtc.intervalTime, self.blowerPtc.counterWorkTime,  self.blowerPtc.dutyCycle, self.blowerPtc.dutyCycleOnFlag, \
                                TChamberAI.tempRange[0], TChamberAI.tempRange[1], self.filterAi.plasmaLampCounter, self.filterAi.plasmaOnFlag, self.filterAi.isOdorFlag

    def GetIntakeFanParams(self):
        return self.intakeAi.bmeData.currBme, self.intakePtc.currPtcTemp, self.intakePtc.intervalTime, self.intakePtc.counterWorkTime, self.intakePtc.dutyCycleOnFlag, self.intakePtc.fanPwm
    
    def DataCollectionCounters(self):
        return   TChamberAI.tempRange, TChamberAI.tempRangeCounter, TChamberAI.increasingChamberTempFlag,  TChamberAI.padTempRangeCounter, self.AiLeft.increasingPadTempFlag, self.AiRight.increasingPadTempFlag, \
            self.blowerPtc.increasingFanPwmFlag,  self.blowerPtc.fanPwmCounter, self.blowerPtc.increasingTempRangeFlag, self.blowerPtc.tempRangeCounter, self.intakePtc.fanPwmCounter, \
            self.filterAi.depletionFlag, self.filterAi.depletionTime

    def GetChamberData(self, lr: int):

        if lr == RIGHT:
            return  [self.AiRight.padTempRange, self.AiRight.currPadTemp],  \
                    self.AiRight.currMass,  self.AiRight.padDutyCycle,   self.AiRight.padHeaterIntervalTime, self.AiRight.padHeaterWorkTime, self.AiRight.padDutyCycleOnFlag, \
                    self.AiRight.mixIntervalTime, self.AiRight.mixingCounter,     self.AiRight.mixPhase, self.AiRight.mixDuration, \
                    self.AiRight.bmeData.currBme,   self.AiRight.compostingState, self.AiRight.motorCurrent

        elif lr == LEFT:
            return  [self.AiLeft.padTempRange, self.AiLeft.currPadTemp],  \
                    self.AiLeft.currMass,  self.AiLeft.padDutyCycle,   self.AiLeft.padHeaterIntervalTime, self.AiLeft.padHeaterWorkTime, self.AiLeft.padDutyCycleOnFlag, \
                    self.AiLeft.mixIntervalTime, self.AiLeft.mixingCounter,     self.AiLeft.mixPhase, self.AiLeft.mixDuration, \
                    self.AiLeft.bmeData.currBme,   self.AiLeft.compostingState, self.AiLeft.motorCurrent

    def SummaryTests(self):
        
        return 

    def PrintChamberOutput(SIDE: str, 
                        compostingState: int, 
                        bmeValues: TBme688Sensor, mass: list,
                        padHeater: list,
                        # padTempRangeCounter: int, padIncreasingFlag: bool, 
                        padIncreasingFlag: bool, 
                        mixIntervalTime: int, mixingCounter: int, mixPhase: int, mixDuration: int):
        
        print()
        print(f"{SIDE}\t"  +  f"Composting State: {compostingState} " )
        IntegrationTest.PrintBMESensor(bmeValues.temperature, bmeValues.humidity, bmeValues.pressure, bmeValues.gasResistance)
        print( f"   Pad_T_Range: {padHeater[0]}\tPad_Temp: {padHeater[1]}°C;\t\tPad_Increasing_Flag: {padIncreasingFlag}" )
        # print(f"   Pad_T_Range: {padHeater[0]}\tPad_Temp: {padHeater[1]}°C\t\tPad_Increasing_Flag: {padIncreasingFlag}"           )
        # print(f"  Pad_T_Range_Counter: {padTempRangeCounter}"         )
        print(f"  Mix_Interval: {mixIntervalTime} s     \tMix_Counter: {mixingCounter} s\tMix_Phase: {mixPhase}")
        print(f"  Mix_Duration: {mixDuration}\tMass: {mass[0]},{mass[1]}g" )
        # print(f"         NTC 1: {ntc_1}\t\tNTC 2: {ntc_2}\t\tNTC 3: {ntc_3}\t\tNTC 4 {ntc_4}")

    def PrintBMESensor(temperature, humidity, pressure, gasResistance):
        print(f"             T: {temperature}°C\t\tHum: {humidity}%\t\tPress: {pressure}\t\tGas: {gasResistance}" )
  

if __name__ == '__main__':

    # title_font =  bcolors.CBOLD  + bcolors.CUNDRLN + bcolors.CGREEN

    P50_COMPORT        = str(sys.argv[1])
    # P50_COMPORT        = "COM7"

    p50IntefaceVIP = InterfaceVIP50()
    result = p50IntefaceVIP.open(P50_COMPORT, 115200)
    if result != 0:
        SystemExit(1)
        # sys.exit("Com Port Does not Open") 

    folder_name = "Data"
    if not path.isdir(f'{folder_name}'):
        mkdir(f'{folder_name}')


    ## TODO get serial number here and make it the file name

    file_path_name = f"{folder_name}\\{P50_COMPORT}_Integration_Test.csv"

    p50Collection = IntegrationTest(p50IntefaceVIP)



    print("Collecting Data...")
    while True:
        dt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)

        # print(p50Collection.incrementCounter)

        if (p50Collection.Run() == 1):
            continue

        rightPadHeater,           rightMass,        \
        rightDutyCycleMode,     rightPadHeaterIntervalTime, rightPadHeaterWorkTime, rightPadDutyCycleOnFlag, \
        rightMixIntervalTime,   rightMixingCounter,         rightMixPhase, rightMixDuration, \
                                                            rightBmeValues, rightCompostingState, rightMotorCurrent = p50Collection.GetChamberData(RIGHT)
        
        leftPadHeater,             leftMass,       \
        leftDutyCycleMode,      leftPadHeaterIntervalTime,  leftPadHeaterWorkTime, leftPadDutyCycleOnFlag, \
        leftMixIntervalTime,    leftMixingCounter,          leftMixPhase, leftMixDuration, \
                                                            leftBmeValues, leftCompostingState, leftMotorCurrent    = p50Collection.GetChamberData(LEFT)

        exhaustBmeValues, blowerPwm, ptcTempRange, blowerPtcTemp, \
                ptcIntervalTime, ptcCounterWorkTime, ptcDutyCycle, ptcDutyCycleOnFlag, lowTemp, highTemp, \
                    plasmaCounter, plasmaFlag, odorFlag = p50Collection.GetAirStateAndParams()
        
        intakeBmeValues, intakePtcTemp, intakePtcIntervalTime, intakePtcFanPwmCounter, intakePtcDutyCycleOnFlag, intakeFanPwm = p50Collection.GetIntakeFanParams()

        chamberTempRange, chamberTempRangeCounter, increasingChamberTempFlag,  padTempRangeCounter, leftIncreasingPadTempFlag, rightIncreasingPadTempFlag, \
            blowerIncreasingFanPwmFlag,  blowerFanPwmCounter, blowerIncreasingPtcTempRangeFlag, blowerTempRangeCounter, intakeFanPwmCounter, depletionFlag, depletionCounter  = p50Collection.DataCollectionCounters()
        

        print(dt)

        IntegrationTest.PrintChamberOutput( "RIGHT", 
                                        rightCompostingState, 
                                        rightBmeValues, rightMass,
                                        rightPadHeater, 
                                        rightIncreasingPadTempFlag,
                                        rightMixIntervalTime, rightMixingCounter, rightMixPhase, rightMixDuration)
                
        IntegrationTest.PrintChamberOutput( "LEFT", 
                                        leftCompostingState, 
                                        leftBmeValues, leftMass,
                                        leftPadHeater, 
                                        leftIncreasingPadTempFlag,
                                        leftMixIntervalTime, leftMixingCounter, leftMixPhase, leftMixDuration)


        print()
        print(f"  Pad_T_Range_Counter: {padTempRangeCounter};")
        
        print()
        print("INTAKE")     
        IntegrationTest.PrintBMESensor(intakeBmeValues.temperature, intakeBmeValues.humidity, intakeBmeValues.pressure, intakeBmeValues.gasResistance)    
        print(f"PTC_Temp_Range: [33, 35]\t" +              f"PTC_Temp: {intakePtcTemp}°C\t\tPTC_Flag: {ptcDutyCycleOnFlag}")
        print(f"  PTC_Interval: {intakePtcIntervalTime} s\t\tIntake_Fan_Counter: {intakeFanPwmCounter} s\n")

        print()
        print("MAIN BLOWER & EXHAUST & FILTER")  
        IntegrationTest.PrintBMESensor(exhaustBmeValues.temperature, exhaustBmeValues.humidity, exhaustBmeValues.pressure, exhaustBmeValues.gasResistance)    
        print(f"    PTC_Temp_Range: {ptcTempRange}\tPTC_Temp: {blowerPtcTemp}°C\t\tCounter: {blowerTempRangeCounter} s;\tIncreasing_T_Flag: {blowerIncreasingPtcTempRangeFlag}"   )
        print(f"Blower_Pwm_Counter: {blowerFanPwmCounter} s    \tBlower_PWM: {blowerPwm};\t\tIncreasing_Fan_Flag: {blowerIncreasingFanPwmFlag};")
        print(f"    Plasma Counter: {plasmaCounter} s\tPlasma Flag: {plasmaFlag};\t\tOdor Flag: {odorFlag}"         )


        print()
        print(f"        Chamber_T_Range: {chamberTempRange};")
        print(f"Chamber_T_Range_Counter: {chamberTempRangeCounter};\tChamber_Increasing_T_Flag: {increasingChamberTempFlag}"  )
        print(f"   O2_Depletion_Counter: {depletionCounter};\tO2_Depletion_Flag: {depletionFlag}"  )

        print("---------------------------------------------------------------")

        data = {
            DATETIME:   dt,
            RIGHT_PAD_T: rightPadHeater[1], LEFT_PAD_T:  leftPadHeater[1], 
            BLOWER_PTC_T: blowerPtcTemp, INTAKE_PTC_T: intakePtcTemp,
            
            
            LEFT_BME_TEMP: leftBmeValues.temperature, LEFT_BME_HUMID: leftBmeValues.humidity, LEFT_BME_PRESS:leftBmeValues.pressure, LEFT_BME_GAS: leftBmeValues.gasResistance,
            RIGHT_BME_TEMP: rightBmeValues.temperature, RIGHT_BME_HUMID: rightBmeValues.humidity, RIGHT_BME_PRESS: rightBmeValues.pressure, RIGHT_BME_GAS: rightBmeValues.gasResistance,
            EXHAUST_BME_TEMP: exhaustBmeValues.temperature, EXHAUST_BME_HUMID: exhaustBmeValues.humidity, EXHAUST_BME_PRESS: exhaustBmeValues.pressure, EXHAUST_BME_GAS: exhaustBmeValues.gasResistance,
            INTAKE_BME_TEMP: intakeBmeValues.temperature, INTAKE_BME_HUMID: intakeBmeValues.humidity, INTAKE_BME_PRESS: intakeBmeValues.pressure, INTAKE_BME_GAS: intakeBmeValues.gasResistance,
                         
            RIGHT_MASS:    rightMass, 
            LEFT_MASS:     leftMass,  
                        
                    
            RIGHT_MIX_PHASE: rightMixPhase, LEFT_MIX_PHASE: leftMixPhase, 
            RIGHT_MIX_DUR: rightMixDuration, LEFT_MIX_DUR: leftMixDuration, 

            RIGHT_MOT_CURRENT: rightMotorCurrent, LEFT_MOT_CURRENT: leftMotorCurrent,

            RIGHT_PAD_RNG: rightPadHeater[0][0], 
            LEFT_PAD_RNG:  leftPadHeater[0][0], 
            
            BME_TEMP_RANGE: chamberTempRange[0],
            INTAKE_FAN_PWM: intakeFanPwm,

            DEPLETION_FLAG: depletionFlag,
            DEPLETION_TIME: depletionCounter,

            BLOWER_PWM: blowerPwm, PTC_HTR_RNG: ptcTempRange[0], 
            PLASMA_FLAG: plasmaFlag,

            "chamberTempRangeCounter": chamberTempRangeCounter, "increasingChamberTempFlag": increasingChamberTempFlag,
            "blowerFanPwmCounter": blowerFanPwmCounter, "blowerIncreasingFanPwmFlag": blowerIncreasingFanPwmFlag,
            "intakeFanPwmCounter": intakeFanPwmCounter, 
        }


        df =  pd.DataFrame.from_dict(data, orient='index').transpose()

        if not os.path.isfile(file_path_name):
           df.to_csv(file_path_name, index=False, mode='x')
        else:
            df.to_csv(file_path_name, index=False, mode='a', header=False)


        df = pd.read_csv(file_path_name)
        
        df[DATETIME] = pd.to_datetime(df[DATETIME])


