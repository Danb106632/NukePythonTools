import nuke
import nukescripts
import os

import writeRead
from customSettings import *

nuke.pluginAddPath('./icons')

DansToolkit = nuke.menu('Nodes').addMenu('Dan\'s Toolkit', icon='toolbox_icon.png')
DansToolkit.addCommand('ReadWrite', writeRead.WriteRead, 'Ctrl+R', icon='Read.png', index=-1)
DansToolkit.addCommand('ReadWriteReplace', writeRead.WriteReadReplace, 'Ctrl+Alt+R', icon='Read.png', index=-1)
DansToolkit.addCommand('PostageReplace', writeRead.PostageReplace, '', icon='PostageStamp.png', index=-1)


