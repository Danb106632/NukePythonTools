import nuke
import nukescripts
import os
import re
from os.path import normpath
from pathlib import PureWindowsPath


def WriteRead():
    executed = False

    for n in nuke.selectedNodes("Write"):
        executed = True
        folder = ''
        file = ''
        relative = False
        OgFile = ''
        sequence = False

        #Get Write Values
        xpos = int(n['xpos'].getValue())
        ypos = int(n['ypos'].getValue())

        filepath = str(n['file'].getText())
        colorspace = int(n['colorspace'].getValue())
        premultiplied = n['premultiplied'].getValue()
        raw = n['raw'].getValue()


        #If relative convert to absolute path
        if '..' in filepath:
            relative = True
            OgFile = filepath
            filepath = normpath(os.path.join(nuke.script_directory(), filepath))
            s = filepath.rsplit('\\', 1)
            folder = s[0] + '\\'
            file = s[1]
        else:
            s = filepath.rsplit('/', 1)
            folder = s[0] + '/'
            file = s[1]

        #get file range and set values
        for seq in nuke.getFileNameList(folder):
            if file in seq:
                split_seq = seq.rsplit(' ', 1)
                if len(split_seq) == 2:
                    if re.search('\d+-?\d+|\d+', split_seq[1]):
                        sequence = True
                        seq = split_seq[0]
            if seq == file:
                readNode = nuke.createNode('Read', inpanel=False)
                readNode['file'].fromUserText(folder + seq)


                readNode['xpos'].setValue(xpos)
                readNode['ypos'].setValue(ypos+60)
                readNode['colorspace'].setValue(colorspace)
                readNode['premultiplied'].setValue(premultiplied)
                readNode['raw'].setValue(raw)
                
                if(sequence):
                    if '-' in split_seq[1]:
                        frame_range = split_seq[1].split('-')
                    
                        readNode['first'].setValue(int(frame_range[0]))
                        readNode['last'].setValue(int(frame_range[1]))
                        readNode['origfirst'].setValue(int(frame_range[0]))
                        readNode['origlast'].setValue(int(frame_range[1]))
                        
                    else:
                        readNode['first'].setValue(int(split_seq[1]))
                        readNode['last'].setValue(int(split_seq[1]))
                        readNode['origfirst'].setValue(int(split_seq[1]))
                        readNode['origlast'].setValue(int(split_seq[1]))
                                                      
                #covert path back to relative - resets frame ranges
                if relative:
                    first = int(readNode['first'].getValue())
                    last = int(readNode['last'].getValue())
                    origfirst = int(readNode['origfirst'].getValue())
                    origlast = int(readNode['origlast'].getValue())

                    readNode['file'].fromUserText(OgFile)

                    readNode['first'].setValue(first)
                    readNode['last'].setValue(last)
                    readNode['origfirst'].setValue(origfirst)
                    readNode['origlast'].setValue(origlast)

    if not executed:
        nuke.message("No Write nodes selected!")


