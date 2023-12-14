# Type help("robodk.robolink") or help("robodk.robomath") for more information
# Press F5 to run the script
# Documentation: https://robodk.com/doc/en/RoboDK-API.html
# Reference:     https://robodk.com/doc/en/PythonAPI/robodk.html
# Note: It is not required to keep a copy of this file, your Python script is saved with your RDK project
from robodk import robolink    # RoboDK API
from robodk import robomath    # Robot toolbox

# The following 2 lines keep your code compatible with older versions or RoboDK:
from robodk import *      # RoboDK API
from robolink import *    # Robot toolbox

# Start the RoboDK API:
RDK = Robolink()
 
# Get the robot (first robot found):
robot = RDK.Item('', ITEM_TYPE_ROBOT)

# Getting the reset position -> joints
reset = [-90.00, -50.00, -125.00, -5.00, 90.00, 180.00]

# Getting the target for the two pieces
pRed = RDK.Item('PiezaRoja')
pOrange = RDK.Item('PiezaNaranja')
pYellow = RDK.Item('PiezaAmarilla')
pGreen = RDK.Item('PiezaVerde')
pBlue = RDK.Item('PiezaAzul')
pPurple = RDK.Item('PiezaMorada')
pWhite = RDK.Item('PiezaBlanca')
pBlack = RDK.Item('PiezaNegra')
pGray = RDK.Item('PiezaGris')

# Lista de las posiciones de las piezas en la mesa
piezas = [pRed, pOrange, pYellow, pGreen, pBlue, pPurple, pWhite, pBlack, pGray]

# Getting the final positions for each of the estation cubicles -> Joints
est1 = [-97.00, -110.00, -45.00, -27.00, 97.00, 90.00]
est2 = [-128.00, -68.00, -85.00, -28.00, 128.00, 90.00]
est3 = [-192.00, -80.00, -77.00, -24.00, 158.00, 90.00]
est4 = [-92.00, -119.00, -105.00, 45.00, 97.00, 90.00]
est5 = [-128.00, -85.00, -152.00, 57.00, 128.00, 90.00]
est6 = [-192.00, -92.00, -135.00, 45.00, 158.00, 90.00]
est7 = [-95.00, -145.00, -70.00, -143.00, 50.00, 90.00]
est8 = [-97.00, -125.00, -125.00, -115.00, 90.00, 90.00]
est9 = [-180.00, -119.00, -144.00, -99.00, 5.00, 90.00]

# Antes tenemos los targets a donde queremos mover el robot
# las estaciones de posicion finales 
estaciones = [est1, est2, est3, est4, est5, est6, est7, est8, est9]

# Go to reset position:
robot.setJoints(reset)

# Movimiento
numEstaciones = 9
for i in range(numEstaciones):
    robot.MoveJ(piezas[i])
    robot.MoveJ(estaciones[i])
    robot.MoveJ(reset)
    robot.Pause(3000)


# Trigger a program call at the end of the movement
robot.RunInstruction('Program_Done')
 