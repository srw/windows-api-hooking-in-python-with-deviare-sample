# Auxiliar Functions =====================================================================

from subprocess import *

def GetPIDByProcessName(aProcessName):
	for proc in psutil.process_iter():
		if proc.name == aProcessName:
			return proc.pid
			
def OpenNotepadAndGetPID():
	print 'Starting Notepad...'
	pid = Popen("notepad").pid
	print 'Notepad started successfully'
	return pid
	
def HookFunctionForProcess(spyManager, functionModuleAndName, notepadPID):
	print 'Hooking function ' + functionModuleAndName + ' for Notepad...'
	hook = spyManager.CreateHook(functionModuleAndName, 0)
	hook.Attach(notepadPID, True)
	hook.Hook(True)
	print 'Notepad successfully hooked'
	return hook
	
def StartNotepadAndHook(spyManager):

	notepadPID = OpenNotepadAndGetPID()
	hook = HookFunctionForProcess(spyManager, "kernel32.dll!CreateFileW", notepadPID)