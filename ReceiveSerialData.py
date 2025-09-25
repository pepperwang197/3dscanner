import serial
import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import json

def analogInputToDistance(input):
  return 1.9252e+04 * (input ** -1.0776)

arduinoComPort = "COM5"
baudRate = 9600
serialPort = serial.Serial(arduinoComPort, baudRate, timeout=1)

data = []
all_data = [[],[],[]]

while True:
  
  lineOfData = serialPort.readline().decode().strip()

  if len(lineOfData) > 0:
    
    if (lineOfData=="hello world"):
      print("break")
      break
    
    # print(lineOfData)
  
    if(lineOfData=="next" and len(data)==3):
    
      all_data[0].append(data[0])
      all_data[1].append(data[1])
      all_data[2].append(data[2])
      
      theta = math.radians((data[0]) - 45)
      phi = math.radians((data[1]) + 60)
      rho = analogInputToDistance((data[2]))
      
      # print((data[0]) - 45, (data[1]) + 60, rho)
      
      x = rho * math.cos(theta) * math.sin(phi)
      y = rho * math.sin(theta) * math.sin(phi)
      z = rho * math.cos(phi)
      
      data = []
      
    elif (lineOfData!="next"):
      data.append((int)(lineOfData))


try:
  with open("file.json", "w") as f:
    json.dump(all_data, f)
except Exception as e:
  print(e)
  

fig = plt.figure()
# ax = fig.add_subplot(projection='3d')
ax = fig.add_subplot()
ax.set_xlabel("x")
ax.set_ylabel("y")
# ax.set_zlabel("z")

ax.scatter(all_data[0], all_data[1], c=all_data[2], cmap="RdPu", norm="linear")

plt.show()