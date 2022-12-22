#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.3),
    on Wed Dec 21 18:43:57 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'Treatment170922'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/elisahartmann/Uni/TU Chemnitz/Dokrotarbeit/Vorkurs/BROCAtreatment_Git_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Willkommen zum BROCAtreat!\nIn den folgenden 3 Zyklen wirst du eine künstliche Sprache erlernen. Du wirst 15 Blöcke bearbeiten, die je aus einem Lernteil, einem Testteil und einem Reaktionsteil bestehen. Zwischen den Blöcken kannst du eine Pause einlegen.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_welcome = keyboard.Keyboard()

# Initialize components for Routine "trainingInstruktions"
trainingInstruktionsClock = core.Clock()
text_10 = visual.TextStim(win=win, name='text_10',
    text='Wir werden das Vorgehen im Experiment an einem kurzen Beispiel üben.\n\nDrücke *space*, um das Training zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "learnTrainingInstruktions"
learnTrainingInstruktionsClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text='Du siehst gleich 4 KORREKTE Sätze einer künstlichen Grammatik. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block kommt eine kurze Pause, dann geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "learnTraining"
learnTrainingClock = core.Clock()
text_12 = visual.TextStim(win=win, name='text_12',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testTrainingInstruktions"
testTrainingInstruktionsClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='Jetzt kommt der Testblock. \nDu siehst 4 Sätze. Die Sätze können nach der verwendeten Grammatik korrekt oder inkorrekt sein.\nSchätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "testTraining"
testTrainingClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTraining"
feedbackTrainingClock = core.Clock()
text_16 = visual.TextStim(win=win, name='text_16',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "startExperiment"
startExperimentClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='Bist du bereit für das Experiment?\n\nDann starte es jetzt mit *space*',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial"
learnTrialClock = core.Clock()
text_lernblock = visual.TextStim(win=win, name='text_lernblock',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial"
testTrialClock = core.Clock()
test_sentences = visual.TextStim(win=win, name='test_sentences',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest"
feedbackTestClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_2"
learnTrial_2Clock = core.Clock()
lern_sentences2 = visual.TextStim(win=win, name='lern_sentences2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial2"
testTrial2Clock = core.Clock()
text_sentences2 = visual.TextStim(win=win, name='text_sentences2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test2 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest2"
feedbackTest2Clock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining1"
controlTraining1Clock = core.Clock()
gelber_kreis = visual.ImageStim(
    win=win,
    name='gelber_kreis', 
    image='BROCANTO_Treatment/gelber_kreis.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_3"
learnTrial_3Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial3"
testTrial3Clock = core.Clock()
test_sentences3 = visual.TextStim(win=win, name='test_sentences3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test3 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest3"
feedbackTest3Clock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining1"
controlTraining1Clock = core.Clock()
gelber_kreis = visual.ImageStim(
    win=win,
    name='gelber_kreis', 
    image='BROCANTO_Treatment/gelber_kreis.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial"
learnTrialClock = core.Clock()
text_lernblock = visual.TextStim(win=win, name='text_lernblock',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial4"
testTrial4Clock = core.Clock()
text_sentences4 = visual.TextStim(win=win, name='text_sentences4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test4 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest4"
feedbackTest4Clock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_2"
learnTrial_2Clock = core.Clock()
lern_sentences2 = visual.TextStim(win=win, name='lern_sentences2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial5"
testTrial5Clock = core.Clock()
text_sentences5 = visual.TextStim(win=win, name='text_sentences5',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test5 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest5"
feedbackTest5Clock = core.Clock()
text_18 = visual.TextStim(win=win, name='text_18',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining1"
controlTraining1Clock = core.Clock()
gelber_kreis = visual.ImageStim(
    win=win,
    name='gelber_kreis', 
    image='BROCANTO_Treatment/gelber_kreis.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "blockPause"
blockPauseClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='Du hast einen Block geschafft! \n\nMach eine kurze PAUSE. Wenn du bereit bist, drücke *space*, um den nächsten Block zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_3"
learnTrial_3Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial6"
testTrial6Clock = core.Clock()
text_sentences6 = visual.TextStim(win=win, name='text_sentences6',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test6 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest6"
feedbackTest6Clock = core.Clock()
text_19 = visual.TextStim(win=win, name='text_19',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial"
learnTrialClock = core.Clock()
text_lernblock = visual.TextStim(win=win, name='text_lernblock',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial7"
testTrial7Clock = core.Clock()
text_sentences7 = visual.TextStim(win=win, name='text_sentences7',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test7 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest7"
feedbackTest7Clock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining1"
controlTraining1Clock = core.Clock()
gelber_kreis = visual.ImageStim(
    win=win,
    name='gelber_kreis', 
    image='BROCANTO_Treatment/gelber_kreis.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_2"
learnTrial_2Clock = core.Clock()
lern_sentences2 = visual.TextStim(win=win, name='lern_sentences2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial8"
testTrial8Clock = core.Clock()
text_sentences8 = visual.TextStim(win=win, name='text_sentences8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test8 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest8"
feedbackTest8Clock = core.Clock()
text_21 = visual.TextStim(win=win, name='text_21',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_3"
learnTrial_3Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial9"
testTrial9Clock = core.Clock()
text_sentences9 = visual.TextStim(win=win, name='text_sentences9',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test9 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest9"
feedbackTest9Clock = core.Clock()
text_22 = visual.TextStim(win=win, name='text_22',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial"
learnTrialClock = core.Clock()
text_lernblock = visual.TextStim(win=win, name='text_lernblock',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial10"
testTrial10Clock = core.Clock()
text_sentences10 = visual.TextStim(win=win, name='text_sentences10',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test10 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest10"
feedbackTest10Clock = core.Clock()
text_23 = visual.TextStim(win=win, name='text_23',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining1"
controlTraining1Clock = core.Clock()
gelber_kreis = visual.ImageStim(
    win=win,
    name='gelber_kreis', 
    image='BROCANTO_Treatment/gelber_kreis.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "blockPause"
blockPauseClock = core.Clock()
text_29 = visual.TextStim(win=win, name='text_29',
    text='Du hast einen Block geschafft! \n\nMach eine kurze PAUSE. Wenn du bereit bist, drücke *space*, um den nächsten Block zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_2"
learnTrial_2Clock = core.Clock()
lern_sentences2 = visual.TextStim(win=win, name='lern_sentences2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial11"
testTrial11Clock = core.Clock()
text_sentences11 = visual.TextStim(win=win, name='text_sentences11',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test11 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest11"
feedbackTest11Clock = core.Clock()
text_24 = visual.TextStim(win=win, name='text_24',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining1"
controlTraining1Clock = core.Clock()
gelber_kreis = visual.ImageStim(
    win=win,
    name='gelber_kreis', 
    image='BROCANTO_Treatment/gelber_kreis.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_3"
learnTrial_3Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial12"
testTrial12Clock = core.Clock()
text_sentences12 = visual.TextStim(win=win, name='text_sentences12',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test12 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest12"
feedbackTest12Clock = core.Clock()
text_25 = visual.TextStim(win=win, name='text_25',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "testControlInstructions"
testControlInstructionsClock = core.Clock()
text_30 = visual.TextStim(win=win, name='text_30',
    text='Du siehst gleich eine farbige Form. Wenn du das rote Quadrat siehst, drücke ‚y‘ und dann *space*.\nSiehst du den gelben Kreis, drücke ’n’und dann *space*.\nVersuche, so schnell wie möglich zu reagieren.\n\nDrücke *space*, um die nächste Aufgabe zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial"
learnTrialClock = core.Clock()
text_lernblock = visual.TextStim(win=win, name='text_lernblock',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial13"
testTrial13Clock = core.Clock()
text_sentences13 = visual.TextStim(win=win, name='text_sentences13',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test13 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest13"
feedbackTest13Clock = core.Clock()
text_26 = visual.TextStim(win=win, name='text_26',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "controlTraining1"
controlTraining1Clock = core.Clock()
gelber_kreis = visual.ImageStim(
    win=win,
    name='gelber_kreis', 
    image='BROCANTO_Treatment/gelber_kreis.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_2"
learnTrial_2Clock = core.Clock()
lern_sentences2 = visual.TextStim(win=win, name='lern_sentences2',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testTrial14"
testTrial14Clock = core.Clock()
text_sentences14 = visual.TextStim(win=win, name='text_sentences14',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test14 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest14"
feedbackTest14Clock = core.Clock()
text_27 = visual.TextStim(win=win, name='text_27',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "learnInstructions"
learnInstructionsClock = core.Clock()
text_6 = visual.TextStim(win=win, name='text_6',
    text='Du siehst gleich 10 KORREKTE Sätze einer künstlichen Sprache. Jeder Satz bleibt für 7s sichtbar.\n\nNach dem Block geht es weiter mit dem Testblock.\n\n\nDrücke *space*, um den Lernblock zu starten.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "learnTask"
learnTaskClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='Lerne die Grammatik!',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "learnTrial_3"
learnTrial_3Clock = core.Clock()
text_8 = visual.TextStim(win=win, name='text_8',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.3, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "testInstructions"
testInstructionsClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Jetzt kommt der Testblock. \nDu siehst 10 Sätze. Schätze ein, ob der Satz grammatikalisch korrekt oder inkorrekt ist. Reagiere so schnell wie möglich. \n\ncorrect = ->\nincorrect = <-\n\nNach jeder Einschätzung bekommst du ein Feedback, ob deine Einschätzung RICHTIG oder FALSCH war.\n\nDrücke *space* zum Starten des Testteils.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_start = keyboard.Keyboard()

# Initialize components for Routine "testTrial15"
testTrial15Clock = core.Clock()
text_sentences15 = visual.TextStim(win=win, name='text_sentences15',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.06, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_test15 = keyboard.Keyboard()

# Initialize components for Routine "feedbackTest15"
feedbackTest15Clock = core.Clock()
text_28 = visual.TextStim(win=win, name='text_28',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.15, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);

# Initialize components for Routine "controlTraining"
controlTrainingClock = core.Clock()
rotes_quadrat = visual.ImageStim(
    win=win,
    name='rotes_quadrat', 
    image='BROCANTO_Treatment/rotes_quadrat.png', mask=None,
    ori=0.0, pos=(0, 0), size=(0.5, 0.5),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=0.0)
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "endScreen"
endScreenClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Geschafft!\n\nVielen Dank für die Teilnahme!',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_End = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_welcome.keys = []
key_welcome.rt = []
_key_welcome_allKeys = []
# keep track of which components have finished
welcomeComponents = [textWelcome, key_welcome]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if textWelcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        textWelcome.frameNStart = frameN  # exact frame index
        textWelcome.tStart = t  # local t and not account for scr refresh
        textWelcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *key_welcome* updates
    waitOnFlip = False
    if key_welcome.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_welcome.frameNStart = frameN  # exact frame index
        key_welcome.tStart = t  # local t and not account for scr refresh
        key_welcome.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_welcome, 'tStartRefresh')  # time at next scr refresh
        key_welcome.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_welcome.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_welcome.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_welcome.status == STARTED and not waitOnFlip:
        theseKeys = key_welcome.getKeys(keyList=['space'], waitRelease=False)
        _key_welcome_allKeys.extend(theseKeys)
        if len(_key_welcome_allKeys):
            key_welcome.keys = _key_welcome_allKeys[-1].name  # just the last key pressed
            key_welcome.rt = _key_welcome_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if key_welcome.keys in ['', [], None]:  # No response was made
    key_welcome.keys = None
thisExp.addData('key_welcome.keys',key_welcome.keys)
if key_welcome.keys != None:  # we had a response
    thisExp.addData('key_welcome.rt', key_welcome.rt)
thisExp.addData('key_welcome.started', key_welcome.tStartRefresh)
thisExp.addData('key_welcome.stopped', key_welcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "trainingInstruktions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
trainingInstruktionsComponents = [text_10, key_resp]
for thisComponent in trainingInstruktionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trainingInstruktionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trainingInstruktions"-------
while continueRoutine:
    # get current time
    t = trainingInstruktionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trainingInstruktionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_10* updates
    if text_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_10.frameNStart = frameN  # exact frame index
        text_10.tStart = t  # local t and not account for scr refresh
        text_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
        text_10.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trainingInstruktionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trainingInstruktions"-------
for thisComponent in trainingInstruktionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_10.started', text_10.tStartRefresh)
thisExp.addData('text_10.stopped', text_10.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "trainingInstruktions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTrainingInstruktions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_3.keys = []
key_resp_3.rt = []
_key_resp_3_allKeys = []
# keep track of which components have finished
learnTrainingInstruktionsComponents = [text_13, key_resp_3]
for thisComponent in learnTrainingInstruktionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTrainingInstruktionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTrainingInstruktions"-------
while continueRoutine:
    # get current time
    t = learnTrainingInstruktionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTrainingInstruktionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *key_resp_3* updates
    waitOnFlip = False
    if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_3.frameNStart = frameN  # exact frame index
        key_resp_3.tStart = t  # local t and not account for scr refresh
        key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
        key_resp_3.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_3.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_3_allKeys.extend(theseKeys)
        if len(_key_resp_3_allKeys):
            key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
            key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTrainingInstruktionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTrainingInstruktions"-------
for thisComponent in learnTrainingInstruktionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# check responses
if key_resp_3.keys in ['', [], None]:  # No response was made
    key_resp_3.keys = None
thisExp.addData('key_resp_3.keys',key_resp_3.keys)
if key_resp_3.keys != None:  # we had a response
    thisExp.addData('key_resp_3.rt', key_resp_3.rt)
thisExp.addData('key_resp_3.started', key_resp_3.tStartRefresh)
thisExp.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnTrainingInstruktions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/training.xlsx', selection='0:4'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTraining"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_12.setText(training)
    # keep track of which components have finished
    learnTrainingComponents = [text_12]
    for thisComponent in learnTrainingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTraining"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrainingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrainingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                text_12.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTraining"-------
    for thisComponent in learnTrainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_12.started', text_12.tStartRefresh)
    trials.addData('text_12.stopped', text_12.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_4.started', text_4.tStartRefresh)
    trials.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "testTrainingInstruktions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
testTrainingInstruktionsComponents = [text_15, key_resp_7]
for thisComponent in testTrainingInstruktionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testTrainingInstruktionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testTrainingInstruktions"-------
while continueRoutine:
    # get current time
    t = testTrainingInstruktionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testTrainingInstruktionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_15* updates
    if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_15.frameNStart = frameN  # exact frame index
        text_15.tStart = t  # local t and not account for scr refresh
        text_15.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
        text_15.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testTrainingInstruktionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testTrainingInstruktions"-------
for thisComponent in testTrainingInstruktionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_15.started', text_15.tStartRefresh)
thisExp.addData('text_15.stopped', text_15.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "testTrainingInstruktions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/training1.xlsx'),
    seed=None, name='trials_2')
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2:
        exec('{} = thisTrial_2[paramName]'.format(paramName))

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2:
            exec('{} = thisTrial_2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTraining"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_14.setText(training)
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    testTrainingComponents = [text_14, key_resp_4]
    for thisComponent in testTrainingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTraining"-------
    while continueRoutine:
        # get current time
        t = testTrainingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrainingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # was this correct?
                if (key_resp_4.keys == str(leftright_key)) or (key_resp_4.keys == leftright_key):
                    key_resp_4.corr = 1
                else:
                    key_resp_4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTraining"-------
    for thisComponent in testTrainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_14.started', text_14.tStartRefresh)
    trials_2.addData('text_14.stopped', text_14.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_resp_4.corr = 1;  # correct non-response
        else:
           key_resp_4.corr = 0;  # failed to respond (incorrectly)
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_4.keys',key_resp_4.keys)
    trials_2.addData('key_resp_4.corr', key_resp_4.corr)
    if key_resp_4.keys != None:  # we had a response
        trials_2.addData('key_resp_4.rt', key_resp_4.rt)
    trials_2.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials_2.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    # the Routine "testTraining" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTraining"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_16.setText(feedback_text)
    # keep track of which components have finished
    feedbackTrainingComponents = [text_16]
    for thisComponent in feedbackTrainingComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTraining"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTrainingClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTrainingClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        if text_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_16.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_16.tStop = t  # not accounting for scr refresh
                text_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                text_16.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTrainingComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTraining"-------
    for thisComponent in feedbackTrainingComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('text_16.started', text_16.tStartRefresh)
    trials_2.addData('text_16.stopped', text_16.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials_2'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "startExperiment"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
startExperimentComponents = [text_11, key_resp_2]
for thisComponent in startExperimentComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startExperimentClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startExperiment"-------
while continueRoutine:
    # get current time
    t = startExperimentClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startExperimentClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_11* updates
    if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_11.frameNStart = frameN  # exact frame index
        text_11.tStart = t  # local t and not account for scr refresh
        text_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
        text_11.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startExperimentComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startExperiment"-------
for thisComponent in startExperimentComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_11.started', text_11.tStartRefresh)
thisExp.addData('text_11.stopped', text_11.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "startExperiment" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_1.xlsx'),
    seed=None, name='trialslearn')
thisExp.addLoop(trialslearn)  # add the loop to the experiment
thisTrialslearn = trialslearn.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn.rgb)
if thisTrialslearn != None:
    for paramName in thisTrialslearn:
        exec('{} = thisTrialslearn[paramName]'.format(paramName))

for thisTrialslearn in trialslearn:
    currentLoop = trialslearn
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn.rgb)
    if thisTrialslearn != None:
        for paramName in thisTrialslearn:
            exec('{} = thisTrialslearn[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_lernblock.setText(correct_sentences_1)
    # keep track of which components have finished
    learnTrialComponents = [text_lernblock]
    for thisComponent in learnTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_lernblock* updates
        if text_lernblock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lernblock.frameNStart = frameN  # exact frame index
            text_lernblock.tStart = t  # local t and not account for scr refresh
            text_lernblock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lernblock, 'tStartRefresh')  # time at next scr refresh
            text_lernblock.setAutoDraw(True)
        if text_lernblock.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_lernblock.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_lernblock.tStop = t  # not accounting for scr refresh
                text_lernblock.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_lernblock, 'tStopRefresh')  # time at next scr refresh
                text_lernblock.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial"-------
    for thisComponent in learnTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn.addData('text_lernblock.started', text_lernblock.tStartRefresh)
    trialslearn.addData('text_lernblock.stopped', text_lernblock.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn.addData('text_4.started', text_4.tStartRefresh)
    trialslearn.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_1.xlsx'),
    seed=None, name='trialstest')
thisExp.addLoop(trialstest)  # add the loop to the experiment
thisTrialstest = trialstest.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest.rgb)
if thisTrialstest != None:
    for paramName in thisTrialstest:
        exec('{} = thisTrialstest[paramName]'.format(paramName))

for thisTrialstest in trialstest:
    currentLoop = trialstest
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest.rgb)
    if thisTrialstest != None:
        for paramName in thisTrialstest:
            exec('{} = thisTrialstest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    test_sentences.setText(testblock_1)
    key_test.keys = []
    key_test.rt = []
    _key_test_allKeys = []
    # keep track of which components have finished
    testTrialComponents = [test_sentences, key_test]
    for thisComponent in testTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial"-------
    while continueRoutine:
        # get current time
        t = testTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_sentences* updates
        if test_sentences.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_sentences.frameNStart = frameN  # exact frame index
            test_sentences.tStart = t  # local t and not account for scr refresh
            test_sentences.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_sentences, 'tStartRefresh')  # time at next scr refresh
            test_sentences.setAutoDraw(True)
        if test_sentences.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_sentences.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                test_sentences.tStop = t  # not accounting for scr refresh
                test_sentences.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test_sentences, 'tStopRefresh')  # time at next scr refresh
                test_sentences.setAutoDraw(False)
        
        # *key_test* updates
        waitOnFlip = False
        if key_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test.frameNStart = frameN  # exact frame index
            key_test.tStart = t  # local t and not account for scr refresh
            key_test.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test, 'tStartRefresh')  # time at next scr refresh
            key_test.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test.status == STARTED and not waitOnFlip:
            theseKeys = key_test.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test_allKeys.extend(theseKeys)
            if len(_key_test_allKeys):
                key_test.keys = _key_test_allKeys[-1].name  # just the last key pressed
                key_test.rt = _key_test_allKeys[-1].rt
                # was this correct?
                if (key_test.keys == str(leftright_key)) or (key_test.keys == leftright_key):
                    key_test.corr = 1
                else:
                    key_test.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial"-------
    for thisComponent in testTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest.addData('test_sentences.started', test_sentences.tStartRefresh)
    trialstest.addData('test_sentences.stopped', test_sentences.tStopRefresh)
    # check responses
    if key_test.keys in ['', [], None]:  # No response was made
        key_test.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test.corr = 1;  # correct non-response
        else:
           key_test.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest (TrialHandler)
    trialstest.addData('key_test.keys',key_test.keys)
    trialstest.addData('key_test.corr', key_test.corr)
    if key_test.keys != None:  # we had a response
        trialstest.addData('key_test.rt', key_test.rt)
    trialstest.addData('key_test.started', key_test.tStartRefresh)
    trialstest.addData('key_test.stopped', key_test.tStopRefresh)
    # the Routine "testTrial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
            
    
    text_3.setText(feedback_text)
    # keep track of which components have finished
    feedbackTestComponents = [text_3]
    for thisComponent in feedbackTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTestClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTestClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTestClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest"-------
    for thisComponent in feedbackTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest.addData('text_3.started', text_3.tStartRefresh)
    trialstest.addData('text_3.stopped', text_3.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_2.xlsx'),
    seed=None, name='trialslearn2')
thisExp.addLoop(trialslearn2)  # add the loop to the experiment
thisTrialslearn2 = trialslearn2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn2.rgb)
if thisTrialslearn2 != None:
    for paramName in thisTrialslearn2:
        exec('{} = thisTrialslearn2[paramName]'.format(paramName))

for thisTrialslearn2 in trialslearn2:
    currentLoop = trialslearn2
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn2.rgb)
    if thisTrialslearn2 != None:
        for paramName in thisTrialslearn2:
            exec('{} = thisTrialslearn2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_2"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    lern_sentences2.setText(correct_sentences_2)
    # keep track of which components have finished
    learnTrial_2Components = [lern_sentences2]
    for thisComponent in learnTrial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lern_sentences2* updates
        if lern_sentences2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lern_sentences2.frameNStart = frameN  # exact frame index
            lern_sentences2.tStart = t  # local t and not account for scr refresh
            lern_sentences2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lern_sentences2, 'tStartRefresh')  # time at next scr refresh
            lern_sentences2.setAutoDraw(True)
        if lern_sentences2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lern_sentences2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                lern_sentences2.tStop = t  # not accounting for scr refresh
                lern_sentences2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lern_sentences2, 'tStopRefresh')  # time at next scr refresh
                lern_sentences2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_2"-------
    for thisComponent in learnTrial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn2.addData('lern_sentences2.started', lern_sentences2.tStartRefresh)
    trialslearn2.addData('lern_sentences2.stopped', lern_sentences2.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn2.addData('text_4.started', text_4.tStartRefresh)
    trialslearn2.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn2'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest2 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_2.xlsx'),
    seed=None, name='trialstest2')
thisExp.addLoop(trialstest2)  # add the loop to the experiment
thisTrialstest2 = trialstest2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest2.rgb)
if thisTrialstest2 != None:
    for paramName in thisTrialstest2:
        exec('{} = thisTrialstest2[paramName]'.format(paramName))

for thisTrialstest2 in trialstest2:
    currentLoop = trialstest2
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest2.rgb)
    if thisTrialstest2 != None:
        for paramName in thisTrialstest2:
            exec('{} = thisTrialstest2[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial2"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences2.setText(testblock_2)
    key_test2.keys = []
    key_test2.rt = []
    _key_test2_allKeys = []
    # keep track of which components have finished
    testTrial2Components = [text_sentences2, key_test2]
    for thisComponent in testTrial2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial2"-------
    while continueRoutine:
        # get current time
        t = testTrial2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences2* updates
        if text_sentences2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences2.frameNStart = frameN  # exact frame index
            text_sentences2.tStart = t  # local t and not account for scr refresh
            text_sentences2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences2, 'tStartRefresh')  # time at next scr refresh
            text_sentences2.setAutoDraw(True)
        if text_sentences2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences2.tStop = t  # not accounting for scr refresh
                text_sentences2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences2, 'tStopRefresh')  # time at next scr refresh
                text_sentences2.setAutoDraw(False)
        
        # *key_test2* updates
        waitOnFlip = False
        if key_test2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test2.frameNStart = frameN  # exact frame index
            key_test2.tStart = t  # local t and not account for scr refresh
            key_test2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test2, 'tStartRefresh')  # time at next scr refresh
            key_test2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test2.status == STARTED and not waitOnFlip:
            theseKeys = key_test2.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test2_allKeys.extend(theseKeys)
            if len(_key_test2_allKeys):
                key_test2.keys = _key_test2_allKeys[-1].name  # just the last key pressed
                key_test2.rt = _key_test2_allKeys[-1].rt
                # was this correct?
                if (key_test2.keys == str(leftright_key)) or (key_test2.keys == leftright_key):
                    key_test2.corr = 1
                else:
                    key_test2.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial2"-------
    for thisComponent in testTrial2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest2.addData('text_sentences2.started', text_sentences2.tStartRefresh)
    trialstest2.addData('text_sentences2.stopped', text_sentences2.tStopRefresh)
    # check responses
    if key_test2.keys in ['', [], None]:  # No response was made
        key_test2.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test2.corr = 1;  # correct non-response
        else:
           key_test2.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest2 (TrialHandler)
    trialstest2.addData('key_test2.keys',key_test2.keys)
    trialstest2.addData('key_test2.corr', key_test2.corr)
    if key_test2.keys != None:  # we had a response
        trialstest2.addData('key_test2.rt', key_test2.rt)
    trialstest2.addData('key_test2.started', key_test2.tStartRefresh)
    trialstest2.addData('key_test2.stopped', key_test2.tStopRefresh)
    # the Routine "testTrial2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest2"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test2.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_9.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest2Components = [text_9]
    for thisComponent in feedbackTest2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_9* updates
        if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_9.frameNStart = frameN  # exact frame index
            text_9.tStart = t  # local t and not account for scr refresh
            text_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
            text_9.setAutoDraw(True)
        if text_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_9.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                text_9.tStop = t  # not accounting for scr refresh
                text_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
                text_9.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest2"-------
    for thisComponent in feedbackTest2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest2.addData('text_9.started', text_9.tStartRefresh)
    trialstest2.addData('text_9.stopped', text_9.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest2'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
controlTraining1Components = [gelber_kreis, key_resp_10]
for thisComponent in controlTraining1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTraining1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining1"-------
while continueRoutine:
    # get current time
    t = controlTraining1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTraining1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gelber_kreis* updates
    if gelber_kreis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gelber_kreis.frameNStart = frameN  # exact frame index
        gelber_kreis.tStart = t  # local t and not account for scr refresh
        gelber_kreis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gelber_kreis, 'tStartRefresh')  # time at next scr refresh
        gelber_kreis.setAutoDraw(True)
    if gelber_kreis.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gelber_kreis.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            gelber_kreis.tStop = t  # not accounting for scr refresh
            gelber_kreis.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gelber_kreis, 'tStopRefresh')  # time at next scr refresh
            gelber_kreis.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['n', 'space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTraining1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining1"-------
for thisComponent in controlTraining1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gelber_kreis.started', gelber_kreis.tStartRefresh)
thisExp.addData('gelber_kreis.stopped', gelber_kreis.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_3.xlsx'),
    seed=None, name='trialslearn3')
thisExp.addLoop(trialslearn3)  # add the loop to the experiment
thisTrialslearn3 = trialslearn3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn3.rgb)
if thisTrialslearn3 != None:
    for paramName in thisTrialslearn3:
        exec('{} = thisTrialslearn3[paramName]'.format(paramName))

for thisTrialslearn3 in trialslearn3:
    currentLoop = trialslearn3
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn3.rgb)
    if thisTrialslearn3 != None:
        for paramName in thisTrialslearn3:
            exec('{} = thisTrialslearn3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_3"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_8.setText(correct_sentences_3)
    # keep track of which components have finished
    learnTrial_3Components = [text_8]
    for thisComponent in learnTrial_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_3"-------
    for thisComponent in learnTrial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn3.addData('text_8.started', text_8.tStartRefresh)
    trialslearn3.addData('text_8.stopped', text_8.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn3.addData('text_4.started', text_4.tStartRefresh)
    trialslearn3.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn3'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest3 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_3.xlsx'),
    seed=None, name='trialstest3')
thisExp.addLoop(trialstest3)  # add the loop to the experiment
thisTrialstest3 = trialstest3.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest3.rgb)
if thisTrialstest3 != None:
    for paramName in thisTrialstest3:
        exec('{} = thisTrialstest3[paramName]'.format(paramName))

for thisTrialstest3 in trialstest3:
    currentLoop = trialstest3
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest3.rgb)
    if thisTrialstest3 != None:
        for paramName in thisTrialstest3:
            exec('{} = thisTrialstest3[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial3"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    test_sentences3.setText(testblock_3)
    key_test3.keys = []
    key_test3.rt = []
    _key_test3_allKeys = []
    # keep track of which components have finished
    testTrial3Components = [test_sentences3, key_test3]
    for thisComponent in testTrial3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial3"-------
    while continueRoutine:
        # get current time
        t = testTrial3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *test_sentences3* updates
        if test_sentences3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            test_sentences3.frameNStart = frameN  # exact frame index
            test_sentences3.tStart = t  # local t and not account for scr refresh
            test_sentences3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(test_sentences3, 'tStartRefresh')  # time at next scr refresh
            test_sentences3.setAutoDraw(True)
        if test_sentences3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > test_sentences3.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                test_sentences3.tStop = t  # not accounting for scr refresh
                test_sentences3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(test_sentences3, 'tStopRefresh')  # time at next scr refresh
                test_sentences3.setAutoDraw(False)
        
        # *key_test3* updates
        waitOnFlip = False
        if key_test3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test3.frameNStart = frameN  # exact frame index
            key_test3.tStart = t  # local t and not account for scr refresh
            key_test3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test3, 'tStartRefresh')  # time at next scr refresh
            key_test3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test3.status == STARTED and not waitOnFlip:
            theseKeys = key_test3.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test3_allKeys.extend(theseKeys)
            if len(_key_test3_allKeys):
                key_test3.keys = _key_test3_allKeys[-1].name  # just the last key pressed
                key_test3.rt = _key_test3_allKeys[-1].rt
                # was this correct?
                if (key_test3.keys == str(leftright_key)) or (key_test3.keys == leftright_key):
                    key_test3.corr = 1
                else:
                    key_test3.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial3"-------
    for thisComponent in testTrial3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest3.addData('test_sentences3.started', test_sentences3.tStartRefresh)
    trialstest3.addData('test_sentences3.stopped', test_sentences3.tStopRefresh)
    # check responses
    if key_test3.keys in ['', [], None]:  # No response was made
        key_test3.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test3.corr = 1;  # correct non-response
        else:
           key_test3.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest3 (TrialHandler)
    trialstest3.addData('key_test3.keys',key_test3.keys)
    trialstest3.addData('key_test3.corr', key_test3.corr)
    if key_test3.keys != None:  # we had a response
        trialstest3.addData('key_test3.rt', key_test3.rt)
    trialstest3.addData('key_test3.started', key_test3.tStartRefresh)
    trialstest3.addData('key_test3.stopped', key_test3.tStopRefresh)
    # the Routine "testTrial3" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest3"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test3.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_5.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest3Components = [text_5]
    for thisComponent in feedbackTest3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        if text_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_5.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_5.tStop = t  # not accounting for scr refresh
                text_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                text_5.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest3"-------
    for thisComponent in feedbackTest3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest3.addData('text_5.started', text_5.tStartRefresh)
    trialstest3.addData('text_5.stopped', text_5.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest3'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
controlTraining1Components = [gelber_kreis, key_resp_10]
for thisComponent in controlTraining1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTraining1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining1"-------
while continueRoutine:
    # get current time
    t = controlTraining1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTraining1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gelber_kreis* updates
    if gelber_kreis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gelber_kreis.frameNStart = frameN  # exact frame index
        gelber_kreis.tStart = t  # local t and not account for scr refresh
        gelber_kreis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gelber_kreis, 'tStartRefresh')  # time at next scr refresh
        gelber_kreis.setAutoDraw(True)
    if gelber_kreis.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gelber_kreis.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            gelber_kreis.tStop = t  # not accounting for scr refresh
            gelber_kreis.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gelber_kreis, 'tStopRefresh')  # time at next scr refresh
            gelber_kreis.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['n', 'space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTraining1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining1"-------
for thisComponent in controlTraining1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gelber_kreis.started', gelber_kreis.tStartRefresh)
thisExp.addData('gelber_kreis.stopped', gelber_kreis.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_1.xlsx'),
    seed=None, name='trialslearn4')
thisExp.addLoop(trialslearn4)  # add the loop to the experiment
thisTrialslearn4 = trialslearn4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn4.rgb)
if thisTrialslearn4 != None:
    for paramName in thisTrialslearn4:
        exec('{} = thisTrialslearn4[paramName]'.format(paramName))

for thisTrialslearn4 in trialslearn4:
    currentLoop = trialslearn4
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn4.rgb)
    if thisTrialslearn4 != None:
        for paramName in thisTrialslearn4:
            exec('{} = thisTrialslearn4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_lernblock.setText(correct_sentences_1)
    # keep track of which components have finished
    learnTrialComponents = [text_lernblock]
    for thisComponent in learnTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_lernblock* updates
        if text_lernblock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lernblock.frameNStart = frameN  # exact frame index
            text_lernblock.tStart = t  # local t and not account for scr refresh
            text_lernblock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lernblock, 'tStartRefresh')  # time at next scr refresh
            text_lernblock.setAutoDraw(True)
        if text_lernblock.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_lernblock.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_lernblock.tStop = t  # not accounting for scr refresh
                text_lernblock.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_lernblock, 'tStopRefresh')  # time at next scr refresh
                text_lernblock.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial"-------
    for thisComponent in learnTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn4.addData('text_lernblock.started', text_lernblock.tStartRefresh)
    trialslearn4.addData('text_lernblock.stopped', text_lernblock.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn4.addData('text_4.started', text_4.tStartRefresh)
    trialslearn4.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn4'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest4 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_4.xlsx'),
    seed=None, name='trialstest4')
thisExp.addLoop(trialstest4)  # add the loop to the experiment
thisTrialstest4 = trialstest4.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest4.rgb)
if thisTrialstest4 != None:
    for paramName in thisTrialstest4:
        exec('{} = thisTrialstest4[paramName]'.format(paramName))

for thisTrialstest4 in trialstest4:
    currentLoop = trialstest4
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest4.rgb)
    if thisTrialstest4 != None:
        for paramName in thisTrialstest4:
            exec('{} = thisTrialstest4[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial4"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences4.setText(testblock_4)
    key_test4.keys = []
    key_test4.rt = []
    _key_test4_allKeys = []
    # keep track of which components have finished
    testTrial4Components = [text_sentences4, key_test4]
    for thisComponent in testTrial4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial4"-------
    while continueRoutine:
        # get current time
        t = testTrial4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences4* updates
        if text_sentences4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences4.frameNStart = frameN  # exact frame index
            text_sentences4.tStart = t  # local t and not account for scr refresh
            text_sentences4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences4, 'tStartRefresh')  # time at next scr refresh
            text_sentences4.setAutoDraw(True)
        if text_sentences4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences4.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences4.tStop = t  # not accounting for scr refresh
                text_sentences4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences4, 'tStopRefresh')  # time at next scr refresh
                text_sentences4.setAutoDraw(False)
        
        # *key_test4* updates
        waitOnFlip = False
        if key_test4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test4.frameNStart = frameN  # exact frame index
            key_test4.tStart = t  # local t and not account for scr refresh
            key_test4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test4, 'tStartRefresh')  # time at next scr refresh
            key_test4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test4.status == STARTED and not waitOnFlip:
            theseKeys = key_test4.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test4_allKeys.extend(theseKeys)
            if len(_key_test4_allKeys):
                key_test4.keys = _key_test4_allKeys[-1].name  # just the last key pressed
                key_test4.rt = _key_test4_allKeys[-1].rt
                # was this correct?
                if (key_test4.keys == str(leftright_key)) or (key_test4.keys == leftright_key):
                    key_test4.corr = 1
                else:
                    key_test4.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial4"-------
    for thisComponent in testTrial4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest4.addData('text_sentences4.started', text_sentences4.tStartRefresh)
    trialstest4.addData('text_sentences4.stopped', text_sentences4.tStopRefresh)
    # check responses
    if key_test4.keys in ['', [], None]:  # No response was made
        key_test4.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test4.corr = 1;  # correct non-response
        else:
           key_test4.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest4 (TrialHandler)
    trialstest4.addData('key_test4.keys',key_test4.keys)
    trialstest4.addData('key_test4.corr', key_test4.corr)
    if key_test4.keys != None:  # we had a response
        trialstest4.addData('key_test4.rt', key_test4.rt)
    trialstest4.addData('key_test4.started', key_test4.tStartRefresh)
    trialstest4.addData('key_test4.stopped', key_test4.tStopRefresh)
    # the Routine "testTrial4" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest4"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test4.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_17.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest4Components = [text_17]
    for thisComponent in feedbackTest4Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest4"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest4Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest4Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                text_17.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest4Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest4"-------
    for thisComponent in feedbackTest4Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest4.addData('text_17.started', text_17.tStartRefresh)
    trialstest4.addData('text_17.stopped', text_17.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest4'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_2.xlsx'),
    seed=None, name='trialslearn5')
thisExp.addLoop(trialslearn5)  # add the loop to the experiment
thisTrialslearn5 = trialslearn5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn5.rgb)
if thisTrialslearn5 != None:
    for paramName in thisTrialslearn5:
        exec('{} = thisTrialslearn5[paramName]'.format(paramName))

for thisTrialslearn5 in trialslearn5:
    currentLoop = trialslearn5
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn5.rgb)
    if thisTrialslearn5 != None:
        for paramName in thisTrialslearn5:
            exec('{} = thisTrialslearn5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_2"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    lern_sentences2.setText(correct_sentences_2)
    # keep track of which components have finished
    learnTrial_2Components = [lern_sentences2]
    for thisComponent in learnTrial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lern_sentences2* updates
        if lern_sentences2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lern_sentences2.frameNStart = frameN  # exact frame index
            lern_sentences2.tStart = t  # local t and not account for scr refresh
            lern_sentences2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lern_sentences2, 'tStartRefresh')  # time at next scr refresh
            lern_sentences2.setAutoDraw(True)
        if lern_sentences2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lern_sentences2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                lern_sentences2.tStop = t  # not accounting for scr refresh
                lern_sentences2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lern_sentences2, 'tStopRefresh')  # time at next scr refresh
                lern_sentences2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_2"-------
    for thisComponent in learnTrial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn5.addData('lern_sentences2.started', lern_sentences2.tStartRefresh)
    trialslearn5.addData('lern_sentences2.stopped', lern_sentences2.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn5.addData('text_4.started', text_4.tStartRefresh)
    trialslearn5.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn5'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest5 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_5.xlsx'),
    seed=None, name='trialstest5')
thisExp.addLoop(trialstest5)  # add the loop to the experiment
thisTrialstest5 = trialstest5.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest5.rgb)
if thisTrialstest5 != None:
    for paramName in thisTrialstest5:
        exec('{} = thisTrialstest5[paramName]'.format(paramName))

for thisTrialstest5 in trialstest5:
    currentLoop = trialstest5
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest5.rgb)
    if thisTrialstest5 != None:
        for paramName in thisTrialstest5:
            exec('{} = thisTrialstest5[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial5"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences5.setText(testblock_5)
    key_test5.keys = []
    key_test5.rt = []
    _key_test5_allKeys = []
    # keep track of which components have finished
    testTrial5Components = [text_sentences5, key_test5]
    for thisComponent in testTrial5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial5"-------
    while continueRoutine:
        # get current time
        t = testTrial5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences5* updates
        if text_sentences5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences5.frameNStart = frameN  # exact frame index
            text_sentences5.tStart = t  # local t and not account for scr refresh
            text_sentences5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences5, 'tStartRefresh')  # time at next scr refresh
            text_sentences5.setAutoDraw(True)
        if text_sentences5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences5.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences5.tStop = t  # not accounting for scr refresh
                text_sentences5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences5, 'tStopRefresh')  # time at next scr refresh
                text_sentences5.setAutoDraw(False)
        
        # *key_test5* updates
        waitOnFlip = False
        if key_test5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test5.frameNStart = frameN  # exact frame index
            key_test5.tStart = t  # local t and not account for scr refresh
            key_test5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test5, 'tStartRefresh')  # time at next scr refresh
            key_test5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test5.status == STARTED and not waitOnFlip:
            theseKeys = key_test5.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test5_allKeys.extend(theseKeys)
            if len(_key_test5_allKeys):
                key_test5.keys = _key_test5_allKeys[-1].name  # just the last key pressed
                key_test5.rt = _key_test5_allKeys[-1].rt
                # was this correct?
                if (key_test5.keys == str(leftright_key)) or (key_test5.keys == leftright_key):
                    key_test5.corr = 1
                else:
                    key_test5.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial5"-------
    for thisComponent in testTrial5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest5.addData('text_sentences5.started', text_sentences5.tStartRefresh)
    trialstest5.addData('text_sentences5.stopped', text_sentences5.tStopRefresh)
    # check responses
    if key_test5.keys in ['', [], None]:  # No response was made
        key_test5.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test5.corr = 1;  # correct non-response
        else:
           key_test5.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest5 (TrialHandler)
    trialstest5.addData('key_test5.keys',key_test5.keys)
    trialstest5.addData('key_test5.corr', key_test5.corr)
    if key_test5.keys != None:  # we had a response
        trialstest5.addData('key_test5.rt', key_test5.rt)
    trialstest5.addData('key_test5.started', key_test5.tStartRefresh)
    trialstest5.addData('key_test5.stopped', key_test5.tStopRefresh)
    # the Routine "testTrial5" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest5"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test5.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_18.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest5Components = [text_18]
    for thisComponent in feedbackTest5Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest5"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest5Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest5Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        if text_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_18.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_18.tStop = t  # not accounting for scr refresh
                text_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
                text_18.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest5Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest5"-------
    for thisComponent in feedbackTest5Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest5.addData('text_18.started', text_18.tStartRefresh)
    trialstest5.addData('text_18.stopped', text_18.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest5'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
controlTraining1Components = [gelber_kreis, key_resp_10]
for thisComponent in controlTraining1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTraining1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining1"-------
while continueRoutine:
    # get current time
    t = controlTraining1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTraining1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gelber_kreis* updates
    if gelber_kreis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gelber_kreis.frameNStart = frameN  # exact frame index
        gelber_kreis.tStart = t  # local t and not account for scr refresh
        gelber_kreis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gelber_kreis, 'tStartRefresh')  # time at next scr refresh
        gelber_kreis.setAutoDraw(True)
    if gelber_kreis.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gelber_kreis.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            gelber_kreis.tStop = t  # not accounting for scr refresh
            gelber_kreis.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gelber_kreis, 'tStopRefresh')  # time at next scr refresh
            gelber_kreis.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['n', 'space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTraining1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining1"-------
for thisComponent in controlTraining1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gelber_kreis.started', gelber_kreis.tStartRefresh)
thisExp.addData('gelber_kreis.stopped', gelber_kreis.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blockPause"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
blockPauseComponents = [text_29, key_resp_6]
for thisComponent in blockPauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blockPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blockPause"-------
while continueRoutine:
    # get current time
    t = blockPauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blockPauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_29* updates
    if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockPauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blockPause"-------
for thisComponent in blockPauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_29.started', text_29.tStartRefresh)
thisExp.addData('text_29.stopped', text_29.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "blockPause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn6 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_3.xlsx'),
    seed=None, name='trialslearn6')
thisExp.addLoop(trialslearn6)  # add the loop to the experiment
thisTrialslearn6 = trialslearn6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn6.rgb)
if thisTrialslearn6 != None:
    for paramName in thisTrialslearn6:
        exec('{} = thisTrialslearn6[paramName]'.format(paramName))

for thisTrialslearn6 in trialslearn6:
    currentLoop = trialslearn6
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn6.rgb)
    if thisTrialslearn6 != None:
        for paramName in thisTrialslearn6:
            exec('{} = thisTrialslearn6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_3"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_8.setText(correct_sentences_3)
    # keep track of which components have finished
    learnTrial_3Components = [text_8]
    for thisComponent in learnTrial_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_3"-------
    for thisComponent in learnTrial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn6.addData('text_8.started', text_8.tStartRefresh)
    trialslearn6.addData('text_8.stopped', text_8.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn6.addData('text_4.started', text_4.tStartRefresh)
    trialslearn6.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn6'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest6 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_6.xlsx'),
    seed=None, name='trialstest6')
thisExp.addLoop(trialstest6)  # add the loop to the experiment
thisTrialstest6 = trialstest6.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest6.rgb)
if thisTrialstest6 != None:
    for paramName in thisTrialstest6:
        exec('{} = thisTrialstest6[paramName]'.format(paramName))

for thisTrialstest6 in trialstest6:
    currentLoop = trialstest6
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest6.rgb)
    if thisTrialstest6 != None:
        for paramName in thisTrialstest6:
            exec('{} = thisTrialstest6[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial6"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences6.setText(testblock_6)
    key_test6.keys = []
    key_test6.rt = []
    _key_test6_allKeys = []
    # keep track of which components have finished
    testTrial6Components = [text_sentences6, key_test6]
    for thisComponent in testTrial6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial6"-------
    while continueRoutine:
        # get current time
        t = testTrial6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences6* updates
        if text_sentences6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences6.frameNStart = frameN  # exact frame index
            text_sentences6.tStart = t  # local t and not account for scr refresh
            text_sentences6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences6, 'tStartRefresh')  # time at next scr refresh
            text_sentences6.setAutoDraw(True)
        if text_sentences6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences6.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences6.tStop = t  # not accounting for scr refresh
                text_sentences6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences6, 'tStopRefresh')  # time at next scr refresh
                text_sentences6.setAutoDraw(False)
        
        # *key_test6* updates
        waitOnFlip = False
        if key_test6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test6.frameNStart = frameN  # exact frame index
            key_test6.tStart = t  # local t and not account for scr refresh
            key_test6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test6, 'tStartRefresh')  # time at next scr refresh
            key_test6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test6.status == STARTED and not waitOnFlip:
            theseKeys = key_test6.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test6_allKeys.extend(theseKeys)
            if len(_key_test6_allKeys):
                key_test6.keys = _key_test6_allKeys[-1].name  # just the last key pressed
                key_test6.rt = _key_test6_allKeys[-1].rt
                # was this correct?
                if (key_test6.keys == str(leftright_key)) or (key_test6.keys == leftright_key):
                    key_test6.corr = 1
                else:
                    key_test6.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial6"-------
    for thisComponent in testTrial6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest6.addData('text_sentences6.started', text_sentences6.tStartRefresh)
    trialstest6.addData('text_sentences6.stopped', text_sentences6.tStopRefresh)
    # check responses
    if key_test6.keys in ['', [], None]:  # No response was made
        key_test6.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test6.corr = 1;  # correct non-response
        else:
           key_test6.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest6 (TrialHandler)
    trialstest6.addData('key_test6.keys',key_test6.keys)
    trialstest6.addData('key_test6.corr', key_test6.corr)
    if key_test6.keys != None:  # we had a response
        trialstest6.addData('key_test6.rt', key_test6.rt)
    trialstest6.addData('key_test6.started', key_test6.tStartRefresh)
    trialstest6.addData('key_test6.stopped', key_test6.tStopRefresh)
    # the Routine "testTrial6" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest6"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test6.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_19.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest6Components = [text_19]
    for thisComponent in feedbackTest6Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest6Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest6"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest6Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest6Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_19* updates
        if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_19.frameNStart = frameN  # exact frame index
            text_19.tStart = t  # local t and not account for scr refresh
            text_19.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
            text_19.setAutoDraw(True)
        if text_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_19.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_19.tStop = t  # not accounting for scr refresh
                text_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_19, 'tStopRefresh')  # time at next scr refresh
                text_19.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest6Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest6"-------
    for thisComponent in feedbackTest6Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest6.addData('text_19.started', text_19.tStartRefresh)
    trialstest6.addData('text_19.stopped', text_19.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest6'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn7 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_1.xlsx'),
    seed=None, name='trialslearn7')
thisExp.addLoop(trialslearn7)  # add the loop to the experiment
thisTrialslearn7 = trialslearn7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn7.rgb)
if thisTrialslearn7 != None:
    for paramName in thisTrialslearn7:
        exec('{} = thisTrialslearn7[paramName]'.format(paramName))

for thisTrialslearn7 in trialslearn7:
    currentLoop = trialslearn7
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn7.rgb)
    if thisTrialslearn7 != None:
        for paramName in thisTrialslearn7:
            exec('{} = thisTrialslearn7[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_lernblock.setText(correct_sentences_1)
    # keep track of which components have finished
    learnTrialComponents = [text_lernblock]
    for thisComponent in learnTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_lernblock* updates
        if text_lernblock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lernblock.frameNStart = frameN  # exact frame index
            text_lernblock.tStart = t  # local t and not account for scr refresh
            text_lernblock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lernblock, 'tStartRefresh')  # time at next scr refresh
            text_lernblock.setAutoDraw(True)
        if text_lernblock.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_lernblock.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_lernblock.tStop = t  # not accounting for scr refresh
                text_lernblock.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_lernblock, 'tStopRefresh')  # time at next scr refresh
                text_lernblock.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial"-------
    for thisComponent in learnTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn7.addData('text_lernblock.started', text_lernblock.tStartRefresh)
    trialslearn7.addData('text_lernblock.stopped', text_lernblock.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn7.addData('text_4.started', text_4.tStartRefresh)
    trialslearn7.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn7'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest7 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_7.xlsx'),
    seed=None, name='trialstest7')
thisExp.addLoop(trialstest7)  # add the loop to the experiment
thisTrialstest7 = trialstest7.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest7.rgb)
if thisTrialstest7 != None:
    for paramName in thisTrialstest7:
        exec('{} = thisTrialstest7[paramName]'.format(paramName))

for thisTrialstest7 in trialstest7:
    currentLoop = trialstest7
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest7.rgb)
    if thisTrialstest7 != None:
        for paramName in thisTrialstest7:
            exec('{} = thisTrialstest7[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial7"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences7.setText(testblock_7)
    key_test7.keys = []
    key_test7.rt = []
    _key_test7_allKeys = []
    # keep track of which components have finished
    testTrial7Components = [text_sentences7, key_test7]
    for thisComponent in testTrial7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial7"-------
    while continueRoutine:
        # get current time
        t = testTrial7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences7* updates
        if text_sentences7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences7.frameNStart = frameN  # exact frame index
            text_sentences7.tStart = t  # local t and not account for scr refresh
            text_sentences7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences7, 'tStartRefresh')  # time at next scr refresh
            text_sentences7.setAutoDraw(True)
        if text_sentences7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences7.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences7.tStop = t  # not accounting for scr refresh
                text_sentences7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences7, 'tStopRefresh')  # time at next scr refresh
                text_sentences7.setAutoDraw(False)
        
        # *key_test7* updates
        waitOnFlip = False
        if key_test7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test7.frameNStart = frameN  # exact frame index
            key_test7.tStart = t  # local t and not account for scr refresh
            key_test7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test7, 'tStartRefresh')  # time at next scr refresh
            key_test7.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test7.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test7.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test7.status == STARTED and not waitOnFlip:
            theseKeys = key_test7.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test7_allKeys.extend(theseKeys)
            if len(_key_test7_allKeys):
                key_test7.keys = _key_test7_allKeys[-1].name  # just the last key pressed
                key_test7.rt = _key_test7_allKeys[-1].rt
                # was this correct?
                if (key_test7.keys == str(leftright_key)) or (key_test7.keys == leftright_key):
                    key_test7.corr = 1
                else:
                    key_test7.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial7"-------
    for thisComponent in testTrial7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest7.addData('text_sentences7.started', text_sentences7.tStartRefresh)
    trialstest7.addData('text_sentences7.stopped', text_sentences7.tStopRefresh)
    # check responses
    if key_test7.keys in ['', [], None]:  # No response was made
        key_test7.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test7.corr = 1;  # correct non-response
        else:
           key_test7.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest7 (TrialHandler)
    trialstest7.addData('key_test7.keys',key_test7.keys)
    trialstest7.addData('key_test7.corr', key_test7.corr)
    if key_test7.keys != None:  # we had a response
        trialstest7.addData('key_test7.rt', key_test7.rt)
    trialstest7.addData('key_test7.started', key_test7.tStartRefresh)
    trialstest7.addData('key_test7.stopped', key_test7.tStopRefresh)
    # the Routine "testTrial7" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest7"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test7.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_20.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest7Components = [text_20]
    for thisComponent in feedbackTest7Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest7Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest7"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest7Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest7Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_20* updates
        if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_20.frameNStart = frameN  # exact frame index
            text_20.tStart = t  # local t and not account for scr refresh
            text_20.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
            text_20.setAutoDraw(True)
        if text_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_20.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_20.tStop = t  # not accounting for scr refresh
                text_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_20, 'tStopRefresh')  # time at next scr refresh
                text_20.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest7Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest7"-------
    for thisComponent in feedbackTest7Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest7.addData('text_20.started', text_20.tStartRefresh)
    trialstest7.addData('text_20.stopped', text_20.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest7'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
controlTraining1Components = [gelber_kreis, key_resp_10]
for thisComponent in controlTraining1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTraining1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining1"-------
while continueRoutine:
    # get current time
    t = controlTraining1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTraining1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gelber_kreis* updates
    if gelber_kreis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gelber_kreis.frameNStart = frameN  # exact frame index
        gelber_kreis.tStart = t  # local t and not account for scr refresh
        gelber_kreis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gelber_kreis, 'tStartRefresh')  # time at next scr refresh
        gelber_kreis.setAutoDraw(True)
    if gelber_kreis.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gelber_kreis.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            gelber_kreis.tStop = t  # not accounting for scr refresh
            gelber_kreis.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gelber_kreis, 'tStopRefresh')  # time at next scr refresh
            gelber_kreis.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['n', 'space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTraining1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining1"-------
for thisComponent in controlTraining1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gelber_kreis.started', gelber_kreis.tStartRefresh)
thisExp.addData('gelber_kreis.stopped', gelber_kreis.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn8 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_2.xlsx'),
    seed=None, name='trialslearn8')
thisExp.addLoop(trialslearn8)  # add the loop to the experiment
thisTrialslearn8 = trialslearn8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn8.rgb)
if thisTrialslearn8 != None:
    for paramName in thisTrialslearn8:
        exec('{} = thisTrialslearn8[paramName]'.format(paramName))

