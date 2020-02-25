import turtle
from Lsystem_class import Lsystem, rule, ruleOutput
from Turtle_class import turtule_initialize,draw_l_system
from randomness import generate_axiom,generate_rule
from PIL import Image
alphabet = 'FXY'
symbols = '[]+-'

ruleF = [rule('F[+F]F[−F]F', 0.33), rule('F[+F]F', 0.33), rule('F[-F]F', 0.34)]
ruleX = [rule(' X[-FFF][+FFF]FX', 1)]
ruleY = [rule(' YFX[+Y][-Y]', 0.8), rule(' YFX[+Y]', 0.1), rule(' YFX[-Y]', 0.1)]
ruleset = {'F': ruleF, 'X': ruleX, 'Y': ruleY}
#ls = Lsystem('Y', ruleset)
ls = Lsystem('F', ruleset)



jill = turtule_initialize()

# create the string of turtle instructions
instruction_string = ls.processGen(6)
print(instruction_string)
# draw the picture, using angle 60 and segment length 5
draw_l_system(jill, instruction_string, 22.5, 3)
ts = turtle.getscreen()
ts.getcanvas().postscript(file="duck.eps")
img = Image.open('duck.eps')
img.save('duck.png', 'png')
turtle.mainloop()
