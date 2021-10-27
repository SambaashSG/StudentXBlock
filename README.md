# StudentXBlock

### Description ###

- This XBlock provides an easy way to go online-assessment app from LMS.

### Customize the XBlock ###

- By default, URL is localhost:8080 the default value can be changed in `StudentXBlock / student_block / student_block / student_block.py`

### Install / Update the XBlock ###

    # Move to the folder where you want to download the XBlock
    cd /edx/app/edxapp
    # Download the XBlock
    sudo -u edxapp git clone https://github.com/SambaashSG/StudentXBlock.git
    # Install the XBlock
    sudo -u edxapp /edx/bin/pip.edxapp install StudentXBlock/student_block/
    # Upgrade the XBlock if it is already installed, using --upgrade
    sudo -u edxapp /edx/bin/pip.edxapp install StudentXBlock/student_block/ --upgrade
    # Remove the installation files
    sudo rm -r StudentXBlock
    
### Reboot if something isn't right ###

    sudo /edx/bin/supervisorctl -c /edx/etc/supervisord.conf restart edxapp:
    
### Activate the XBlock in your course ###
Go to `Settings -> Advanced Settings` and set `advanced_modules` to `["student_block"]`.

### Use the XBlock in a unit ###
Select `Advanced -> student_block` in your unit.
