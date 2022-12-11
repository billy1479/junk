@echo off
@REM this is for mounting company files as a network drive
net use v: \\billysrv\company

@REM this is for adding my home printer which is called printer1 when added to the home server - this wont work unless the printer is connected and will return an error
rundll32 printui.dll PrintUIEntry /in /n \\billysrv\printer1
