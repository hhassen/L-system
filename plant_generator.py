""" Use this script file to generate numerous random L-systems """
import turtle
import os
from Lsystem_class import Lsystem
from Turtle_class import turtule_initialize,draw_l_system
from randomness import generate_axiom,generate_rule
from PIL import Image

directory = 'export/'
alphabet = 'FXY'
symbols = '[]+-'

file_path = os.path.join(directory, 'output.txt')
text_file = open(file_path, "w")
for i in range(10000):
    ruleset = {'F': generate_rule(5), 'X': generate_rule(5), 'Y': generate_rule(5)}
    axiom = generate_axiom()
    text_file.write("%02d axiom: %s ruleset : %s \n" % (i, axiom, ruleset))
    ls = Lsystem(axiom, ruleset)
    jill = turtule_initialize()
    # create the string of turtle instructions
    instruction_string = ls.processGen(6)
    # draw the picture, using angle 30 and segment length 5
    draw_l_system(jill, instruction_string, 30, 10)
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="export/"+str(i)+".eps")
    img = Image.open("export/"+str(i)+".eps")
    img.save("export/"+str(i)+".png", 'png')
    print(i, ' loop done')
text_file.close()
print("finish")
