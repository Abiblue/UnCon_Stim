#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.5),
    on Wed 02 Dec 2020 01:38:09 PM +0330
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
expInfo = {'Education': '', 'Age': '', 'Sex': '', 'participant': '', 'session': '001'}
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
    originPath='/home/abi/Desktop/thesis-GitHub/UnCon_Stim/UnCon-CFS.py',
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
    monitor='testMonitor', color=[-1.000,-1.000,-1.000], colorSpace='rgb',
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
# Colors used during the experiment.
# Color variables end with _c.
def set_colors():
    global screen_c # screen color
    global frame_c # frame color
    global cross_c  # cross color
    screen_c = [.002, .002, .002]
    frame_c = [-1,-1,-1]
    cross_c = 'black'
# Sizes used during the experiment
# Size variables end with _s.
def set_sizes():
    global frame_s
    global sq_s # square size (square where the stimulus is shown)
    #global sq_f_s # square size (square underneath is shown)
    global image_s
    global txt_frame_s # frame size of textbox
    global txt_sq_s # square size of textbox
    global txt_s
    global icon_s #size of the mouse icons
    global fix_s  # size of fixation crosses on top of stimuli
    
    
    screen_size = np.array( win.size )
    frame_s = np.array( [ win.size[0]/2, win.size[1] ] )
    sq_s = (frame_s) * 0.95
    image_s = (sq_s) * 0.87
    txt_frame_s = (np.array( [ win.size[0]/2, win.size[1]/2 ] )) * 0.95
    txt_sq_s = (txt_frame_s) * 0.95
    txt_s = (txt_sq_s) * 0.95
    icon_s = np.array( [ win.size[0]/10, win.size[1]/8 ] )
    fix_s = (frame_s) * 0.75
# set positions used during the experiment
# Position variables end with _p.
def set_positions():
  global stim_p # position of the text and image stimuli (left or right according experiment settings).
  global flash_p # position of the flash stimulus (right or left according experiment settings).
  global txt_r_p
  global txt_l_p
  global icon_r_p
  global icon_l_p
  global like_r_p
  global like_l_p
  global dislike_r_p
  global dislike_l_p
  global share_r_p
  global share_l_p
  global next_r_p
  global next_l_p
  
  delta_x, delta_y = win.size/4
  quarter_centers = [ [-delta_x, +delta_y], [+delta_x, +delta_y], [+delta_x, -delta_y], [-delta_x, -delta_y] ] #centers when window is quartered.
  half_centers = [ [-delta_x , 0], [delta_x, 0] ] #centers when window is halved.
  
  stim_p = half_centers[0]
  flash_p = half_centers[1]
  txt_r_p = quarter_centers[1]
  txt_l_p = quarter_centers[0]
  icon_l_p = quarter_centers[3]
  icon_r_p = quarter_centers[2]
  
  icon_dist_x = win.size[0]/14
  icon_dist_y = win.size[1]/10
  icon_centers = [[+icon_dist_x, +icon_dist_y], [+icon_dist_x, -icon_dist_y], [-icon_dist_x, +icon_dist_y], [-icon_dist_x, -icon_dist_y]]
  
  like_l_p = icon_l_p + np.array( icon_centers[2] )
  dislike_l_p = icon_l_p + np.array( icon_centers[0] )
  share_l_p = icon_l_p + np.array( icon_centers[3] )
  next_l_p = icon_l_p + np.array( icon_centers[1] )
  like_r_p = icon_r_p + np.array( icon_centers[2] )
  dislike_r_p = icon_r_p + np.array( icon_centers[0] )
  share_r_p = icon_r_p + np.array( icon_centers[3] )
  next_r_p = icon_r_p + np.array( icon_centers[1] )
  
# define timings
# Time variables used during the experiment
# Time variables end with _t.
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
    
    f_t = 5
    fps = 100 # frames per second
    
    # TIMES FOR OPACITY
    before_t = 0 * fps
    fade_i_t = 1 * fps
    inside_t = 8 * fps
    fade_o_t = 0 * fps
    after_t = 0 * fps
    stim_t  = fade_i_t + inside_t + fade_o_t
    total_t  = before_t + stim_t + after_t
    fade_i_end_t = before_t + fade_i_t
    fade_o_beg_t = fade_i_end_t + inside_t
    fade_o_end_t = before_t + stim_t
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
def flash_init(win, position=[0,0], square_size=30, columns=10, rows=10):
    global flash # The flash stimulus (an array of flashing squares)
    #sqsp=30
    red = [1, -1, -1]
    green = [-1, 1, -1]
    blue = [-1, -1, 1]
    yellow = [1, 0.97, -0.55]
    pink = [1, 0.6, 0.6]
    black = [-1, -1, -1]
    color_set = [red, green, blue, yellow, pink]
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
flash_init(win, flash_p, square_size=40, columns=13, rows=16)
#flash_s_init(win, s_p, square_size=50, columns=10, rows=10)

