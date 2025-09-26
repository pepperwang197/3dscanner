import serial
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import json

# Calibration curve formula
def analogInputToDistance(input):
  return 1.9252e+04 * (input ** -1.0776)

arduinoComPort = "COM5"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

data = [] # Array to store one data point at a time
all_data = [[],[],[]] # Array to store all data points

# Loop until Arduino code finishes (and prints "hello world" to serial)
while True:
  
  lineOfData = serialPort.readline().decode().strip()

  if len(lineOfData) > 0:
    
    if (lineOfData=="hello world"):
      print("break")
      break
  
    if(lineOfData=="next" and len(data)==3):
      
      theta = math.radians((data[0]) - 45)
      phi = math.radians((data[1]) + 60)
      rho = analogInputToDistance((data[2]))
      
      # Convert from spherical to rectangular coordinates
      x = rho * math.cos(theta) * math.sin(phi)
      y = rho * math.sin(theta) * math.sin(phi)
      z = rho * math.cos(phi)
      
      # Add to data array
      all_data[0].append(x)
      all_data[1].append(y)
      all_data[2].append(z)
      
      # Clear temporary data array
      data = []
      
    elif (lineOfData!="next"):
      data.append((int)(lineOfData))

# Save data to JSON file
with open("file.json", "w") as f:
  json.dump(all_data, f)  

# Scatter plot
fig = plt.figure()
ax = fig.add_subplot()
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.scatter(all_data[0], all_data[1], s=15, marker="s", c=all_data[2], cmap="RdPu", norm="linear")
plt.show()