for thisTrialslearn8 in trialslearn8:
    currentLoop = trialslearn8
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn8.rgb)
    if thisTrialslearn8 != None:
        for paramName in thisTrialslearn8:
            exec('{} = thisTrialslearn8[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_2"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    lern_sentences2.setText(correct_sentences_2)
    # keep track of which components have finished
    learnTrial_2Components = [lern_sentences2]
    for thisComponent in learnTrial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lern_sentences2* updates
        if lern_sentences2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lern_sentences2.frameNStart = frameN  # exact frame index
            lern_sentences2.tStart = t  # local t and not account for scr refresh
            lern_sentences2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lern_sentences2, 'tStartRefresh')  # time at next scr refresh
            lern_sentences2.setAutoDraw(True)
        if lern_sentences2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lern_sentences2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                lern_sentences2.tStop = t  # not accounting for scr refresh
                lern_sentences2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lern_sentences2, 'tStopRefresh')  # time at next scr refresh
                lern_sentences2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_2"-------
    for thisComponent in learnTrial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn8.addData('lern_sentences2.started', lern_sentences2.tStartRefresh)
    trialslearn8.addData('lern_sentences2.stopped', lern_sentences2.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn8.addData('text_4.started', text_4.tStartRefresh)
    trialslearn8.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn8'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest8 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_8.xlsx'),
    seed=None, name='trialstest8')
