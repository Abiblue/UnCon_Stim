#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on Thu 28 May 2020 11:57:48 AM +0430
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.5'
expName = 'UnCon-CFS'  # from the Builder filename that created this script
expInfo = {'education': '', 'sex': '', 'age': '', 'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
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
    originPath='/home/abi/Desktop/thesis/UnCon_Stim/UnCon-CFS.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1366, 768], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='pix')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "flash_init"
flash_initClock = core.Clock()
# set_colors()
# Colors used during the experiment.
# Color variables end with _c.
def set_colors():
    global sc_c # screen color
    global f_c # frame color
    global f2_c # frame 2 color
    global sq_c # square color
    global sq_f_c # square color
    global t_c  # text color
    global c_c  # circle color    
    # 1 = white
    # -0.06 = grey 80
    # -0.37 = grey 120
    # -1 = black
    sc_c = [.002, .002, .002]
    f_c = [-1,-1,-1]
    f2_c = [1,1,1]
    sq_c = [.002, .002, .002]
    sq_f_c = [.002, .002, .002]
    t_c = [1,1,1]
    c_c = 'red'
# set_sizes()
# Sizes used during the experiment
# Size variables end with _s.
def set_sizes():
    global f_s # frame size (square) (frame surrounding the stimulus)
    global f2_s # frame 2 size (square) (frame surrounding the stimulus)
    global sq_s # square size (square where the stimulus is shown)
    global sq_f_s # square size (square underneath is shown)
    global l_s # line size (the width of the line surrounding the stimulus)
    global fix_s  # size of fixation crosses on top of stimuli
    global pic_s  # size of the face (useful when showing smaller face above/below fixation cross)
    f_s = 340
    f2_s = 320
    sq_s = 300
    sq_f_s = 300
    l_s = 20
    fix_s = 70
    pic_s = sq_s/2

# set_positions()
# Positions used during the experiment
# Position variables end with _p.
def set_positions():
  global s_p # position of the text and image stimuli (left or right according experiment settings).
  global f_p # position of the flash stimulus (right or left according experiment settings).
  global txt_above_f_p # position of the reminder for the button for above.
  global txt_below_f_p # position of the reminder for the button for below.
  global txt_above_s_p # position of the reminder for the button for above.
  global txt_below_s_p # position of the reminder for the button for below.
  global line_left_start  # start position of vertical lines sticking out of frame
  global line_left_end
  global line_right_start  
  global line_right_end  
  offset = 0 # To displace the center from the real center.
                  # Positive offset approach to the screen center
                  # while negative offset move away the screen center.
  center_l = offset - win.size[0]/4 # center of left part of the screen
  center_r = -center_l # center of right part of the screen
  s_p = [center_r, 0]
  f_p = [center_l, 0]
  txt_above_f_p = [center_l+50, -250]
  txt_below_f_p = [center_l-50, -250]
  txt_above_s_p = [center_r+50, -250]
  txt_below_s_p = [center_r-50, -250]
  line_left_start = (- f_s/2 - 50, 0)
  line_left_end =  ( - f_s/2, 0)
  line_right_start = (+ f_s/2, 0) 
  line_right_end = ( + f_s/2 + 50, 0) 
    

# define timings
def jittery():
    global before_t # The duration (in frames) before the stimulus presentation
    global fade_i_t # The duration (in frames) of the fade in of stimulus
    global inside_t # The duration (in frames) of a stimulus presentation beetwen fade in and out
    global fade_o_t # The duration (in frames) of the fade out of stimulus
    global after_t # The duration (in frames) after stimulus presentation
    global stim_t # The duration (in frames) of the stimulus (in + inside + out)
    global total_t # The duration (in frames) of a stimulus presentation (before + stimulus + after)
    global fade_i_end_t # The frame end of the fade in
    global fade_o_beg_t # The frame end of the inside
    global fade_o_end_t # The frame end of the fade out
    
    global before_t_f # The duration (in frames) before the stimulus presentation
    global fade_i_t_f # The duration (in frames) of the fade in of stimulus
    global inside_t_f # The duration (in frames) of a stimulus presentation beetwen fade in and out
    global fade_o_t_f # The duration (in frames) of the fade out of stimulus
    global after_t_f # The duration (in frames) after stimulus presentation
    global stim_t_f # The duration (in frames) of the stimulus (in + inside + out)
    global total_t_f # The duration (in frames) of a stimulus presentation (before + stimulus + after)
    global fade_i_end_t_f # The frame end of the fade in
    global fade_o_beg_t_f # The frame end of the inside
    global fade_o_end_t_f # The frame end of the fade out    
    
    global f_t # The duration (in frames) of a flash image presentation
    f_t = 6
    fps = 60 # frames per second
    
#    before_t = x * fps # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    
    # TIMES FOR OPACITY OF FACE 
    before_t = 0 * fps
    fade_i_t = 1 * fps
    inside_t = 8 * fps
    fade_o_t = 0 * fps
    after_t = 0 * fps
    stim_t  = fade_i_t + inside_t + fade_o_t  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    total_t  = before_t + stim_t + after_t  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    fade_i_end_t = before_t + fade_i_t   # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    fade_o_beg_t = fade_i_end_t + inside_t  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    fade_o_end_t = before_t + stim_t  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    
    
#    # TIMES FOR OPACITY OF FLASHES
#    before_t_f = 0 * fps
#    fade_i_t_f = 0 * fps
#    inside_t_f = 1 * fps
#    fade_o_t_f = 7 * fps
#    after_t_f = 0 * fps
#    stim_t_f  = fade_i_t_f + inside_t_f + fade_o_t_f  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
#    total_t_f  = before_t_f + stim_t_f + after_t_f  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
#    fade_i_end_t_f = before_t_f + fade_i_t_f   # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
#    fade_o_beg_t_f = fade_i_end_t_f + inside_t_f  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
#    fade_o_end_t_f = before_t_f + stim_t_f  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    #f_t = 6
    
    # TIMES FOR OPACITY OF FRAME BEHIND FLASHES
    before_t_f = 2 * fps
    fade_i_t_f = 7 * fps
    inside_t_f = 0 * fps
    fade_o_t_f = 0 * fps
    after_t_f = 0 * fps
    stim_t_f  = fade_i_t_f + inside_t_f + fade_o_t_f  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    total_t_f  = before_t_f + stim_t_f + after_t_f  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    fade_i_end_t_f = before_t_f + fade_i_t_f   # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    fade_o_beg_t_f = fade_i_end_t_f + inside_t_f  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER
    fade_o_end_t_f = before_t_f + stim_t_f  # ATTENTION, THIS ONE NEEDS TO CHANGE AT EACH TRIAL FOR FIXATION CROSS JITTER

# flash stimulus functions
# flash initialization
def flash_init(win, position=[0,0], square_size=10, columns=10, rows=10):
    global flash # The flash stimulus (an array of flashing squares)
    sqsp=30
    red = [1, -1, -1]
    green = [-1, 1, -1]
    blue = [-1, -1, 1]
    yellow = [1, 0.97, -0.55]
    pink = [1, 0.6, 0.6]
    color_set = [red, green, blue, yellow, pink]
    cell_number = columns * rows
    by_color = int(np.floor(float(cell_number)/len(color_set)))     # np.floor returns the next biggest integer (e.g. np.floor of 2.5 is 2)
    # fill an array with colors. Each color should appear approximatively the same number of times.
    f_colors = []
    for c in color_set:
        for i in range(by_color):
            f_colors.append(c)
    shuffle(color_set)
    i = cell_number - len(f_colors)
    while i > 0:
        f_colors.append(color_set[i])
        i -= 1
    # randomize color order.
    shuffle(f_colors)
    # fill an array with coordinate for each color square. First square should be at the upper left
    # and next should follow from left to right and up to down.
    xys = []
    x_left = (1 - columns) * sqsp / 2
    y_top = (1 - rows) * sqsp / 2
    #for i in range(1,5):
    for l in range(rows):
        for c in range(columns):
            r1=(random()-0.5)*sqsp #ariel
            r2=(random()-0.5)*sqsp
            xys.append((x_left+r1 + c * sqsp, y_top+r2 + l * sqsp))
    flash = visual.ElementArrayStim(win=win,
                        fieldPos=position,
                        fieldShape='sqr',
                        nElements=cell_number,
                        sizes=square_size,
                        xys=xys,
                        colors=f_colors,
                        elementTex=None,
                        elementMask=None,
                        name='flash',
                        autoLog=False)
    #print dir(flash)

def flash_s_init(win, position=[0,0], square_size=10, columns=10, rows=10):
    global flash_s
    sqsp=30
    red = [1, -1, -1]
    green = [-1, 1, -1]
    blue = [-1, -1, 1]
    yellow = [1, 0.97, -0.55]
    pink = [1, 0.6, 0.6]
    color_set = [red, green, blue, yellow, pink]
    cell_number = columns * rows
    by_color = int(np.floor(float(cell_number)/len(color_set)))     # np.floor returns the next biggest integer (e.g. np.floor of 2.5 is 2)
    # fill an array with colors. Each color should appear approximatively the same number of times.
    f_colors = []
    for c in color_set:
        for i in range(by_color):
            f_colors.append(c)
    shuffle(color_set)
    i = cell_number - len(f_colors)
    while i > 0:
        f_colors.append(color_set[i])
        i -= 1
    # randomize color order.
    shuffle(f_colors)
    # fill an array with coordinate for each color square. First square should be at the upper left
    # and next should follow from left to right and up to down.
    xys = []
    x_left = (1 - columns) * sqsp / 2
    y_top = (1 - rows) * sqsp / 2
    #for i in range(1,5):
    for l in range(rows):
        for c in range(columns):
            r1=(random()-0.5)*sqsp #ariel
            r2=(random()-0.5)*sqsp
            xys.append((x_left+r1 + c * sqsp, y_top+r2 + l * sqsp))
    flash_s = visual.ElementArrayStim(win=win,
                        fieldPos=position,
                        fieldShape='sqr',
                        nElements=cell_number,
                        sizes=square_size,
                        xys=xys,
                        colors=f_colors,
                        elementTex=None,
                        elementMask=None,
                        name='flash',
                        autoLog=False)

# flash stimulus change
def flash_change():
    global flash
    global flash_s
    square_size=30
    columns=10
    rows=10
    shuffle(flash.colors)
    flash.setColors(flash.colors)
    flash_s.setColors(flash.colors)
    x_left = (1 - columns) * square_size / 2
    y_top = (1 - rows) * square_size / 2
    xys=[]
    for l in range(rows):
        for c in range(columns):
            r1=(random()-0.5)*30 #ariel
            r2=(random()-0.5)*30
            xys.append((x_left+r1 + c * square_size, y_top+r2 + l * square_size))

    flash.setXYs(xys)
    flash_s.setXYs(xys)

    #a=flash.setXY
    
# initiate colors
set_colors()
set_sizes()
set_positions()
jittery()
flash_init(win, f_p, square_size=50, columns=10, rows=10)
flash_s_init(win, s_p, square_size=50, columns=10, rows=10)

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
text_instruction1_f = visual.TextStim(win=win, name='text_instruction1_f',
    text='درود؛\nبه این آزمون خوش\u200cآمدید.',
    font='Nazli',
    pos=(f_p[0], 0), height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
text_instruction1_s = visual.TextStim(win=win, name='text_instruction1_s',
    text='درود؛\nبه این آزمون خوش\u200cآمدید.',
    font='Nazli',
    pos=[s_p[0], 0], height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-1.0);
text_instruction2_f = visual.TextStim(win=win, name='text_instruction2_f',
    text='در هر مرحله به شما یک پیام نشان\u200cداده خواهد شد.\nباتوجه به میزان اهمیت پیام برای شما، \nتصمیم بگیرد که اگر در این پیام را در یک\nشبکه\u200cی اجتماعی مشاهده می\u200cکردید\nچه واکنشی نشان می\u200cدادید؟\n',
    font='Nazli',
    pos=(f_p[0], 0), height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-2.0);
text_instruction2_s = visual.TextStim(win=win, name='text_instruction2_s',
    text='در هر مرحله به شما یک پیام نشان\u200cداده خواهد شد.\nباتوجه به میزان اهمیت پیام برای شما، \nتصمیم بگیرد که اگر در این پیام را در یک\nشبکه\u200cی اجتماعی مشاهده می\u200cکردید\nچه واکنشی نشان می\u200cدادید؟\n',
    font='Nazli',
    pos=(s_p[0], 0), height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-3.0);

# Initialize components for Routine "calibration"
calibrationClock = core.Clock()
triangle_s_sq = visual.ShapeStim(
    win=win, name='triangle_s_sq',units='pix', 
    vertices=[[-(sq_s,sq_s)[0]/2.0,-(sq_s,sq_s)[1]/2.0], [+(sq_s,sq_s)[0]/2.0,-(sq_s,sq_s)[1]/2.0], [0,(sq_s,sq_s)[1]/2.0]],
    ori=0, pos=s_p,
    lineWidth=10, lineColor=c_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
frame_f_sq = visual.Rect(
    win=win, name='frame_f_sq',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
frame2_f_sq = visual.Rect(
    win=win, name='frame2_f_sq',units='pix', 
    width=(f2_s,f2_s)[0], height=(f2_s,f2_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
square_f_sq1 = visual.Rect(
    win=win, name='square_f_sq1',units='pix', 
    width=(sq_s,sq_s)[0], height=(sq_s,sq_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "SmileOrFrown"
SmileOrFrownClock = core.Clock()
frame_s_instblock = visual.Rect(
    win=win, name='frame_s_instblock',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
frame2_s_instblock = visual.Rect(
    win=win, name='frame2_s_instblock',units='pix', 
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
square_s_instblock = visual.Rect(
    win=win, name='square_s_instblock',units='pix', 
    width=(sq_s, sq_s)[0], height=(sq_s, sq_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
frame_f_instblock = visual.Rect(
    win=win, name='frame_f_instblock',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
frame2_f_instblock = visual.Rect(
    win=win, name='frame2_f_instblock',units='pix', 
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
square_f_instblock = visual.Rect(
    win=win, name='square_f_instblock',units='pix', 
    width=(sq_s, sq_s)[0], height=(sq_s, sq_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
textinstrblock_f = visual.TextStim(win=win, name='textinstrblock_f',
    text=None,
    font='Arial',
    pos=f_p, height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
textinstrblock_s = visual.TextStim(win=win, name='textinstrblock_s',
    text=None,
    font='Arial',
    pos=s_p, height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
button_above_f = visual.TextStim(win=win, name='button_above_f',
    text='+',
    font='Arial',
    pos=txt_above_f_p, height=fix_s, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
button_below_f = visual.TextStim(win=win, name='button_below_f',
    text='+',
    font='Arial',
    pos=txt_below_f_p, height=fix_s, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
button_above_s = visual.TextStim(win=win, name='button_above_s',
    text='+',
    font='Arial',
    pos=txt_above_s_p, height=fix_s, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
button_below_s = visual.TextStim(win=win, name='button_below_s',
    text='+',
    font='Arial',
    pos=txt_below_s_p, height=fix_s, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "pause"
pauseClock = core.Clock()
text_pause_f = visual.TextStim(win=win, name='text_pause_f',
    text='می\u200cتوانید استراحت کنید. \nبرای شروع کلید space را فشار دهید.',
    font='Nazli',
    pos=[f_p[0], 0], height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
text_pause_s = visual.TextStim(win=win, name='text_pause_s',
    text='می\u200cتوانید استراحت کنید. \nبرای شروع کلید space را فشار دهید.',
    font='Nazli',
    pos=[s_p[0], 0], height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-1.0);

# Initialize components for Routine "Relax"
RelaxClock = core.Clock()
frame_s_relax = visual.Rect(
    win=win, name='frame_s_relax',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
frame2_s_relax = visual.Rect(
    win=win, name='frame2_s_relax',units='pix', 
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
square_s_relax = visual.Rect(
    win=win, name='square_s_relax',units='pix', 
    width=(sq_s, sq_s)[0], height=(sq_s, sq_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
frame_f_relax = visual.Rect(
    win=win, name='frame_f_relax',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
frame2_f_relax = visual.Rect(
    win=win, name='frame2_f_relax',units='pix', 
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
square_f_relax = visual.Rect(
    win=win, name='square_f_relax',units='pix', 
    width=(sq_s, sq_s)[0], height=(sq_s, sq_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
textrelax_f = visual.TextStim(win=win, name='textrelax_f',
    text='RELAX',
    font='Arial',
    pos=f_p, height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
textrelax_s = visual.TextStim(win=win, name='textrelax_s',
    text='RELAX',
    font='Arial',
    pos=s_p, height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "trial"
trialClock = core.Clock()
line_left_s_i = visual.Line(
    win=win, name='line_left_s_i',units='pix', 
    start=(-(line_left_start + line_left_end)[0]/2.0, 0), end=(+(line_left_start + line_left_end)[0]/2.0, 0),
    ori=0, pos=s_p,
    lineWidth=10, lineColor=f_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
line_right_s_i = visual.Line(
    win=win, name='line_right_s_i',units='pix', 
    start=(-(line_right_start + line_right_end)[0]/2.0, 0), end=(+(line_right_start + line_right_end)[0]/2.0, 0),
    ori=0, pos=s_p,
    lineWidth=10, lineColor=f_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
line_above_s_i = visual.Line(
    win=win, name='line_above_s_i',units='pix', 
    start=(-(line_left_start + line_left_end)[0]/2.0, 0), end=(+(line_left_start + line_left_end)[0]/2.0, 0),
    ori=90, pos=s_p,
    lineWidth=10, lineColor=f_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
line_below_s_i = visual.Line(
    win=win, name='line_below_s_i',units='pix', 
    start=(-(line_right_start + line_right_end)[0]/2.0, 0), end=(+(line_right_start + line_right_end)[0]/2.0, 0),
    ori=90, pos=s_p,
    lineWidth=10, lineColor=f_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
line_left_f_i = visual.Line(
    win=win, name='line_left_f_i',units='pix', 
    start=(-(line_left_start + line_left_end)[0]/2.0, 0), end=(+(line_left_start + line_left_end)[0]/2.0, 0),
    ori=0, pos=f_p,
    lineWidth=10, lineColor=f_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
line_right_f_i = visual.Line(
    win=win, name='line_right_f_i',units='pix', 
    start=(-(line_right_start + line_right_end)[0]/2.0, 0), end=(+(line_right_start + line_right_end)[0]/2.0, 0),
    ori=0, pos=f_p,
    lineWidth=10, lineColor=f_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
line_above_f_i = visual.Line(
    win=win, name='line_above_f_i',units='pix', 
    start=(-(line_left_start + line_left_end)[0]/2.0, 0), end=(+(line_left_start + line_left_end)[0]/2.0, 0),
    ori=90, pos=f_p,
    lineWidth=10, lineColor=f_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
line_below_f_i = visual.Line(
    win=win, name='line_below_f_i',units='pix', 
    start=(-(line_right_start + line_right_end)[0]/2.0, 0), end=(+(line_right_start + line_right_end)[0]/2.0, 0),
    ori=90, pos=f_p,
    lineWidth=10, lineColor=f_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
frame_s_i = visual.Rect(
    win=win, name='frame_s_i',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
frame2_s_i = visual.Rect(
    win=win, name='frame2_s_i',units='pix', 
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
square_s_i = visual.Rect(
    win=win, name='square_s_i',units='pix', 
    width=(sq_s, sq_s)[0], height=(sq_s, sq_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-10.0, interpolate=True)
frame_f_i = visual.Rect(
    win=win, name='frame_f_i',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=-11.0, interpolate=True)
frame2_f_i = visual.Rect(
    win=win, name='frame2_f_i',units='pix', 
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-12.0, interpolate=True)
square_f_sq = visual.Rect(
    win=win, name='square_f_sq',units='pix', 
    width=(sq_s,sq_s)[0], height=(sq_s,sq_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-13.0, interpolate=True)
image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=s_p, size=pic_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)

fix_cross_stim_side = visual.TextStim(win=win, name='fix_cross_stim_side',
    text='+',
    font='Arial',
    pos=s_p, height=fix_s, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-16.0);
fix_cross_flash_side = visual.TextStim(win=win, name='fix_cross_flash_side',
    text='+',
    font='Arial',
    pos=f_p, height=fix_s, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-17.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText_f = visual.TextStim(win=win, name='thanksText_f',
    text='پایان آزمون.\nبا سپاس از شما',
    font='Nazli',
    pos=f_p, height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
thanksText_s = visual.TextStim(win=win, name='thanksText_s',
    text='پایان آزمون.\nبا سپاس از شما',
    font='Nazli',
    pos=s_p, height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "flash_init"-------
t = 0
flash_initClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat






# keep track of which components have finished
flash_initComponents = []
for thisComponent in flash_initComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "flash_init"-------
while continueRoutine:
    # get current time
    t = flash_initClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    
    
    
    
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in flash_initComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "flash_init"-------
for thisComponent in flash_initComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)






# the Routine "flash_init" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_instruction = event.BuilderKeyResponse()
# keep track of which components have finished
InstructionsComponents = [text_instruction1_f, text_instruction1_s, text_instruction2_f, text_instruction2_s, key_resp_instruction]
for thisComponent in InstructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "Instructions"-------
while continueRoutine:
    # get current time
    t = InstructionsClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_instruction1_f* updates
    if t >= 0.0 and text_instruction1_f.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instruction1_f.tStart = t  # not accounting for scr refresh
        text_instruction1_f.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_instruction1_f, 'tStartRefresh')  # time at next scr refresh
        text_instruction1_f.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_instruction1_f.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_instruction1_f.tStop = t  # not accounting for scr refresh
        text_instruction1_f.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_instruction1_f, 'tStopRefresh')  # time at next scr refresh
        text_instruction1_f.setAutoDraw(False)
    
    # *text_instruction1_s* updates
    if t >= 0.0 and text_instruction1_s.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instruction1_s.tStart = t  # not accounting for scr refresh
        text_instruction1_s.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_instruction1_s, 'tStartRefresh')  # time at next scr refresh
        text_instruction1_s.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text_instruction1_s.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text_instruction1_s.tStop = t  # not accounting for scr refresh
        text_instruction1_s.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text_instruction1_s, 'tStopRefresh')  # time at next scr refresh
        text_instruction1_s.setAutoDraw(False)
    
    # *text_instruction2_f* updates
    if t >= 1 and text_instruction2_f.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instruction2_f.tStart = t  # not accounting for scr refresh
        text_instruction2_f.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_instruction2_f, 'tStartRefresh')  # time at next scr refresh
        text_instruction2_f.setAutoDraw(True)
    
    # *text_instruction2_s* updates
    if t >= 1 and text_instruction2_s.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_instruction2_s.tStart = t  # not accounting for scr refresh
        text_instruction2_s.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text_instruction2_s, 'tStartRefresh')  # time at next scr refresh
        text_instruction2_s.setAutoDraw(True)
    
    # *key_resp_instruction* updates
    if t >= 1 and key_resp_instruction.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_instruction.tStart = t  # not accounting for scr refresh
        key_resp_instruction.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_instruction, 'tStartRefresh')  # time at next scr refresh
        key_resp_instruction.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if key_resp_instruction.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in InstructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "Instructions"-------
for thisComponent in InstructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_instruction1_f.started', text_instruction1_f.tStartRefresh)
thisExp.addData('text_instruction1_f.stopped', text_instruction1_f.tStopRefresh)
thisExp.addData('text_instruction1_s.started', text_instruction1_s.tStartRefresh)
thisExp.addData('text_instruction1_s.stopped', text_instruction1_s.tStopRefresh)
thisExp.addData('text_instruction2_f.started', text_instruction2_f.tStartRefresh)
thisExp.addData('text_instruction2_f.stopped', text_instruction2_f.tStopRefresh)
thisExp.addData('text_instruction2_s.started', text_instruction2_s.tStartRefresh)
thisExp.addData('text_instruction2_s.stopped', text_instruction2_s.tStopRefresh)
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "calibration"-------
t = 0
calibrationClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_5 = event.BuilderKeyResponse()
# keep track of which components have finished
calibrationComponents = [triangle_s_sq, frame_f_sq, frame2_f_sq, square_f_sq1, key_resp_5]
for thisComponent in calibrationComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "calibration"-------
while continueRoutine:
    # get current time
    t = calibrationClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *triangle_s_sq* updates
    if t >= 0.0 and triangle_s_sq.status == NOT_STARTED:
        # keep track of start time/frame for later
        triangle_s_sq.tStart = t  # not accounting for scr refresh
        triangle_s_sq.frameNStart = frameN  # exact frame index
        win.timeOnFlip(triangle_s_sq, 'tStartRefresh')  # time at next scr refresh
        triangle_s_sq.setAutoDraw(True)
    
    # *frame_f_sq* updates
    if t >= 0.0 and frame_f_sq.status == NOT_STARTED:
        # keep track of start time/frame for later
        frame_f_sq.tStart = t  # not accounting for scr refresh
        frame_f_sq.frameNStart = frameN  # exact frame index
        win.timeOnFlip(frame_f_sq, 'tStartRefresh')  # time at next scr refresh
        frame_f_sq.setAutoDraw(True)
    
    # *frame2_f_sq* updates
    if t >= 0.0 and frame2_f_sq.status == NOT_STARTED:
        # keep track of start time/frame for later
        frame2_f_sq.tStart = t  # not accounting for scr refresh
        frame2_f_sq.frameNStart = frameN  # exact frame index
        win.timeOnFlip(frame2_f_sq, 'tStartRefresh')  # time at next scr refresh
        frame2_f_sq.setAutoDraw(True)
    
    # *square_f_sq1* updates
    if t >= 0.0 and square_f_sq1.status == NOT_STARTED:
        # keep track of start time/frame for later
        square_f_sq1.tStart = t  # not accounting for scr refresh
        square_f_sq1.frameNStart = frameN  # exact frame index
        win.timeOnFlip(square_f_sq1, 'tStartRefresh')  # time at next scr refresh
        square_f_sq1.setAutoDraw(True)
    
    # *key_resp_5* updates
    if t >= 0.0 and key_resp_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_5.tStart = t  # not accounting for scr refresh
        key_resp_5.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
        key_resp_5.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_5.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_5.keys = theseKeys[-1]  # just the last key pressed
            key_resp_5.rt = key_resp_5.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in calibrationComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "calibration"-------
for thisComponent in calibrationComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('triangle_s_sq.started', triangle_s_sq.tStartRefresh)
thisExp.addData('triangle_s_sq.stopped', triangle_s_sq.tStopRefresh)
thisExp.addData('frame_f_sq.started', frame_f_sq.tStartRefresh)
thisExp.addData('frame_f_sq.stopped', frame_f_sq.tStopRefresh)
thisExp.addData('frame2_f_sq.started', frame2_f_sq.tStartRefresh)
thisExp.addData('frame2_f_sq.stopped', frame2_f_sq.tStopRefresh)
thisExp.addData('square_f_sq1.started', square_f_sq1.tStartRefresh)
thisExp.addData('square_f_sq1.stopped', square_f_sq1.tStopRefresh)
# check responses
if key_resp_5.keys in ['', [], None]:  # No response was made
    key_resp_5.keys=None
thisExp.addData('key_resp_5.keys',key_resp_5.keys)
if key_resp_5.keys != None:  # we had a response
    thisExp.addData('key_resp_5.rt', key_resp_5.rt)
thisExp.addData('key_resp_5.started', key_resp_5.tStartRefresh)
thisExp.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
thisExp.nextEntry()
# the Routine "calibration" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "SmileOrFrown"-------
t = 0
SmileOrFrownClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_SmileOrFrown = event.BuilderKeyResponse()
# keep track of which components have finished
SmileOrFrownComponents = [frame_s_instblock, frame2_s_instblock, square_s_instblock, frame_f_instblock, frame2_f_instblock, square_f_instblock, textinstrblock_f, textinstrblock_s, button_above_f, button_below_f, button_above_s, button_below_s, key_resp_SmileOrFrown]
for thisComponent in SmileOrFrownComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "SmileOrFrown"-------
while continueRoutine:
    # get current time
    t = SmileOrFrownClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *frame_s_instblock* updates
    if t >= 0.0 and frame_s_instblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        frame_s_instblock.tStart = t  # not accounting for scr refresh
        frame_s_instblock.frameNStart = frameN  # exact frame index
        win.timeOnFlip(frame_s_instblock, 'tStartRefresh')  # time at next scr refresh
        frame_s_instblock.setAutoDraw(True)
    
    # *frame2_s_instblock* updates
    if t >= 0.0 and frame2_s_instblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        frame2_s_instblock.tStart = t  # not accounting for scr refresh
        frame2_s_instblock.frameNStart = frameN  # exact frame index
        win.timeOnFlip(frame2_s_instblock, 'tStartRefresh')  # time at next scr refresh
        frame2_s_instblock.setAutoDraw(True)
    
    # *square_s_instblock* updates
    if t >= 0.0 and square_s_instblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        square_s_instblock.tStart = t  # not accounting for scr refresh
        square_s_instblock.frameNStart = frameN  # exact frame index
        win.timeOnFlip(square_s_instblock, 'tStartRefresh')  # time at next scr refresh
        square_s_instblock.setAutoDraw(True)
    
    # *frame_f_instblock* updates
    if t >= 0.0 and frame_f_instblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        frame_f_instblock.tStart = t  # not accounting for scr refresh
        frame_f_instblock.frameNStart = frameN  # exact frame index
        win.timeOnFlip(frame_f_instblock, 'tStartRefresh')  # time at next scr refresh
        frame_f_instblock.setAutoDraw(True)
    
    # *frame2_f_instblock* updates
    if t >= 0.0 and frame2_f_instblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        frame2_f_instblock.tStart = t  # not accounting for scr refresh
        frame2_f_instblock.frameNStart = frameN  # exact frame index
        win.timeOnFlip(frame2_f_instblock, 'tStartRefresh')  # time at next scr refresh
        frame2_f_instblock.setAutoDraw(True)
    
    # *square_f_instblock* updates
    if t >= 0.0 and square_f_instblock.status == NOT_STARTED:
        # keep track of start time/frame for later
        square_f_instblock.tStart = t  # not accounting for scr refresh
        square_f_instblock.frameNStart = frameN  # exact frame index
        win.timeOnFlip(square_f_instblock, 'tStartRefresh')  # time at next scr refresh
        square_f_instblock.setAutoDraw(True)
    
    # *textinstrblock_f* updates
    if t >= 0.0 and textinstrblock_f.status == NOT_STARTED:
        # keep track of start time/frame for later
        textinstrblock_f.tStart = t  # not accounting for scr refresh
        textinstrblock_f.frameNStart = frameN  # exact frame index
        win.timeOnFlip(textinstrblock_f, 'tStartRefresh')  # time at next scr refresh
        textinstrblock_f.setAutoDraw(True)
    
    # *textinstrblock_s* updates
    if t >= 0.0 and textinstrblock_s.status == NOT_STARTED:
        # keep track of start time/frame for later
        textinstrblock_s.tStart = t  # not accounting for scr refresh
        textinstrblock_s.frameNStart = frameN  # exact frame index
        win.timeOnFlip(textinstrblock_s, 'tStartRefresh')  # time at next scr refresh
        textinstrblock_s.setAutoDraw(True)
    
    # *button_above_f* updates
    if t >= 0.0 and button_above_f.status == NOT_STARTED:
        # keep track of start time/frame for later
        button_above_f.tStart = t  # not accounting for scr refresh
        button_above_f.frameNStart = frameN  # exact frame index
        win.timeOnFlip(button_above_f, 'tStartRefresh')  # time at next scr refresh
        button_above_f.setAutoDraw(True)
    
    # *button_below_f* updates
    if t >= 0.0 and button_below_f.status == NOT_STARTED:
        # keep track of start time/frame for later
        button_below_f.tStart = t  # not accounting for scr refresh
        button_below_f.frameNStart = frameN  # exact frame index
        win.timeOnFlip(button_below_f, 'tStartRefresh')  # time at next scr refresh
        button_below_f.setAutoDraw(True)
    
    # *button_above_s* updates
    if t >= 0.0 and button_above_s.status == NOT_STARTED:
        # keep track of start time/frame for later
        button_above_s.tStart = t  # not accounting for scr refresh
        button_above_s.frameNStart = frameN  # exact frame index
        win.timeOnFlip(button_above_s, 'tStartRefresh')  # time at next scr refresh
        button_above_s.setAutoDraw(True)
    
    # *button_below_s* updates
    if t >= 0.0 and button_below_s.status == NOT_STARTED:
        # keep track of start time/frame for later
        button_below_s.tStart = t  # not accounting for scr refresh
        button_below_s.frameNStart = frameN  # exact frame index
        win.timeOnFlip(button_below_s, 'tStartRefresh')  # time at next scr refresh
        button_below_s.setAutoDraw(True)
    
    # *key_resp_SmileOrFrown* updates
    if t >= 0.0 and key_resp_SmileOrFrown.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_SmileOrFrown.tStart = t  # not accounting for scr refresh
        key_resp_SmileOrFrown.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_SmileOrFrown, 'tStartRefresh')  # time at next scr refresh
        key_resp_SmileOrFrown.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_SmileOrFrown.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_SmileOrFrown.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_SmileOrFrown.keys = theseKeys[-1]  # just the last key pressed
            key_resp_SmileOrFrown.rt = key_resp_SmileOrFrown.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in SmileOrFrownComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "SmileOrFrown"-------
for thisComponent in SmileOrFrownComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('frame_s_instblock.started', frame_s_instblock.tStartRefresh)
thisExp.addData('frame_s_instblock.stopped', frame_s_instblock.tStopRefresh)
thisExp.addData('frame2_s_instblock.started', frame2_s_instblock.tStartRefresh)
thisExp.addData('frame2_s_instblock.stopped', frame2_s_instblock.tStopRefresh)
thisExp.addData('square_s_instblock.started', square_s_instblock.tStartRefresh)
thisExp.addData('square_s_instblock.stopped', square_s_instblock.tStopRefresh)
thisExp.addData('frame_f_instblock.started', frame_f_instblock.tStartRefresh)
thisExp.addData('frame_f_instblock.stopped', frame_f_instblock.tStopRefresh)
thisExp.addData('frame2_f_instblock.started', frame2_f_instblock.tStartRefresh)
thisExp.addData('frame2_f_instblock.stopped', frame2_f_instblock.tStopRefresh)
thisExp.addData('square_f_instblock.started', square_f_instblock.tStartRefresh)
thisExp.addData('square_f_instblock.stopped', square_f_instblock.tStopRefresh)
thisExp.addData('textinstrblock_f.started', textinstrblock_f.tStartRefresh)
thisExp.addData('textinstrblock_f.stopped', textinstrblock_f.tStopRefresh)
thisExp.addData('textinstrblock_s.started', textinstrblock_s.tStartRefresh)
thisExp.addData('textinstrblock_s.stopped', textinstrblock_s.tStopRefresh)
thisExp.addData('button_above_f.started', button_above_f.tStartRefresh)
thisExp.addData('button_above_f.stopped', button_above_f.tStopRefresh)
thisExp.addData('button_below_f.started', button_below_f.tStartRefresh)
thisExp.addData('button_below_f.stopped', button_below_f.tStopRefresh)
thisExp.addData('button_above_s.started', button_above_s.tStartRefresh)
thisExp.addData('button_above_s.stopped', button_above_s.tStopRefresh)
thisExp.addData('button_below_s.started', button_below_s.tStartRefresh)
thisExp.addData('button_below_s.stopped', button_below_s.tStopRefresh)
# check responses
if key_resp_SmileOrFrown.keys in ['', [], None]:  # No response was made
    key_resp_SmileOrFrown.keys=None
thisExp.addData('key_resp_SmileOrFrown.keys',key_resp_SmileOrFrown.keys)
if key_resp_SmileOrFrown.keys != None:  # we had a response
    thisExp.addData('key_resp_SmileOrFrown.rt', key_resp_SmileOrFrown.rt)
thisExp.addData('key_resp_SmileOrFrown.started', key_resp_SmileOrFrown.tStartRefresh)
thisExp.addData('key_resp_SmileOrFrown.stopped', key_resp_SmileOrFrown.tStopRefresh)
thisExp.nextEntry()
# the Routine "SmileOrFrown" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ImageConditions.xlsx'),
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
    
    # ------Prepare to start Routine "pause"-------
    t = 0
    pauseClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_pause = event.BuilderKeyResponse()
    # keep track of which components have finished
    pauseComponents = [text_pause_f, text_pause_s, key_resp_pause]
    for thisComponent in pauseComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pause"-------
    while continueRoutine:
        # get current time
        t = pauseClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_pause_f* updates
        if t >= 0.0 and text_pause_f.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_pause_f.tStart = t  # not accounting for scr refresh
            text_pause_f.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_pause_f, 'tStartRefresh')  # time at next scr refresh
            text_pause_f.setAutoDraw(True)
        
        # *text_pause_s* updates
        if t >= 0.0 and text_pause_s.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_pause_s.tStart = t  # not accounting for scr refresh
            text_pause_s.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_pause_s, 'tStartRefresh')  # time at next scr refresh
            text_pause_s.setAutoDraw(True)
        
        # *key_resp_pause* updates
        if t >= 0.0 and key_resp_pause.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_pause.tStart = t  # not accounting for scr refresh
            key_resp_pause.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_pause, 'tStartRefresh')  # time at next scr refresh
            key_resp_pause.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if key_resp_pause.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    trials_2.addData('text_pause_f.started', text_pause_f.tStartRefresh)
    trials_2.addData('text_pause_f.stopped', text_pause_f.tStopRefresh)
    trials_2.addData('text_pause_s.started', text_pause_s.tStartRefresh)
    trials_2.addData('text_pause_s.stopped', text_pause_s.tStopRefresh)
    # the Routine "pause" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "Relax"-------
    t = 0
    RelaxClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3 = event.BuilderKeyResponse()
    # keep track of which components have finished
    RelaxComponents = [frame_s_relax, frame2_s_relax, square_s_relax, frame_f_relax, frame2_f_relax, square_f_relax, textrelax_f, textrelax_s, key_resp_3]
    for thisComponent in RelaxComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Relax"-------
    while continueRoutine:
        # get current time
        t = RelaxClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *frame_s_relax* updates
        if t >= 0.0 and frame_s_relax.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_s_relax.tStart = t  # not accounting for scr refresh
            frame_s_relax.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame_s_relax, 'tStartRefresh')  # time at next scr refresh
            frame_s_relax.setAutoDraw(True)
        
        # *frame2_s_relax* updates
        if t >= 0.0 and frame2_s_relax.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame2_s_relax.tStart = t  # not accounting for scr refresh
            frame2_s_relax.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame2_s_relax, 'tStartRefresh')  # time at next scr refresh
            frame2_s_relax.setAutoDraw(True)
        
        # *square_s_relax* updates
        if t >= 0.0 and square_s_relax.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_s_relax.tStart = t  # not accounting for scr refresh
            square_s_relax.frameNStart = frameN  # exact frame index
            win.timeOnFlip(square_s_relax, 'tStartRefresh')  # time at next scr refresh
            square_s_relax.setAutoDraw(True)
        
        # *frame_f_relax* updates
        if t >= 0.0 and frame_f_relax.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_f_relax.tStart = t  # not accounting for scr refresh
            frame_f_relax.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame_f_relax, 'tStartRefresh')  # time at next scr refresh
            frame_f_relax.setAutoDraw(True)
        
        # *frame2_f_relax* updates
        if t >= 0.0 and frame2_f_relax.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame2_f_relax.tStart = t  # not accounting for scr refresh
            frame2_f_relax.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame2_f_relax, 'tStartRefresh')  # time at next scr refresh
            frame2_f_relax.setAutoDraw(True)
        
        # *square_f_relax* updates
        if t >= 0.0 and square_f_relax.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_f_relax.tStart = t  # not accounting for scr refresh
            square_f_relax.frameNStart = frameN  # exact frame index
            win.timeOnFlip(square_f_relax, 'tStartRefresh')  # time at next scr refresh
            square_f_relax.setAutoDraw(True)
        
        # *textrelax_f* updates
        if t >= 0.0 and textrelax_f.status == NOT_STARTED:
            # keep track of start time/frame for later
            textrelax_f.tStart = t  # not accounting for scr refresh
            textrelax_f.frameNStart = frameN  # exact frame index
            win.timeOnFlip(textrelax_f, 'tStartRefresh')  # time at next scr refresh
            textrelax_f.setAutoDraw(True)
        
        # *textrelax_s* updates
        if t >= 0.0 and textrelax_s.status == NOT_STARTED:
            # keep track of start time/frame for later
            textrelax_s.tStart = t  # not accounting for scr refresh
            textrelax_s.frameNStart = frameN  # exact frame index
            win.timeOnFlip(textrelax_s, 'tStartRefresh')  # time at next scr refresh
            textrelax_s.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # not accounting for scr refresh
            key_resp_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in RelaxComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Relax"-------
    for thisComponent in RelaxComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('frame_s_relax.started', frame_s_relax.tStartRefresh)
    trials_2.addData('frame_s_relax.stopped', frame_s_relax.tStopRefresh)
    trials_2.addData('frame2_s_relax.started', frame2_s_relax.tStartRefresh)
    trials_2.addData('frame2_s_relax.stopped', frame2_s_relax.tStopRefresh)
    trials_2.addData('square_s_relax.started', square_s_relax.tStartRefresh)
    trials_2.addData('square_s_relax.stopped', square_s_relax.tStopRefresh)
    trials_2.addData('frame_f_relax.started', frame_f_relax.tStartRefresh)
    trials_2.addData('frame_f_relax.stopped', frame_f_relax.tStopRefresh)
    trials_2.addData('frame2_f_relax.started', frame2_f_relax.tStartRefresh)
    trials_2.addData('frame2_f_relax.stopped', frame2_f_relax.tStopRefresh)
    trials_2.addData('square_f_relax.started', square_f_relax.tStartRefresh)
    trials_2.addData('square_f_relax.stopped', square_f_relax.tStopRefresh)
    trials_2.addData('textrelax_f.started', textrelax_f.tStartRefresh)
    trials_2.addData('textrelax_f.stopped', textrelax_f.tStopRefresh)
    trials_2.addData('textrelax_s.started', textrelax_s.tStartRefresh)
    trials_2.addData('textrelax_s.stopped', textrelax_s.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys=None
    trials_2.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_2.addData('key_resp_3.rt', key_resp_3.rt)
    trials_2.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    trials_2.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "Relax" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    image.setImage(Image)
    # flash begin routine
    f_change = 0
    key_resp_image = event.BuilderKeyResponse()
    # keep track of which components have finished
    trialComponents = [line_left_s_i, line_right_s_i, line_above_s_i, line_below_s_i, line_left_f_i, line_right_f_i, line_above_f_i, line_below_f_i, frame_s_i, frame2_s_i, square_s_i, frame_f_i, frame2_f_i, square_f_sq, image, fix_cross_stim_side, fix_cross_flash_side, key_resp_image]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *line_left_s_i* updates
        if t >= 0.0 and line_left_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            line_left_s_i.tStart = t  # not accounting for scr refresh
            line_left_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(line_left_s_i, 'tStartRefresh')  # time at next scr refresh
            line_left_s_i.setAutoDraw(True)
        
        # *line_right_s_i* updates
        if t >= 0.0 and line_right_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            line_right_s_i.tStart = t  # not accounting for scr refresh
            line_right_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(line_right_s_i, 'tStartRefresh')  # time at next scr refresh
            line_right_s_i.setAutoDraw(True)
        
        # *line_above_s_i* updates
        if t >= 0.0 and line_above_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            line_above_s_i.tStart = t  # not accounting for scr refresh
            line_above_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(line_above_s_i, 'tStartRefresh')  # time at next scr refresh
            line_above_s_i.setAutoDraw(True)
        
        # *line_below_s_i* updates
        if t >= 0.0 and line_below_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            line_below_s_i.tStart = t  # not accounting for scr refresh
            line_below_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(line_below_s_i, 'tStartRefresh')  # time at next scr refresh
            line_below_s_i.setAutoDraw(True)
        
        # *line_left_f_i* updates
        if t >= 0.0 and line_left_f_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            line_left_f_i.tStart = t  # not accounting for scr refresh
            line_left_f_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(line_left_f_i, 'tStartRefresh')  # time at next scr refresh
            line_left_f_i.setAutoDraw(True)
        
        # *line_right_f_i* updates
        if t >= 0.0 and line_right_f_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            line_right_f_i.tStart = t  # not accounting for scr refresh
            line_right_f_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(line_right_f_i, 'tStartRefresh')  # time at next scr refresh
            line_right_f_i.setAutoDraw(True)
        
        # *line_above_f_i* updates
        if t >= 0.0 and line_above_f_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            line_above_f_i.tStart = t  # not accounting for scr refresh
            line_above_f_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(line_above_f_i, 'tStartRefresh')  # time at next scr refresh
            line_above_f_i.setAutoDraw(True)
        
        # *line_below_f_i* updates
        if t >= 0.0 and line_below_f_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            line_below_f_i.tStart = t  # not accounting for scr refresh
            line_below_f_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(line_below_f_i, 'tStartRefresh')  # time at next scr refresh
            line_below_f_i.setAutoDraw(True)
        
        # *frame_s_i* updates
        if t >= 0.0 and frame_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_s_i.tStart = t  # not accounting for scr refresh
            frame_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame_s_i, 'tStartRefresh')  # time at next scr refresh
            frame_s_i.setAutoDraw(True)
        
        # *frame2_s_i* updates
        if t >= 0.0 and frame2_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame2_s_i.tStart = t  # not accounting for scr refresh
            frame2_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame2_s_i, 'tStartRefresh')  # time at next scr refresh
            frame2_s_i.setAutoDraw(True)
        
        # *square_s_i* updates
        if t >= 0.0 and square_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_s_i.tStart = t  # not accounting for scr refresh
            square_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(square_s_i, 'tStartRefresh')  # time at next scr refresh
            square_s_i.setAutoDraw(True)
        
        # *frame_f_i* updates
        if t >= 0.0 and frame_f_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_f_i.tStart = t  # not accounting for scr refresh
            frame_f_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame_f_i, 'tStartRefresh')  # time at next scr refresh
            frame_f_i.setAutoDraw(True)
        
        # *frame2_f_i* updates
        if t >= 0.0 and frame2_f_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame2_f_i.tStart = t  # not accounting for scr refresh
            frame2_f_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame2_f_i, 'tStartRefresh')  # time at next scr refresh
            frame2_f_i.setAutoDraw(True)
        
        # *square_f_sq* updates
        if t >= 0.0 and square_f_sq.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_f_sq.tStart = t  # not accounting for scr refresh
            square_f_sq.frameNStart = frameN  # exact frame index
            win.timeOnFlip(square_f_sq, 'tStartRefresh')  # time at next scr refresh
            square_f_sq.setAutoDraw(True)
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # not accounting for scr refresh
            image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        # flash each frame
        if frameN >= f_change:
            flash_change()
            myRand =randint(1,100)
            f_change += f_t
        flash.draw()
        
        # *fix_cross_stim_side* updates
        if t >= 0.0 and fix_cross_stim_side.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix_cross_stim_side.tStart = t  # not accounting for scr refresh
            fix_cross_stim_side.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix_cross_stim_side, 'tStartRefresh')  # time at next scr refresh
            fix_cross_stim_side.setAutoDraw(True)
        
        # *fix_cross_flash_side* updates
        if t >= 0.0 and fix_cross_flash_side.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix_cross_flash_side.tStart = t  # not accounting for scr refresh
            fix_cross_flash_side.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix_cross_flash_side, 'tStartRefresh')  # time at next scr refresh
            fix_cross_flash_side.setAutoDraw(True)
        
        # *key_resp_image* updates
        if t >= 0.0 and key_resp_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_image.tStart = t  # not accounting for scr refresh
            key_resp_image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_image, 'tStartRefresh')  # time at next scr refresh
            key_resp_image.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_image.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_image.status == STARTED:
            theseKeys = event.getKeys(keyList=['l', 'a'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_image.keys = theseKeys[-1]  # just the last key pressed
                key_resp_image.rt = key_resp_image.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('line_left_s_i.started', line_left_s_i.tStartRefresh)
    trials_2.addData('line_left_s_i.stopped', line_left_s_i.tStopRefresh)
    trials_2.addData('line_right_s_i.started', line_right_s_i.tStartRefresh)
    trials_2.addData('line_right_s_i.stopped', line_right_s_i.tStopRefresh)
    trials_2.addData('line_above_s_i.started', line_above_s_i.tStartRefresh)
    trials_2.addData('line_above_s_i.stopped', line_above_s_i.tStopRefresh)
    trials_2.addData('line_below_s_i.started', line_below_s_i.tStartRefresh)
    trials_2.addData('line_below_s_i.stopped', line_below_s_i.tStopRefresh)
    trials_2.addData('line_left_f_i.started', line_left_f_i.tStartRefresh)
    trials_2.addData('line_left_f_i.stopped', line_left_f_i.tStopRefresh)
    trials_2.addData('line_right_f_i.started', line_right_f_i.tStartRefresh)
    trials_2.addData('line_right_f_i.stopped', line_right_f_i.tStopRefresh)
    trials_2.addData('line_above_f_i.started', line_above_f_i.tStartRefresh)
    trials_2.addData('line_above_f_i.stopped', line_above_f_i.tStopRefresh)
    trials_2.addData('line_below_f_i.started', line_below_f_i.tStartRefresh)
    trials_2.addData('line_below_f_i.stopped', line_below_f_i.tStopRefresh)
    trials_2.addData('frame_s_i.started', frame_s_i.tStartRefresh)
    trials_2.addData('frame_s_i.stopped', frame_s_i.tStopRefresh)
    trials_2.addData('frame2_s_i.started', frame2_s_i.tStartRefresh)
    trials_2.addData('frame2_s_i.stopped', frame2_s_i.tStopRefresh)
    trials_2.addData('square_s_i.started', square_s_i.tStartRefresh)
    trials_2.addData('square_s_i.stopped', square_s_i.tStopRefresh)
    trials_2.addData('frame_f_i.started', frame_f_i.tStartRefresh)
    trials_2.addData('frame_f_i.stopped', frame_f_i.tStopRefresh)
    trials_2.addData('frame2_f_i.started', frame2_f_i.tStartRefresh)
    trials_2.addData('frame2_f_i.stopped', frame2_f_i.tStopRefresh)
    trials_2.addData('square_f_sq.started', square_f_sq.tStartRefresh)
    trials_2.addData('square_f_sq.stopped', square_f_sq.tStopRefresh)
    trials_2.addData('image.started', image.tStartRefresh)
    trials_2.addData('image.stopped', image.tStopRefresh)
    
    trials_2.addData('fix_cross_stim_side.started', fix_cross_stim_side.tStartRefresh)
    trials_2.addData('fix_cross_stim_side.stopped', fix_cross_stim_side.tStopRefresh)
    trials_2.addData('fix_cross_flash_side.started', fix_cross_flash_side.tStartRefresh)
    trials_2.addData('fix_cross_flash_side.stopped', fix_cross_flash_side.tStopRefresh)
    # check responses
    if key_resp_image.keys in ['', [], None]:  # No response was made
        key_resp_image.keys=None
    trials_2.addData('key_resp_image.keys',key_resp_image.keys)
    if key_resp_image.keys != None:  # we had a response
        trials_2.addData('key_resp_image.rt', key_resp_image.rt)
    trials_2.addData('key_resp_image.started', key_resp_image.tStartRefresh)
    trials_2.addData('key_resp_image.stopped', key_resp_image.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
key_resp_thanks = event.BuilderKeyResponse()
# keep track of which components have finished
thanksComponents = [thanksText_f, thanksText_s, key_resp_thanks]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText_f* updates
    if t >= 0.0 and thanksText_f.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText_f.tStart = t  # not accounting for scr refresh
        thanksText_f.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thanksText_f, 'tStartRefresh')  # time at next scr refresh
        thanksText_f.setAutoDraw(True)
    
    # *thanksText_s* updates
    if t >= 0.0 and thanksText_s.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText_s.tStart = t  # not accounting for scr refresh
        thanksText_s.frameNStart = frameN  # exact frame index
        win.timeOnFlip(thanksText_s, 'tStartRefresh')  # time at next scr refresh
        thanksText_s.setAutoDraw(True)
    
    # *key_resp_thanks* updates
    if t >= 0.0 and key_resp_thanks.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_thanks.tStart = t  # not accounting for scr refresh
        key_resp_thanks.frameNStart = frameN  # exact frame index
        win.timeOnFlip(key_resp_thanks, 'tStartRefresh')  # time at next scr refresh
        key_resp_thanks.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_thanks.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_thanks.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_thanks.keys = theseKeys[-1]  # just the last key pressed
            key_resp_thanks.rt = key_resp_thanks.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanksText_f.started', thanksText_f.tStartRefresh)
thisExp.addData('thanksText_f.stopped', thanksText_f.tStopRefresh)
thisExp.addData('thanksText_s.started', thanksText_s.tStartRefresh)
thisExp.addData('thanksText_s.stopped', thanksText_s.tStopRefresh)
# check responses
if key_resp_thanks.keys in ['', [], None]:  # No response was made
    key_resp_thanks.keys=None
thisExp.addData('key_resp_thanks.keys',key_resp_thanks.keys)
if key_resp_thanks.keys != None:  # we had a response
    thisExp.addData('key_resp_thanks.rt', key_resp_thanks.rt)
thisExp.addData('key_resp_thanks.started', key_resp_thanks.tStartRefresh)
thisExp.addData('key_resp_thanks.stopped', key_resp_thanks.tStopRefresh)
thisExp.nextEntry()
# the Routine "thanks" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()







# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