def WriteReadReplace():
    executed = False

    for n in nuke.selectedNodes("Write"):
        executed = True
        folder = ''
        file = ''
        relative = False
        OgFile = ''
        sequence = False

        #Get Write Values
        xpos = int(n['xpos'].getValue())
        ypos = int(n['ypos'].getValue())

        filepath = str(n['file'].getText())
        colorspace = int(n['colorspace'].getValue())
        premultiplied = n['premultiplied'].getValue()
        raw = n['raw'].getValue()


        #If relative convert to absolute path
        if '..' in filepath:
            relative = True
            OgFile = filepath
            filepath = normpath(os.path.join(nuke.script_directory(), filepath))
            s = filepath.rsplit('\\', 1)
            folder = s[0] + '\\'
            file = s[1]
        else:
            s = filepath.rsplit('/', 1)
            folder = s[0] + '/'
            file = s[1]

        #get file range and set values
        for seq in nuke.getFileNameList(folder):
            if file in seq:
                split_seq = seq.rsplit(' ', 1)
                if len(split_seq) == 2:
                    if re.search('\d+-?\d+|\d+', split_seq[1]):
                        sequence = True
                        seq = split_seq[0]
            if seq == file:
                readNode = nuke.createNode('Read', inpanel=False)
                readNode['file'].fromUserText(folder + seq)


                readNode['xpos'].setValue(xpos)
                readNode['ypos'].setValue(ypos+60)
                readNode['colorspace'].setValue(colorspace)
                readNode['premultiplied'].setValue(premultiplied)
                readNode['raw'].setValue(raw)
                
                if(sequence):
                    if '-' in split_seq[1]:
                        frame_range = split_seq[1].split('-')
                    
                        readNode['first'].setValue(int(frame_range[0]))
                        readNode['last'].setValue(int(frame_range[1]))
                        readNode['origfirst'].setValue(int(frame_range[0]))
                        readNode['origlast'].setValue(int(frame_range[1]))
                        
                    else:
                        readNode['first'].setValue(int(split_seq[1]))
                        readNode['last'].setValue(int(split_seq[1]))
                        readNode['origfirst'].setValue(int(split_seq[1]))
                        readNode['origlast'].setValue(int(split_seq[1]))
                                                      
                #covert path back to relative - resets frame ranges
                if relative:
                    first = int(readNode['first'].getValue())
                    last = int(readNode['last'].getValue())
                    origfirst = int(readNode['origfirst'].getValue())
                    origlast = int(readNode['origlast'].getValue())

                    readNode['file'].fromUserText(OgFile)

                    readNode['first'].setValue(first)
                    readNode['last'].setValue(last)
                    readNode['origfirst'].setValue(origfirst)
                    readNode['origlast'].setValue(origlast)

        nuke.delete(n)

    if not executed:
        nuke.message("No Write nodes selected!")


def PostageReplace():
    #Verify if read node is selected
    if len(nuke.selectedNodes()) > 1:
        nuke.message("Select one Read node!")
        return
    
    #Verify Node is selected
    ReadNode = nuke.selectedNode()
    if ReadNode.Class() != 'Read':
        nuke.message("No Read nodes selected!")
        return 

    postageName = nuke.getInput("Name for PostageStamps", "Scan")
    #If operation is cancelled or input is empty
    if postageName is None or postageName == '':
        return
    


    i = 0
    #Make sure that there will be no duplicate names
    for n in nuke.selectedNodes('Read'):
        if n['file'].getValue() == ReadNode['file'].getValue():
            name = ''
            if i == 0:
                name = postageName
            else:
                name = postageName+str(i)
            
            print(name)

            if nuke.exists(name):
                nuke.message(f"Node already exists called '{name}'. Make sure name is unique!")
                return
        
            i += 1

    nodename = "NoOp" if nuke.ask("Use NoOp?") else "PostageStamp"

    #Select By Class
    nuke.selectSimilar(0)
    ReadNode['selected'].setValue(False)

    executed = False

    j = 0
    for n in nuke.selectedNodes('Read'):
        #If filepath are the same, rest of the values should be
        if n['file'].getValue() == ReadNode['file'].getValue():
            executed = True

            #set selection to Read node
            nukescripts.clear_selection_recursive()
            n['selected'].setValue(True)

            
            #Copy pos and set knobs
            xpos = int(n['xpos'].value())
            ypos = int(n['ypos'].value())
            PS = nuke.createNode(nodename, inpanel=False)
            PS['xpos'].setValue(xpos)
            PS['ypos'].setValue(ypos)
            PS['hide_input'].setValue(True)
   
            #connect to Orignal read
            PS.setInput(0, ReadNode)

            # No duplicate names
            if j == 0:
                PS['name'].setValue(postageName)
            else:
                PS['name'].setValue(postageName+str(j))

            print(j)
            j += 1

            #Delete Read
            nuke.delete(n)

    #Reset Selection after changes
    nukescripts.clear_selection_recursive()
    ReadNode['selected'].setValue(True)

    if not executed:
        nuke.message("No Changes occured!")
    else:
        nuke.message("Changed!")