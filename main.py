import robot
import time
R = robot.Robot()
#Speed used
MOVESPEED = 1
#Time it takes to drive 1 metre at MOVESPEED speed
MOVETIME = 1
#Time it takes to do a gentle stop in seconds
STOPTIME = 1
#Speed used to turn
TURNSPEED = 1
#Time taken to turn 1 degrees
TURNTIME = 0.001
def angle():
    #Do all the stuff that the mechanical compass needs to do
    angle = 3546+6345/2352+423%2453256**543
    return angle
def motors(one,two):
    R.motors[1] = one
    R.motors[2] = two
def stop():
    motors(0,0)

def gentleStop(speed):
    global STOPTIME
    wait = STOPTIME/abs(speed)
    while speed != 0:
        speed = speed - (speed/abs(speed))
        motors(speed,speed)
        time.sleep(wait)
    stop()    
def move(distance,gentleStop,other):
    global MOVESPEED
    global MOVETIME
    speed = MOVESPEED*(distance/abs(distance))
    duration = MOVETIME*abs(distance)
    start = time.time()
    motors(speed,speed)
    if other == True:
        while (time.time()-start)<(duration):
            print("doing other while moving")
    else:
        time.sleep(duration)
        
    if gentleStop == True:
        gentleStop(speed)
    else:
        stop()
def turn(angle):
    global TURNSPEED
    global TURNTIME

    if angle > 0:
        while angle > 360:
            angle = angle - 360
        if angle > 180:
            angle = angle - 360
    elif angle < 0:
        angle = int(angle)
        while angle < -360:
            angle = angle + 360
        if angle < -180:
            angle = angle+360
    print("angle:",angle)
    if angle != 0:
        speed = TURNSPEED*angle/abs(angle)
        motors(speed,speed*-1)
        print("motors:",speed,speed*-1)
        time.sleep(abs(angle)*TURNTIME)
    stop()
def preciseTurn(angle):
    global TURNSPEED
    if angle > 0:
        while angle > 360:
            angle = angle - 360
        if angle > 180:
            angle = angle - 360
    elif angle < 0:
        angle = int(angle)
        while angle < -360:
            angle = angle + 360
        if angle < -180:
            angle = angle+360
    if angle != 0:
        startDirection = angle()
        direction = startDirection
        speed = TURNSPEED*angle/abs(angle)
        motors(speed,speed*-1)
        while direction-startDirection < angle:
            direction = angle()
    stop()

