' 737061776e6d65.vbs - benign VBS script for detection validation
' Author: https://github.com/0xjyl
' Description: This script is intentionally benign and designed to trigger logging of wscript.exe execution without performing any harmful actions for detection rule validation.
' Purpose: Used to validate that EDR/SIEM systems correctly detect or log VBScript execution events from file download events, i.e. "Browser spawning wscript.exe"

MsgBox "This is a benign VBS test executed by wscript.exe.", vbInformation, "Browser Spawning Test"
