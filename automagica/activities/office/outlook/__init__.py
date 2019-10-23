def _start_outlook():
    """Utility function to create the Outlook application scope object

    :return: Application object (win32com.client)
    """
    try:
        import win32com.client

        outlook = win32com.client.Dispatch("outlook.application").GetNamespace("MAPI")

    except:
        raise Exception(
            "Could not launch Outlook, do you have Microsoft Office installed on Windows?"
        )

    return outlook


def send(to_address, subject, body, html_body=None, attachment_paths=None):
    """Send an e-mail with Outlook.

    :param to_address: The e-mail address the e-mail should be sent to
    :param subject: The subject of the e-mail
    :param body: The text body contents of the e-mail
    :param html_body: The HTML body contents of the e-mail (optional)
    :param attachment_paths: List of file paths to attachments
    """
    try:
        import win32com.client

        outlook = win32com.client.Dispatch("outlook.application")

    except:
        raise Exception(
            "Could not launch Outlook, do you have Microsoft Office installed on Windows?"
        )

    # Create a new e-mail
    mail = outlook.CreateItem(0)

    mail.To = to_address
    mail.Subject = subject
    mail.Body = body

    if html_body:
        mail.HTMLBody = html_body

    # Add attachments
    if attachment_paths:
        for attachment_path in attachment_paths:
            mail.Attachments.Add(attachment_path)

    # Send the e-mail
    mail.Send()


def get_folders(limit=100):
    """Retrieve list of folders from Outlook

    :param limit: Maximum number of folders to retrieve
    """
    outlook = _start_outlook()

    folders = []

    for i in range(limit):
        try:
            box = outlook.GetDefaultFolder(i)
            name = box.Name
            folders.append(name)
        except:
            pass

    return folders


def get_messages(folder_name="Inbox", limit=10, fields=None):
    """Retrieve list of messages from Outlook
    
    :param folder_name: Name of the Outlook folder, can be found using :function:`get_folders`.
    :param limit: Number of messages to retrieve

    :return: List of dictionaries containing the e-mail messages with from, to, subject, body and html.
    """

    if not fields:
        fields = ("To", "Subject", "Body", "SentOn")

    messages = []

    outlook = _start_outlook()

    # Find the appropriate folder
    for i in range(limit):
        try:
            box = outlook.GetDefaultFolder(i)
            name = box.Name
            if name == folder_name:
                break
        except:
            pass
    else:
        raise Exception("Could not find the folder with name '{}'.".format(folder_name))

    # Loop over the items in the folder
    for item in box.Items:
        try:
            message = {}

            for key in item._prop_map_get_:
                if key in fields:
                    message[key] = getattr(item, key)

            messages.append(message)

        except:
            pass

    return messages


def save_attachments(folder_name="Inbox", target_folder_path=None):
    """Save all attachments from Outlook

    :param folder_name: Name of the Outlook folder, can be found using :function:`get_folders`.

    :return: List of paths to saved attachments.
    """
    import os

    paths = []

    # Set to user home if no path specified
    if not target_folder_path:
        target_folder_path = os.path.expanduser("~")

    outlook = _start_outlook()

    # Find the appropriate folder
    for i in range(999):
        try:
            box = outlook.GetDefaultFolder(i)
            name = box.Name
            if name == folder_name:
                break
        except:
            pass
    else:
        raise Exception("Could not find the folder with name '{}'.".format(folder_name))

    # Loop over the items in the folder
    for item in box.Items:
        for attachment in item.Attachments:
            path = os.path.join(target_folder_path, attachment.FileName)
            attachment.SaveAsFile(path)
            paths.append(path)

    return paths


def get_contacts(limit=9999, fields=None):
    """Retrieve list of contacts from Outlook
    
    :return: List of dictionaries containing the e-mail messages with from, to, subject, body and html.
    """
    import win32com.client

    if not fields:
        fields = ("LastName", "FirstName", "Email1Address")

    contacts = []

    outlook = win32com.client.gencache.EnsureDispatch(
        "Outlook.Application"
    ).GetNamespace("MAPI")

    data = outlook.GetDefaultFolder(win32com.client.constants.olFolderContacts)

    for item in data.Items:
        if item.Class == win32com.client.constants.olContact:
            contact = {}
            for key in item._prop_map_get_:
                if key in fields:
                    if isinstance(getattr(item, key), (int, str)):
                        contact[key] = getattr(item, key)
            contacts.append(contact)

    return contacts


def create_contact(email, first_name="", last_name=""):
    """Create a contact in Outlook

    :param email: The e-mail address for the contact
    :param first_name: First name for the contact (optional)
    :param last_name: Last name for the contact (otpional)
    """
    try:
        import win32com.client

        outlook = win32com.client.Dispatch("outlook.application")

    except:
        raise Exception(
            "Could not launch Outlook, do you have Microsoft Office installed on Windows?"
        )

    # Create a new contact
    contact = outlook.CreateItem(2)

    contact.Email1Address = email

    if first_name:
        contact.FirstName = first_name

    if last_name:
        contact.LastName = last_name

    contact.Save()
