import subprocess
cmd = "ipconfig"
output = subprocess.run(cmd, capture_output=True)
print(output.stdout.decode())