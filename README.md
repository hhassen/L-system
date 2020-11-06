# L-system : Probabilistic L-systems using Python
This project allows you to define [L-systems](https://medium.com/@hhtun21/l-systems-draw-your-first-fractals-139ed0bfcac2)
 (or generate random ones), then plot them and save them to a PNG picture.

You can define standard L-systems, as well as probabilistic ones that use probability's distribution to choose the rule applied.


![plant animation](https://raw.githubusercontent.com/hhassen/L-system/master/images/plant_animation.gif "plant animation")

### Prerequisites
* Python 3
* Turtle package
```
python3 -m pip install --upgrade turtle
```
* Pillow (PIL) package
```
python3 -m pip install --upgrade Pillow
```

### How to use
**Edit `main.py` to define your own L-system :**

First, **define the rules** that will be used.
A rule has the following format :
```python
# Replace to XF in 40% of the time and to XY in 60% of the time
ruleF = [rule('XF', 0.4), rule('XY', 0.6)]
```

This rule, which will be used later to parse F character, will replace `F -> XF` with probability of 40% and replace `F -> XY` with a probability of 60%.

Then, **define your ruleset**, which contains sets of characters and rules that will be used to these characters.
```python
ruleset = {'F': ruleF, 'X': ruleX, 'Y': ruleY}
```
In this ruleset, we will associate the character `F` to `ruleF`, `X` to `ruleX` and `Y` to `ruleY`.

Finally, **create the L-system** which is defined using an axiom and a ruleset.
```python
ls = Lsystem('F', ruleset)
```

You can also specify at which **generation** you would like to stop:
```python
# Stop at the 6th generation
instruction_string = ls.processGen(6)
```
And you can also **specify the angle and the length of segments** used while plotting the L-system:
```python
# draw the picture, using angle 22.5 and segment length 3
draw_l_system(jill, instruction_string, 22.5, 3)
```


Now, execute `main.py` using python to generate and plot the L-system:
```python
python main.py
```
Your L-systems is saved as `ouput.png`.
### Examples
### Plant
![plant](https://raw.githubusercontent.com/hhassen/L-system/master/images/plant.png "plant")

```python
# ...
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
# ...
```

### Snowflake

![snowflake](https://raw.githubusercontent.com/hhassen/L-system/master/images/snowflake.png "snowflake")
```python
# ...
# Rules definition
ruleF = [rule('F-F++F-F', 1)]
# Ruleset definition
ruleset = {'F': ruleF}
# Lsystem definition (initial state, ruleset)
ls = Lsystem('F++F++F', ruleset)

# generate the string of turtle instructions
instruction_string = ls.processGen(4)
print("Drawing the following L-system :\n",instruction_string)
jill = turtule_initialize()
# Move the turtle to the center before drawing
jill.penup()
jill.goto(-150 ,-200)
jill.pendown()
# draw the picture, using angle 60 and segment length 5
draw_l_system(jill, instruction_string, 60, 5)
ts = turtle.getscreen()
# ...
```


### More information
For more details, please read my article on L-systems:
1. [L-systems : draw nice fractals and plants (part I)](https://medium.com/@hhtun21/l-systems-draw-your-first-fractals-139ed0bfcac2)
2. [L-systems: draw a stochastic plant (part II)](https://medium.com/@hhtun21/l-systems-draw-a-stochastic-plant-ii-f322df2ea3c5)

This project is licensed under the terms of the MIT license.