thisExp.addLoop(trialstest8)  # add the loop to the experiment
thisTrialstest8 = trialstest8.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest8.rgb)
if thisTrialstest8 != None:
    for paramName in thisTrialstest8:
        exec('{} = thisTrialstest8[paramName]'.format(paramName))

for thisTrialstest8 in trialstest8:
    currentLoop = trialstest8
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest8.rgb)
    if thisTrialstest8 != None:
        for paramName in thisTrialstest8:
            exec('{} = thisTrialstest8[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial8"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences8.setText(testblock_8)
    key_test8.keys = []
    key_test8.rt = []
    _key_test8_allKeys = []
    # keep track of which components have finished
    testTrial8Components = [text_sentences8, key_test8]
    for thisComponent in testTrial8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial8"-------
    while continueRoutine:
        # get current time
        t = testTrial8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences8* updates
        if text_sentences8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences8.frameNStart = frameN  # exact frame index
            text_sentences8.tStart = t  # local t and not account for scr refresh
            text_sentences8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences8, 'tStartRefresh')  # time at next scr refresh
            text_sentences8.setAutoDraw(True)
        if text_sentences8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences8.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences8.tStop = t  # not accounting for scr refresh
                text_sentences8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences8, 'tStopRefresh')  # time at next scr refresh
                text_sentences8.setAutoDraw(False)
        
        # *key_test8* updates
        waitOnFlip = False
        if key_test8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test8.frameNStart = frameN  # exact frame index
            key_test8.tStart = t  # local t and not account for scr refresh
            key_test8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test8, 'tStartRefresh')  # time at next scr refresh
            key_test8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test8.status == STARTED and not waitOnFlip:
            theseKeys = key_test8.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test8_allKeys.extend(theseKeys)
            if len(_key_test8_allKeys):
                key_test8.keys = _key_test8_allKeys[-1].name  # just the last key pressed
                key_test8.rt = _key_test8_allKeys[-1].rt
                # was this correct?
                if (key_test8.keys == str(leftright_key)) or (key_test8.keys == leftright_key):
                    key_test8.corr = 1
                else:
                    key_test8.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial8"-------
    for thisComponent in testTrial8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest8.addData('text_sentences8.started', text_sentences8.tStartRefresh)
    trialstest8.addData('text_sentences8.stopped', text_sentences8.tStopRefresh)
    # check responses
    if key_test8.keys in ['', [], None]:  # No response was made
        key_test8.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test8.corr = 1;  # correct non-response
        else:
           key_test8.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest8 (TrialHandler)
    trialstest8.addData('key_test8.keys',key_test8.keys)
    trialstest8.addData('key_test8.corr', key_test8.corr)
    if key_test8.keys != None:  # we had a response
        trialstest8.addData('key_test8.rt', key_test8.rt)
    trialstest8.addData('key_test8.started', key_test8.tStartRefresh)
    trialstest8.addData('key_test8.stopped', key_test8.tStopRefresh)
    # the Routine "testTrial8" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest8"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test8.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_21.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest8Components = [text_21]
    for thisComponent in feedbackTest8Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest8Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest8"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest8Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest8Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_21* updates
        if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            text_21.setAutoDraw(True)
        if text_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_21.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_21.tStop = t  # not accounting for scr refresh
                text_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
                text_21.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest8Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest8"-------
    for thisComponent in feedbackTest8Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest8.addData('text_21.started', text_21.tStartRefresh)
    trialstest8.addData('text_21.stopped', text_21.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest8'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn9 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_3.xlsx'),
    seed=None, name='trialslearn9')
