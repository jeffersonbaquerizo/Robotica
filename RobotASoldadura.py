
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
from time import sleep

RDK = Robolink()

robot =RDK.Item('ROBOTA',ITEM_TYPE_ROBOT)
frame_mesa=RDK.Item('Mesa',ITEM_TYPE_FRAME)
target_soldar=RDK.Item('TargetWeld',ITEM_TYPE_TARGET)

#Main

#Soldar pieza 1

while True:
    RDK.RunProgram('WeldOn(RESET)')
    sleep(1)
    robot.setSpeed(100,100)
    robot.MoveJ(target_soldar)
    robot.setPoseFrame(frame_mesa)
    while RDK.getParam('BoolWeld')==0:
        sleep(1)
    
    target_pose_in = transl(-125,-125,5)*roty(-5*pi/6)
    robot.MoveJ(target_pose_in)
    RDK.RunProgram('WeldOn(ON)')
    sleep(1)
    robot.setSpeed(10,10)
    target_pose_fin = transl(-125,125,5)*roty(-5*pi/6)
    robot.MoveL(target_pose_fin)
    RDK.setParam('BoolMove', 1)
    RDK.setParam('BoolWeld', 0)


#Soldar pieza 2
    RDK.RunProgram('WeldOn(OFF)')
    sleep(1)
    robot.setSpeed(100,100)
    robot.MoveJ(target_soldar)
    robot.setPoseFrame(frame_mesa)
    while RDK.getParam('BoolWeld')==0:
        sleep(1)

    target_pose_in = transl(125,125,5)*roty(5.5*pi/6)
    robot.MoveJ(target_pose_in)
    RDK.RunProgram('WeldOn(ON)')
    sleep(1)
    robot.setSpeed(10,10)
    target_pose_fin = transl(125,-125,5)*roty(5.5*pi/6)
    robot.MoveL(target_pose_fin)
    RDK.setParam('BoolMove', 1)
    RDK.setParam('BoolWeld', 0)

    #Soldar pieza 3
    RDK.RunProgram('WeldOn(OFF)')
    sleep(1)
    robot.setSpeed(100,100)
    robot.MoveJ(target_soldar)
    robot.setPoseFrame(frame_mesa)
    while RDK.getParam('BoolWeld')==0:
        sleep(1)

    target_pose_fin = transl(-125,125,250)*rotx(pi/12)*roty(-5*pi/6)
    robot.MoveL(target_pose_fin)
    RDK.RunProgram('WeldOn(ON)')
    sleep(1)
    robot.setSpeed(10,10)
    target_pose_in = transl(-125,125,5)*rotx(pi/12)*roty(-5*pi/6)
    robot.MoveL(target_pose_in)

    target_pose_fin = transl(125,125,5)*rotx(pi/12)*roty(5.5*pi/6)
    robot.MoveL(target_pose_fin)

    target_pose_fin = transl(125,125,250)*rotx(pi/12)*roty(5.5*pi/6)
    robot.MoveL(target_pose_fin)
    RDK.setParam('BoolMove', 1)
    RDK.setParam('BoolWeld', 0)


    #Soldar pieza 4
    RDK.RunProgram('WeldOn(OFF)')
    sleep(1)
    robot.setSpeed(100,100)
    robot.MoveJ(target_soldar)
    robot.setPoseFrame(frame_mesa)
    while RDK.getParam('BoolWeld')==0:
        sleep(1)

    target_pose_in = transl(-125,-125,250)*rotx(pi/12)*roty(5*pi/6)
    robot.MoveJ(target_pose_in)
    RDK.RunProgram('WeldOn(ON)')
    sleep(1)
    robot.setSpeed(10,10)
    target_pose_fin = transl(-125,125,250)*rotx(pi/12)*roty(5*pi/6)
    robot.MoveL(target_pose_fin)

    RDK.RunProgram('WeldOn(OFF)')
    sleep(1)
    robot.setSpeed(100,100)
    robot.MoveJ(target_soldar)
    robot.setPoseFrame(frame_mesa)

    target_pose_fin = transl(125,-125,250)*rotx(pi/12)*roty(-3*pi/6)
    robot.MoveL(target_pose_fin)
    RDK.RunProgram('WeldOn(ON)')
    sleep(1)
    robot.setSpeed(10,10)
    target_pose_fin = transl(125,125,250)*rotx(pi/12)*roty(-3*pi/6)
    robot.MoveL(target_pose_fin)

    RDK.RunProgram('WeldOn(OFF)')
    sleep(1)
    robot.setSpeed(100,100)
    robot.MoveJ(target_soldar)
    robot.setPoseFrame(frame_mesa)
    RDK.setParam('BoolMove', 1)
    RDK.setParam('BoolWeld', 0)

    robot.MoveJ(target_soldar)
    robot.setPoseFrame(frame_mesa)
    while RDK.getParam('BoolWeld')==0:
        sleep(1)


    target_pose_in = transl(-125,125,250)*rotx(7*pi/6)
    robot.MoveJ(target_pose_in)
    RDK.RunProgram('WeldOn(ON)')
    sleep(1)
    robot.setSpeed(10,10)
    target_pose_fin = transl(125,125,250)*rotx(7*pi/6)
    robot.MoveL(target_pose_fin)


    #Retorno
    RDK.RunProgram('WeldOn(OFF)')
    sleep(1)
    robot.setSpeed(100,100)
    robot.MoveJ(target_soldar)
    robot.setPoseFrame(frame_mesa)

    RDK.setParam('BoolMove', 1)
    RDK.setParam('BoolWeld', 0)



