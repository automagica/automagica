# Running unattended automations
Some functionalities that Automagica offers, mostly those that rely on computer vision or OCR, require an active desktop. This can sometimes lead to issues on virtualized environments (servers, VMWare, Virtualbox, Hyper-V, ...) where no computer display is present and the only way of interacting with the machine is through a remote desktop connection. This sometimes causes problems on Microsoft operating systems as various mechanics designed by Microsoft cause the desktop to stop working or group policies set-up within an organization which cause the connection to be closed after a specific amount of time, or example Remote Desktop connections going stale or not rendering a desktop at all. To mitigate or resolve these issues, we provide some solutions here.

## Problem description
If the Remote Desktop Protocol connection closes to a virtualized desktop on Windows Server or Windows 10, it could be that the desktop session is ended on the side of the Automagica Bot and this causes the bot to be unable to perform any actions requiring access to the visual layer of the Graphical User Interface (GUI). 

## Option 1: Keep the Remote Desktop Connection open
The easiest way is to keep the Remote Desktop alive for the robot to work, is to keep a Remote Desktop Connection open from another machine. 

For example:

```
Machine 1: Bot's working environment
Machine 2: Other machine

Machine 2 connects with Remote Desktop Protocol to machine 1.
```
To recap, Machine 1 can be viewed and controlled from Machine 2. Once Machine 2 is restarted or the user session is ended in which the Remote Desktop Connections were made, the Remote Desktop connection will close and the session on Machine 1 becomes unresponsive.

The same can be done for multiple machines, but you can have the same machine (for example Machine 2) have multiple connections open at the same time, as long as the Remote Desktop Connection windows are not minimized.

___Important note:__ the Remote Desktop window cannot be minimized unless some registry values are modified. The default behavior or Microsoft Remote Desktop is that once the window becomes minimized on the client side, the server side stops rendering the visual desktop and therefore the Automagica Bot can no longer access this visual layer. The screen becomes essentially black from the Bot's perspective.__

### Modifying the registry for allowing minimized RDP sessions to continue rendering
_Important note_: in practice, we have seen mixed results for changing these registry values and modifying them poses no guarantee that Microsoft's Remote Desktop actually respects these settings. Please test whether the expected behaviour manifests.

Modify the `HKEY_CURRENT_USER\Software\Wow6432Node\Microsoft\Terminal Server Client` key by adding a new DWORD value with the name `RemoteDesktop_SuppressWhenMinimized`. Edit the DWORD value as Hexadecimal and enter `2` as data. Reboot the machine.

## Option 2: Set-up a VNC server
Another possible solution, and probably the most robust, is to set-up a VNC server on the Automagica Bot's machine. As a VNC server functions differently from Microsoft's Remote Desktop, it creates a virtual display driver which remains active even when the remote connection is closed or a client window is minimized. This also provides the most robust way of creating a stable and predictable environment for the Automagica Bot to work with as the display resolution remains consistent across sessions.

Some VNC server solutions:

- [TigerVNC](https://tigervnc.org/) (open source)
- [UltraVNC](https://www.uvnc.com/) (open source)
- [TightVNC](https://www.tightvnc.com/) (open source)
- [RealVNC](https://www.realvnc.com/en/) (open source/proprietary)
- [TurboVNC](https://www.turbovnc.org/) (open source)

___Important note 1:__ we are not affiliated, associated, authorized, endorsed by, or in any way officially connected with any of the proposed solutions_

___Important note 2:__ the VNC protocol has some inherent security flaws, however, there are solutions to mitigate most of the security risks involved, such as choosing a strong password or encrypting the connection with SSH tunnels. More details can be found [here](https://www.bleepingcomputer.com/news/security/dozens-of-vnc-vulnerabilities-found-in-linux-windows-solutions/)_

___Important note 3:__ it is possible that the VNC server configuration conflicts with Microsoft's Remote Desktop, so make sure that you are not locked out of the machine. Connecting through Remote Desktop might also conflict with the VNC Server, so it is advisable to connect only through VNC if this solution is implemented._

### Setting up OpenSSH on Windows Server
To provide an additional security layer on top of VNC, one can use an encrypted SSH tunnel to connect to the VNC server. To install the OpenSSH Client/Server component in Windows Server and Windows 10, please follow [Microsoft's documentation on installing OpenSSH](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse).


## Option 3: Set-up a virtual display in your virtualization environment
Most virtualization software packages have the option to add a virtual display. Please consult the documentation of your virtualization technology provider to find instructions on how to enable such a virtual display driver. This virtual display provides the Automagica Bot with a persistent visual desktop.

Some popular links:

- [Configure Display Settings for a Virtual Machine with VMWare](https://docs.vmware.com/en/VMware-Workstation-Player-for-Windows/15.0/com.vmware.player.win.using.doc/GUID-FF434E5C-2FEE-48C9-BEAF-943F0536301E.html)
- [Display adapters should be enabled in virtual machines to provide video capabilities (Microsoft Hyper-V)](https://docs.microsoft.com/en-us/windows-server/virtualization/hyper-v/best-practices-analyzer/display-adapters-should-be-enabled-in-virtual-machines-to-provide-video)
- [How to Fix VirtualBox Video Driver Problems in Windows 10](https://windowsreport.com/virtualbox-video-driver-problem-windows-10/)
- [How to connect to a VirtualBox VM desktop remotely](https://www.techrepublic.com/article/how-to-connect-to-a-virtualbox-vm-desktop-remotely/)

___Important note:__ note 3 for VNC also applies here, the virtual display driver might conflict with Remote Desktop connections. It is advisable to use the virtual display provided by the virtualization provider rather than Remote Desktop connection to interact with the Automagica Bot._

# Error: VCRUNTIME140.dll missing
Install the Visual C++ runtime from Microsoft: https://www.microsoft.com/en-us/download/details.aspx?id=48145 and try re-installing.