thisExp.addLoop(trialslearn9)  # add the loop to the experiment
thisTrialslearn9 = trialslearn9.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn9.rgb)
if thisTrialslearn9 != None:
    for paramName in thisTrialslearn9:
        exec('{} = thisTrialslearn9[paramName]'.format(paramName))

for thisTrialslearn9 in trialslearn9:
    currentLoop = trialslearn9
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn9.rgb)
    if thisTrialslearn9 != None:
        for paramName in thisTrialslearn9:
            exec('{} = thisTrialslearn9[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_3"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_8.setText(correct_sentences_3)
    # keep track of which components have finished
    learnTrial_3Components = [text_8]
    for thisComponent in learnTrial_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_3"-------
    for thisComponent in learnTrial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn9.addData('text_8.started', text_8.tStartRefresh)
    trialslearn9.addData('text_8.stopped', text_8.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn9.addData('text_4.started', text_4.tStartRefresh)
    trialslearn9.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn9'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest9 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_9.xlsx'),
    seed=None, name='trialstest9')
thisExp.addLoop(trialstest9)  # add the loop to the experiment
thisTrialstest9 = trialstest9.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest9.rgb)
if thisTrialstest9 != None:
    for paramName in thisTrialstest9:
        exec('{} = thisTrialstest9[paramName]'.format(paramName))

