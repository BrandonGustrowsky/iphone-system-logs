import subprocess

# Run the `idevicesyslog` command and capture its output
proc = subprocess.Popen(["idevicesyslog"], stdout=subprocess.PIPE)

# Read the output and print it to the console
while True:
    line = proc.stdout.readline()
    if not line:
        break
    line_info = line.decode("utf-8").strip()
    print(line_info)

# If the connection is destroyed or some other catastrophic action takes place
print("Something happened and I stopped recieving data.")