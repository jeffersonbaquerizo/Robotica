
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox
from time import sleep

RDK = Robolink()

robot =RDK.Item('ROBOTB',ITEM_TYPE_ROBOT)
tool=RDK.Item('GripperA',ITEM_TYPE_TOOL)
frame_pallet=RDK.Item('PalletInicial',ITEM_TYPE_FRAME)
frame_mesa=RDK.Item('Mesa',ITEM_TYPE_FRAME)
frame_pallet_final=RDK.Item('FinalPallet',ITEM_TYPE_FRAME)
target_pallet=RDK.Item('PalletInicio',ITEM_TYPE_TARGET)
target_mesa=RDK.Item('MesaTarget',ITEM_TYPE_TARGET)
target_mesa_Obj=RDK.Item('MesaObject',ITEM_TYPE_TARGET)
target_pallet_final=RDK.Item('PalletFinal',ITEM_TYPE_TARGET)
target_derecha=RDK.Item('MesaDerecha',ITEM_TYPE_TARGET)
target_frente=RDK.Item('MesaFrente',ITEM_TYPE_TARGET)
target_izquierda=RDK.Item('MesaIzquierda',ITEM_TYPE_TARGET)

def MetalPosition(xs,ys,zs,xp,yp,zp):
    PositionsList=[]
    for k in range(zp):
        for j in range(yp):
            for i in range(xp):
                PositionsList=PositionsList+[[(i+0.5)*xs,(j+0.5)*ys,(k+0.5)*zs]]
    return PositionsList

def TCP_On(toolitem):
    """Attaches the closest object to the toolitem Htool pose,
    It will also output appropriate function calls on the generated robot program (call to TCP_On)"""
    toolitem.AttachClosest()
    toolitem.RDK().RunMessage('Set air valve on')
    toolitem.RDK().RunProgram('TCP_On()')
      
def TCP_Off(toolitem, itemleave=0):
    """Detaches the closest object attached to the toolitem Htool pose,
    It will also output appropriate function calls on the generated robot program (call to TCP_Off)"""
    toolitem.DetachAll(itemleave)
    toolitem.RDK().RunMessage('Set air valve off')
    toolitem.RDK().RunProgram('TCP_Off()')

def BoxPosition(xs,ys,zs,xp,yp,zp):
    PositionsList=[]
    for k in range(zp):
        for j in range(yp):
            for i in range(xp):
                PositionsList=PositionsList+[[(i+0.5)*xs,(j+0.5)*ys,(k)*zs]]
    return PositionsList    

#Main
positionsXYZ=MetalPosition(250,250,5,3,4,5)
n = len(positionsXYZ)
i=n-1
BoxPositionXYZ=BoxPosition(250,250,250,3,4,3)

