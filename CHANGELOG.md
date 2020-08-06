# Changelog

All notable changes to Automagica are documented per version and product here.

## 3.0.5
### Automagica Flow
- Added icons to the selection menu on the left for activities
- Fixed a bug with auto-save not functioning properly
- Increased interval for auto-save and state checking for undo (CTRL+Z), should now happen every 100 ms
- New nodes without selection are added in the center of the canvas
- Added warning when closing a Flow without saving

### Automagica activities
- Added parameters to press_key activity 

## 3.0.4
### Automagica Flow
- Added user selectable delay for Automagica Wand (0 to 5 seconds)
- Added help information for object variables to the properties window for activity classes (for example Chrome's object variable)
- Pressing the delete button will now delete the selected element
- Record new Automagica ID/element in properties window of an Automagica Wand activity (click, doubleclick, ...)
- Added empty option to node selection menues so it becomes easier to clear connections
- Added "on exception node" to activity nodes
- Fixed bug with empty arguments for activities (fe third key in 'press key combination')
- Fixed bug where sometimes nodes would not be connected when adding them to a selection
- Increased parameters field size for certain activity


### Automagica Windows installer
- File size reduced with 20MB (100MB to 80MB) by removing unnecessary files

### Automagica activities
- Fixed Excel.get_table for Flow by adding return variable in the docstring
- Fixed issue with read text activity (OCR)

### Automagica CLI
- Added delay parameter option for Wand

### Automagica installer
- Shortcuts will now be properly removed on running uninstall (Windows)

## 3.0.3
### Automagica Flow
- Newly added nodes will start from the selected nodes
- Added protocol handlers for automagica:// both for Flow and Lab.

## 3.0.2
### Automagica Flow
- Added Undo <kbd>ctrl+z</kbd> feature.
- Connectors can now also be removed by right-clicking on them and selecting delete.
- The variable explorer window is now resizable. We're still looking how to further improve this. Any ideas are more than welcome.
- Loop node properties window is now more straightforward.
- Flow execution now stops when an exception occurs in an activity node.

### Automagica Wand
- Pressing <kbd>Return</kbd> now saves the UI element.
- Saved UI elements are now private by default and can be managed through the Automagica Portal.

### Automagica Lab
- Activity selection menu was removed as it contained outdated information.

## 3.0.1
- Added __Automagica Flow__, a new low-code/no-code way of building Python automations with a visual flow-chart style.
- Added the __Automagica Command Line Interface (CLI)__ with click. Now you can run the `automagica` command from within the console to access the Automagica Bot, Flow, Lab and Wand. We also included a configuration wizard for your convenience. 

The changelog is kept starting from version 3.0.0