This document describes how to deploy new Git code updates to the production site.

1. Push local changes to the Git repo.
2. SSH into server, cd into `upstate_tech_cal_service` folder.
3. `git pull` changes from the Git repo.
4. Make `update_cal_data.py` executable: `chmod +x update_cal_data.py`
5. Make sure that config.ini is up to date (make edits as needed).
6. Reload daemon: `sudo systemctl daemon-reload`
7. Restart gunicorn: `sudo systemctl restart gunicorn`
8. Restart nginx: `sudo systemctl restart nginx`
9. Run the app, either manually `pipenv shell && python update_cal_data.py && exit`  or when the next cronjob runs
