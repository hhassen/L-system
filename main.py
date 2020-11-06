""" Use this script file to generate your L-system """
import turtle
from Lsystem_class import Lsystem, rule, ruleOutput
from Turtle_class import turtule_initialize,draw_l_system
from randomness import generate_axiom,generate_rule
from PIL import Image

# The alphabet used for the L-system
alphabet = 'FXY'
# Symbols used in L-system
symbols = '[]+-'

""" L-system definition """
# Rules definition
ruleF = [rule('F[+F]F[−F]F', 0.33), rule('F[+F]F', 0.33), rule('F[-F]F', 0.34)]
ruleX = [rule(' X[-FFF][+FFF]FX', 1)]
ruleY = [rule(' YFX[+Y][-Y]', 0.8), rule(' YFX[+Y]', 0.1), rule(' YFX[-Y]', 0.1)]
# Ruleset definition
ruleset = {'F': ruleF, 'X': ruleX, 'Y': ruleY}
# Lsystem definition (initial state, ruleset)
ls = Lsystem('F', ruleset)

# generate the string of turtle instructions
instruction_string = ls.processGen(6)
print("Drawing the following L-system :\n",instruction_string)
jill = turtule_initialize()
# draw the picture, using angle 22.5 and segment length 3
draw_l_system(jill, instruction_string, 22.5, 3)
ts = turtle.getscreen()
# Save to EPS
ts.getcanvas().postscript(file="output.eps")
# Convert EPS to PNG 
img = Image.open('output.eps')
img.save('output.png', 'png')
turtle.mainloop()
