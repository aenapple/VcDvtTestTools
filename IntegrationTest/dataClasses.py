from dataclasses import dataclass, field
from TASKSYS import *
from typing import ClassVar
# from tensorflow import lite


AI_ODOR_DATA_ACTIVATION_1_SIZE      = 6712
AI_ODOR_IN_1_SIZE                   = 270
AI_ODOR_OUT_1_SIZE                  = 6

AI_MOISTURE_DATA_ACTIVATION_1_SIZE  = 192
# AI_MOISTURE_IN_1_SIZE               = 6
AI_MOISTURE_IN_1_SIZE               = 180
AI_MOISTURE_OUT_1_SIZE              = 1


AI_OXYGEN_DATA_ACTIVATION_1_SIZE    = 6712
AI_OXYGEN_IN_1_SIZE                 = 270
AI_OXYGEN_OUT_1_SIZE                = 1


@dataclass
class TSafetyParameters: # All static values
     

    # TODO find better values to make this work
    MAX_MOTOR_TORQUE: int       = 150
    MAX_TORQUE_TIMER: int       = 1
    MAX_TORQUE_X: int           = 7

    NOMINAL_MOTOR_CURR: int     = 65

    MAX_MOTOR_TORQUE_DIFF: int  = 10


    MAX_INTAKE_TEMP: int        = 35
    MIN_INTAKE_TEMP: int        = 33

        
    MIN_NTC_TEMP: int           = 40
    MAX_NTC_TEMP: int           = 75


    BLOWER_PTC_PWM: int         = 50
    INTAKE_PTC_PWM: int         = 10

    PAD_PWM: int                = 100


@dataclass
class TCompostParameters: # All static values
    MAX_BLOWER_PWM: int         = 60
    MIN_BLOWER_PWM: int         = 7

    MOTOR_ONE_RTN:  float       = TASK_SYS_1_MINUTE/2.5  # = 24 seconds
    MIX_FWD_MIN:    int         = int(1.2*MOTOR_ONE_RTN)
    MIX_BCK_MIN:    int         = int(1.7*MOTOR_ONE_RTN)
    MIX_RATIO:      int         = MIX_FWD_MIN / MIX_BCK_MIN
    

    MIX_TRIGGER_MULT:  float    = 1.5
    MIN_MASS:  int              = 500
    
    
    # Temp for testing
    AI_MOISTURE_ML_WINDOW: int  = TASK_PROC_INCREMENT * 30
    AI_FILTER_ML_WINDOW:   int  = TASK_PROC_INCREMENT * 30
    AI_INTAKE_ML_WINDOW:   int  = TASK_PROC_INCREMENT * 30
    
    # AI_MOISTURE_ML_WINDOW: int  = TASK_SYS_15_MINUTES
    # AI_FILTER_ML_WINDOW:   int  = TASK_SYS_15_MINUTES

    AI_SAMPLES_SHORT:      int  = int(AI_MOISTURE_ML_WINDOW / TASK_PROC_INCREMENT)
        
    AI_MOISTURE_CHANNELS:   int = 6
    AI_OXYGEN_CHANNELS:     int = 9
    AI_ODOR_CHANNELS:       int = 9




    LOW_MOISTURE:       int     = 40
    MEDIUM_MOISTURE:    int     = 55
    HIGH_MOISTURE:      int     = 70

    HIGH_HUMIDITY:      int     = 5500

    LOW_TEMP:           int     = 4700
    MED_TEMP:           int     = 4900
    HIGH_TEMP:          int     = 5000

    MIN_TEMP:           int     = 4300
    MAX_TEMP:           int     = 6900


    MAX_GAS_R:          int     = 500000

     
     
@dataclass
class TBme688Sensor:
	temperature: int = field()
	humidity: int = field()
	pressure: int = field()
	gasResistance: int = field()

@dataclass
class TBmeSensorCollection:
    currBme: TBme688Sensor  = field(default_factory=lambda: TBme688Sensor(0, 0, 0, 0))   

    temperature: list[float] = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)
    humidity: list[float] = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)
    pressure: list[float] = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)
    gasResistance: list[float] = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)

 
@dataclass
class TPTCCollection:
	collectedTemp: list[float] = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)
	collectedFanPwm: list[float] = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)


@dataclass
class TPTCControl:
    intervalTime: int
    counterWorkTime: int
    fanPwm: int
    dutyCycle: int #EDutyCycleMode
    dutyCycleOnFlag: bool = field(init=False, default=False)

    tempRange: list[int] = field(default_factory=lambda: [None]*2)

    currPtcTemp: int  = field(init=False, default=0)

    # -------- Collecting Data ONLY -------------------------------------
    fanPwmCounter: int          = field(init=False)
    increasingFanPwmFlag: bool  = field(init=False)

    increasingTempRangeFlag: bool = field(init=False)

    tempRangeCounter: int       = field(init=False)

@dataclass()
class TFilterAI:
    isOdorFlag: bool
    plasmaOnFlag: bool
    plasmaLampCounter: int

    # catalyticOnFlag: bool
    # catalyticLEDCounter: bool

    mlWindowCounter: int

    bmeData: TBmeSensorCollection               = field(default_factory=TBmeSensorCollection)

    # odor_model: ClassVar[lite.Interpreter]      = field(default=lite.Interpreter(model_path="tf_models\\odor.tflite"),init=False)
    ptcCollection: TPTCCollection               = field(init=False)
    

    mlWindow: ClassVar[int]                     = TCompostParameters.AI_FILTER_ML_WINDOW     # static
    activation_buffer: ClassVar[int]            = [None]*AI_ODOR_DATA_ACTIVATION_1_SIZE      # static

    in2: int                                    = field(default_factory=lambda: [None]*AI_ODOR_IN_1_SIZE)
    out2: int                                   = field(default_factory=lambda: [None]*AI_ODOR_OUT_1_SIZE)


    # -------- Collecting Data ONLY -------------------------------------
    depletionTime: int                          = field(init=False)
    depletionFlag: bool                         = field(init=False)

    def __post_init__(self):
        if not isinstance(self.bmeData, TBmeSensorCollection):
            self.bmeData = TBmeSensorCollection()

        self.ptcCollection = TPTCCollection()

