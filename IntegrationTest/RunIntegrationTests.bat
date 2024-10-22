@echo off
setlocal enabledelayedexpansion

echo Listing available COM Ports:
echo ----------------------------

set "comports="

for /f "tokens=1,2*" %%A in ('reg query HKLM\HARDWARE\DEVICEMAP\SERIALCOMM') do (
    set "value=%%C"
    if not "!value!"=="" (
        @REM echo !value!


        echo Executing Python script with ports !value! as argument:
        
        start "Integration Test" cmd /c python IntegrationTest.py !value!
        @REM start pythonw integrationTest.py !value!

        @REM set "comports=!comports! !value!"
    )
)

echo ----------------------------------------------------
