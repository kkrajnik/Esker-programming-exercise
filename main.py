def analyze_line(line):
  

with open("samplefile.txt", "r") as file:
  end = false
  while !end:
    line = file.readline()
    if line == "":
      end = true
    else:
      analyze_line(line)