for thisTrialstest9 in trialstest9:
    currentLoop = trialstest9
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest9.rgb)
    if thisTrialstest9 != None:
        for paramName in thisTrialstest9:
            exec('{} = thisTrialstest9[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial9"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences9.setText(testblock_9)
    key_test9.keys = []
    key_test9.rt = []
    _key_test9_allKeys = []
    # keep track of which components have finished
    testTrial9Components = [text_sentences9, key_test9]
    for thisComponent in testTrial9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial9"-------
    while continueRoutine:
        # get current time
        t = testTrial9Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial9Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences9* updates
        if text_sentences9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences9.frameNStart = frameN  # exact frame index
            text_sentences9.tStart = t  # local t and not account for scr refresh
            text_sentences9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences9, 'tStartRefresh')  # time at next scr refresh
            text_sentences9.setAutoDraw(True)
        if text_sentences9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences9.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences9.tStop = t  # not accounting for scr refresh
                text_sentences9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences9, 'tStopRefresh')  # time at next scr refresh
                text_sentences9.setAutoDraw(False)
        
        # *key_test9* updates
        waitOnFlip = False
        if key_test9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test9.frameNStart = frameN  # exact frame index
            key_test9.tStart = t  # local t and not account for scr refresh
            key_test9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test9, 'tStartRefresh')  # time at next scr refresh
            key_test9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test9.status == STARTED and not waitOnFlip:
            theseKeys = key_test9.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test9_allKeys.extend(theseKeys)
            if len(_key_test9_allKeys):
                key_test9.keys = _key_test9_allKeys[-1].name  # just the last key pressed
                key_test9.rt = _key_test9_allKeys[-1].rt
                # was this correct?
                if (key_test9.keys == str(leftright_key)) or (key_test9.keys == leftright_key):
                    key_test9.corr = 1
                else:
                    key_test9.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial9"-------
    for thisComponent in testTrial9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest9.addData('text_sentences9.started', text_sentences9.tStartRefresh)
    trialstest9.addData('text_sentences9.stopped', text_sentences9.tStopRefresh)
    # check responses
    if key_test9.keys in ['', [], None]:  # No response was made
        key_test9.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test9.corr = 1;  # correct non-response
        else:
           key_test9.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest9 (TrialHandler)
    trialstest9.addData('key_test9.keys',key_test9.keys)
    trialstest9.addData('key_test9.corr', key_test9.corr)
    if key_test9.keys != None:  # we had a response
        trialstest9.addData('key_test9.rt', key_test9.rt)
    trialstest9.addData('key_test9.started', key_test9.tStartRefresh)
    trialstest9.addData('key_test9.stopped', key_test9.tStopRefresh)
    # the Routine "testTrial9" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest9"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test9.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_22.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest9Components = [text_22]
    for thisComponent in feedbackTest9Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest9Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest9"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest9Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest9Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_22* updates
        if text_22.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_22.frameNStart = frameN  # exact frame index
            text_22.tStart = t  # local t and not account for scr refresh
            text_22.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
            text_22.setAutoDraw(True)
        if text_22.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_22.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_22.tStop = t  # not accounting for scr refresh
                text_22.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_22, 'tStopRefresh')  # time at next scr refresh
                text_22.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest9Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest9"-------
    for thisComponent in feedbackTest9Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest9.addData('text_22.started', text_22.tStartRefresh)
    trialstest9.addData('text_22.stopped', text_22.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest9'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn10 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_1.xlsx'),
    seed=None, name='trialslearn10')
thisExp.addLoop(trialslearn10)  # add the loop to the experiment
thisTrialslearn10 = trialslearn10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn10.rgb)
if thisTrialslearn10 != None:
    for paramName in thisTrialslearn10:
        exec('{} = thisTrialslearn10[paramName]'.format(paramName))

for thisTrialslearn10 in trialslearn10:
    currentLoop = trialslearn10
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn10.rgb)
    if thisTrialslearn10 != None:
        for paramName in thisTrialslearn10:
            exec('{} = thisTrialslearn10[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_lernblock.setText(correct_sentences_1)
    # keep track of which components have finished
    learnTrialComponents = [text_lernblock]
    for thisComponent in learnTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_lernblock* updates
        if text_lernblock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lernblock.frameNStart = frameN  # exact frame index
            text_lernblock.tStart = t  # local t and not account for scr refresh
            text_lernblock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lernblock, 'tStartRefresh')  # time at next scr refresh
            text_lernblock.setAutoDraw(True)
        if text_lernblock.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_lernblock.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_lernblock.tStop = t  # not accounting for scr refresh
                text_lernblock.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_lernblock, 'tStopRefresh')  # time at next scr refresh
                text_lernblock.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial"-------
    for thisComponent in learnTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn10.addData('text_lernblock.started', text_lernblock.tStartRefresh)
    trialslearn10.addData('text_lernblock.stopped', text_lernblock.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn10.addData('text_4.started', text_4.tStartRefresh)
    trialslearn10.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn10'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest10 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_10.xlsx'),
    seed=None, name='trialstest10')
thisExp.addLoop(trialstest10)  # add the loop to the experiment
thisTrialstest10 = trialstest10.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest10.rgb)
if thisTrialstest10 != None:
    for paramName in thisTrialstest10:
        exec('{} = thisTrialstest10[paramName]'.format(paramName))

