from subprocess import Popen, PIPE

proc = Popen('./runService.sh', shell=True, stdout=PIPE)
proc.wait()
proc.communicate()