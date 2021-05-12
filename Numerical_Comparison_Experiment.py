"""This is a simple decision experiment.
At each trial, a tow-digit number (between 11 and 99) is presented at the center of the
screen and the participant must press the key 'f' if the number is smaller than 55, and 'j' if
it is larger than 55.
"""

import random
import listes
from expyriment import design, control, stimuli

STANDARD = listes.MEAN_2DIGITS_NUMBER
TRAINING_LIST_LENGHT = 10
MAX_RESPONSE_DELAY = 2000
TARGETS = listes.create_valid_experimental_list(STANDARD, TRAINING_LIST_LENGHT)
SMALLER_RESPONSE = 'f'
LARGER_RESPONSE = 'j'

exp = design.Experiment(name = "Numerical Comparison", text_size = 40)
control.initialize(exp)

cue = stimuli.FixCross(size = (80, 80), line_width = 4)
blankscreen = stimuli.BlankScreen()
instructions = stimuli.TextScreen("Instructions",
    f"""You will see two-digit numbers, distributed around {STANDARD}, appear on the screen one by one.
    You task is to decide as fast as possible but by minimising errors, whether it is smaller or larger than {STANDARD}.
    
    If it is smaller than {STANDARD}, press '{SMALLER_RESPONSE}'
    If it is larger than {STANDARD}, press '{LARGER_RESPONSE}'
    
    There will be {len(TARGETS)} trials in total.
    Press the space bar to start.""")

# Prepare the stimuli
trials = []
for number in TARGETS:
    trials.append((number, stimuli.TextLine(str(number), text_size = 200)))


exp.add_data_variable_names(['number', 'respkey', 'RT'])

control.start(skip_ready_screen = True)
instructions.present()
exp.keyboard.wait()

for t in trials:
    blankscreen.present()
    exp.clock.wait(500)
    cue.present()
    exp.clock.wait(2000)
    t[1].present()
    key, rt = exp.keyboard.wait(SMALLER_RESPONSE + LARGER_RESPONSE, duration = MAX_RESPONSE_DELAY)
    exp.data.add([t[0],  key, rt])
# This function from expyriment saves automatically participant data
control.end() 
