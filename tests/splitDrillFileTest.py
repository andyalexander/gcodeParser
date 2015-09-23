__author__ = 'Andrew'
from splitDrillFile import splitDrillFile

path = r"../files"
fn = "reflow_controller.top.drill.gcode"
fnIn = path + '/' + fn

splitDrillFile(fnIn, True)
