# cod-hud-builder
Quickly design the layout for your new cod hud.

Beta version 1.0
-bugs to be expected
-will try to make small updates here and there

Feel free to share, modify etc

No credit necessary, Enjoy!

-Phil81334 (CME)

###################
Tested with waw and bo1, works fine in both. 
Will do a cod4 test at some point when i re-install it.

-BO1 note:
  dont use 'UI_FONT_OBJECTIVE' as thats a waw specific font
  
-Elem note:
  I initially removed the Button elem as this tool is a hud builder, not a menu builder, but someone asked me to put it back in for them.
  You should only worry about using the Text/Material elems (unless you know what you're doing).
###################

###################
Link to .exe: [29-04-23]
https://mega.nz/file/sphQmYYJ#rbXujys4pk6Fn7i4KzmbIB11LKX4SQVyrEsq5A4NRwU
###################

###################
Overview: (1hr) [25-04-23]
https://www.youtube.com/watch?v=nqlbc8oprK0&ab_channel=PhilGibson

Showcase example test: (1hr+) [27-04-23]
https://www.youtube.com/watch?v=JV0oycK8gHo&ab_channel=PhilGibson

Result of above example test: [27-04-23]
https://imgur.com/UBKp26F
###################

###################
To Fix:
-text align not saving [Done ~ 29-04-23]
  will auto adjust until manually overridden
  
-account for when user uses colons on text elems [Done ~ 29-04-23]
  '¬' is a reserved program keyword now. if you wish to use it, then you need to do so in the generated file, not the program.
 
 -button elem arg indentation in generated file
###################

###################
Updated:
-button elem args for: (action, mouseEnter, mouseExit), now go on seperate lines [29-04-23]
  you need to seperate each arg via the '~' symbol

-save feature will now also store: [29-04-23]
  text elem:
    visible
    textfont
    textscale
    textstyle
    textalign
    decoration
    forecolor
  material elem:
    visible
    forecolor
###################
