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
.. autofunction:: generate_date_today
.. autofunction:: generate_unique_identifier


Output
------
.. autofunction:: display_osd_message
.. autofunction:: print_console


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
.. autofunction:: click_coordinates
.. autofunction:: double_click_coordinates
.. autofunction:: double_click
.. autofunction:: right_click
.. autofunction:: right_click_coordinates
.. autofunction:: move_mouse_to
.. autofunction:: move_mouse_to_coordinates
.. autofunction:: move_mouse_relative
.. autofunction:: drag_mouse_to_coordinates
.. autofunction:: drag_mouse_to


Image
-----
.. autofunction:: random_screen_snippet
.. autofunction:: take_screenshot


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