for thisTrialstest10 in trialstest10:
    currentLoop = trialstest10
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest10.rgb)
    if thisTrialstest10 != None:
        for paramName in thisTrialstest10:
            exec('{} = thisTrialstest10[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial10"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences10.setText(testblock_10)
    key_test10.keys = []
    key_test10.rt = []
    _key_test10_allKeys = []
    # keep track of which components have finished
    testTrial10Components = [text_sentences10, key_test10]
    for thisComponent in testTrial10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial10"-------
    while continueRoutine:
        # get current time
        t = testTrial10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences10* updates
        if text_sentences10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences10.frameNStart = frameN  # exact frame index
            text_sentences10.tStart = t  # local t and not account for scr refresh
            text_sentences10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences10, 'tStartRefresh')  # time at next scr refresh
            text_sentences10.setAutoDraw(True)
        if text_sentences10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences10.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences10.tStop = t  # not accounting for scr refresh
                text_sentences10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences10, 'tStopRefresh')  # time at next scr refresh
                text_sentences10.setAutoDraw(False)
        
        # *key_test10* updates
        waitOnFlip = False
        if key_test10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test10.frameNStart = frameN  # exact frame index
            key_test10.tStart = t  # local t and not account for scr refresh
            key_test10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test10, 'tStartRefresh')  # time at next scr refresh
            key_test10.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test10.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test10.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test10.status == STARTED and not waitOnFlip:
            theseKeys = key_test10.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test10_allKeys.extend(theseKeys)
            if len(_key_test10_allKeys):
                key_test10.keys = _key_test10_allKeys[-1].name  # just the last key pressed
                key_test10.rt = _key_test10_allKeys[-1].rt
                # was this correct?
                if (key_test10.keys == str(leftright_key)) or (key_test10.keys == leftright_key):
                    key_test10.corr = 1
                else:
                    key_test10.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial10"-------
    for thisComponent in testTrial10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest10.addData('text_sentences10.started', text_sentences10.tStartRefresh)
    trialstest10.addData('text_sentences10.stopped', text_sentences10.tStopRefresh)
    # check responses
    if key_test10.keys in ['', [], None]:  # No response was made
        key_test10.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test10.corr = 1;  # correct non-response
        else:
           key_test10.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest10 (TrialHandler)
    trialstest10.addData('key_test10.keys',key_test10.keys)
    trialstest10.addData('key_test10.corr', key_test10.corr)
    if key_test10.keys != None:  # we had a response
        trialstest10.addData('key_test10.rt', key_test10.rt)
    trialstest10.addData('key_test10.started', key_test10.tStartRefresh)
    trialstest10.addData('key_test10.stopped', key_test10.tStopRefresh)
    # the Routine "testTrial10" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest10"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test10.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_23.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest10Components = [text_23]
    for thisComponent in feedbackTest10Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest10Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest10"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest10Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest10Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            text_23.setAutoDraw(True)
        if text_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_23.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_23.tStop = t  # not accounting for scr refresh
                text_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_23, 'tStopRefresh')  # time at next scr refresh
                text_23.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest10Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest10"-------
    for thisComponent in feedbackTest10Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest10.addData('text_23.started', text_23.tStartRefresh)
    trialstest10.addData('text_23.stopped', text_23.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest10'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
controlTraining1Components = [gelber_kreis, key_resp_10]
for thisComponent in controlTraining1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTraining1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining1"-------
while continueRoutine:
    # get current time
    t = controlTraining1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTraining1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gelber_kreis* updates
    if gelber_kreis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gelber_kreis.frameNStart = frameN  # exact frame index
        gelber_kreis.tStart = t  # local t and not account for scr refresh
        gelber_kreis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gelber_kreis, 'tStartRefresh')  # time at next scr refresh
        gelber_kreis.setAutoDraw(True)
    if gelber_kreis.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gelber_kreis.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            gelber_kreis.tStop = t  # not accounting for scr refresh
            gelber_kreis.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gelber_kreis, 'tStopRefresh')  # time at next scr refresh
            gelber_kreis.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['n', 'space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTraining1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining1"-------
for thisComponent in controlTraining1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gelber_kreis.started', gelber_kreis.tStartRefresh)
thisExp.addData('gelber_kreis.stopped', gelber_kreis.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "blockPause"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_6.keys = []
key_resp_6.rt = []
_key_resp_6_allKeys = []
# keep track of which components have finished
blockPauseComponents = [text_29, key_resp_6]
for thisComponent in blockPauseComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
blockPauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "blockPause"-------
while continueRoutine:
    # get current time
    t = blockPauseClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=blockPauseClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_29* updates
    if text_29.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_29.frameNStart = frameN  # exact frame index
        text_29.tStart = t  # local t and not account for scr refresh
        text_29.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_29, 'tStartRefresh')  # time at next scr refresh
        text_29.setAutoDraw(True)
    
    # *key_resp_6* updates
    waitOnFlip = False
    if key_resp_6.status == NOT_STARTED and tThisFlip >= 3-frameTolerance:
        # keep track of start time/frame for later
        key_resp_6.frameNStart = frameN  # exact frame index
        key_resp_6.tStart = t  # local t and not account for scr refresh
        key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
        key_resp_6.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_6.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_6_allKeys.extend(theseKeys)
        if len(_key_resp_6_allKeys):
            key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
            key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in blockPauseComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "blockPause"-------
for thisComponent in blockPauseComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_29.started', text_29.tStartRefresh)
thisExp.addData('text_29.stopped', text_29.tStopRefresh)
# check responses
if key_resp_6.keys in ['', [], None]:  # No response was made
    key_resp_6.keys = None
thisExp.addData('key_resp_6.keys',key_resp_6.keys)
if key_resp_6.keys != None:  # we had a response
    thisExp.addData('key_resp_6.rt', key_resp_6.rt)
thisExp.addData('key_resp_6.started', key_resp_6.tStartRefresh)
thisExp.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
thisExp.nextEntry()
# the Routine "blockPause" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn11 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_2.xlsx'),
    seed=None, name='trialslearn11')
thisExp.addLoop(trialslearn11)  # add the loop to the experiment
thisTrialslearn11 = trialslearn11.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn11.rgb)
if thisTrialslearn11 != None:
    for paramName in thisTrialslearn11:
        exec('{} = thisTrialslearn11[paramName]'.format(paramName))

for thisTrialslearn11 in trialslearn11:
    currentLoop = trialslearn11
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn11.rgb)
    if thisTrialslearn11 != None:
        for paramName in thisTrialslearn11:
            exec('{} = thisTrialslearn11[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_2"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    lern_sentences2.setText(correct_sentences_2)
    # keep track of which components have finished
    learnTrial_2Components = [lern_sentences2]
    for thisComponent in learnTrial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lern_sentences2* updates
        if lern_sentences2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lern_sentences2.frameNStart = frameN  # exact frame index
            lern_sentences2.tStart = t  # local t and not account for scr refresh
            lern_sentences2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lern_sentences2, 'tStartRefresh')  # time at next scr refresh
            lern_sentences2.setAutoDraw(True)
        if lern_sentences2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lern_sentences2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                lern_sentences2.tStop = t  # not accounting for scr refresh
                lern_sentences2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lern_sentences2, 'tStopRefresh')  # time at next scr refresh
                lern_sentences2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_2"-------
    for thisComponent in learnTrial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn11.addData('lern_sentences2.started', lern_sentences2.tStartRefresh)
    trialslearn11.addData('lern_sentences2.stopped', lern_sentences2.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn11.addData('text_4.started', text_4.tStartRefresh)
    trialslearn11.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn11'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest11 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_11.xlsx'),
    seed=None, name='trialstest11')
thisExp.addLoop(trialstest11)  # add the loop to the experiment
thisTrialstest11 = trialstest11.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest11.rgb)
if thisTrialstest11 != None:
    for paramName in thisTrialstest11:
        exec('{} = thisTrialstest11[paramName]'.format(paramName))

for thisTrialstest11 in trialstest11:
    currentLoop = trialstest11
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest11.rgb)
    if thisTrialstest11 != None:
        for paramName in thisTrialstest11:
            exec('{} = thisTrialstest11[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial11"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences11.setText(testblock_11)
    key_test11.keys = []
    key_test11.rt = []
    _key_test11_allKeys = []
    # keep track of which components have finished
    testTrial11Components = [text_sentences11, key_test11]
    for thisComponent in testTrial11Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial11Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial11"-------
    while continueRoutine:
        # get current time
        t = testTrial11Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial11Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences11* updates
        if text_sentences11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences11.frameNStart = frameN  # exact frame index
            text_sentences11.tStart = t  # local t and not account for scr refresh
            text_sentences11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences11, 'tStartRefresh')  # time at next scr refresh
            text_sentences11.setAutoDraw(True)
        if text_sentences11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences11.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences11.tStop = t  # not accounting for scr refresh
                text_sentences11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences11, 'tStopRefresh')  # time at next scr refresh
                text_sentences11.setAutoDraw(False)
        
        # *key_test11* updates
        waitOnFlip = False
        if key_test11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test11.frameNStart = frameN  # exact frame index
            key_test11.tStart = t  # local t and not account for scr refresh
            key_test11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test11, 'tStartRefresh')  # time at next scr refresh
            key_test11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test11.status == STARTED and not waitOnFlip:
            theseKeys = key_test11.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test11_allKeys.extend(theseKeys)
            if len(_key_test11_allKeys):
                key_test11.keys = _key_test11_allKeys[-1].name  # just the last key pressed
                key_test11.rt = _key_test11_allKeys[-1].rt
                # was this correct?
                if (key_test11.keys == str(leftright_key)) or (key_test11.keys == leftright_key):
                    key_test11.corr = 1
                else:
                    key_test11.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial11Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial11"-------
    for thisComponent in testTrial11Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest11.addData('text_sentences11.started', text_sentences11.tStartRefresh)
    trialstest11.addData('text_sentences11.stopped', text_sentences11.tStopRefresh)
    # check responses
    if key_test11.keys in ['', [], None]:  # No response was made
        key_test11.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test11.corr = 1;  # correct non-response
        else:
           key_test11.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest11 (TrialHandler)
    trialstest11.addData('key_test11.keys',key_test11.keys)
    trialstest11.addData('key_test11.corr', key_test11.corr)
    if key_test11.keys != None:  # we had a response
        trialstest11.addData('key_test11.rt', key_test11.rt)
    trialstest11.addData('key_test11.started', key_test11.tStartRefresh)
    trialstest11.addData('key_test11.stopped', key_test11.tStopRefresh)
    # the Routine "testTrial11" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest11"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test11.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_24.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest11Components = [text_24]
    for thisComponent in feedbackTest11Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest11Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest11"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest11Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest11Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_24* updates
        if text_24.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_24.frameNStart = frameN  # exact frame index
            text_24.tStart = t  # local t and not account for scr refresh
            text_24.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_24, 'tStartRefresh')  # time at next scr refresh
            text_24.setAutoDraw(True)
        if text_24.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_24.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_24.tStop = t  # not accounting for scr refresh
                text_24.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_24, 'tStopRefresh')  # time at next scr refresh
                text_24.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest11Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest11"-------
    for thisComponent in feedbackTest11Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest11.addData('text_24.started', text_24.tStartRefresh)
    trialstest11.addData('text_24.stopped', text_24.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest11'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
controlTraining1Components = [gelber_kreis, key_resp_10]
for thisComponent in controlTraining1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTraining1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining1"-------
while continueRoutine:
    # get current time
    t = controlTraining1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTraining1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gelber_kreis* updates
    if gelber_kreis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gelber_kreis.frameNStart = frameN  # exact frame index
        gelber_kreis.tStart = t  # local t and not account for scr refresh
        gelber_kreis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gelber_kreis, 'tStartRefresh')  # time at next scr refresh
        gelber_kreis.setAutoDraw(True)
    if gelber_kreis.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gelber_kreis.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            gelber_kreis.tStop = t  # not accounting for scr refresh
            gelber_kreis.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gelber_kreis, 'tStopRefresh')  # time at next scr refresh
            gelber_kreis.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['n', 'space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTraining1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining1"-------
for thisComponent in controlTraining1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gelber_kreis.started', gelber_kreis.tStartRefresh)
thisExp.addData('gelber_kreis.stopped', gelber_kreis.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn12 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_3.xlsx'),
    seed=None, name='trialslearn12')
thisExp.addLoop(trialslearn12)  # add the loop to the experiment
thisTrialslearn12 = trialslearn12.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn12.rgb)
if thisTrialslearn12 != None:
    for paramName in thisTrialslearn12:
        exec('{} = thisTrialslearn12[paramName]'.format(paramName))

for thisTrialslearn12 in trialslearn12:
    currentLoop = trialslearn12
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn12.rgb)
    if thisTrialslearn12 != None:
        for paramName in thisTrialslearn12:
            exec('{} = thisTrialslearn12[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_3"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_8.setText(correct_sentences_3)
    # keep track of which components have finished
    learnTrial_3Components = [text_8]
    for thisComponent in learnTrial_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_3"-------
    for thisComponent in learnTrial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn12.addData('text_8.started', text_8.tStartRefresh)
    trialslearn12.addData('text_8.stopped', text_8.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn12.addData('text_4.started', text_4.tStartRefresh)
    trialslearn12.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn12'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest12 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_12.xlsx'),
    seed=None, name='trialstest12')
thisExp.addLoop(trialstest12)  # add the loop to the experiment
thisTrialstest12 = trialstest12.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest12.rgb)
if thisTrialstest12 != None:
    for paramName in thisTrialstest12:
        exec('{} = thisTrialstest12[paramName]'.format(paramName))

for thisTrialstest12 in trialstest12:
    currentLoop = trialstest12
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest12.rgb)
    if thisTrialstest12 != None:
        for paramName in thisTrialstest12:
            exec('{} = thisTrialstest12[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial12"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences12.setText(testblock_12)
    key_test12.keys = []
    key_test12.rt = []
    _key_test12_allKeys = []
    # keep track of which components have finished
    testTrial12Components = [text_sentences12, key_test12]
    for thisComponent in testTrial12Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial12Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial12"-------
    while continueRoutine:
        # get current time
        t = testTrial12Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial12Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences12* updates
        if text_sentences12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences12.frameNStart = frameN  # exact frame index
            text_sentences12.tStart = t  # local t and not account for scr refresh
            text_sentences12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences12, 'tStartRefresh')  # time at next scr refresh
            text_sentences12.setAutoDraw(True)
        if text_sentences12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences12.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences12.tStop = t  # not accounting for scr refresh
                text_sentences12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences12, 'tStopRefresh')  # time at next scr refresh
                text_sentences12.setAutoDraw(False)
        
        # *key_test12* updates
        waitOnFlip = False
        if key_test12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test12.frameNStart = frameN  # exact frame index
            key_test12.tStart = t  # local t and not account for scr refresh
            key_test12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test12, 'tStartRefresh')  # time at next scr refresh
            key_test12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test12.status == STARTED and not waitOnFlip:
            theseKeys = key_test12.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test12_allKeys.extend(theseKeys)
            if len(_key_test12_allKeys):
                key_test12.keys = _key_test12_allKeys[-1].name  # just the last key pressed
                key_test12.rt = _key_test12_allKeys[-1].rt
                # was this correct?
                if (key_test12.keys == str(leftright_key)) or (key_test12.keys == leftright_key):
                    key_test12.corr = 1
                else:
                    key_test12.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial12Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial12"-------
    for thisComponent in testTrial12Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest12.addData('text_sentences12.started', text_sentences12.tStartRefresh)
    trialstest12.addData('text_sentences12.stopped', text_sentences12.tStopRefresh)
    # check responses
    if key_test12.keys in ['', [], None]:  # No response was made
        key_test12.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test12.corr = 1;  # correct non-response
        else:
           key_test12.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest12 (TrialHandler)
    trialstest12.addData('key_test12.keys',key_test12.keys)
    trialstest12.addData('key_test12.corr', key_test12.corr)
    if key_test12.keys != None:  # we had a response
        trialstest12.addData('key_test12.rt', key_test12.rt)
    trialstest12.addData('key_test12.started', key_test12.tStartRefresh)
    trialstest12.addData('key_test12.stopped', key_test12.tStopRefresh)
    # the Routine "testTrial12" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest12"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test12.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_25.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest12Components = [text_25]
    for thisComponent in feedbackTest12Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest12Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest12"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest12Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest12Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_25* updates
        if text_25.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_25.frameNStart = frameN  # exact frame index
            text_25.tStart = t  # local t and not account for scr refresh
            text_25.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_25, 'tStartRefresh')  # time at next scr refresh
            text_25.setAutoDraw(True)
        if text_25.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_25.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_25.tStop = t  # not accounting for scr refresh
                text_25.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_25, 'tStopRefresh')  # time at next scr refresh
                text_25.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest12Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest12"-------
    for thisComponent in feedbackTest12Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest12.addData('text_25.started', text_25.tStartRefresh)
    trialstest12.addData('text_25.stopped', text_25.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest12'


# ------Prepare to start Routine "testControlInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
testControlInstructionsComponents = [text_30, key_resp_9]
for thisComponent in testControlInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testControlInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testControlInstructions"-------
while continueRoutine:
    # get current time
    t = testControlInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testControlInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_30* updates
    if text_30.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_30.frameNStart = frameN  # exact frame index
        text_30.tStart = t  # local t and not account for scr refresh
        text_30.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_30, 'tStartRefresh')  # time at next scr refresh
        text_30.setAutoDraw(True)
    if text_30.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_30.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            text_30.tStop = t  # not accounting for scr refresh
            text_30.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_30, 'tStopRefresh')  # time at next scr refresh
            text_30.setAutoDraw(False)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testControlInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testControlInstructions"-------