while i>=0:
    tool_xyzrpw = tool.PoseTool()*transl(0,0,7.5)
    tool_tcp = robot.AddTool(tool_xyzrpw, 'TCP A')
    robot.setPoseTool(tool_tcp)
    while RDK.getParam('BoolMove')==0:
        sleep(1)

    # Primera Pieza
    
    robot.setPoseFrame(frame_pallet)
    MetalPosicion_i = positionsXYZ[i]

    target_i = transl(MetalPosicion_i)*rotx(pi)
    target_i_app = target_i*transl(0,0,2.5)

    robot.MoveJ(target_pallet)

    robot.MoveJ(target_i_app)
    robot.MoveL(target_i)

    TCP_On(tool)
    robot.MoveL(target_i_app)
    robot.MoveJ(target_pallet)

    robot.setPoseFrame(frame_mesa)
    target_pose = transl(0,0,5)*rotx(pi)
    target_app = transl(0,0,7.5)*rotx(pi)

    robot.MoveJ(target_mesa)
    robot.MoveJ(target_app)
    robot.MoveL(target_pose)
    TCP_Off(tool, frame_mesa) 
    robot.MoveL(target_app)
    robot.MoveJ(target_mesa)
    
    i = i - 1

    # Segunda Pieza
    robot.setPoseFrame(frame_pallet)
    MetalPosicion_i = positionsXYZ[i]

    target_i = transl(MetalPosicion_i)*rotx(pi)
    target_i_app = target_i*transl(0,0,2.5)

    robot.MoveJ(target_pallet)

    robot.MoveJ(target_i_app)
    robot.MoveL(target_i)

    TCP_On(tool)
    robot.MoveL(target_i_app)
    robot.MoveJ(target_pallet)

    robot.setPoseFrame(frame_mesa)
    target_pose = transl(-125,0,125)*roty(pi/2)
    target_app = transl(-125,2.5,125)*roty(pi/2)

    robot.MoveJ(target_mesa)
    robot.MoveJ(target_derecha)
    robot.MoveJ(target_app)
    robot.MoveL(target_pose)
    TCP_Off(tool, frame_mesa) 
    robot.MoveL(target_app)
    sleep(1)
    RDK.setParam('BoolWeld', 1)
    RDK.setParam('BoolMove', 0)
    while RDK.getParam('BoolMove')==0:
        sleep(1)

    robot.MoveJ(target_derecha)
    robot.MoveJ(target_mesa)

    i = i - 1

    # Tercera Pieza
    robot.setPoseFrame(frame_pallet)
    MetalPosicion_i = positionsXYZ[i]

    target_i = transl(MetalPosicion_i)*rotx(pi)
    target_i_app = target_i*transl(0,0,2.5)

    robot.MoveJ(target_pallet)

    robot.MoveJ(target_i_app)
    robot.MoveL(target_i)

    TCP_On(tool)
    robot.MoveL(target_i_app)
    robot.MoveJ(target_pallet)

    robot.setPoseFrame(frame_mesa)
    target_pose = transl(125,0,125)*roty(-pi/2)
    target_app = transl(125,2.5,125)*roty(-pi/2)

    robot.MoveJ(target_mesa)
    robot.MoveJ(target_izquierda)
    robot.MoveJ(target_app)
    robot.MoveL(target_pose)
    TCP_Off(tool, frame_mesa)
    robot.MoveL(target_app)
    sleep(1)
    RDK.setParam('BoolWeld', 1)
    RDK.setParam('BoolMove', 0)
    while RDK.getParam('BoolMove')==0:
        sleep(1)

    robot.MoveJ(target_izquierda)
    robot.MoveJ(target_mesa)

    i = i - 1

    # Cuarta Pieza
    robot.setPoseFrame(frame_pallet)
    MetalPosicion_i = positionsXYZ[i]

    target_i = transl(MetalPosicion_i)*rotx(pi)
    target_i_app = target_i*transl(0,0,2.5)

    robot.MoveJ(target_pallet)

    robot.MoveJ(target_i_app)
    robot.MoveL(target_i)

    TCP_On(tool)
    robot.MoveL(target_i_app)
    robot.MoveJ(target_pallet)

    robot.setPoseFrame(frame_mesa)
    target_pose = transl(0,125,125)*rotx(pi/2)
    target_app = transl(2.5,125,125)*rotx(pi/2)

    robot.MoveJ(target_mesa)
    robot.MoveJ(target_frente)
    robot.MoveJ(target_app)
    robot.MoveL(target_pose)
    TCP_Off(tool, frame_mesa)
    robot.MoveL(target_app)
    sleep(1)
    RDK.setParam('BoolWeld', 1)
    RDK.setParam('BoolMove', 0)
    while RDK.getParam('BoolMove')==0:
        sleep(1)

    robot.MoveJ(target_frente)
    robot.MoveJ(target_mesa)
    
    i = i - 1
    
    # Quinta Pieza
    robot.setPoseFrame(frame_pallet)
    MetalPosicion_i = positionsXYZ[i]

    target_i = transl(MetalPosicion_i)*rotx(pi)
    target_i_app = target_i*transl(0,0,2.5)

    robot.MoveJ(target_pallet)

    robot.MoveJ(target_i_app)
    robot.MoveL(target_i)

    TCP_On(tool)
    robot.MoveL(target_i_app)
    robot.MoveJ(target_pallet)

    robot.setPoseFrame(frame_mesa)
    target_pose = transl(0,0,250)*rotx(pi)
    target_app = transl(0,0,252.5)*rotx(pi)

    robot.MoveJ(target_mesa)
    robot.MoveJ(target_app)
    robot.MoveL(target_pose)
    TCP_Off(tool, frame_mesa) 
    robot.MoveL(target_app)
    sleep(1)
    RDK.setParam('BoolWeld', 1)
    RDK.setParam('BoolMove', 0)
    while RDK.getParam('BoolMove')==0:
        sleep(1)
    robot.MoveJ(target_mesa)

    RDK.setParam('BoolWeld', 1)
    RDK.setParam('BoolMove', 0)
    while RDK.getParam('BoolMove')==0:
        sleep(1)
    
    i = i - 1

    # Construir caja

    RDK.RunProgram('BuildBox')
    RDK.RunProgram('WeldOn(RESET)')
    sleep(1)
   
    # Caja recogida

    tool_xyzrpw = tool.PoseTool()*transl(0,0,250)
    tool_tcp = robot.AddTool(tool_xyzrpw, 'TCP A')
    robot.setPoseTool(tool_tcp)


    target_pose = transl(0,0,-2.5)*rotx(pi)
    target_app = transl(0,0,0)*rotx(pi)


    robot.MoveJ(target_app)
    robot.MoveL(target_pose)
    TCP_On(tool)
    robot.MoveL(target_app)
    robot.MoveL(target_pose)
    robot.MoveJ(target_mesa)

    # Mover Caja

    robot.MoveJ(target_pallet_final)
    robot.setPoseFrame(frame_pallet_final)
    positionBox=transl(BoxPositionXYZ[int((n-i)/5-1)])*roty(-pi)
    robot.MoveJ(positionBox)

    TCP_Off(tool, frame_pallet_final)
    

