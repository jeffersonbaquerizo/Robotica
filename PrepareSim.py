from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox

PARAM_BOOL_WELD= 'BoolWeld'
PARAM_BOOL_MOVE= 'BoolMove'
PARAM_BOX_NUMBER= 'BoxNumber'

RDK = Robolink()

RDK.setParam(PARAM_BOOL_WELD, 0)
RDK.setParam(PARAM_BOOL_MOVE, 0)
RDK.setParam(PARAM_BOX_NUMBER,1)

frame_pallet=RDK.Item('PalletInicial',ITEM_TYPE_FRAME)

def MetalPosition(xs,ys,zs,xp,yp,zp):
    PositionsList=[]
    for k in range(zp):
        for j in range(yp):
            for i in range(xp):
                PositionsList=PositionsList+[[(i+0.5)*xs,(j+0.5)*ys,(k+0.5)*zs]]
    return PositionsList

def MetalSetup(frame,positions,xs,ys,zs):
    n=len(positions)
    for i in range(n):
        newMetal=frame.Paste()
        newMetal.Scale([xs/100,ys/100,zs/100])
        newMetal.setName('Metal_'+str(i+1))
        newMetal.setPose(transl(positions[i]))
        newMetal.setVisible(True, False)
        newMetal.Recolor([0.6719, 0.6953, 0.7031, 1])

def cleanup(objects, startswith="Part "):
    """Deletes all objects where the name starts with "startswith", from the provided list of objects."""    
    for item in objects:
        if item.Name().startswith(startswith):
            item.Delete()

#MAIN

RDK.Render(False)
# Elimina los objetos de la simulacion anterior
all_Objects=RDK.ItemList(ITEM_TYPE_OBJECT,False)
cleanup(all_Objects, 'Box_')
cleanup(all_Objects,'Metal_')

all_tools = RDK.ItemList(ITEM_TYPE_TOOL, False)
cleanup(all_tools, 'TCP ')

# Copiar la pieza
Metal=RDK.Item('Square')
Metal.Copy()

# Calculo de posiciones iniciales
positionsXYZ=MetalPosition(250,250,5,3,4,5)
MetalSetup(frame_pallet,positionsXYZ,250,250,5)

RDK.setParam(PARAM_BOOL_MOVE, 1)
RDK.setParam(PARAM_BOOL_WELD, 0)
RDK.RunProgram('WeldOn(RESET)')

RDK.Render(True)