for thisComponent in testControlInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_30.started', text_30.tStartRefresh)
thisExp.addData('text_30.stopped', text_30.tStopRefresh)
# check responses
if key_resp_9.keys in ['', [], None]:  # No response was made
    key_resp_9.keys = None
thisExp.addData('key_resp_9.keys',key_resp_9.keys)
if key_resp_9.keys != None:  # we had a response
    thisExp.addData('key_resp_9.rt', key_resp_9.rt)
thisExp.addData('key_resp_9.started', key_resp_9.tStartRefresh)
thisExp.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
thisExp.nextEntry()
# the Routine "testControlInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn13 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_1.xlsx'),
    seed=None, name='trialslearn13')
thisExp.addLoop(trialslearn13)  # add the loop to the experiment
thisTrialslearn13 = trialslearn13.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn13.rgb)
if thisTrialslearn13 != None:
    for paramName in thisTrialslearn13:
        exec('{} = thisTrialslearn13[paramName]'.format(paramName))

for thisTrialslearn13 in trialslearn13:
    currentLoop = trialslearn13
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn13.rgb)
    if thisTrialslearn13 != None:
        for paramName in thisTrialslearn13:
            exec('{} = thisTrialslearn13[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_lernblock.setText(correct_sentences_1)
    # keep track of which components have finished
    learnTrialComponents = [text_lernblock]
    for thisComponent in learnTrialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_lernblock* updates
        if text_lernblock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_lernblock.frameNStart = frameN  # exact frame index
            text_lernblock.tStart = t  # local t and not account for scr refresh
            text_lernblock.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_lernblock, 'tStartRefresh')  # time at next scr refresh
            text_lernblock.setAutoDraw(True)
        if text_lernblock.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_lernblock.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_lernblock.tStop = t  # not accounting for scr refresh
                text_lernblock.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_lernblock, 'tStopRefresh')  # time at next scr refresh
                text_lernblock.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial"-------
    for thisComponent in learnTrialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn13.addData('text_lernblock.started', text_lernblock.tStartRefresh)
    trialslearn13.addData('text_lernblock.stopped', text_lernblock.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn13.addData('text_4.started', text_4.tStartRefresh)
    trialslearn13.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn13'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest13 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_13.xlsx'),
    seed=None, name='trialstest13')
thisExp.addLoop(trialstest13)  # add the loop to the experiment
thisTrialstest13 = trialstest13.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest13.rgb)
if thisTrialstest13 != None:
    for paramName in thisTrialstest13:
        exec('{} = thisTrialstest13[paramName]'.format(paramName))

for thisTrialstest13 in trialstest13:
    currentLoop = trialstest13
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest13.rgb)
    if thisTrialstest13 != None:
        for paramName in thisTrialstest13:
            exec('{} = thisTrialstest13[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial13"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences13.setText(testblock_13)
    key_test13.keys = []
    key_test13.rt = []
    _key_test13_allKeys = []
    # keep track of which components have finished
    testTrial13Components = [text_sentences13, key_test13]
    for thisComponent in testTrial13Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial13Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial13"-------
    while continueRoutine:
        # get current time
        t = testTrial13Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial13Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences13* updates
        if text_sentences13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences13.frameNStart = frameN  # exact frame index
            text_sentences13.tStart = t  # local t and not account for scr refresh
            text_sentences13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences13, 'tStartRefresh')  # time at next scr refresh
            text_sentences13.setAutoDraw(True)
        if text_sentences13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences13.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences13.tStop = t  # not accounting for scr refresh
                text_sentences13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences13, 'tStopRefresh')  # time at next scr refresh
                text_sentences13.setAutoDraw(False)
        
        # *key_test13* updates
        waitOnFlip = False
        if key_test13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test13.frameNStart = frameN  # exact frame index
            key_test13.tStart = t  # local t and not account for scr refresh
            key_test13.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test13, 'tStartRefresh')  # time at next scr refresh
            key_test13.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test13.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test13.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test13.status == STARTED and not waitOnFlip:
            theseKeys = key_test13.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test13_allKeys.extend(theseKeys)
            if len(_key_test13_allKeys):
                key_test13.keys = _key_test13_allKeys[-1].name  # just the last key pressed
                key_test13.rt = _key_test13_allKeys[-1].rt
                # was this correct?
                if (key_test13.keys == str(leftright_key)) or (key_test13.keys == leftright_key):
                    key_test13.corr = 1
                else:
                    key_test13.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial13Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial13"-------
    for thisComponent in testTrial13Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest13.addData('text_sentences13.started', text_sentences13.tStartRefresh)
    trialstest13.addData('text_sentences13.stopped', text_sentences13.tStopRefresh)
    # check responses
    if key_test13.keys in ['', [], None]:  # No response was made
        key_test13.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test13.corr = 1;  # correct non-response
        else:
           key_test13.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest13 (TrialHandler)
    trialstest13.addData('key_test13.keys',key_test13.keys)
    trialstest13.addData('key_test13.corr', key_test13.corr)
    if key_test13.keys != None:  # we had a response
        trialstest13.addData('key_test13.rt', key_test13.rt)
    trialstest13.addData('key_test13.started', key_test13.tStartRefresh)
    trialstest13.addData('key_test13.stopped', key_test13.tStopRefresh)
    # the Routine "testTrial13" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest13"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test13.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_26.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest13Components = [text_26]
    for thisComponent in feedbackTest13Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest13Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest13"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest13Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest13Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_26* updates
        if text_26.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_26.frameNStart = frameN  # exact frame index
            text_26.tStart = t  # local t and not account for scr refresh
            text_26.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_26, 'tStartRefresh')  # time at next scr refresh
            text_26.setAutoDraw(True)
        if text_26.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_26.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_26.tStop = t  # not accounting for scr refresh
                text_26.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_26, 'tStopRefresh')  # time at next scr refresh
                text_26.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest13Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest13"-------
    for thisComponent in feedbackTest13Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest13.addData('text_26.started', text_26.tStartRefresh)
    trialstest13.addData('text_26.stopped', text_26.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest13'


# ------Prepare to start Routine "controlTraining1"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
controlTraining1Components = [gelber_kreis, key_resp_10]
for thisComponent in controlTraining1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTraining1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining1"-------
while continueRoutine:
    # get current time
    t = controlTraining1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTraining1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *gelber_kreis* updates
    if gelber_kreis.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        gelber_kreis.frameNStart = frameN  # exact frame index
        gelber_kreis.tStart = t  # local t and not account for scr refresh
        gelber_kreis.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(gelber_kreis, 'tStartRefresh')  # time at next scr refresh
        gelber_kreis.setAutoDraw(True)
    if gelber_kreis.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > gelber_kreis.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            gelber_kreis.tStop = t  # not accounting for scr refresh
            gelber_kreis.frameNStop = frameN  # exact frame index
            win.timeOnFlip(gelber_kreis, 'tStopRefresh')  # time at next scr refresh
            gelber_kreis.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['n', 'space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTraining1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining1"-------
for thisComponent in controlTraining1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('gelber_kreis.started', gelber_kreis.tStartRefresh)
thisExp.addData('gelber_kreis.stopped', gelber_kreis.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn14 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_2.xlsx'),
    seed=None, name='trialslearn14')
thisExp.addLoop(trialslearn14)  # add the loop to the experiment
thisTrialslearn14 = trialslearn14.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn14.rgb)
if thisTrialslearn14 != None:
    for paramName in thisTrialslearn14:
        exec('{} = thisTrialslearn14[paramName]'.format(paramName))

for thisTrialslearn14 in trialslearn14:
    currentLoop = trialslearn14
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn14.rgb)
    if thisTrialslearn14 != None:
        for paramName in thisTrialslearn14:
            exec('{} = thisTrialslearn14[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_2"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    lern_sentences2.setText(correct_sentences_2)
    # keep track of which components have finished
    learnTrial_2Components = [lern_sentences2]
    for thisComponent in learnTrial_2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_2Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_2Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *lern_sentences2* updates
        if lern_sentences2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            lern_sentences2.frameNStart = frameN  # exact frame index
            lern_sentences2.tStart = t  # local t and not account for scr refresh
            lern_sentences2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(lern_sentences2, 'tStartRefresh')  # time at next scr refresh
            lern_sentences2.setAutoDraw(True)
        if lern_sentences2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > lern_sentences2.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                lern_sentences2.tStop = t  # not accounting for scr refresh
                lern_sentences2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(lern_sentences2, 'tStopRefresh')  # time at next scr refresh
                lern_sentences2.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_2"-------
    for thisComponent in learnTrial_2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn14.addData('lern_sentences2.started', lern_sentences2.tStartRefresh)
    trialslearn14.addData('lern_sentences2.stopped', lern_sentences2.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn14.addData('text_4.started', text_4.tStartRefresh)
    trialslearn14.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn14'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialstest14 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_14.xlsx'),
    seed=None, name='trialstest14')
thisExp.addLoop(trialstest14)  # add the loop to the experiment
thisTrialstest14 = trialstest14.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest14.rgb)
if thisTrialstest14 != None:
    for paramName in thisTrialstest14:
        exec('{} = thisTrialstest14[paramName]'.format(paramName))

for thisTrialstest14 in trialstest14:
    currentLoop = trialstest14
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest14.rgb)
    if thisTrialstest14 != None:
        for paramName in thisTrialstest14:
            exec('{} = thisTrialstest14[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial14"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences14.setText(testblock_14)
    key_test14.keys = []
    key_test14.rt = []
    _key_test14_allKeys = []
    # keep track of which components have finished
    testTrial14Components = [text_sentences14, key_test14]
    for thisComponent in testTrial14Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial14Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial14"-------
    while continueRoutine:
        # get current time
        t = testTrial14Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial14Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences14* updates
        if text_sentences14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences14.frameNStart = frameN  # exact frame index
            text_sentences14.tStart = t  # local t and not account for scr refresh
            text_sentences14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences14, 'tStartRefresh')  # time at next scr refresh
            text_sentences14.setAutoDraw(True)
        if text_sentences14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences14.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences14.tStop = t  # not accounting for scr refresh
                text_sentences14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences14, 'tStopRefresh')  # time at next scr refresh
                text_sentences14.setAutoDraw(False)
        
        # *key_test14* updates
        waitOnFlip = False
        if key_test14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test14.frameNStart = frameN  # exact frame index
            key_test14.tStart = t  # local t and not account for scr refresh
            key_test14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test14, 'tStartRefresh')  # time at next scr refresh
            key_test14.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test14.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test14.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test14.status == STARTED and not waitOnFlip:
            theseKeys = key_test14.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test14_allKeys.extend(theseKeys)
            if len(_key_test14_allKeys):
                key_test14.keys = _key_test14_allKeys[-1].name  # just the last key pressed
                key_test14.rt = _key_test14_allKeys[-1].rt
                # was this correct?
                if (key_test14.keys == str(leftright_key)) or (key_test14.keys == leftright_key):
                    key_test14.corr = 1
                else:
                    key_test14.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial14Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial14"-------
    for thisComponent in testTrial14Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest14.addData('text_sentences14.started', text_sentences14.tStartRefresh)
    trialstest14.addData('text_sentences14.stopped', text_sentences14.tStopRefresh)
    # check responses
    if key_test14.keys in ['', [], None]:  # No response was made
        key_test14.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test14.corr = 1;  # correct non-response
        else:
           key_test14.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest14 (TrialHandler)
    trialstest14.addData('key_test14.keys',key_test14.keys)
    trialstest14.addData('key_test14.corr', key_test14.corr)
    if key_test14.keys != None:  # we had a response
        trialstest14.addData('key_test14.rt', key_test14.rt)
    trialstest14.addData('key_test14.started', key_test14.tStartRefresh)
    trialstest14.addData('key_test14.stopped', key_test14.tStopRefresh)
    # the Routine "testTrial14" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest14"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test14.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_27.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest14Components = [text_27]
    for thisComponent in feedbackTest14Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest14Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest14"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest14Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest14Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_27* updates
        if text_27.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_27.frameNStart = frameN  # exact frame index
            text_27.tStart = t  # local t and not account for scr refresh
            text_27.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_27, 'tStartRefresh')  # time at next scr refresh
            text_27.setAutoDraw(True)
        if text_27.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_27.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_27.tStop = t  # not accounting for scr refresh
                text_27.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_27, 'tStopRefresh')  # time at next scr refresh
                text_27.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest14Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest14"-------
    for thisComponent in feedbackTest14Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest14.addData('text_27.started', text_27.tStartRefresh)
    trialstest14.addData('text_27.stopped', text_27.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest14'


# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_5.keys = []
key_resp_5.rt = []
_key_resp_5_allKeys = []
# keep track of which components have finished
learnInstructionsComponents = [text_6, key_resp_5]
for thisComponent in learnInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnInstructions"-------
while continueRoutine:
    # get current time
    t = learnInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *key_resp_5* updates
    waitOnFlip = False
    if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_5.frameNStart = frameN  # exact frame index
        key_resp_5.tStart = t  # local t and not account for scr refresh
        key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_5.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_5_allKeys.extend(theseKeys)
        if len(_key_resp_5_allKeys):
            key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
            key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnInstructions"-------
for thisComponent in learnInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys = None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "learnInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "learnTask"-------
continueRoutine = True
routineTimer.add(3.000000)
# update component parameters for each repeat
# keep track of which components have finished
learnTaskComponents = [text_7]
for thisComponent in learnTaskComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
learnTaskClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "learnTask"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = learnTaskClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=learnTaskClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    if text_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_7.tStartRefresh + 3-frameTolerance:
            # keep track of stop time/frame for later
            text_7.tStop = t  # not accounting for scr refresh
            text_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
            text_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in learnTaskComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "learnTask"-------
for thisComponent in learnTaskComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)

