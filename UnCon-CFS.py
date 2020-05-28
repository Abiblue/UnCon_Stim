#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on Thu 28 May 2020 08:38:21 PM +0430
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
    f_s = 685
    f2_s = 665
    sq_s = 645
    sq_f_s = 645
    l_s = 30
    fix_s = 80
    pic_s = sq_s

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
  txt_above_f_p = [center_l+100, -200]
  txt_below_f_p = [center_l-100, -200]
  txt_above_s_p = [center_r+100, -200]
  txt_below_s_p = [center_r-100, -200]
  line_left_start = (- f_s/2 - 1000, 0)
  line_left_end =  ( - f_s/2, 0)
  line_right_start = (+ f_s/2, 0) 
  line_right_end = ( + f_s/2 + 1000, 0) 
    

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
    #sqsp=30
    red = [1, -1, -1]
    green = [-1, 1, -1]
    blue = [-1, -1, 1]
    yellow = [1, 0.97, -0.55]
    pink = [1, 0.6, 0.6]
    black = [-1, -1, -1]
    color_set = [red, green, blue, yellow, pink, black]
    cell_number = columns * rows
    by_color = int(np.floor(float(cell_number)/len(color_set)))     
    # np.floor returns the next biggest integer (e.g. np.floor of 2.5 is 2)
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
    x_left = (1 - columns) * square_size / 2
    y_top = (1 - rows) * square_size / 2
    for l in range(rows):
        for c in range(columns):
           #r1=(random()-0.5)*square_size #ariel
           #r2=(random()-0.5)*square_size
            xys.append((x_left+ c * square_size, y_top+ l * square_size))
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

# flash stimulus change
def flash_change():
    global flash
    shuffle(flash.colors)
    flash.setColors(flash.colors)
# initiate colors
set_colors()
set_sizes()
set_positions()
jittery()
flash_init(win, f_p, square_size=60, columns=11, rows=21)
#flash_s_init(win, s_p, square_size=50, columns=10, rows=10)

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

