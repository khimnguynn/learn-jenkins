import subprocess
subprocess.Popen(["python3", "app.py"], shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, close_fds=True)