# set up handler to look after randomisation of conditions etc
trialslearn15 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/correct_sentences_3.xlsx'),
    seed=None, name='trialslearn15')
thisExp.addLoop(trialslearn15)  # add the loop to the experiment
thisTrialslearn15 = trialslearn15.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialslearn15.rgb)
if thisTrialslearn15 != None:
    for paramName in thisTrialslearn15:
        exec('{} = thisTrialslearn15[paramName]'.format(paramName))

for thisTrialslearn15 in trialslearn15:
    currentLoop = trialslearn15
    # abbreviate parameter names if possible (e.g. rgb = thisTrialslearn15.rgb)
    if thisTrialslearn15 != None:
        for paramName in thisTrialslearn15:
            exec('{} = thisTrialslearn15[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "learnTrial_3"-------
    continueRoutine = True
    routineTimer.add(7.000000)
    # update component parameters for each repeat
    text_8.setText(correct_sentences_3)
    # keep track of which components have finished
    learnTrial_3Components = [text_8]
    for thisComponent in learnTrial_3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    learnTrial_3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "learnTrial_3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = learnTrial_3Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=learnTrial_3Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in learnTrial_3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "learnTrial_3"-------
    for thisComponent in learnTrial_3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn15.addData('text_8.started', text_8.tStartRefresh)
    trialslearn15.addData('text_8.stopped', text_8.tStopRefresh)
    
    # ------Prepare to start Routine "pause"-------
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    text_4.setText('+')
    # keep track of which components have finished
    pauseComponents = [text_4]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    pauseClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "pause"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pauseClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=pauseClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 3-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pause"-------
    for thisComponent in pauseComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialslearn15.addData('text_4.started', text_4.tStartRefresh)
    trialslearn15.addData('text_4.stopped', text_4.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialslearn15'


# ------Prepare to start Routine "testInstructions"-------
continueRoutine = True
# update component parameters for each repeat
key_start.keys = []
key_start.rt = []
_key_start_allKeys = []
# keep track of which components have finished
testInstructionsComponents = [text_2, key_start]
for thisComponent in testInstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
testInstructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "testInstructions"-------
while continueRoutine:
    # get current time
    t = testInstructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=testInstructionsClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_start* updates
    waitOnFlip = False
    if key_start.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_start.frameNStart = frameN  # exact frame index
        key_start.tStart = t  # local t and not account for scr refresh
        key_start.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_start, 'tStartRefresh')  # time at next scr refresh
        key_start.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_start.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_start.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_start.status == STARTED and not waitOnFlip:
        theseKeys = key_start.getKeys(keyList=['space'], waitRelease=False)
        _key_start_allKeys.extend(theseKeys)
        if len(_key_start_allKeys):
            key_start.keys = _key_start_allKeys[-1].name  # just the last key pressed
            key_start.rt = _key_start_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in testInstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "testInstructions"-------
for thisComponent in testInstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_start.keys in ['', [], None]:  # No response was made
    key_start.keys = None
thisExp.addData('key_start.keys',key_start.keys)
if key_start.keys != None:  # we had a response
    thisExp.addData('key_start.rt', key_start.rt)
thisExp.addData('key_start.started', key_start.tStartRefresh)
thisExp.addData('key_start.stopped', key_start.tStopRefresh)
thisExp.nextEntry()
# the Routine "testInstructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialstest15 = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('BROCANTO_Treatment/sentences_lists/t_15.xlsx'),
    seed=None, name='trialstest15')
thisExp.addLoop(trialstest15)  # add the loop to the experiment
thisTrialstest15 = trialstest15.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialstest15.rgb)
if thisTrialstest15 != None:
    for paramName in thisTrialstest15:
        exec('{} = thisTrialstest15[paramName]'.format(paramName))

for thisTrialstest15 in trialstest15:
    currentLoop = trialstest15
    # abbreviate parameter names if possible (e.g. rgb = thisTrialstest15.rgb)
    if thisTrialstest15 != None:
        for paramName in thisTrialstest15:
            exec('{} = thisTrialstest15[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "testTrial15"-------
    continueRoutine = True
    # update component parameters for each repeat
    if(correctness == 'correct'):
        leftright_key = 'right'
    if(correctness == 'incorrect'):
        leftright_key = 'left'
    text_sentences15.setText(testblock_15)
    key_test15.keys = []
    key_test15.rt = []
    _key_test15_allKeys = []
    # keep track of which components have finished
    testTrial15Components = [text_sentences15, key_test15]
    for thisComponent in testTrial15Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    testTrial15Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "testTrial15"-------
    while continueRoutine:
        # get current time
        t = testTrial15Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=testTrial15Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_sentences15* updates
        if text_sentences15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_sentences15.frameNStart = frameN  # exact frame index
            text_sentences15.tStart = t  # local t and not account for scr refresh
            text_sentences15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_sentences15, 'tStartRefresh')  # time at next scr refresh
            text_sentences15.setAutoDraw(True)
        if text_sentences15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_sentences15.tStartRefresh + 7-frameTolerance:
                # keep track of stop time/frame for later
                text_sentences15.tStop = t  # not accounting for scr refresh
                text_sentences15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_sentences15, 'tStopRefresh')  # time at next scr refresh
                text_sentences15.setAutoDraw(False)
        
        # *key_test15* updates
        waitOnFlip = False
        if key_test15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_test15.frameNStart = frameN  # exact frame index
            key_test15.tStart = t  # local t and not account for scr refresh
            key_test15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_test15, 'tStartRefresh')  # time at next scr refresh
            key_test15.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_test15.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_test15.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_test15.status == STARTED and not waitOnFlip:
            theseKeys = key_test15.getKeys(keyList=['left', 'right'], waitRelease=False)
            _key_test15_allKeys.extend(theseKeys)
            if len(_key_test15_allKeys):
                key_test15.keys = _key_test15_allKeys[-1].name  # just the last key pressed
                key_test15.rt = _key_test15_allKeys[-1].rt
                # was this correct?
                if (key_test15.keys == str(leftright_key)) or (key_test15.keys == leftright_key):
                    key_test15.corr = 1
                else:
                    key_test15.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in testTrial15Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "testTrial15"-------
    for thisComponent in testTrial15Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest15.addData('text_sentences15.started', text_sentences15.tStartRefresh)
    trialstest15.addData('text_sentences15.stopped', text_sentences15.tStopRefresh)
    # check responses
    if key_test15.keys in ['', [], None]:  # No response was made
        key_test15.keys = None
        # was no response the correct answer?!
        if str(leftright_key).lower() == 'none':
           key_test15.corr = 1;  # correct non-response
        else:
           key_test15.corr = 0;  # failed to respond (incorrectly)
    # store data for trialstest15 (TrialHandler)
    trialstest15.addData('key_test15.keys',key_test15.keys)
    trialstest15.addData('key_test15.corr', key_test15.corr)
    if key_test15.keys != None:  # we had a response
        trialstest15.addData('key_test15.rt', key_test15.rt)
    trialstest15.addData('key_test15.started', key_test15.tStartRefresh)
    trialstest15.addData('key_test15.stopped', key_test15.tStopRefresh)
    # the Routine "testTrial15" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedbackTest15"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if(key_test15.corr == 1):
        feedback_text = "RICHTIG"
    else:
            feedback_text = "FALSCH"
    text_28.setText(feedback_text)
    # keep track of which components have finished
    feedbackTest15Components = [text_28]
    for thisComponent in feedbackTest15Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackTest15Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedbackTest15"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackTest15Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackTest15Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_28* updates
        if text_28.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_28.frameNStart = frameN  # exact frame index
            text_28.tStart = t  # local t and not account for scr refresh
            text_28.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_28, 'tStartRefresh')  # time at next scr refresh
            text_28.setAutoDraw(True)
        if text_28.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_28.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_28.tStop = t  # not accounting for scr refresh
                text_28.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_28, 'tStopRefresh')  # time at next scr refresh
                text_28.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackTest15Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedbackTest15"-------
    for thisComponent in feedbackTest15Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trialstest15.addData('text_28.started', text_28.tStartRefresh)
    trialstest15.addData('text_28.stopped', text_28.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialstest15'


# ------Prepare to start Routine "controlTraining"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_8.keys = []
key_resp_8.rt = []
_key_resp_8_allKeys = []
# keep track of which components have finished
controlTrainingComponents = [rotes_quadrat, key_resp_8]
for thisComponent in controlTrainingComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
controlTrainingClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "controlTraining"-------
while continueRoutine:
    # get current time
    t = controlTrainingClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=controlTrainingClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *rotes_quadrat* updates
    if rotes_quadrat.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        rotes_quadrat.frameNStart = frameN  # exact frame index
        rotes_quadrat.tStart = t  # local t and not account for scr refresh
        rotes_quadrat.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(rotes_quadrat, 'tStartRefresh')  # time at next scr refresh
        rotes_quadrat.setAutoDraw(True)
    if rotes_quadrat.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > rotes_quadrat.tStartRefresh + 1-frameTolerance:
            # keep track of stop time/frame for later
            rotes_quadrat.tStop = t  # not accounting for scr refresh
            rotes_quadrat.frameNStop = frameN  # exact frame index
            win.timeOnFlip(rotes_quadrat, 'tStopRefresh')  # time at next scr refresh
            rotes_quadrat.setAutoDraw(False)
    
    # *key_resp_8* updates
    waitOnFlip = False
    if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_8.frameNStart = frameN  # exact frame index
        key_resp_8.tStart = t  # local t and not account for scr refresh
        key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
        key_resp_8.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_8.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_8.getKeys(keyList=['y', 'space'], waitRelease=False)
        _key_resp_8_allKeys.extend(theseKeys)
        if len(_key_resp_8_allKeys):
            key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
            key_resp_8.rt = _key_resp_8_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in controlTrainingComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "controlTraining"-------
for thisComponent in controlTrainingComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('rotes_quadrat.started', rotes_quadrat.tStartRefresh)
thisExp.addData('rotes_quadrat.stopped', rotes_quadrat.tStopRefresh)
# check responses
if key_resp_8.keys in ['', [], None]:  # No response was made
    key_resp_8.keys = None
thisExp.addData('key_resp_8.keys',key_resp_8.keys)
if key_resp_8.keys != None:  # we had a response
    thisExp.addData('key_resp_8.rt', key_resp_8.rt)
thisExp.addData('key_resp_8.started', key_resp_8.tStartRefresh)
thisExp.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
thisExp.nextEntry()
# the Routine "controlTraining" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "endScreen"-------
continueRoutine = True
# update component parameters for each repeat
key_End.keys = []
key_End.rt = []
_key_End_allKeys = []
# keep track of which components have finished
endScreenComponents = [text, key_End]
for thisComponent in endScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
endScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "endScreen"-------
while continueRoutine:
    # get current time
    t = endScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=endScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_End* updates
    waitOnFlip = False
    if key_End.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_End.frameNStart = frameN  # exact frame index
        key_End.tStart = t  # local t and not account for scr refresh
        key_End.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_End, 'tStartRefresh')  # time at next scr refresh
        key_End.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_End.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_End.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_End.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_End.tStartRefresh + 10-frameTolerance:
            # keep track of stop time/frame for later
            key_End.tStop = t  # not accounting for scr refresh
            key_End.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_End, 'tStopRefresh')  # time at next scr refresh
            key_End.status = FINISHED
    if key_End.status == STARTED and not waitOnFlip:
        theseKeys = key_End.getKeys(keyList=['space'], waitRelease=False)
        _key_End_allKeys.extend(theseKeys)
        if len(_key_End_allKeys):
            key_End.keys = _key_End_allKeys[-1].name  # just the last key pressed
            key_End.rt = _key_End_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in endScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "endScreen"-------
for thisComponent in endScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_End.keys in ['', [], None]:  # No response was made
    key_End.keys = None
thisExp.addData('key_End.keys',key_End.keys)
if key_End.keys != None:  # we had a response
    thisExp.addData('key_End.rt', key_End.rt)
thisExp.addData('key_End.started', key_End.tStartRefresh)
thisExp.addData('key_End.stopped', key_End.tStopRefresh)
thisExp.nextEntry()
# the Routine "endScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
