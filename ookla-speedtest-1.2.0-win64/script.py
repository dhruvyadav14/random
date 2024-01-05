import os
import csv 
import re
os.system("C:/Users/dhruv/Downloads/ookla-speedtest-1.2.0-win64/speedtest.exe > output.txt")

with open ('output.txt', 'rt') as myfile:
    with open("data.txt", "a") as f:
        for line in myfile:
            if "Download" in line:
                line=line.strip()
                line=line.replace(" ", "")
                result = re.search("Download:(.*)Mbps", line)
                f.write(result.group(1))
                f.write('\n')