# Initialize components for Routine "cfs"
cfsClock = core.Clock()
frame_s_i = visual.Rect(
    win=win, name='frame_s_i',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
frame2_s_i = visual.Rect(
    win=win, name='frame2_s_i',units='pix', 
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
square_s_i = visual.Rect(
    win=win, name='square_s_i',units='pix', 
    width=(sq_s, sq_s)[0], height=(sq_s, sq_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
image_flash = visual.ImageStim(
    win=win, name='image_flash',
    image=None, mask=None,
    ori=0, pos=f_p, size=(sq_s, sq_s),
    color=0.06, colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)

image = visual.ImageStim(
    win=win, name='image',
    image='sin', mask=None,
    ori=0, pos=s_p, size=pic_s,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
fix_cross_stim_side = visual.TextStim(win=win, name='fix_cross_stim_side',
    text='+',
    font='Arial',
    pos=s_p, height=fix_s, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
fix_cross_flash_side = visual.TextStim(win=win, name='fix_cross_flash_side',
    text='+',
    font='Arial',
    pos=f_p, height=fix_s, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
backblank_f = visual.Rect(
    win=win, name='backblank_f',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=f_p,
    lineWidth=1, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
backblank_s = visual.Rect(
    win=win, name='backblank_s',
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=s_p,
    lineWidth=1, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
text_blank_s = visual.TextStim(win=win, name='text_blank_s',
    text=None,
    font='Arial',
    pos=s_p, height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
text_blank_f = visual.TextStim(win=win, name='text_blank_f',
    text=None,
    font='Arial',
    pos=s_p, height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "Tweet"
TweetClock = core.Clock()
frame_tw_s = visual.Rect(
    win=win, name='frame_tw_s',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
frame_tw_f = visual.Rect(
    win=win, name='frame_tw_f',units='pix', 
    width=(f_s, f_s)[0], height=(f_s, f_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f_c, lineColorSpace='rgb',
    fillColor=f_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
frame2_tw_s = visual.Rect(
    win=win, name='frame2_tw_s',
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
frame2_tw_f = visual.Rect(
    win=win, name='frame2_tw_f',units='pix', 
    width=(f2_s, f2_s)[0], height=(f2_s, f2_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=f2_c, lineColorSpace='rgb',
    fillColor=f2_c, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
square_tw_s = visual.Rect(
    win=win, name='square_tw_s',units='pix', 
    width=(sq_s, sq_s)[0], height=(sq_s, sq_s)[1],
    ori=0, pos=s_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
square_tw_f = visual.Rect(
    win=win, name='square_tw_f',units='pix', 
    width=(sq_s,sq_s)[0], height=(sq_s,sq_s)[1],
    ori=0, pos=f_p,
    lineWidth=0, lineColor=sc_c, lineColorSpace='rgb',
    fillColor=sc_c, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_tweet_s1 = visual.TextStim(win=win, name='text_tweet_s1',
    text='default text',
    font='Nazli',
    pos=s_p, height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-6.0);
text_tweet_f1 = visual.TextStim(win=win, name='text_tweet_f1',
    text='default text',
    font='Nazli',
    pos=f_p, height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-7.0);

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
    
    # ------Prepare to start Routine "cfs"-------
    t = 0
    cfsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    image.setImage(Image)
    # keep track of which components have finished
    cfsComponents = [frame_s_i, frame2_s_i, square_s_i, image_flash, image, fix_cross_stim_side, fix_cross_flash_side]
    for thisComponent in cfsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "cfs"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = cfsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *frame_s_i* updates
        if t >= 0.0 and frame_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_s_i.tStart = t  # not accounting for scr refresh
            frame_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame_s_i, 'tStartRefresh')  # time at next scr refresh
            frame_s_i.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if frame_s_i.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            frame_s_i.tStop = t  # not accounting for scr refresh
            frame_s_i.frameNStop = frameN  # exact frame index
            win.timeOnFlip(frame_s_i, 'tStopRefresh')  # time at next scr refresh
            frame_s_i.setAutoDraw(False)
        
        # *frame2_s_i* updates
        if t >= 0.0 and frame2_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame2_s_i.tStart = t  # not accounting for scr refresh
            frame2_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame2_s_i, 'tStartRefresh')  # time at next scr refresh
            frame2_s_i.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if frame2_s_i.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            frame2_s_i.tStop = t  # not accounting for scr refresh
            frame2_s_i.frameNStop = frameN  # exact frame index
            win.timeOnFlip(frame2_s_i, 'tStopRefresh')  # time at next scr refresh
            frame2_s_i.setAutoDraw(False)
        
        # *square_s_i* updates
        if t >= 0.0 and square_s_i.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_s_i.tStart = t  # not accounting for scr refresh
            square_s_i.frameNStart = frameN  # exact frame index
            win.timeOnFlip(square_s_i, 'tStartRefresh')  # time at next scr refresh
            square_s_i.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if square_s_i.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            square_s_i.tStop = t  # not accounting for scr refresh
            square_s_i.frameNStop = frameN  # exact frame index
            win.timeOnFlip(square_s_i, 'tStopRefresh')  # time at next scr refresh
            square_s_i.setAutoDraw(False)
        
        # *image_flash* updates
        if t >= 0.0 and image_flash.status == NOT_STARTED:
            # keep track of start time/frame for later
            image_flash.tStart = t  # not accounting for scr refresh
            image_flash.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image_flash, 'tStartRefresh')  # time at next scr refresh
            image_flash.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image_flash.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image_flash.tStop = t  # not accounting for scr refresh
            image_flash.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_flash, 'tStopRefresh')  # time at next scr refresh
            image_flash.setAutoDraw(False)
        # flash each frame
        if frameN >= f_change:
            flash_change()
            myRand =randint(1,100)
            f_change += f_t
        flash.draw()
        
        # *image* updates
        if t >= 0.0 and image.status == NOT_STARTED:
            # keep track of start time/frame for later
            image.tStart = t  # not accounting for scr refresh
            image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            image.tStop = t  # not accounting for scr refresh
            image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
            image.setAutoDraw(False)
        
        # *fix_cross_stim_side* updates
        if t >= 0.0 and fix_cross_stim_side.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix_cross_stim_side.tStart = t  # not accounting for scr refresh
            fix_cross_stim_side.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix_cross_stim_side, 'tStartRefresh')  # time at next scr refresh
            fix_cross_stim_side.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix_cross_stim_side.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fix_cross_stim_side.tStop = t  # not accounting for scr refresh
            fix_cross_stim_side.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix_cross_stim_side, 'tStopRefresh')  # time at next scr refresh
            fix_cross_stim_side.setAutoDraw(False)
        
        # *fix_cross_flash_side* updates
        if t >= 0.0 and fix_cross_flash_side.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix_cross_flash_side.tStart = t  # not accounting for scr refresh
            fix_cross_flash_side.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix_cross_flash_side, 'tStartRefresh')  # time at next scr refresh
            fix_cross_flash_side.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fix_cross_flash_side.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            fix_cross_flash_side.tStop = t  # not accounting for scr refresh
            fix_cross_flash_side.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix_cross_flash_side, 'tStopRefresh')  # time at next scr refresh
            fix_cross_flash_side.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in cfsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "cfs"-------
    for thisComponent in cfsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('frame_s_i.started', frame_s_i.tStartRefresh)
    trials_2.addData('frame_s_i.stopped', frame_s_i.tStopRefresh)
    trials_2.addData('frame2_s_i.started', frame2_s_i.tStartRefresh)
    trials_2.addData('frame2_s_i.stopped', frame2_s_i.tStopRefresh)
    trials_2.addData('square_s_i.started', square_s_i.tStartRefresh)
    trials_2.addData('square_s_i.stopped', square_s_i.tStopRefresh)
    trials_2.addData('image_flash.started', image_flash.tStartRefresh)
    trials_2.addData('image_flash.stopped', image_flash.tStopRefresh)
    
    trials_2.addData('image.started', image.tStartRefresh)
    trials_2.addData('image.stopped', image.tStopRefresh)
    trials_2.addData('fix_cross_stim_side.started', fix_cross_stim_side.tStartRefresh)
    trials_2.addData('fix_cross_stim_side.stopped', fix_cross_stim_side.tStopRefresh)
    trials_2.addData('fix_cross_flash_side.started', fix_cross_flash_side.tStartRefresh)
    trials_2.addData('fix_cross_flash_side.stopped', fix_cross_flash_side.tStopRefresh)
    
    # ------Prepare to start Routine "blank"-------
    t = 0
    blankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [backblank_f, backblank_s, text_blank_s, text_blank_f]
    for thisComponent in blankComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "blank"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = blankClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *backblank_f* updates
        if t >= 0.0 and backblank_f.status == NOT_STARTED:
            # keep track of start time/frame for later
            backblank_f.tStart = t  # not accounting for scr refresh
            backblank_f.frameNStart = frameN  # exact frame index
            win.timeOnFlip(backblank_f, 'tStartRefresh')  # time at next scr refresh
            backblank_f.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if backblank_f.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            backblank_f.tStop = t  # not accounting for scr refresh
            backblank_f.frameNStop = frameN  # exact frame index
            win.timeOnFlip(backblank_f, 'tStopRefresh')  # time at next scr refresh
            backblank_f.setAutoDraw(False)
        
        # *backblank_s* updates
        if t >= 0.0 and backblank_s.status == NOT_STARTED:
            # keep track of start time/frame for later
            backblank_s.tStart = t  # not accounting for scr refresh
            backblank_s.frameNStart = frameN  # exact frame index
            win.timeOnFlip(backblank_s, 'tStartRefresh')  # time at next scr refresh
            backblank_s.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if backblank_s.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            backblank_s.tStop = t  # not accounting for scr refresh
            backblank_s.frameNStop = frameN  # exact frame index
            win.timeOnFlip(backblank_s, 'tStopRefresh')  # time at next scr refresh
            backblank_s.setAutoDraw(False)
        
        # *text_blank_s* updates
        if t >= 0.0 and text_blank_s.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_blank_s.tStart = t  # not accounting for scr refresh
            text_blank_s.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_blank_s, 'tStartRefresh')  # time at next scr refresh
            text_blank_s.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_blank_s.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_blank_s.tStop = t  # not accounting for scr refresh
            text_blank_s.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank_s, 'tStopRefresh')  # time at next scr refresh
            text_blank_s.setAutoDraw(False)
        
        # *text_blank_f* updates
        if t >= 0.0 and text_blank_f.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_blank_f.tStart = t  # not accounting for scr refresh
            text_blank_f.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_blank_f, 'tStartRefresh')  # time at next scr refresh
            text_blank_f.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if text_blank_f.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            text_blank_f.tStop = t  # not accounting for scr refresh
            text_blank_f.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_blank_f, 'tStopRefresh')  # time at next scr refresh
            text_blank_f.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in blankComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "blank"-------
    for thisComponent in blankComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('backblank_f.started', backblank_f.tStartRefresh)
    trials_2.addData('backblank_f.stopped', backblank_f.tStopRefresh)
    trials_2.addData('backblank_s.started', backblank_s.tStartRefresh)
    trials_2.addData('backblank_s.stopped', backblank_s.tStopRefresh)
    trials_2.addData('text_blank_s.started', text_blank_s.tStartRefresh)
    trials_2.addData('text_blank_s.stopped', text_blank_s.tStopRefresh)
    trials_2.addData('text_blank_f.started', text_blank_f.tStartRefresh)
    trials_2.addData('text_blank_f.stopped', text_blank_f.tStopRefresh)
    
    # ------Prepare to start Routine "Tweet"-------
    t = 0
    TweetClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    text_tweet_s1.setText(Tweets)
    text_tweet_f1.setText(Tweets
)
    key_resp_tweet = event.BuilderKeyResponse()
    # keep track of which components have finished
    TweetComponents = [frame_tw_s, frame_tw_f, frame2_tw_s, frame2_tw_f, square_tw_s, square_tw_f, text_tweet_s1, text_tweet_f1, key_resp_tweet]
    for thisComponent in TweetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Tweet"-------
    while continueRoutine:
        # get current time
        t = TweetClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *frame_tw_s* updates
        if t >= 0.0 and frame_tw_s.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_tw_s.tStart = t  # not accounting for scr refresh
            frame_tw_s.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame_tw_s, 'tStartRefresh')  # time at next scr refresh
            frame_tw_s.setAutoDraw(True)
        
        # *frame_tw_f* updates
        if t >= 0.0 and frame_tw_f.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame_tw_f.tStart = t  # not accounting for scr refresh
            frame_tw_f.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame_tw_f, 'tStartRefresh')  # time at next scr refresh
            frame_tw_f.setAutoDraw(True)
        
        # *frame2_tw_s* updates
        if t >= 0.0 and frame2_tw_s.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame2_tw_s.tStart = t  # not accounting for scr refresh
            frame2_tw_s.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame2_tw_s, 'tStartRefresh')  # time at next scr refresh
            frame2_tw_s.setAutoDraw(True)
        
        # *frame2_tw_f* updates
        if t >= 0.0 and frame2_tw_f.status == NOT_STARTED:
            # keep track of start time/frame for later
            frame2_tw_f.tStart = t  # not accounting for scr refresh
            frame2_tw_f.frameNStart = frameN  # exact frame index
            win.timeOnFlip(frame2_tw_f, 'tStartRefresh')  # time at next scr refresh
            frame2_tw_f.setAutoDraw(True)
        
        # *square_tw_s* updates
        if t >= 0.0 and square_tw_s.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_tw_s.tStart = t  # not accounting for scr refresh
            square_tw_s.frameNStart = frameN  # exact frame index
            win.timeOnFlip(square_tw_s, 'tStartRefresh')  # time at next scr refresh
            square_tw_s.setAutoDraw(True)
        
        # *square_tw_f* updates
        if t >= 0.0 and square_tw_f.status == NOT_STARTED:
            # keep track of start time/frame for later
            square_tw_f.tStart = t  # not accounting for scr refresh
            square_tw_f.frameNStart = frameN  # exact frame index
            win.timeOnFlip(square_tw_f, 'tStartRefresh')  # time at next scr refresh
            square_tw_f.setAutoDraw(True)
        
        # *text_tweet_s1* updates
        if t >= 0.0 and text_tweet_s1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_tweet_s1.tStart = t  # not accounting for scr refresh
            text_tweet_s1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_tweet_s1, 'tStartRefresh')  # time at next scr refresh
            text_tweet_s1.setAutoDraw(True)
        
        # *text_tweet_f1* updates
        if t >= 0.0 and text_tweet_f1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_tweet_f1.tStart = t  # not accounting for scr refresh
            text_tweet_f1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_tweet_f1, 'tStartRefresh')  # time at next scr refresh
            text_tweet_f1.setAutoDraw(True)
        
        # *key_resp_tweet* updates
        if t >= 0.0 and key_resp_tweet.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_tweet.tStart = t  # not accounting for scr refresh
            key_resp_tweet.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_tweet, 'tStartRefresh')  # time at next scr refresh
            key_resp_tweet.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_tweet.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_tweet.status == STARTED:
            theseKeys = event.getKeys(keyList=['left', 'right'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_tweet.keys = theseKeys[-1]  # just the last key pressed
                key_resp_tweet.rt = key_resp_tweet.clock.getTime()
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TweetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Tweet"-------
    for thisComponent in TweetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials_2.addData('frame_tw_s.started', frame_tw_s.tStartRefresh)
    trials_2.addData('frame_tw_s.stopped', frame_tw_s.tStopRefresh)
    trials_2.addData('frame_tw_f.started', frame_tw_f.tStartRefresh)
    trials_2.addData('frame_tw_f.stopped', frame_tw_f.tStopRefresh)
    trials_2.addData('frame2_tw_s.started', frame2_tw_s.tStartRefresh)
    trials_2.addData('frame2_tw_s.stopped', frame2_tw_s.tStopRefresh)
    trials_2.addData('frame2_tw_f.started', frame2_tw_f.tStartRefresh)
    trials_2.addData('frame2_tw_f.stopped', frame2_tw_f.tStopRefresh)
    trials_2.addData('square_tw_s.started', square_tw_s.tStartRefresh)
    trials_2.addData('square_tw_s.stopped', square_tw_s.tStopRefresh)
    trials_2.addData('square_tw_f.started', square_tw_f.tStartRefresh)
    trials_2.addData('square_tw_f.stopped', square_tw_f.tStopRefresh)
    trials_2.addData('text_tweet_s1.started', text_tweet_s1.tStartRefresh)
    trials_2.addData('text_tweet_s1.stopped', text_tweet_s1.tStopRefresh)
    trials_2.addData('text_tweet_f1.started', text_tweet_f1.tStartRefresh)
    trials_2.addData('text_tweet_f1.stopped', text_tweet_f1.tStopRefresh)
    # check responses
    if key_resp_tweet.keys in ['', [], None]:  # No response was made
        key_resp_tweet.keys=None
    trials_2.addData('key_resp_tweet.keys',key_resp_tweet.keys)
    if key_resp_tweet.keys != None:  # we had a response
        trials_2.addData('key_resp_tweet.rt', key_resp_tweet.rt)
    trials_2.addData('key_resp_tweet.started', key_resp_tweet.tStartRefresh)
    trials_2.addData('key_resp_tweet.stopped', key_resp_tweet.tStopRefresh)
    # the Routine "Tweet" was not non-slip safe, so reset the non-slip timer
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
