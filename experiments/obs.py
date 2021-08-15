def turn_left():
    x=0.0
    y=0.0
    theta  = (math.pi/2)
    motion.moveTo(x, y, theta)

def turn_right():
    x=0.0
    y=0.0
    theta  = -(math.pi/2)
    motion.moveTo(x, y, theta)

def move_forward():
    x=0.1
    y=0.0
    theta  = 0
    motion.moveTo(x, y, theta)

def get_sensor_data():
    left_sonar = memory.getData("Device/SubDeviceList/US/Left/Sensor/Value")
    right_sonar = memory.getData("Device/SubDeviceList/US/Right/Sensor/Value")
    return left_sonar, right_sonar

while(True):
    sonar.subscribe("myApplication")

    left_sonar, right_sonar = get_sensor_data()
    
    if(left_sonar < thres or right_sonar < thres):
        turn_left()
        left_sonar, right_sonar = get_sensor_data()

        if(left_sonar < thres or right_sonar < thres):
            turn_right()
            left_sonar, right_sonar = get_sensor_data()
            
            if(left_sonar < thres and right_sonar < thres):
                    x=0.0
                    y=0.0
                    theta  = (math.pi/2)
                    print('Move Left')
                    tts.say('Oops! I detected something in front of me.')
                    print(LeftSonar)
                    print(RightSonar)
                    motion.moveTo(x, y, theta)
            else:
                    x=0.1
                    y=0.0
                    theta=0
                    motion.moveTo(x, y, theta)
                    print('Move Straight3')
                    
                    continue
        else:
                x=0.1
                y=0.0
                theta=0
                motion.moveTo(x, y, theta)
                print('Move Straight2')
                print(LeftSonar)
                print(RightSonar)
                continue
    else:
        x=0.05
        y=0.0
        theta=0
        motion.moveTo(x, y, theta)
        print('Move Straight1')
        print(LeftSonar)
        print(RightSonar)
        continue
        
    cnt+=1
    sonar.unsubscribe("myApplication")
        