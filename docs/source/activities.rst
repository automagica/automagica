.. module:: automagica.activities

Activities
==========



Cryptography
------------
.. autofunction:: generate_random_key
.. autofunction:: encrypt_text_with_key
.. autofunction:: decrypt_text_with_key
.. autofunction:: encrypt_file_with_key
.. autofunction:: decrypt_file_with_key
.. autofunction:: generate_key_from_password
.. autofunction:: generate_hash_from_file
.. autofunction:: generate_hash_from_text


Random
------
.. autofunction:: generate_random_number
.. autofunction:: generate_random_boolean
.. autofunction:: generate_random_name
.. autofunction:: generate_random_sentence
.. autofunction:: generate_random_address
.. autofunction:: generate_random_beep
.. autofunction:: generate_random_date
.. autofunction:: generate_unique_identifier


User Input
----------
.. autofunction:: ask_user_input
.. autofunction:: ask_user_password
.. autofunction:: ask_credentials
.. autofunction:: display_message_box
.. autofunction:: display_osd_message


Browser
-------
.. autoclass:: Chrome
   :members:


Credential Management
---------------------
.. autofunction:: set_credential
.. autofunction:: delete_credential
.. autofunction:: get_credential


FTP
---
.. autoclass:: FTP
   :members:


Keyboard
--------
.. autofunction:: press_key
.. autofunction:: press_key_combination
.. autofunction:: typing


Mouse
-----
.. autofunction:: get_mouse_position
.. autofunction:: display_mouse_position
.. autofunction:: click
.. autofunction:: double_click
.. autofunction:: right_click
.. autofunction:: move_mouse_to
.. autofunction:: move_mouse_relative
.. autofunction:: drag_mouse_to


Image
-----
.. autofunction:: random_screen_snippet
.. autofunction:: take_screenshot
.. autofunction:: click_image
.. autofunction:: double_click_image
.. autofunction:: right_click_image
.. autofunction:: locate_image_on_screen


Folder Operations
-----------------
.. autofunction:: get_files_in_folder
.. autofunction:: create_folder
.. autofunction:: rename_folder
.. autofunction:: show_folder
.. autofunction:: move_folder
.. autofunction:: remove_folder
.. autofunction:: empty_folder
.. autofunction:: folder_exists
.. autofunction:: copy_folder
.. autofunction:: zip_folder
.. autofunction:: unzip
.. autofunction:: most_recent_file


Delay
-----
.. autofunction:: wait
.. autofunction:: wait_for_image
.. autofunction:: wait_folder_exists


Word Application
----------------
.. autoclass:: Word
   :members:


Word File
---------
.. autoclass:: WordFile
   :members:


Outlook Application
-------------------
.. autoclass:: Outlook
   :members:


Excel Application
-----------------
.. autoclass:: Excel
   :members:


Excel File
----------
.. autoclass:: ExcelFile
   :members:


PowerPoint Application
----------------------
.. autoclass:: PowerPoint
   :members:


Office 365
----------
.. autofunction:: send_email_with_outlook365


Salesforce
----------
.. autofunction:: salesforce_api_call


E-mail (SMTP)
-------------
.. autofunction:: send_mail_smtp
.. autofunction:: send_mail_attachment


Windows OS
----------
.. autofunction:: find_window_title
.. autofunction:: start_remote_desktop
.. autofunction:: close_remote_desktop
.. autofunction:: set_user_password
.. autofunction:: validate_user_password
.. autofunction:: lock_windows
.. autofunction:: is_logged_in
.. autofunction:: is_desktop_locked
.. autofunction:: get_username
.. autofunction:: set_to_clipboard
.. autofunction:: get_from_clipboard
.. autofunction:: clear_clipboard
.. autofunction:: run_vbs_script
.. autofunction:: beep
.. autofunction:: get_all_network_interface_names
.. autofunction:: enable_network_interface
.. autofunction:: disable_network_interface
.. autofunction:: get_default_printer_name
.. autofunction:: set_default_printer
.. autofunction:: remove_printer
.. autofunction:: get_service_status
.. autofunction:: start_service
.. autofunction:: stop_service
.. autofunction:: set_window_to_foreground
.. autofunction:: get_foreground_window_title
.. autofunction:: close_window
.. autofunction:: maximize_window
.. autofunction:: restore_window
.. autofunction:: minimize_window
.. autofunction:: resize_window
.. autofunction:: hide_window


Terminal
--------
.. autofunction:: run_ssh_command


SNMP
----
.. autofunction:: snmp_get


Active Directory
----------------
.. autoclass:: ActiveDirectory
   :members:


Utilities
---------
.. autofunction:: home_path
.. autofunction:: desktop_path
.. autofunction:: downloads_path
.. autofunction:: open_file
.. autofunction:: set_wallpaper
.. autofunction:: download_file_from_url


Trello
------
.. autofunction:: add_trello_card


System
------
.. autofunction:: rename_file
.. autofunction:: move_file
.. autofunction:: remove_file
.. autofunction:: file_exists
.. autofunction:: wait_file_exists
.. autofunction:: write_list_to_file
.. autofunction:: read_list_from_txt
.. autofunction:: append_line
.. autofunction:: make_textfile
.. autofunction:: copy_file
.. autofunction:: get_file_extension
.. autofunction:: send_to_printer


PDF
---
.. autofunction:: read_text_from_pdf
.. autofunction:: join_pdf_files
.. autofunction:: extract_page_range_from_pdf
.. autofunction:: extract_images_from_pdf
.. autofunction:: apply_watermark_to_pdf


System Monitoring
-----------------
.. autofunction:: get_cpu_load
.. autofunction:: get_number_of_cpu
.. autofunction:: get_cpu_frequency
.. autofunction:: get_cpu_stats
.. autofunction:: get_memory_stats
.. autofunction:: get_disk_stats
.. autofunction:: get_disk_partitions
.. autofunction:: get_boot_time
.. autofunction:: get_time_since_last_boot


Image Processing
----------------
.. autofunction:: show_image
.. autofunction:: rotate_image
.. autofunction:: resize_image
.. autofunction:: get_image_width
.. autofunction:: get_image_height
.. autofunction:: crop_image
.. autofunction:: mirror_image_horizontally
.. autofunction:: mirror_image_vertically


Process
-------
.. autofunction:: run_manual
.. autofunction:: run
.. autofunction:: is_process_running
.. autofunction:: get_running_processes
.. autofunction:: kill_process


Optical Character Recognition (OCR)
-----------------------------------
.. autofunction:: extract_text_ocr
.. autofunction:: find_text_on_screen_ocr
.. autofunction:: click_on_text_ocr
.. autofunction:: double_click_on_text_ocr
.. autofunction:: right_click_on_text_ocr


UiPath
------
.. autofunction:: execute_uipath_process


AutoIt
------
.. autofunction:: run_autoit_script


Robot Framework
---------------
.. autofunction:: execute_robotframework_test


Blue Prism
----------
.. autofunction:: run_blueprism_process


Automation Anywhere
-------------------
.. autofunction:: run_automationanywhere_task


SAP GUI
-------
.. autofunction:: quit
.. autofunction:: login
.. autofunction:: click_sap
.. autofunction:: get_text
.. autofunction:: set_text
.. autofunction:: highlight


Portal
------
.. autofunction:: create_new_job


Vision
------
.. autofunction:: is_visible
.. autofunction:: wait_appear
.. autofunction:: wait_vanish
.. autofunction:: read_text
