import subprocess


res = subprocess.call(["ls","-l"])
print(res)

subprocess.call("ls -l",shell=True)
