import re
with open ('output.txt', 'rt') as myfile:
    with open("data.txt", "w") as f:
        for line in myfile:
            if "Download" in line:
                line=line.strip()
                line=line.replace(" ", "")
                result = re.search("Download:(.*)Mbps", line)
                f.write(result.group(1))
            
