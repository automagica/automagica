# Automagica Flow

## Introduction
Automagica Flow allows you to build software robots with a visual interface. Automagica Flow is the best and easiest way to get started building software automations.

## Getting started
You can get started with Automagica Flow either by:
- double-clicking the shortcut on your desktop after installation (Windows One-Click installer)
- by running the `automagica flow new` command in the command line
- by starting Automagica Flow in the [portal](https://www.portal.automagica.com) (Windows One-Click installer)
- if you have Automagica installed on this machine through our one-click installer, you can also start Automagica Flow by clicking [here](automagica://flow/new)

## Inserting activities

You can use the activity search to look for predefined activities, for example if you want to automate Excel you can look for all Excel-related activities by entering a keyword in the search. 
Double click the activity to insert it in the canvas. If you first select a node (blue outline) and then insert an activity, the next activity wil automatically be connected to the one selected.

![Search video](https://i.imgur.com/hGbnpNJ.gifv)

Options for a node can be opened by double-clicking on the node in the canvas. This will reveal the parameters to configure the node. Parameters are divided in two blocks: 'options' and 'node'.

- __Options__: These parameters are activity specific. Some activities require certain parameters to work and parameter will be indicated with (required). Others are optional and can range from changing the behavior to selecting paths for in- or output for example.
  - __Return variable__: Whenever this field is available for an activity this means there is some sort of output which can be stored in a variable. It is recommended to enter a variable name in this field as it allows you to use this value in consecutive nodes. These variables can be viewed at any time through the variable explorer.
- __Node__: Node options are available for most nodes.
  - __Unique ID__: Each node has a unique ID which can be seen either in the parameters or in the canvas. Can not be changed.
  - __Label__: Custom name for the node. It is recommended to give activities a more specific name, as it helps with debugging larger automations on multiple levels.
  - __Next Node__: Automated Flows follow the activities on the canvas, to change the order of occurrence you can use this option to select the next node. 
  - __On Exception Node__: Whenever something goes wrong in an activity (e.g. Wand was not able to find an element, Excel could not be started, ..) there is the possibility to reroute to another node. If an Exception occurs without specifying an Exception node, the Flow will stop and raise an Exception. Exception details are visible in the console when running with Automagica Flow, or in the Logs when running through Automagica Portal.

![Options video](https://i.imgur.com/OYegXlL.gifv)

## Special nodes

Special nodes are designed to add flexibility to automations, something that is typically not possible with a one dimensional automation script. Down below an overview of the different Nodes:

- __Start__: Entry point for your automation, activity following this node will be the first action.
- __If Else__: Conditional Node to split a flow based on a condition. Conditions can included earlier set variables.
- __Python Script__: Python allows you to import a Python (.py) file in your workflow. This allows the user to fully integrate Python code for more complex parts of an automation (e.g. complex data transformation or usage of third-party libraries).
- __Sub Flow__: Allows to insert a Sub Flow. Can be used to split large flows in to re-usable parts to keep things organized. 
- __Python Code__: Python Code is similar to Python Script node, except that instead of importing a file it opens a small editor to write custom Python code. Variables are shared with Automagica Flow and allows sharing of variables.

## Running and debugging

Running (parts of) your Flow can be done in one of the following methods:

- The green 'Run Flow' button in the top runs all steps in the Automation beginning at from the 'Start' node. A popup will show the progress and current step of the Flow
- 'Run step-by-step' also starts at the 'Start' node but pauses after each node, waiting for the user to specifically press 'continue' in a popup to advance to the next step. Can be used for debugging and development, variable explorer and command line can be used while paused.
- Clicking the play icon in the upper right corner of a node will only execute that specific node

## Using the integrated command line

The integrated command line allows you to write and debug Python code in the same environment as where the activities are performed. Information is shown here and exceptions are raised similar to working with Python in a command line or developers tools like IPython or Jupyter Notebooks.

When running a node you can see the equivalent Python command with your parameters in the command line. You can also use the command line to explore or manipulate variables, run activities ad-hoc, import third party Python libraries or write Python code (similar to using a 'Python Script' or 'Python Code' - Node).

![Command line video](https://i.imgur.com/hGbnpNJ.gifv)

## Variable Explorer

Activities that have a 'Return variable' can hold different types of variables (integer, float, string, ..). The variable explorer gives you an easy overview of the assigned variables at that specific moment.
Resetting the bot will clear all variables.



## Tips and tricks using the canvas

- Once nodes are inserted you can move them around while holding middle mouse button
- Double clicking opens up the properties
- Middle mouse click deletes a node. Alternatively you can press delete after selecting a node to delete a node.
- Holding shift allows you to select, move/delete multiple nodes at once with the left mouse button.
- Keyboard shortcut 'ctrl + z' allows for undo
- Once a node is selected, newly inserted nodes will automatically be connected to the selected node

## Examples
Be sure to check out the following videos on our YouTube channel for some hands-on examples and tutorials with Automagica Flow:

[![Automate the browser using Excel and Automagica](https://img.youtube.com/vi/MVBvqlPn518/0.jpg)](https://www.youtube.com/watch?v=MVBvqlPn518)

[![Robots reply your e-mail with Automagica Open Source Robotic Process (RPA) Software](https://img.youtube.com/vi/8x-bIpWcumw/0.jpg)](https://www.youtube.com/watch?v=8x-bIpWcumw)

[![Automate mouse clicks using AI with Automagica](https://img.youtube.com/vi/3QPevxV0dy4/0.jpg)](https://www.youtube.com/watch?v=3QPevxV0dy4)

## Deployment
Once your Automagica Flow is finished, you can upload it to the [Automagica Portal](portal.md) to either start it by a schedule or by other triggers such as by sending an e-mail or by a REST API-call.

