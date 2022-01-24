
from robolink import *    # RoboDK API
from robodk import *      # Robot toolbox

RDK = Robolink()
Frame_Mesa=RDK.Item('Mesa',ITEM_TYPE_FRAME)

def cleanup(objects, startswith="Part "):
    """Deletes all objects where the name starts with "startswith", from the provided list of objects."""    
    for item in objects:
        if item.Name().startswith(startswith) and item.Parent().Name().startswith('Mesa'):
            item.Delete()


RDK.Render(False)

all_Objects=RDK.ItemList(ITEM_TYPE_OBJECT,False)
cleanup(all_Objects,'Metal_')

# Construir la Caja
Box=RDK.Item('Cube')
Box.Copy()
num=RDK.getParam('BoxNumber')
NewBox=Frame_Mesa.Paste()
NewBox.Scale([250/100,250/100,250/100])
NewBox.setName('Box_'+str(int(num)))
NewBox.setPose(transl([0,0,125]))
NewBox.Recolor([0.6719, 0.6953, 0.7031, 1])
NewBox.setVisible(True, False)

RDK.setParam('BoxNumber',num+1)
RDK.Render(True)