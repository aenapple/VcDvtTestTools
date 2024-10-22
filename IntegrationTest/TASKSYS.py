import json

LEFT = 0
RIGHT = 1

SHORT = 0
MEDIUM = 1
LONG = 2

ML_LINEAR = 0
ML_POLYNOMIAL = 1

TASK_SYS_10_SECONDS = 10
TASK_SYS_20_SECONDS = 20
TASK_SYS_30_SECONDS = 30
TASK_SYS_40_SECONDS = 40
TASK_SYS_50_SECONDS = 50

TASK_SYS_1_MINUTE   =  1*60
TASK_SYS_2_MINUTES  =  2*TASK_SYS_1_MINUTE
TASK_SYS_3_MINUTES  =  3*TASK_SYS_1_MINUTE
TASK_SYS_4_MINUTES  =  4*TASK_SYS_1_MINUTE
TASK_SYS_5_MINUTES  =  5*TASK_SYS_1_MINUTE
TASK_SYS_6_MINUTES  =  6*TASK_SYS_1_MINUTE
TASK_SYS_7_MINUTES  =  7*TASK_SYS_1_MINUTE
TASK_SYS_8_MINUTES  =  8*TASK_SYS_1_MINUTE
TASK_SYS_10_MINUTES = 10*TASK_SYS_1_MINUTE
TASK_SYS_13_MINUTES = 13*TASK_SYS_1_MINUTE
TASK_SYS_15_MINUTES = 15*TASK_SYS_1_MINUTE
TASK_SYS_20_MINUTES = 20*TASK_SYS_1_MINUTE
TASK_SYS_25_MINUTES = 25*TASK_SYS_1_MINUTE
TASK_SYS_30_MINUTES = 30*TASK_SYS_1_MINUTE
TASK_SYS_40_MINUTES = 40*TASK_SYS_1_MINUTE
TASK_SYS_60_MINUTES = 60*TASK_SYS_1_MINUTE
TASK_SYS_90_MINUTES = 90*TASK_SYS_1_MINUTE

TASK_SYS_1_HOUR     = 60*TASK_SYS_1_MINUTE
TASK_SYS_2_HOURS    =  2*TASK_SYS_1_HOUR
TASK_SYS_3_HOURS    =  3*TASK_SYS_1_HOUR
TASK_SYS_4_HOURS    =  4*TASK_SYS_1_HOUR
TASK_SYS_5_HOURS    =  5*TASK_SYS_1_HOUR
TASK_SYS_6_HOURS    =  6*TASK_SYS_1_HOUR
TASK_SYS_10_HOURS   = 10*TASK_SYS_1_HOUR
TASK_SYS_20_HOURS   = 20*TASK_SYS_1_HOUR
TASK_SYS_24_HOURS   = 24*TASK_SYS_1_HOUR

with open('config.json', 'r') as f:
        config = json.load(f)

TASK_PROC_INCREMENT          = config['INCREMENT']


CompostingState_StartingUp  = "StartingUp"
CompostingState_Collection  = "Collection"
CompostingState_Thermo      = "Thermo"
CompostingState_Meso        = "Meso"
CompostingState_HeatPurge   = "HeatPurge"

CompostingState_Stasis      = "Stasis" 

ptcDutyCycleMode_0  = 0
ptcDutyCycleMode_1  = 1  # High A, High B
ptcDutyCycleMode_2  = 2  # High A, Med B   
ptcDutyCycleMode_3  = 3  # High A, Low B
ptcDutyCycleMode_4  = 4  # Med  A, Med B
ptcDutyCycleMode_5  = 5  # Med  A, Low B
ptcDutyCycleMode_6  = 6  # Low  A, Low B
ptcDutyCycleMode_7  = 7  # Either A or B are too low

ptcDutyCycleMode_99 = 99


padDutyCycleMode_0 = 0  # Starting up
padDutyCycleMode_1 = 1  # Raise/High Temp
padDutyCycleMode_2 = 2  # Moderate/High Temp
padDutyCycleMode_3 = 3  # Moderate Temp
padDutyCycleMode_4 = 4  # Moderate Temp

mixPhase_0         = 0
mixPhase_1         = 1
mixPhase_2         = 2
mixPhase_3         = 3
mixPhase_4         = 4


TaskRegionLeftChamber   = 0
TaskRegionRightChamber  = 1
TaskRegionFilter        = 2
TaskRegionExhaust       = 3


class bcolors:
        CEND      = '\33[0m'
        CBOLD     = '\33[1m'
        CITALIC   = '\33[3m'
        CUNDRLN   = '\33[4m'
        CBLINK    = '\33[5m'
        CBLINK2   = '\33[6m'
        CSELECTED = '\33[7m'

        CBLACK  = '\33[30m'
        CRED    = '\33[31m'
        CGREEN  = '\33[32m'
        CYELLOW = '\33[33m'
        CBLUE   = '\33[34m'
        CVIOLET = '\33[35m'
        CBEIGE  = '\33[36m'
        CWHITE  = '\33[37m'

        CBLACKBG  = '\33[40m'
        CREDBG    = '\33[41m'
        CGREENBG  = '\33[42m'
        CYELLOWBG = '\33[43m'
        CBLUEBG   = '\33[44m'
        CVIOLETBG = '\33[45m'
        CBEIGEBG  = '\33[46m'
        CWHITEBG  = '\33[47m'

        CGREY    = '\33[90m'
        CRED2    = '\33[91m'
        CGREEN2  = '\33[92m'
        CYELLOW2 = '\33[93m'
        CBLUE2   = '\33[94m'
        CVIOLET2 = '\33[95m'
        CBEIGE2  = '\33[96m'
        CWHITE2  = '\33[97m'

        CGREYBG    = '\33[100m'
        CREDBG2    = '\33[101m'
        CGREENBG2  = '\33[102m'
        CYELLOWBG2 = '\33[103m'
        CBLUEBG2   = '\33[104m'
        CVIOLETBG2 = '\33[105m'
        CBEIGEBG2  = '\33[106m'
        CWHITEBG2  = '\33[107m'