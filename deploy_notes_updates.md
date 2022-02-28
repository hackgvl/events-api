This document describes how to deploy new Git code updates to the production site.

1. Push local changes to the Git repo.
2. SSH into server, cd into `upstate_tech_cal_service` folder.
3. `git pull` changes from the Git repo.
4. Make sure that config.ini is up to date (make edits as needed).
5. Reload daemon: `sudo systemctl daemon-reload`
6. Restart gunicorn: `sudo systemctl restart gunicorn`
7. Restart nginx: `sudo systemctl restart nginx`
8. Run the app, either manually `pipenv shell && python update_cal_data.py && exit`  or when the next cronjob runs