# Initialize components for Routine "contest"
contestClock = core.Clock()
contest_frame_r = visual.Rect(
    win=win, name='contest_frame_r',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
contest_screen_r = visual.Rect(
    win=win, name='contest_screen_r',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
contest_text_r = visual.TextStim(win=win, name='contest_text_r',
    text='رضایت نامه',
    font='Nazli',
    pos=txt_r_p, height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-2.0);
contest_swipe_r = visual.ImageStim(
    win=win, name='contest_swipe_r',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=icon_r_p, size=(100, 100),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
contest_frame_l = visual.Rect(
    win=win, name='contest_frame_l',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
contest_screen_l = visual.Rect(
    win=win, name='contest_screen_l',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text = visual.TextStim(win=win, name='text',
    text='رضایت نامه',
    font='Nazli',
    pos=txt_l_p, height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-6.0);
contest_swipe_l = visual.ImageStim(
    win=win, name='contest_swipe_l',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=icon_l_p, size=(100, 100),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
swipe_click = event.Mouse(win=win)
x, y = [None, None]
swipe_click.mouseClock = core.Clock()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
inst_frame_r = visual.Rect(
    win=win, name='inst_frame_r',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
inst_screen_r = visual.Rect(
    win=win, name='inst_screen_r',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
inst_txt_r = visual.TextStim(win=win, name='inst_txt_r',
    text='در هر مرحله به شما یک پیام نشان\u200cداده خواهد شد.\nباتوجه به میزان اهمیت پیام برای شما، \nتصمیم بگیرد که اگر در این پیام را در یک\nشبکه\u200cی اجتماعی مشاهده می\u200cکردید\nچه واکنشی نشان می\u200cدادید؟\n',
    font='Nazli',
    pos=txt_r_p, height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-2.0);
inst_swipe_r = visual.ImageStim(
    win=win, name='inst_swipe_r',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=icon_r_p, size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
inst_frame_l = visual.Rect(
    win=win, name='inst_frame_l',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
inst_screen_l = visual.Rect(
    win=win, name='inst_screen_l',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
inst_txt_l = visual.TextStim(win=win, name='inst_txt_l',
    text='در هر مرحله به شما یک پیام نشان\u200cداده خواهد شد.\nباتوجه به میزان اهمیت پیام برای شما، \nتصمیم بگیرد که اگر در این پیام را در یک\nشبکه\u200cی اجتماعی مشاهده می\u200cکردید\nچه واکنشی نشان می\u200cدادید؟',
    font='Nazli',
    pos=txt_l_p, height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-6.0);
inst_swipe_l = visual.ImageStim(
    win=win, name='inst_swipe_l',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=icon_l_p, size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
swipe2_click = event.Mouse(win=win)
x, y = [None, None]
swipe2_click.mouseClock = core.Clock()

# Initialize components for Routine "fixation_point"
fixation_pointClock = core.Clock()
fix_frame_l = visual.Rect(
    win=win, name='fix_frame_l',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=stim_p,
    lineWidth=0, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
fix_screen_l = visual.Rect(
    win=win, name='fix_screen_l',
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=stim_p,
    lineWidth=0, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
fix_cross_l = visual.ShapeStim(
    win=win, name='fix_cross_l', vertices='cross',units='pix', 
    size=fix_s,
    ori=0, pos=stim_p,
    lineWidth=10, lineColor=cross_c, lineColorSpace='rgb',
    fillColor=cross_c, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
fix_frame_r = visual.Rect(
    win=win, name='fix_frame_r',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=flash_p,
    lineWidth=0, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
fix_screen_r = visual.Rect(
    win=win, name='fix_screen_r',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=flash_p,
    lineWidth=0, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
fix_cross_r = visual.ShapeStim(
    win=win, name='fix_cross_r', vertices='cross',units='pix', 
    size=fix_s,
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=cross_c, lineColorSpace='rgb',
    fillColor=cross_c, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)

# Initialize components for Routine "pre_cfs"
pre_cfsClock = core.Clock()

stim_frame = visual.Rect(
    win=win, name='stim_frame',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
stim_screen = visual.Rect(
    win=win, name='stim_screen',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
flash_frame = visual.Rect(
    win=win, name='flash_frame',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
flash_screen = visual.Rect(
    win=win, name='flash_screen',units='pix', 
    width=image_s[0], height=image_s[1],
    ori=0, pos=flash_p,
    lineWidth=100, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=None, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
stim_image = visual.ImageStim(
    win=win, name='stim_image',units='pix', 
    image='sin', mask=None,
    ori=0, pos=stim_p, size=image_s,
    color=[1,1,1], colorSpace='rgb', opacity=1.0,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-5.0)
fix_cross_stim = visual.TextStim(win=win, name='fix_cross_stim',
    text='+',
    font='Arial',
    pos=stim_p, height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
fix_cross_flash = visual.TextStim(win=win, name='fix_cross_flash',
    text='+',
    font='Arial',
    pos=flash_p, height=50, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);

# Initialize components for Routine "blank"
blankClock = core.Clock()
blank_frame_l = visual.Rect(
    win=win, name='blank_frame_l',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=stim_p,
    lineWidth=0, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
balnk_frame_r = visual.Rect(
    win=win, name='balnk_frame_r',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=flash_p,
    lineWidth=0, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
blank_screen_r = visual.Rect(
    win=win, name='blank_screen_r',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-2.0, interpolate=True)
blank_screen_l = visual.Rect(
    win=win, name='blank_screen_l',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)

# Initialize components for Routine "pre_statement"
pre_statementClock = core.Clock()
statement_frame_r = visual.Rect(
    win=win, name='statement_frame_r',units='pix', 
    width=txt_frame_s[0], height=txt_frame_s[1],
    ori=0, pos=txt_r_p,
    lineWidth=0, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
statement_screen_r = visual.Rect(
    win=win, name='statement_screen_r',units='pix', 
    width=txt_sq_s[0], height=txt_sq_s[1],
    ori=0, pos=txt_r_p,
    lineWidth=0, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
statement_r = visual.TextStim(win=win, name='statement_r',
    text='default text',
    font='Nazli',
    pos=txt_r_p, height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-2.0);
statement_frame_l = visual.Rect(
    win=win, name='statement_frame_l',units='pix', 
    width=txt_frame_s[0], height=txt_frame_s[1],
    ori=0, pos=txt_l_p,
    lineWidth=0, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-3.0, interpolate=True)
statement_screen_l = visual.Rect(
    win=win, name='statement_screen_l',units='pix', 
    width=txt_sq_s[0], height=txt_sq_s[1],
    ori=0, pos=txt_l_p,
    lineWidth=0, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
text_tweet_f1 = visual.TextStim(win=win, name='text_tweet_f1',
    text='default text',
    font='Nazli',
    pos=txt_l_p, height=30, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-5.0);
icon_frame_r = visual.Rect(
    win=win, name='icon_frame_r',units='pix', 
    width=txt_frame_s[0], height=txt_frame_s[1],
    ori=0, pos=icon_r_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-6.0, interpolate=True)
icon_screen_r = visual.Rect(
    win=win, name='icon_screen_r',units='pix', 
    width=txt_sq_s[0], height=txt_sq_s[1],
    ori=0, pos=icon_r_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-7.0, interpolate=True)
icon_frame_l = visual.Rect(
    win=win, name='icon_frame_l',units='pix', 
    width=txt_frame_s[0], height=txt_frame_s[1],
    ori=0, pos=icon_l_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-8.0, interpolate=True)
icon_screen_l = visual.Rect(
    win=win, name='icon_screen_l',units='pix', 
    width=txt_sq_s[0], height=txt_sq_s[1],
    ori=0, pos=icon_l_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-9.0, interpolate=True)
like_r = visual.ImageStim(
    win=win, name='like_r',units='pix', 
    image='noun_like.png', mask=None,
    ori=0, pos=like_r_p, size=(115, 115),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-10.0)
dislike_r = visual.ImageStim(
    win=win, name='dislike_r',units='pix', 
    image='noun_Dislike.png', mask=None,
    ori=0, pos=dislike_r_p, size=(100, 100),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-11.0)
share_r = visual.ImageStim(
    win=win, name='share_r',units='pix', 
    image='noun_share.png', mask=None,
    ori=0, pos=share_r_p, size=(120, 120),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-12.0)
swipe_r = visual.ImageStim(
    win=win, name='swipe_r',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=next_r_p, size=(125, 125),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-13.0)
like_l = visual.ImageStim(
    win=win, name='like_l',units='pix', 
    image='noun_like.png', mask=None,
    ori=0, pos=like_l_p, size=(100, 100),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-14.0)
dislike_l = visual.ImageStim(
    win=win, name='dislike_l',units='pix', 
    image='noun_Dislike.png', mask=None,
    ori=0, pos=dislike_l_p, size=(110, 110),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-15.0)
share_l = visual.ImageStim(
    win=win, name='share_l',units='pix', 
    image='noun_share.png', mask=None,
    ori=0, pos=share_l_p, size=(80, 80),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-16.0)
swipe_l = visual.ImageStim(
    win=win, name='swipe_l',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=next_l_p, size=(90, 90),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-17.0)
response = event.Mouse(win=win)
x, y = [None, None]
response.mouseClock = core.Clock()

# Initialize components for Routine "Instructions"
InstructionsClock = core.Clock()
inst_frame_r = visual.Rect(
    win=win, name='inst_frame_r',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
inst_screen_r = visual.Rect(
    win=win, name='inst_screen_r',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=flash_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
inst_txt_r = visual.TextStim(win=win, name='inst_txt_r',
    text='در هر مرحله به شما یک پیام نشان\u200cداده خواهد شد.\nباتوجه به میزان اهمیت پیام برای شما، \nتصمیم بگیرد که اگر در این پیام را در یک\nشبکه\u200cی اجتماعی مشاهده می\u200cکردید\nچه واکنشی نشان می\u200cدادید؟\n',
    font='Nazli',
    pos=txt_r_p, height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-2.0);
inst_swipe_r = visual.ImageStim(
    win=win, name='inst_swipe_r',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=icon_r_p, size=(150, 150),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
inst_frame_l = visual.Rect(
    win=win, name='inst_frame_l',units='pix', 
    width=frame_s[0], height=frame_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=frame_c, lineColorSpace='rgb',
    fillColor=frame_c, fillColorSpace='rgb',
    opacity=1, depth=-4.0, interpolate=True)
inst_screen_l = visual.Rect(
    win=win, name='inst_screen_l',units='pix', 
    width=sq_s[0], height=sq_s[1],
    ori=0, pos=stim_p,
    lineWidth=1, lineColor=screen_c, lineColorSpace='rgb',
    fillColor=screen_c, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
inst_txt_l = visual.TextStim(win=win, name='inst_txt_l',
    text='در هر مرحله به شما یک پیام نشان\u200cداده خواهد شد.\nباتوجه به میزان اهمیت پیام برای شما، \nتصمیم بگیرد که اگر در این پیام را در یک\nشبکه\u200cی اجتماعی مشاهده می\u200cکردید\nچه واکنشی نشان می\u200cدادید؟',
    font='Nazli',
    pos=txt_l_p, height=25, wrapWidth=float(win.size[0]/3), ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=-6.0);
inst_swipe_l = visual.ImageStim(
    win=win, name='inst_swipe_l',units='pix', 
    image='noun_swipe.png', mask=None,
    ori=0, pos=icon_l_p, size=(200, 200),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-7.0)
swipe2_click = event.Mouse(win=win)
x, y = [None, None]
swipe2_click.mouseClock = core.Clock()

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText_f = visual.TextStim(win=win, name='thanksText_f',
    text='پایان آزمون.\nبا سپاس از شما',
    font='Nazli',
    pos=flash_p, height=30, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='Arabic',
    depth=0.0);
thanksText_s = visual.TextStim(win=win, name='thanksText_s',
    text='پایان آزمون.\nبا سپاس از شما',
    font='Nazli',
    pos=stim_p, height=30, wrapWidth=None, ori=0, 
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

# ------Prepare to start Routine "contest"-------
t = 0
contestClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the swipe_click
swipe_click.x = []
swipe_click.y = []
swipe_click.leftButton = []
swipe_click.midButton = []
swipe_click.rightButton = []
swipe_click.time = []
swipe_click.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
contestComponents = [contest_frame_r, contest_screen_r, contest_text_r, contest_swipe_r, contest_frame_l, contest_screen_l, text, contest_swipe_l, swipe_click]
for thisComponent in contestComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "contest"-------
while continueRoutine:
    # get current time
    t = contestClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *contest_frame_r* updates
    if t >= 0.0 and contest_frame_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        contest_frame_r.tStart = t  # not accounting for scr refresh
        contest_frame_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(contest_frame_r, 'tStartRefresh')  # time at next scr refresh
        contest_frame_r.setAutoDraw(True)
    
    # *contest_screen_r* updates
    if t >= 0.0 and contest_screen_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        contest_screen_r.tStart = t  # not accounting for scr refresh
        contest_screen_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(contest_screen_r, 'tStartRefresh')  # time at next scr refresh
        contest_screen_r.setAutoDraw(True)
    
    # *contest_text_r* updates
    if t >= 0.0 and contest_text_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        contest_text_r.tStart = t  # not accounting for scr refresh
        contest_text_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(contest_text_r, 'tStartRefresh')  # time at next scr refresh
        contest_text_r.setAutoDraw(True)
    
    # *contest_swipe_r* updates
    if t >= 0.0 and contest_swipe_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        contest_swipe_r.tStart = t  # not accounting for scr refresh
        contest_swipe_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(contest_swipe_r, 'tStartRefresh')  # time at next scr refresh
        contest_swipe_r.setAutoDraw(True)
    
    # *contest_frame_l* updates
    if t >= 0.0 and contest_frame_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        contest_frame_l.tStart = t  # not accounting for scr refresh
        contest_frame_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(contest_frame_l, 'tStartRefresh')  # time at next scr refresh
        contest_frame_l.setAutoDraw(True)
    
    # *contest_screen_l* updates
    if t >= 0.0 and contest_screen_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        contest_screen_l.tStart = t  # not accounting for scr refresh
        contest_screen_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(contest_screen_l, 'tStartRefresh')  # time at next scr refresh
        contest_screen_l.setAutoDraw(True)
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *contest_swipe_l* updates
    if t >= 0.0 and contest_swipe_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        contest_swipe_l.tStart = t  # not accounting for scr refresh
        contest_swipe_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(contest_swipe_l, 'tStartRefresh')  # time at next scr refresh
        contest_swipe_l.setAutoDraw(True)
    # *swipe_click* updates
    if t >= 0.0 and swipe_click.status == NOT_STARTED:
        # keep track of start time/frame for later
        swipe_click.tStart = t  # not accounting for scr refresh
        swipe_click.frameNStart = frameN  # exact frame index
        win.timeOnFlip(swipe_click, 'tStartRefresh')  # time at next scr refresh
        swipe_click.status = STARTED
        swipe_click.mouseClock.reset()
        prevButtonState = swipe_click.getPressed()  # if button is down already this ISN'T a new click
    if swipe_click.status == STARTED:  # only update if started and not finished!
        buttons = swipe_click.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [contest_swipe_r, contest_swipe_l]:
                    if obj.contains(swipe_click):
                        gotValidClick = True
                        swipe_click.clicked_name.append(obj.name)
                x, y = swipe_click.getPos()
                swipe_click.x.append(x)
                swipe_click.y.append(y)
                buttons = swipe_click.getPressed()
                swipe_click.leftButton.append(buttons[0])
                swipe_click.midButton.append(buttons[1])
                swipe_click.rightButton.append(buttons[2])
                swipe_click.time.append(swipe_click.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
                    continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in contestComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "contest"-------
for thisComponent in contestComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('contest_frame_r.started', contest_frame_r.tStartRefresh)
thisExp.addData('contest_frame_r.stopped', contest_frame_r.tStopRefresh)
thisExp.addData('contest_screen_r.started', contest_screen_r.tStartRefresh)
thisExp.addData('contest_screen_r.stopped', contest_screen_r.tStopRefresh)
thisExp.addData('contest_text_r.started', contest_text_r.tStartRefresh)
thisExp.addData('contest_text_r.stopped', contest_text_r.tStopRefresh)
thisExp.addData('contest_swipe_r.started', contest_swipe_r.tStartRefresh)
thisExp.addData('contest_swipe_r.stopped', contest_swipe_r.tStopRefresh)
thisExp.addData('contest_frame_l.started', contest_frame_l.tStartRefresh)
thisExp.addData('contest_frame_l.stopped', contest_frame_l.tStopRefresh)
thisExp.addData('contest_screen_l.started', contest_screen_l.tStartRefresh)
thisExp.addData('contest_screen_l.stopped', contest_screen_l.tStopRefresh)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
thisExp.addData('contest_swipe_l.started', contest_swipe_l.tStartRefresh)
thisExp.addData('contest_swipe_l.stopped', contest_swipe_l.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(swipe_click.x): thisExp.addData('swipe_click.x', swipe_click.x[0])
if len(swipe_click.y): thisExp.addData('swipe_click.y', swipe_click.y[0])
if len(swipe_click.leftButton): thisExp.addData('swipe_click.leftButton', swipe_click.leftButton[0])
if len(swipe_click.midButton): thisExp.addData('swipe_click.midButton', swipe_click.midButton[0])
if len(swipe_click.rightButton): thisExp.addData('swipe_click.rightButton', swipe_click.rightButton[0])
if len(swipe_click.time): thisExp.addData('swipe_click.time', swipe_click.time[0])
if len(swipe_click.clicked_name): thisExp.addData('swipe_click.clicked_name', swipe_click.clicked_name[0])
thisExp.addData('swipe_click.started', swipe_click.tStart)
thisExp.addData('swipe_click.stopped', swipe_click.tStop)
thisExp.nextEntry()
# the Routine "contest" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the swipe2_click
swipe2_click.x = []
swipe2_click.y = []
swipe2_click.leftButton = []
swipe2_click.midButton = []
swipe2_click.rightButton = []
swipe2_click.time = []
swipe2_click.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstructionsComponents = [inst_frame_r, inst_screen_r, inst_txt_r, inst_swipe_r, inst_frame_l, inst_screen_l, inst_txt_l, inst_swipe_l, swipe2_click]
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
    
    # *inst_frame_r* updates
    if t >= 0.0 and inst_frame_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_frame_r.tStart = t  # not accounting for scr refresh
        inst_frame_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_frame_r, 'tStartRefresh')  # time at next scr refresh
        inst_frame_r.setAutoDraw(True)
    
    # *inst_screen_r* updates
    if t >= 0.0 and inst_screen_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_screen_r.tStart = t  # not accounting for scr refresh
        inst_screen_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_screen_r, 'tStartRefresh')  # time at next scr refresh
        inst_screen_r.setAutoDraw(True)
    
    # *inst_txt_r* updates
    if t >= 0 and inst_txt_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_txt_r.tStart = t  # not accounting for scr refresh
        inst_txt_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_txt_r, 'tStartRefresh')  # time at next scr refresh
        inst_txt_r.setAutoDraw(True)
    
    # *inst_swipe_r* updates
    if t >= 0.0 and inst_swipe_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_swipe_r.tStart = t  # not accounting for scr refresh
        inst_swipe_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_swipe_r, 'tStartRefresh')  # time at next scr refresh
        inst_swipe_r.setAutoDraw(True)
    
    # *inst_frame_l* updates
    if t >= 0.0 and inst_frame_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_frame_l.tStart = t  # not accounting for scr refresh
        inst_frame_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_frame_l, 'tStartRefresh')  # time at next scr refresh
        inst_frame_l.setAutoDraw(True)
    
    # *inst_screen_l* updates
    if t >= 0.0 and inst_screen_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_screen_l.tStart = t  # not accounting for scr refresh
        inst_screen_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_screen_l, 'tStartRefresh')  # time at next scr refresh
        inst_screen_l.setAutoDraw(True)
    
    # *inst_txt_l* updates
    if t >= 0 and inst_txt_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_txt_l.tStart = t  # not accounting for scr refresh
        inst_txt_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_txt_l, 'tStartRefresh')  # time at next scr refresh
        inst_txt_l.setAutoDraw(True)
    
    # *inst_swipe_l* updates
    if t >= 0.0 and inst_swipe_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_swipe_l.tStart = t  # not accounting for scr refresh
        inst_swipe_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_swipe_l, 'tStartRefresh')  # time at next scr refresh
        inst_swipe_l.setAutoDraw(True)
    # *swipe2_click* updates
    if t >= 0.0 and swipe2_click.status == NOT_STARTED:
        # keep track of start time/frame for later
        swipe2_click.tStart = t  # not accounting for scr refresh
        swipe2_click.frameNStart = frameN  # exact frame index
        win.timeOnFlip(swipe2_click, 'tStartRefresh')  # time at next scr refresh
        swipe2_click.status = STARTED
        swipe2_click.mouseClock.reset()
        prevButtonState = swipe2_click.getPressed()  # if button is down already this ISN'T a new click
    if swipe2_click.status == STARTED:  # only update if started and not finished!
        buttons = swipe2_click.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [inst_swipe_r, inst_swipe_l]:
                    if obj.contains(swipe2_click):
                        gotValidClick = True
                        swipe2_click.clicked_name.append(obj.name)
                x, y = swipe2_click.getPos()
                swipe2_click.x.append(x)
                swipe2_click.y.append(y)
                buttons = swipe2_click.getPressed()
                swipe2_click.leftButton.append(buttons[0])
                swipe2_click.midButton.append(buttons[1])
                swipe2_click.rightButton.append(buttons[2])
                swipe2_click.time.append(swipe2_click.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
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
thisExp.addData('inst_frame_r.started', inst_frame_r.tStartRefresh)
thisExp.addData('inst_frame_r.stopped', inst_frame_r.tStopRefresh)
thisExp.addData('inst_screen_r.started', inst_screen_r.tStartRefresh)
thisExp.addData('inst_screen_r.stopped', inst_screen_r.tStopRefresh)
thisExp.addData('inst_txt_r.started', inst_txt_r.tStartRefresh)
thisExp.addData('inst_txt_r.stopped', inst_txt_r.tStopRefresh)
thisExp.addData('inst_swipe_r.started', inst_swipe_r.tStartRefresh)
thisExp.addData('inst_swipe_r.stopped', inst_swipe_r.tStopRefresh)
thisExp.addData('inst_frame_l.started', inst_frame_l.tStartRefresh)
thisExp.addData('inst_frame_l.stopped', inst_frame_l.tStopRefresh)
thisExp.addData('inst_screen_l.started', inst_screen_l.tStartRefresh)
thisExp.addData('inst_screen_l.stopped', inst_screen_l.tStopRefresh)
thisExp.addData('inst_txt_l.started', inst_txt_l.tStartRefresh)
thisExp.addData('inst_txt_l.stopped', inst_txt_l.tStopRefresh)
thisExp.addData('inst_swipe_l.started', inst_swipe_l.tStartRefresh)
thisExp.addData('inst_swipe_l.stopped', inst_swipe_l.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(swipe2_click.x): thisExp.addData('swipe2_click.x', swipe2_click.x[0])
if len(swipe2_click.y): thisExp.addData('swipe2_click.y', swipe2_click.y[0])
if len(swipe2_click.leftButton): thisExp.addData('swipe2_click.leftButton', swipe2_click.leftButton[0])
if len(swipe2_click.midButton): thisExp.addData('swipe2_click.midButton', swipe2_click.midButton[0])
if len(swipe2_click.rightButton): thisExp.addData('swipe2_click.rightButton', swipe2_click.rightButton[0])
if len(swipe2_click.time): thisExp.addData('swipe2_click.time', swipe2_click.time[0])
if len(swipe2_click.clicked_name): thisExp.addData('swipe2_click.clicked_name', swipe2_click.clicked_name[0])
thisExp.addData('swipe2_click.started', swipe2_click.tStart)
thisExp.addData('swipe2_click.stopped', swipe2_click.tStop)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "fixation_point"-------
t = 0
fixation_pointClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
fix_response = event.BuilderKeyResponse()
# keep track of which components have finished
fixation_pointComponents = [fix_frame_l, fix_screen_l, fix_cross_l, fix_frame_r, fix_screen_r, fix_cross_r, fix_response]
for thisComponent in fixation_pointComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "fixation_point"-------
while continueRoutine:
    # get current time
    t = fixation_pointClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *fix_frame_l* updates
    if t >= 0.0 and fix_frame_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_frame_l.tStart = t  # not accounting for scr refresh
        fix_frame_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_frame_l, 'tStartRefresh')  # time at next scr refresh
        fix_frame_l.setAutoDraw(True)
    
    # *fix_screen_l* updates
    if t >= 0.0 and fix_screen_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_screen_l.tStart = t  # not accounting for scr refresh
        fix_screen_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_screen_l, 'tStartRefresh')  # time at next scr refresh
        fix_screen_l.setAutoDraw(True)
    
    # *fix_cross_l* updates
    if t >= 0.0 and fix_cross_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_cross_l.tStart = t  # not accounting for scr refresh
        fix_cross_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_cross_l, 'tStartRefresh')  # time at next scr refresh
        fix_cross_l.setAutoDraw(True)
    
    # *fix_frame_r* updates
    if t >= 0.0 and fix_frame_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_frame_r.tStart = t  # not accounting for scr refresh
        fix_frame_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_frame_r, 'tStartRefresh')  # time at next scr refresh
        fix_frame_r.setAutoDraw(True)
    
    # *fix_screen_r* updates
    if t >= 0.0 and fix_screen_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_screen_r.tStart = t  # not accounting for scr refresh
        fix_screen_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_screen_r, 'tStartRefresh')  # time at next scr refresh
        fix_screen_r.setAutoDraw(True)
    
    # *fix_cross_r* updates
    if t >= 0.0 and fix_cross_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_cross_r.tStart = t  # not accounting for scr refresh
        fix_cross_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_cross_r, 'tStartRefresh')  # time at next scr refresh
        fix_cross_r.setAutoDraw(True)
    
    # *fix_response* updates
    if t >= 0.0 and fix_response.status == NOT_STARTED:
        # keep track of start time/frame for later
        fix_response.tStart = t  # not accounting for scr refresh
        fix_response.frameNStart = frameN  # exact frame index
        win.timeOnFlip(fix_response, 'tStartRefresh')  # time at next scr refresh
        fix_response.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(fix_response.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if fix_response.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            fix_response.keys = theseKeys[-1]  # just the last key pressed
            fix_response.rt = fix_response.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in fixation_pointComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fixation_point"-------
for thisComponent in fixation_pointComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('fix_frame_l.started', fix_frame_l.tStartRefresh)
thisExp.addData('fix_frame_l.stopped', fix_frame_l.tStopRefresh)
thisExp.addData('fix_screen_l.started', fix_screen_l.tStartRefresh)
thisExp.addData('fix_screen_l.stopped', fix_screen_l.tStopRefresh)
thisExp.addData('fix_cross_l.started', fix_cross_l.tStartRefresh)
thisExp.addData('fix_cross_l.stopped', fix_cross_l.tStopRefresh)
thisExp.addData('fix_frame_r.started', fix_frame_r.tStartRefresh)
thisExp.addData('fix_frame_r.stopped', fix_frame_r.tStopRefresh)
thisExp.addData('fix_screen_r.started', fix_screen_r.tStartRefresh)
thisExp.addData('fix_screen_r.stopped', fix_screen_r.tStopRefresh)
thisExp.addData('fix_cross_r.started', fix_cross_r.tStartRefresh)
thisExp.addData('fix_cross_r.stopped', fix_cross_r.tStopRefresh)
# check responses
if fix_response.keys in ['', [], None]:  # No response was made
    fix_response.keys=None
thisExp.addData('fix_response.keys',fix_response.keys)
if fix_response.keys != None:  # we had a response
    thisExp.addData('fix_response.rt', fix_response.rt)
thisExp.addData('fix_response.started', fix_response.tStartRefresh)
thisExp.addData('fix_response.stopped', fix_response.tStopRefresh)
thisExp.nextEntry()
# the Routine "fixation_point" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pretest = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('ImageConditions.xlsx'),
    seed=None, name='pretest')
thisExp.addLoop(pretest)  # add the loop to the experiment
thisPretest = pretest.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPretest.rgb)
if thisPretest != None:
    for paramName in thisPretest:
        exec('{} = thisPretest[paramName]'.format(paramName))

for thisPretest in pretest:
    currentLoop = pretest
    # abbreviate parameter names if possible (e.g. rgb = thisPretest.rgb)
    if thisPretest != None:
        for paramName in thisPretest:
            exec('{} = thisPretest[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "pre_cfs"-------
    t = 0
    pre_cfsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    # flash begin routine
    f_change = 0
    stim_image.setImage(Image)
    # keep track of which components have finished
    pre_cfsComponents = [stim_frame, stim_screen, flash_frame, flash_screen, stim_image, fix_cross_stim, fix_cross_flash]
    for thisComponent in pre_cfsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pre_cfs"-------
    while continueRoutine:
        # get current time
        t = pre_cfsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # flash each frame
        if frameN >= f_change:
            flash_change()
            myRand =randint(1,100)
            f_change += f_t
        flash.draw()
        
        # *stim_frame* updates
        if t >= 0.0 and stim_frame.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_frame.tStart = t  # not accounting for scr refresh
            stim_frame.frameNStart = frameN  # exact frame index
            win.timeOnFlip(stim_frame, 'tStartRefresh')  # time at next scr refresh
            stim_frame.setAutoDraw(True)
        if stim_frame.status == STARTED and frameN >= (stim_frame.frameNStart + total_t):
            # keep track of stop time/frame for later
            stim_frame.tStop = t  # not accounting for scr refresh
            stim_frame.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stim_frame, 'tStopRefresh')  # time at next scr refresh
            stim_frame.setAutoDraw(False)
        
        # *stim_screen* updates
        if t >= 0.0 and stim_screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_screen.tStart = t  # not accounting for scr refresh
            stim_screen.frameNStart = frameN  # exact frame index
            win.timeOnFlip(stim_screen, 'tStartRefresh')  # time at next scr refresh
            stim_screen.setAutoDraw(True)
        if stim_screen.status == STARTED and frameN >= (stim_screen.frameNStart + total_t):
            # keep track of stop time/frame for later
            stim_screen.tStop = t  # not accounting for scr refresh
            stim_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stim_screen, 'tStopRefresh')  # time at next scr refresh
            stim_screen.setAutoDraw(False)
        
        # *flash_frame* updates
        if t >= 0.0 and flash_frame.status == NOT_STARTED:
            # keep track of start time/frame for later
            flash_frame.tStart = t  # not accounting for scr refresh
            flash_frame.frameNStart = frameN  # exact frame index
            win.timeOnFlip(flash_frame, 'tStartRefresh')  # time at next scr refresh
            flash_frame.setAutoDraw(True)
        if flash_frame.status == STARTED and bool(stim_frame.status==FINISHED):
            # keep track of stop time/frame for later
            flash_frame.tStop = t  # not accounting for scr refresh
            flash_frame.frameNStop = frameN  # exact frame index
            win.timeOnFlip(flash_frame, 'tStopRefresh')  # time at next scr refresh
            flash_frame.setAutoDraw(False)
        
        # *flash_screen* updates
        if t >= 0.0 and flash_screen.status == NOT_STARTED:
            # keep track of start time/frame for later
            flash_screen.tStart = t  # not accounting for scr refresh
            flash_screen.frameNStart = frameN  # exact frame index
            win.timeOnFlip(flash_screen, 'tStartRefresh')  # time at next scr refresh
            flash_screen.setAutoDraw(True)
        frameRemains = 0.0 + stim_screen.status==FINISHED- win.monitorFramePeriod * 0.75  # most of one frame period left
        if flash_screen.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            flash_screen.tStop = t  # not accounting for scr refresh
            flash_screen.frameNStop = frameN  # exact frame index
            win.timeOnFlip(flash_screen, 'tStopRefresh')  # time at next scr refresh
            flash_screen.setAutoDraw(False)
        
        # *stim_image* updates
        if t >= before_t and stim_image.status == NOT_STARTED:
            # keep track of start time/frame for later
            stim_image.tStart = t  # not accounting for scr refresh
            stim_image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(stim_image, 'tStartRefresh')  # time at next scr refresh
            stim_image.setAutoDraw(True)
        if stim_image.status == STARTED and frameN >= (stim_image.frameNStart + stim_t):
            # keep track of stop time/frame for later
            stim_image.tStop = t  # not accounting for scr refresh
            stim_image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(stim_image, 'tStopRefresh')  # time at next scr refresh
            stim_image.setAutoDraw(False)
        if stim_image.status == STARTED:  # only update if drawing
            stim_image.setOpacity(((frameN - before_t) / fade_i_t) if (frameN < fade_i_end_t) else (1 if(frameN < fade_o_beg_t) else (fade_o_end_t - frameN) / fade_o_t), log=False)
        
        # *fix_cross_stim* updates
        if t >= 0.0 and fix_cross_stim.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix_cross_stim.tStart = t  # not accounting for scr refresh
            fix_cross_stim.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix_cross_stim, 'tStartRefresh')  # time at next scr refresh
            fix_cross_stim.setAutoDraw(True)
        if fix_cross_stim.status == STARTED and frameN >= (fix_cross_stim.frameNStart + total_t):
            # keep track of stop time/frame for later
            fix_cross_stim.tStop = t  # not accounting for scr refresh
            fix_cross_stim.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix_cross_stim, 'tStopRefresh')  # time at next scr refresh
            fix_cross_stim.setAutoDraw(False)
        
        # *fix_cross_flash* updates
        if t >= 0.0 and fix_cross_flash.status == NOT_STARTED:
            # keep track of start time/frame for later
            fix_cross_flash.tStart = t  # not accounting for scr refresh
            fix_cross_flash.frameNStart = frameN  # exact frame index
            win.timeOnFlip(fix_cross_flash, 'tStartRefresh')  # time at next scr refresh
            fix_cross_flash.setAutoDraw(True)
        if fix_cross_flash.status == STARTED and frameN >= (fix_cross_flash.frameNStart + total_t):
            # keep track of stop time/frame for later
            fix_cross_flash.tStop = t  # not accounting for scr refresh
            fix_cross_flash.frameNStop = frameN  # exact frame index
            win.timeOnFlip(fix_cross_flash, 'tStopRefresh')  # time at next scr refresh
            fix_cross_flash.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_cfsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pre_cfs"-------
    for thisComponent in pre_cfsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    pretest.addData('stim_frame.started', stim_frame.tStartRefresh)
    pretest.addData('stim_frame.stopped', stim_frame.tStopRefresh)
    pretest.addData('stim_screen.started', stim_screen.tStartRefresh)
    pretest.addData('stim_screen.stopped', stim_screen.tStopRefresh)
    pretest.addData('flash_frame.started', flash_frame.tStartRefresh)
    pretest.addData('flash_frame.stopped', flash_frame.tStopRefresh)
    pretest.addData('flash_screen.started', flash_screen.tStartRefresh)
    pretest.addData('flash_screen.stopped', flash_screen.tStopRefresh)
    pretest.addData('stim_image.started', stim_image.tStartRefresh)
    pretest.addData('stim_image.stopped', stim_image.tStopRefresh)
    pretest.addData('fix_cross_stim.started', fix_cross_stim.tStartRefresh)
    pretest.addData('fix_cross_stim.stopped', fix_cross_stim.tStopRefresh)
    pretest.addData('fix_cross_flash.started', fix_cross_flash.tStartRefresh)
    pretest.addData('fix_cross_flash.stopped', fix_cross_flash.tStopRefresh)
    # the Routine "pre_cfs" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "blank"-------
    t = 0
    blankClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    blankComponents = [blank_frame_l, balnk_frame_r, blank_screen_r, blank_screen_l]
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
        
        # *blank_frame_l* updates
        if t >= 0.0 and blank_frame_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_frame_l.tStart = t  # not accounting for scr refresh
            blank_frame_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(blank_frame_l, 'tStartRefresh')  # time at next scr refresh
            blank_frame_l.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank_frame_l.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            blank_frame_l.tStop = t  # not accounting for scr refresh
            blank_frame_l.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank_frame_l, 'tStopRefresh')  # time at next scr refresh
            blank_frame_l.setAutoDraw(False)
        
        # *balnk_frame_r* updates
        if t >= 0.0 and balnk_frame_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            balnk_frame_r.tStart = t  # not accounting for scr refresh
            balnk_frame_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(balnk_frame_r, 'tStartRefresh')  # time at next scr refresh
            balnk_frame_r.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if balnk_frame_r.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            balnk_frame_r.tStop = t  # not accounting for scr refresh
            balnk_frame_r.frameNStop = frameN  # exact frame index
            win.timeOnFlip(balnk_frame_r, 'tStopRefresh')  # time at next scr refresh
            balnk_frame_r.setAutoDraw(False)
        
        # *blank_screen_r* updates
        if t >= 0.0 and blank_screen_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_screen_r.tStart = t  # not accounting for scr refresh
            blank_screen_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(blank_screen_r, 'tStartRefresh')  # time at next scr refresh
            blank_screen_r.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank_screen_r.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            blank_screen_r.tStop = t  # not accounting for scr refresh
            blank_screen_r.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank_screen_r, 'tStopRefresh')  # time at next scr refresh
            blank_screen_r.setAutoDraw(False)
        
        # *blank_screen_l* updates
        if t >= 0.0 and blank_screen_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank_screen_l.tStart = t  # not accounting for scr refresh
            blank_screen_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(blank_screen_l, 'tStartRefresh')  # time at next scr refresh
            blank_screen_l.setAutoDraw(True)
        frameRemains = 0.0 + 1- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank_screen_l.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            blank_screen_l.tStop = t  # not accounting for scr refresh
            blank_screen_l.frameNStop = frameN  # exact frame index
            win.timeOnFlip(blank_screen_l, 'tStopRefresh')  # time at next scr refresh
            blank_screen_l.setAutoDraw(False)
        
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
    pretest.addData('blank_frame_l.started', blank_frame_l.tStartRefresh)
    pretest.addData('blank_frame_l.stopped', blank_frame_l.tStopRefresh)
    pretest.addData('balnk_frame_r.started', balnk_frame_r.tStartRefresh)
    pretest.addData('balnk_frame_r.stopped', balnk_frame_r.tStopRefresh)
    pretest.addData('blank_screen_r.started', blank_screen_r.tStartRefresh)
    pretest.addData('blank_screen_r.stopped', blank_screen_r.tStopRefresh)
    pretest.addData('blank_screen_l.started', blank_screen_l.tStartRefresh)
    pretest.addData('blank_screen_l.stopped', blank_screen_l.tStopRefresh)
    
    # ------Prepare to start Routine "pre_statement"-------
    t = 0
    pre_statementClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    statement_r.setText(Tweets)
    text_tweet_f1.setText(Tweets
)
    # setup some python lists for storing info about the response
    response.x = []
    response.y = []
    response.leftButton = []
    response.midButton = []
    response.rightButton = []
    response.time = []
    response.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    pre_statementComponents = [statement_frame_r, statement_screen_r, statement_r, statement_frame_l, statement_screen_l, text_tweet_f1, icon_frame_r, icon_screen_r, icon_frame_l, icon_screen_l, like_r, dislike_r, share_r, swipe_r, like_l, dislike_l, share_l, swipe_l, response]
    for thisComponent in pre_statementComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "pre_statement"-------
    while continueRoutine:
        # get current time
        t = pre_statementClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *statement_frame_r* updates
        if t >= 0.0 and statement_frame_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            statement_frame_r.tStart = t  # not accounting for scr refresh
            statement_frame_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(statement_frame_r, 'tStartRefresh')  # time at next scr refresh
            statement_frame_r.setAutoDraw(True)
        
        # *statement_screen_r* updates
        if t >= 0.0 and statement_screen_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            statement_screen_r.tStart = t  # not accounting for scr refresh
            statement_screen_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(statement_screen_r, 'tStartRefresh')  # time at next scr refresh
            statement_screen_r.setAutoDraw(True)
        
        # *statement_r* updates
        if t >= 0.0 and statement_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            statement_r.tStart = t  # not accounting for scr refresh
            statement_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(statement_r, 'tStartRefresh')  # time at next scr refresh
            statement_r.setAutoDraw(True)
        
        # *statement_frame_l* updates
        if t >= 0.0 and statement_frame_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            statement_frame_l.tStart = t  # not accounting for scr refresh
            statement_frame_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(statement_frame_l, 'tStartRefresh')  # time at next scr refresh
            statement_frame_l.setAutoDraw(True)
        
        # *statement_screen_l* updates
        if t >= 0.0 and statement_screen_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            statement_screen_l.tStart = t  # not accounting for scr refresh
            statement_screen_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(statement_screen_l, 'tStartRefresh')  # time at next scr refresh
            statement_screen_l.setAutoDraw(True)
        
        # *text_tweet_f1* updates
        if t >= 0.0 and text_tweet_f1.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_tweet_f1.tStart = t  # not accounting for scr refresh
            text_tweet_f1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_tweet_f1, 'tStartRefresh')  # time at next scr refresh
            text_tweet_f1.setAutoDraw(True)
        
        # *icon_frame_r* updates
        if t >= 0.0 and icon_frame_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            icon_frame_r.tStart = t  # not accounting for scr refresh
            icon_frame_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(icon_frame_r, 'tStartRefresh')  # time at next scr refresh
            icon_frame_r.setAutoDraw(True)
        
        # *icon_screen_r* updates
        if t >= 0.0 and icon_screen_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            icon_screen_r.tStart = t  # not accounting for scr refresh
            icon_screen_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(icon_screen_r, 'tStartRefresh')  # time at next scr refresh
            icon_screen_r.setAutoDraw(True)
        
        # *icon_frame_l* updates
        if t >= 0.0 and icon_frame_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            icon_frame_l.tStart = t  # not accounting for scr refresh
            icon_frame_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(icon_frame_l, 'tStartRefresh')  # time at next scr refresh
            icon_frame_l.setAutoDraw(True)
        
        # *icon_screen_l* updates
        if t >= 0.0 and icon_screen_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            icon_screen_l.tStart = t  # not accounting for scr refresh
            icon_screen_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(icon_screen_l, 'tStartRefresh')  # time at next scr refresh
            icon_screen_l.setAutoDraw(True)
        
        # *like_r* updates
        if t >= 0.0 and like_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            like_r.tStart = t  # not accounting for scr refresh
            like_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(like_r, 'tStartRefresh')  # time at next scr refresh
            like_r.setAutoDraw(True)
        
        # *dislike_r* updates
        if t >= 0.0 and dislike_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            dislike_r.tStart = t  # not accounting for scr refresh
            dislike_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(dislike_r, 'tStartRefresh')  # time at next scr refresh
            dislike_r.setAutoDraw(True)
        
        # *share_r* updates
        if t >= 0.0 and share_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            share_r.tStart = t  # not accounting for scr refresh
            share_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(share_r, 'tStartRefresh')  # time at next scr refresh
            share_r.setAutoDraw(True)
        
        # *swipe_r* updates
        if t >= 0.0 and swipe_r.status == NOT_STARTED:
            # keep track of start time/frame for later
            swipe_r.tStart = t  # not accounting for scr refresh
            swipe_r.frameNStart = frameN  # exact frame index
            win.timeOnFlip(swipe_r, 'tStartRefresh')  # time at next scr refresh
            swipe_r.setAutoDraw(True)
        
        # *like_l* updates
        if t >= 0.0 and like_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            like_l.tStart = t  # not accounting for scr refresh
            like_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(like_l, 'tStartRefresh')  # time at next scr refresh
            like_l.setAutoDraw(True)
        
        # *dislike_l* updates
        if t >= 0.0 and dislike_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            dislike_l.tStart = t  # not accounting for scr refresh
            dislike_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(dislike_l, 'tStartRefresh')  # time at next scr refresh
            dislike_l.setAutoDraw(True)
        
        # *share_l* updates
        if t >= 0.0 and share_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            share_l.tStart = t  # not accounting for scr refresh
            share_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(share_l, 'tStartRefresh')  # time at next scr refresh
            share_l.setAutoDraw(True)
        
        # *swipe_l* updates
        if t >= 0.0 and swipe_l.status == NOT_STARTED:
            # keep track of start time/frame for later
            swipe_l.tStart = t  # not accounting for scr refresh
            swipe_l.frameNStart = frameN  # exact frame index
            win.timeOnFlip(swipe_l, 'tStartRefresh')  # time at next scr refresh
            swipe_l.setAutoDraw(True)
        # *response* updates
        if t >= 0.0 and response.status == NOT_STARTED:
            # keep track of start time/frame for later
            response.tStart = t  # not accounting for scr refresh
            response.frameNStart = frameN  # exact frame index
            win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
            response.status = STARTED
            response.mouseClock.reset()
            prevButtonState = response.getPressed()  # if button is down already this ISN'T a new click
        if response.status == STARTED:  # only update if started and not finished!
            buttons = response.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    for obj in [like_r, like_l, dislike_r, dislike_l, share_r, share_l, swipe_r, swipe_l]:
                        if obj.contains(response):
                            gotValidClick = True
                            response.clicked_name.append(obj.name)
                    x, y = response.getPos()
                    response.x.append(x)
                    response.y.append(y)
                    buttons = response.getPressed()
                    response.leftButton.append(buttons[0])
                    response.midButton.append(buttons[1])
                    response.rightButton.append(buttons[2])
                    response.time.append(response.mouseClock.getTime())
                    if gotValidClick:  # abort routine on response
                        continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_statementComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "pre_statement"-------
    for thisComponent in pre_statementComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pretest.addData('statement_frame_r.started', statement_frame_r.tStartRefresh)
    pretest.addData('statement_frame_r.stopped', statement_frame_r.tStopRefresh)
    pretest.addData('statement_screen_r.started', statement_screen_r.tStartRefresh)
    pretest.addData('statement_screen_r.stopped', statement_screen_r.tStopRefresh)
    pretest.addData('statement_r.started', statement_r.tStartRefresh)
    pretest.addData('statement_r.stopped', statement_r.tStopRefresh)
    pretest.addData('statement_frame_l.started', statement_frame_l.tStartRefresh)
    pretest.addData('statement_frame_l.stopped', statement_frame_l.tStopRefresh)
    pretest.addData('statement_screen_l.started', statement_screen_l.tStartRefresh)
    pretest.addData('statement_screen_l.stopped', statement_screen_l.tStopRefresh)
    pretest.addData('text_tweet_f1.started', text_tweet_f1.tStartRefresh)
    pretest.addData('text_tweet_f1.stopped', text_tweet_f1.tStopRefresh)
    pretest.addData('icon_frame_r.started', icon_frame_r.tStartRefresh)
    pretest.addData('icon_frame_r.stopped', icon_frame_r.tStopRefresh)
    pretest.addData('icon_screen_r.started', icon_screen_r.tStartRefresh)
    pretest.addData('icon_screen_r.stopped', icon_screen_r.tStopRefresh)
    pretest.addData('icon_frame_l.started', icon_frame_l.tStartRefresh)
    pretest.addData('icon_frame_l.stopped', icon_frame_l.tStopRefresh)
    pretest.addData('icon_screen_l.started', icon_screen_l.tStartRefresh)
    pretest.addData('icon_screen_l.stopped', icon_screen_l.tStopRefresh)
    pretest.addData('like_r.started', like_r.tStartRefresh)
    pretest.addData('like_r.stopped', like_r.tStopRefresh)
    pretest.addData('dislike_r.started', dislike_r.tStartRefresh)
    pretest.addData('dislike_r.stopped', dislike_r.tStopRefresh)
    pretest.addData('share_r.started', share_r.tStartRefresh)
    pretest.addData('share_r.stopped', share_r.tStopRefresh)
    pretest.addData('swipe_r.started', swipe_r.tStartRefresh)
    pretest.addData('swipe_r.stopped', swipe_r.tStopRefresh)
    pretest.addData('like_l.started', like_l.tStartRefresh)
    pretest.addData('like_l.stopped', like_l.tStopRefresh)
    pretest.addData('dislike_l.started', dislike_l.tStartRefresh)
    pretest.addData('dislike_l.stopped', dislike_l.tStopRefresh)
    pretest.addData('share_l.started', share_l.tStartRefresh)
    pretest.addData('share_l.stopped', share_l.tStopRefresh)
    pretest.addData('swipe_l.started', swipe_l.tStartRefresh)
    pretest.addData('swipe_l.stopped', swipe_l.tStopRefresh)
    # store data for pretest (TrialHandler)
    if len(response.x): pretest.addData('response.x', response.x[0])
    if len(response.y): pretest.addData('response.y', response.y[0])
    if len(response.leftButton): pretest.addData('response.leftButton', response.leftButton[0])
    if len(response.midButton): pretest.addData('response.midButton', response.midButton[0])
    if len(response.rightButton): pretest.addData('response.rightButton', response.rightButton[0])
    if len(response.time): pretest.addData('response.time', response.time[0])
    if len(response.clicked_name): pretest.addData('response.clicked_name', response.clicked_name[0])
    pretest.addData('response.started', response.tStart)
    pretest.addData('response.stopped', response.tStop)
    # the Routine "pre_statement" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'pretest'


# ------Prepare to start Routine "Instructions"-------
t = 0
InstructionsClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
# setup some python lists for storing info about the swipe2_click
swipe2_click.x = []
swipe2_click.y = []
swipe2_click.leftButton = []
swipe2_click.midButton = []
swipe2_click.rightButton = []
swipe2_click.time = []
swipe2_click.clicked_name = []
gotValidClick = False  # until a click is received
# keep track of which components have finished
InstructionsComponents = [inst_frame_r, inst_screen_r, inst_txt_r, inst_swipe_r, inst_frame_l, inst_screen_l, inst_txt_l, inst_swipe_l, swipe2_click]
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
    
    # *inst_frame_r* updates
    if t >= 0.0 and inst_frame_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_frame_r.tStart = t  # not accounting for scr refresh
        inst_frame_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_frame_r, 'tStartRefresh')  # time at next scr refresh
        inst_frame_r.setAutoDraw(True)
    
    # *inst_screen_r* updates
    if t >= 0.0 and inst_screen_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_screen_r.tStart = t  # not accounting for scr refresh
        inst_screen_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_screen_r, 'tStartRefresh')  # time at next scr refresh
        inst_screen_r.setAutoDraw(True)
    
    # *inst_txt_r* updates
    if t >= 0 and inst_txt_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_txt_r.tStart = t  # not accounting for scr refresh
        inst_txt_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_txt_r, 'tStartRefresh')  # time at next scr refresh
        inst_txt_r.setAutoDraw(True)
    
    # *inst_swipe_r* updates
    if t >= 0.0 and inst_swipe_r.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_swipe_r.tStart = t  # not accounting for scr refresh
        inst_swipe_r.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_swipe_r, 'tStartRefresh')  # time at next scr refresh
        inst_swipe_r.setAutoDraw(True)
    
    # *inst_frame_l* updates
    if t >= 0.0 and inst_frame_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_frame_l.tStart = t  # not accounting for scr refresh
        inst_frame_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_frame_l, 'tStartRefresh')  # time at next scr refresh
        inst_frame_l.setAutoDraw(True)
    
    # *inst_screen_l* updates
    if t >= 0.0 and inst_screen_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_screen_l.tStart = t  # not accounting for scr refresh
        inst_screen_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_screen_l, 'tStartRefresh')  # time at next scr refresh
        inst_screen_l.setAutoDraw(True)
    
    # *inst_txt_l* updates
    if t >= 0 and inst_txt_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_txt_l.tStart = t  # not accounting for scr refresh
        inst_txt_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_txt_l, 'tStartRefresh')  # time at next scr refresh
        inst_txt_l.setAutoDraw(True)
    
    # *inst_swipe_l* updates
    if t >= 0.0 and inst_swipe_l.status == NOT_STARTED:
        # keep track of start time/frame for later
        inst_swipe_l.tStart = t  # not accounting for scr refresh
        inst_swipe_l.frameNStart = frameN  # exact frame index
        win.timeOnFlip(inst_swipe_l, 'tStartRefresh')  # time at next scr refresh
        inst_swipe_l.setAutoDraw(True)
    # *swipe2_click* updates
    if t >= 0.0 and swipe2_click.status == NOT_STARTED:
        # keep track of start time/frame for later
        swipe2_click.tStart = t  # not accounting for scr refresh
        swipe2_click.frameNStart = frameN  # exact frame index
        win.timeOnFlip(swipe2_click, 'tStartRefresh')  # time at next scr refresh
        swipe2_click.status = STARTED
        swipe2_click.mouseClock.reset()
        prevButtonState = swipe2_click.getPressed()  # if button is down already this ISN'T a new click
    if swipe2_click.status == STARTED:  # only update if started and not finished!
        buttons = swipe2_click.getPressed()
        if buttons != prevButtonState:  # button state changed?
            prevButtonState = buttons
            if sum(buttons) > 0:  # state changed to a new click
                # check if the mouse was inside our 'clickable' objects
                gotValidClick = False
                for obj in [inst_swipe_r, inst_swipe_l]:
                    if obj.contains(swipe2_click):
                        gotValidClick = True
                        swipe2_click.clicked_name.append(obj.name)
                x, y = swipe2_click.getPos()
                swipe2_click.x.append(x)
                swipe2_click.y.append(y)
                buttons = swipe2_click.getPressed()
                swipe2_click.leftButton.append(buttons[0])
                swipe2_click.midButton.append(buttons[1])
                swipe2_click.rightButton.append(buttons[2])
                swipe2_click.time.append(swipe2_click.mouseClock.getTime())
                if gotValidClick:  # abort routine on response
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
thisExp.addData('inst_frame_r.started', inst_frame_r.tStartRefresh)
thisExp.addData('inst_frame_r.stopped', inst_frame_r.tStopRefresh)
thisExp.addData('inst_screen_r.started', inst_screen_r.tStartRefresh)
thisExp.addData('inst_screen_r.stopped', inst_screen_r.tStopRefresh)
thisExp.addData('inst_txt_r.started', inst_txt_r.tStartRefresh)
thisExp.addData('inst_txt_r.stopped', inst_txt_r.tStopRefresh)
thisExp.addData('inst_swipe_r.started', inst_swipe_r.tStartRefresh)
thisExp.addData('inst_swipe_r.stopped', inst_swipe_r.tStopRefresh)
thisExp.addData('inst_frame_l.started', inst_frame_l.tStartRefresh)
thisExp.addData('inst_frame_l.stopped', inst_frame_l.tStopRefresh)
thisExp.addData('inst_screen_l.started', inst_screen_l.tStartRefresh)
thisExp.addData('inst_screen_l.stopped', inst_screen_l.tStopRefresh)
thisExp.addData('inst_txt_l.started', inst_txt_l.tStartRefresh)
thisExp.addData('inst_txt_l.stopped', inst_txt_l.tStopRefresh)
thisExp.addData('inst_swipe_l.started', inst_swipe_l.tStartRefresh)
thisExp.addData('inst_swipe_l.stopped', inst_swipe_l.tStopRefresh)
# store data for thisExp (ExperimentHandler)
if len(swipe2_click.x): thisExp.addData('swipe2_click.x', swipe2_click.x[0])
if len(swipe2_click.y): thisExp.addData('swipe2_click.y', swipe2_click.y[0])
if len(swipe2_click.leftButton): thisExp.addData('swipe2_click.leftButton', swipe2_click.leftButton[0])
if len(swipe2_click.midButton): thisExp.addData('swipe2_click.midButton', swipe2_click.midButton[0])
if len(swipe2_click.rightButton): thisExp.addData('swipe2_click.rightButton', swipe2_click.rightButton[0])
if len(swipe2_click.time): thisExp.addData('swipe2_click.time', swipe2_click.time[0])
if len(swipe2_click.clicked_name): thisExp.addData('swipe2_click.clicked_name', swipe2_click.clicked_name[0])
thisExp.addData('swipe2_click.started', swipe2_click.tStart)
thisExp.addData('swipe2_click.stopped', swipe2_click.tStop)
thisExp.nextEntry()
# the Routine "Instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
