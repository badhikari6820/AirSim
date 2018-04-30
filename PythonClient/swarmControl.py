from AirSimClient import *
import time

baseIP = "127.0.0.1"
basePort = 41451
numMAV = 2
MAVClient = []

def move(mav, x, y, z, v):
    MAVClient[int(mav)].moveToPosition(int(x), int(y), int(z), int(v))

def takeoff(mav):
    MAVClient[int(mav)].takeoff()

def land(mav):
    MAVClient[int(mav)].land()

def goHome(mav):
    MAVClient[int(mav)].goHome()

def hover(mav):
    MAVClient[int(mav)].hover()

def spawn(mav):
    MAVClient[int(mav)].spawnVehicle()

def isNumber(n):
    try:
        float(n)
        return True
    except ValueError:
        return False

func_dict = {'takeoff': takeoff, 'move': move, 'goHome': goHome, 'hover': hover, 'spawn': spawn, 'land': land}

if __name__ == "__main__":

    print("Initializing " + str(numMAV) + " vehicles...")
    for i in range(numMAV):
        MAVClient.append(MultirotorClient(baseIP, basePort + i))
        MAVClient[i].confirmConnection()
        MAVClient[i].enableApiControl(True)
        MAVClient[i].armDisarm(True)
        time.sleep(1)
    
    print("All vehicles have been initialized.")

    while True:
        command = input("> ")
        parsedCmd = command.split(' ')
        if not parsedCmd[0]:
            print("Error: Target vehicle not specified.")
        elif not isNumber(parsedCmd[0]):
            if parsedCmd[0] == 'exit':
                exit()
            else:
                print("Error: First argument needs to be the vehicle index.")
        else:
            if len(parsedCmd) == 1:
                print("Error: No command given.")
            else:
                if parsedCmd[2:]:
                    try:
                        func_dict[parsedCmd[1]](parsedCmd[0], *parsedCmd[2:])
                    except:
                        func_dict[parsedCmd[1]](parsedCmd[0], *parsedCmd[2:])
                        print("Error: Invalid command. Try again.")
                else:
                    try:
                        func_dict[parsedCmd[1]](parsedCmd[0])
                    except:
                        print(func_dict[parsedCmd[1]], func_dict[parsedCmd[1]](parsedCmd[0]))
                        print("Error: Invalid command. Try again.")