@dataclass()
class TIntakeAI:
    mlWindowCounter: int

    bmeData: TBmeSensorCollection               = field(default_factory=TBmeSensorCollection)

    # oxygen_model: ClassVar[lite.Interpreter]    = field(default=lite.Interpreter(model_path="tf_models\\oxygen.tflite"), init=False)
    ptcCollection: TPTCCollection               = field(init=False)

    mlWindow: ClassVar[int]                     = TCompostParameters.AI_INTAKE_ML_WINDOW                    # static
    activation_buffer: ClassVar[int]            = [None]*AI_OXYGEN_DATA_ACTIVATION_1_SIZE      # static

    in2: int                                    = field(default_factory=lambda: [None]*AI_OXYGEN_IN_1_SIZE)
    out2: int                                   = field(default_factory=lambda: [None]*AI_OXYGEN_OUT_1_SIZE)
    # out2: int                                   = field(init=False, default = None)

    def __post_init__(self):
        if not isinstance(self.bmeData, TBmeSensorCollection):
            self.bmeData = TBmeSensorCollection()

        self.ptcCollection = TPTCCollection()

@dataclass()
class TChamberAI:
    

    mlWindowCounter: int              

    taskRegion: int         # ETaskRegion 
    
    padDutyCycle: int                           = field(init=False, default=padDutyCycleMode_0)    
    compostingStateCounter: int                 = field(init=False, default=0)
    compostingState: str                        = field(init=False, default=CompostingState_StartingUp)          

    padDutyCycleOnFlag: bool                    = field(init=False, default=True)

    padHeaterIntervalTime: int                  = field(init=False, default=TASK_SYS_30_MINUTES)
    padHeaterWorkTime: int                      = field(init=False, default=TASK_SYS_30_MINUTES)

    mixingCounter: int   
    mixIntervalTime: int                        = field(init=False, default=TASK_SYS_10_MINUTES)
    mixPhase: int                               = field(init=False, default=mixPhase_0) #EMixingPhase

    bmeData: TBmeSensorCollection               = field(default_factory=TBmeSensorCollection)

    massFront: float                            = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)
    massBack:  float                            = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)

    currMass:  float                            = field(init=False, default_factory=lambda: [None]*2)


    padTemp:      int                           = field(init=False, default_factory=lambda: [None]*TCompostParameters.AI_SAMPLES_SHORT)
    currPadTemp:  int                           = field(init=False, default=0)
    padTempRange: int                           = field(default_factory=lambda: [68,70])  


    mixDuration: int                            = field(default_factory=lambda: [TCompostParameters.MIX_FWD_MIN,TCompostParameters.MIX_BCK_MIN])  
    highTorqueTime: int                         = field(init=False, default=TSafetyParameters.MAX_TORQUE_TIMER)
    
    highTorqueFailures: int                     = field(init=False, default=0)
    isChamberMotorStuck: bool                   = field(init=False, default=False)
    motorCurrent: int                           = field(init=False, default=0)

    moisturePrediction: float                   = field(init=False, default=None)
    activation_buffer: ClassVar[int]            = [None]*AI_MOISTURE_DATA_ACTIVATION_1_SIZE      # static
    mlWindow: ClassVar[int]                     = TCompostParameters.AI_FILTER_ML_WINDOW                       # static

    in2: int                                    = field(default_factory=lambda: [None]*AI_MOISTURE_IN_1_SIZE)
    out2: int                                   = field(default_factory=lambda: [None]*AI_MOISTURE_OUT_1_SIZE)
    # out2: int                                   = field(init=False, default= None)

    
    tempRange: ClassVar[list[int]]              = [None]*2
    # moisture_model:  ClassVar[lite.Interpreter] = field(default = lite.Interpreter(model_path="tf_models\\moisture_cnn_2.tflite"), init=False) #static
    ptcCollection: ClassVar[TPTCCollection]     = field(init=False)






    # -------- Collecting Data ONLY -------------------------------------
    increasingPadTempFlag:      bool            = field(init=False)
    padTempRangeCounter:        int             = field(init=False)
    increasingChamberTempFlag:  bool            = field(init=False)
    tempRangeCounter:           int             = field(init=False)

    staticPadTempRange:     ClassVar[list[int]] = [68,70]

    def __post_init__(self):
        if not isinstance(self.bmeData, TBmeSensorCollection):
            self.bmeData = TBmeSensorCollection()

        self.ptcCollection = TPTCCollection()


# -------- Measuring Power ONLY -------------------------------------
@dataclass
class LogActuators:
    LOG_Intake_PTC_PWM: int         = 0
    LOG_Intake_Fan_PWM: int         = 0

    LOG_Blower_PTC_PWM: int         = 0
    LOG_Blower_Fan_PWM: int         = 0

    LOG_Pad_Heater_R: int           = 0
    LOG_Pad_Heater_L: int           = 0

    LOG_Chamber_Motor_R: int        = 0
    LOG_Chamber_Motor_L: int        = 0

    LOG_Plasma: int                 = 0
    LOG_Catalytic: int              = 0
