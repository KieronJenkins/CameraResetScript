import maya.cmds as cmds
import maya.OpenMaya as om

def maya_camera_clipping():
	cmds.viewClipPlane("frontShape", ncp="1", fcp = "100000.0") # To change the clipping planes, change the numbers inbetween the " " to what you need
	cmds.viewClipPlane("perspShape", ncp="1", fcp = "100000.0") # ncp = near clip plane // fcp = far clip plane
	cmds.viewClipPlane("sideShape", ncp="1", fcp = "100000.0")
	cmds.viewClipPlane("topShape", ncp="1", fcp = "100000.0")
	cmds.delete(constructionHistory = True) # Delete this if you don't want to delete history
	om.MGlobal.displayWarning("Cameras Updated") # Displays warning to confirm cameras have changed


    
maya_camera_clipping()

# Set Up: Create a custom button in your shelf editor then Set to Python and then copy paste the above in and save
