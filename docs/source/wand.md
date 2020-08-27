# Automagica Wand

An easy way to interact with UI elements on the screen is to use Automagica Wand. For convenience, the main Wand activities are shown in the upper panel of Automagica Flow. 
Wand uses machine learning algorithms to look for elements on the screen that were recorded, which allows you to build robust automations using the GUI. This is different from comparing pixels as Wand mimics the way people use elements to navigate. For example, Just like humans, Wand can still find a button even if it is on a different place on the screen or if it changed slightly (e.g. screen resolution changed, button text is slightly different, color/theme variation, ..). 

## Automagica Wand in Automagica Flow

- by running the `automagica wand` command in the command line
- by starting Automagica Wand in the [UI elements section of the portal](https://portal.automagica.com/ui-element/) (Windows One-Click installer)
- if you have Automagica installed on this machine through our one-click installer, you can start Automagica Wand activities in the top bar of [Automagica Flow](automagica://flow/new)

Automagica Wand can be useful for different kinds of activities:

- Clicking: Move the mouse or (double) click elements with Automagica Wand 
- Typing: Data entry in all kinds of editable fields, note that most of the time input fields are only distinguishable by using the anchoring feature
- Read Text: Use Wand in combination with OCR to read text directly from the screen. Note this activity requires you to use anchors to work properly
- Element existence: Use wand to validate the existence/absence of a certain element, e.g. continue when loading screen is over

## Example

Let's say we want to click on the desktop recycle bin icon using Automagica Wand. In this example we will use Automagica Flow to record and run the example. As an illustration of the robustness we will empty the recycle bin and move the element on the screen after recording with Automagica Wand. Emptying the recycle bin causes the icon to slightly change in Windows, which would mean it would not be recognizable anymore with traditional pixel-comparison methods.

[Automagica Wand video](https://i.imgur.com/G5AeFXL.gifv)


## Anchoring

After selecting an element there is an option to add an anchor. An anchor is an unambiguous element on the screen that always has the same relative position to the element you want to reach. 
Take the example of a form with two identical input fields down below. 

<html>
<style>
  .anchor {
    width: 105px;
    padding: 5px;
    border: 3px solid #2196f3;
    border-radius: 8px;
  }
  .target {
    width: 175px;
    padding: 5px;
    border: 3px solid red;
    border-radius: 8px;
  }
</style>

 <body>
  <form id="loginForm">
<div class="target">
   <input name="username" type="text" />
</div>
   <input name="password" type="password" />
<div class="anchor">
   <input name="continue" type="submit" value="Login" />
   <input name="continue" type="button" value="Clear" />
</div>
  </form>
</body>
<html>

&nbsp;

If we wanted to point to the field outlined in red and were to simply record this field as a target, it could be mistaken by the second identical input field. 
A solution would be to anchor the Login / Clear button (outlined in blue). The bot would then look for this anchor and move to the element based on the _relative position to this anchor_. 


## Tips and Tricks

Elements can be viewed within the Portal and are shared with team members if a bot is shared. This allows you to record, develop and run on different machines. In the Automagica Portal you can see counters successful detections and failed detections, quickly allowing you to debug automations and clean recorded elements that are not in use. 

Each element has a unique ID, entering this ID in a suitable activity will automatically point the robot to this element.

[My Ui elements portal video](https://i.imgur.com/BjN7Fms.gifv)

__Note__: To use Automagica Wand you need an API key, which is automatically installed and configured if you use the Windows one-click-installer. Screen data gets send to the Automagica servers where the ML algorithms analyse the screen. You can view and edit your elements and data in the Automagica Portal, which is connected with your API key. If you want to use Automagica Wand while keeping your promise within your network, we can help you set up a commercial [on-premise deployment.](https://automagica.com/contact/)