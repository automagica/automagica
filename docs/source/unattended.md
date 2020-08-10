# Running unattended automations
Running unattended automations on a Microsoft Windows machine requires an active desktop for the Automagica Bot to perform its activities. This can sometimes lead to issues as various mechanics designed by Microsoft cause the desktop to stop working. Here we provide some solutions/resolutions to resolve or mitigate these issues.

## Windows (Server 2016 R2)

If a connection with RDP closes, it could be that the desktop session is ended and therefore the Automagica Bot is unable to perform any actions requiring access to the Graphical User Interface (GUI). Therefore, a few things can be done to keep the desktop alive.

### Keep a Remote Desktop Connection open
One solution is to keep a Remote Desktop Connection open from another machine or another server. For example:

```
Machine 1: Bot's working environment
Machine 2: arbitrary machine

2 connects with Remote Desktop Protocol to 1
```

### Modifying the registry for minimized RDP sessions
Modify the `HKEY_CURRENT_USER\Software\Wow6432Node\Microsoft\Terminal Server Client` key by adding a new DWORD value with the name `RemoteDesktop_SuppressWhenMinimized`. Edit the DWORD value as Hexadecimal and enter `2` as data. Reboot the machine.

### Automatic logon for Windows
Try this resolution from [Microsoft's documentation](https://support.microsoft.com/en-us/help/324737/how-to-turn-on-automatic-logon-in-windows)

### Other solutions worth trying
[Minizmed window by Smartbear](https://support.smartbear.com/testcomplete/docs/testing-with/running/via-rdp/in-minimized-window.html)

[Keeping computer unlocked by Smartbear](https://support.smartbear.com/testcomplete/docs/testing-with/running/via-rdp/keeping-computer-unlocked.html)