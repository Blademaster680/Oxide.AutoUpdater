# Oxide.AutoUpdater
This python script was made to help keep Oxide on my Rust Servers up to date when the server restarted. It works by fetching the latest Oxide.zip file from their website and downloads it to the server directory. It then extracts the Oxide.zip into the servers current directory replacing the old Oxide files.

## Instructions

1) Place the script in the same directory as your Rust server start.bat file
2) Insert the line below into your start script below the App_Update line.
```
python oxide-updater.py
```
3) Restart your server
