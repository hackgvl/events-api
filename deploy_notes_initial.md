1. Open a Command Prompt / Terminal / Shell, either:
   1. On your local computer / localhost
   1. Or, if you develop on a remote server then SSH into th remote machine.
2. Execute the following commands:
   1. (Optional) For Production or Remote Servers Only
      1. `sudo useradd usernamehere -s /bin/bash && passwd usernamehere`
      2. `sudo mkdir /home/usernamehere/public_html && chown -Rf usernamehere:groupnamehere /home/usernamehere/public_html`
   3. (Optional) Install Git on your operating system, assuming you don't already have it installed:
      1. RedHat / CentOS / Fedora: `sudo update yum` && `sudo yum install git`
      1. Ubuntu / Debian: `sudo apt-get update` && `sudo apt-get install git`
      1. Mac: `sudo brew install git`
   1. `cd` to change the directory to where you want the git repository / application to be downloaded
   5. Clone the GitHub repository
      1. Using the SSH protocol: `git clone git@github.com:codeforgreenville/upstate_tech_cal_service.git`
      1. Or, using the HTTPS protcol: `git clone https://github.com/codeforgreenville/upstate_tech_cal_service.git`
   6. `cd upstate_tech_cal_service`
   7. `curl https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh`
   8. `sh miniconda.sh -b -p $HOME/miniconda`
   9. `export PATH="$HOME/miniconda/bin:$PATH"`
   10. `conda env create -f environment.yml`
   1. Activate the application environment
      1. `conda activate cal_service`
      1. Or, the older way will work too: `source activate cal_service`
3. Create a local config.ini file, if one does not exist.
   1. `cp config.ini.example config.ini && nano config.ini`
   1. Fill in the placeholder values in your config.ini with the real values for the following, `nano config.ini`
      1. Register your own [Eventbrite token](https://www.eventbrite.com/platform/api#/introduction/authentication)
       1. Flask secret can be any long random string
       1. (No longer needed) Version 3 of the Meetup.com API requires an Oauth Key. However, as of Oct 2019, we're using only public GET API endpoints that require not authentication. It's not necessary to register a Meetup.com API key unless/until the app needs access to an authenticated endpoint, at which point the key could be added to the config file
4. Create a local logging_config.ini file
   1. `cp logging_config.ini.example logging_config.ini`
   2. `mkdir logs`
5. Test with gunicorn WSGI Server on a localhost port
   1. Run the following to generate / update the `all_meetsups.json` file in your application directory.
   2. cd ~/upstate_tech_cal_service && conda activate cal_service && python update_cal_data.py && conda deactivate
   2. Start a "localhost" web server: `gunicorn --bind 0.0.0.0:8000 app:app`
   2. Visit the localhost application in your web browser, and see if it works: `http://localhost:8000/api/gtc?tags=1'`
4. (Optional) On Remote or Production Servers - Setup a cronjob to generate the all_meetings.json, for example, at :35 after every hour
   1. `crontab -e -u usernamehere`
   2. `35 * * * * source $HOME/.bashrc; cd ~/upstate_tech_cal_service && conda activate cal_service && python update_cal_data.py && conda deactivate`
6. (Optional) Configure hosting via a real Web Server, like Apache or Nginx
   1. Setup gunicorn as a systemd daemon. **Change "apache" to "nginx" in this file if you're using Nginx.**
      1. `sudo nano /etc/systemd/system/gunicorn.service`
      1. ~~~
         [Unit]
         Description=Gunicorn instance to serve cal_service
         After=network.target

         [Service]
         User=root
         Group=apache
         WorkingDirectory=/home/eventapi/upstate_tech_cal_service
         Environment="PATH=/home/eventapi/miniconda/envs/cal_service/bin"
         ExecStart=/home/eventapi/miniconda/envs/cal_service/bin/gunicorn --workers 3 --log-file /var/log/gunicorn.log --log-level error --bind unix:/var/run/cal_service.sock -m 007 app:app

         [Install]
         WantedBy=multi-user.target
         ~~~
      1. Save and reload the new systemd daemon "unit file" using `sudo systemctl daemon-reload`
      1. To make any future edits to the gunicorn systemd unit file, use `systemctl edit --full gunicorn.service` and be sure to reload using `sudo systemctl daemon-reload`
      1. Start the Gunicorn systemd daemon using `systemctl restart gunicorn`
      1. Verify it's running by using `systemctl status gunicorn` and check that /var/run/cal_service.sock exists. You can also use a tool like `htop` to see there are 3 active/worker gunicorn threads
   2. Configure an Nginx or Apache to "talk" to the gunicorn via the respective "proxy" directive(s)
      1. Apache Example
         ~~~
         <VirtualHost *:443>

         UseCanonicalName On

          ServerName events.openupstate.org

          DocumentRoot /home/eventapi/public_html
          DirectoryIndex index.html
          ErrorLog /var/log/httpd/events.openupstate.org_error_log
          CustomLog /var/log/httpd/events.openupstate.org_access_log combined

          ProxyPass /api/ unix:/var/run/cal_service.sock|http://events.openupstate.org/api/

          <Directory /home/eventapi/public_html>
             Options -Indexes +IncludesNOEXEC +SymLinksifOwnerMatch +ExecCGI
             allow from all

             AllowOverride None
             Include /home/eventapi/public_html/.htaccess
          </Directory>

          # HSTS to force browsers to always ask for https
          Header always set Strict-Transport-Security "max-age=31536000;"

          SSLCertificateFile /etc/letsencrypt/live/events.openupstate.org/fullchain.pem
          SSLCertificateKeyFile /etc/letsencrypt/live/events.openupstate.org/privkey.pem
          Include /etc/letsencrypt/options-ssl-apache.conf
         </VirtualHost>
         ~~~
      2. Nginx Virtual Host Example - [modified from Boban, and not tested](https://serverfault.com/q/892944)
         ~~~
         server {
             server_tokens off;
             listen      443 ssl;
             server_name         events.openupstate.org;

             ssl_certificate     /etc/letsencrypt/live/events.openupstate.org/fullchain.pem;
             ssl_certificate_key /etc/letsencrypt/live/events.openupstate.org/privkey.pem;

             access_log      /var/log/nginx/access.myserver.log;
             error_log       /var/log/nginx/error.myserver.log;

             location /api {
                 include proxy_params;
                 proxy_pass http://unix:/var/run/cal_service.sock;
             }
         }
         ~~~
   1. Create a Gunicorn log file for the web server and the web server user may need permissions to write to it, `sudo touch /var/log/gunicorn.log && chown apache:apache /var/log/gunicorn.log && chmod g+w /var/log/gunicorn.log`


Kudos To
* https://djangodeployment.com/2016/11/30/how-to-setup-apache-with-gunicorn/
* https://github.com/nrk/predis/issues/277
* https://axilleas.me/en/blog/2013/selinux-policy-for-nginx-and-gitlab-unix-socket-in-fedora-19/
* https://stackoverflow.com/q/36527427
* http://vicch.github.io/pkb/programming/book/servers_for_hackers.html
* http://dev.prodigi.us/post/python-gunicorn-apache-simple-and-performant-method-deploy-your-django-projects/
* https://www.vioan.eu/blog/2016/10/10/deploy-your-flask-python-app-on-ubuntu-with-apache-gunicorn-and-systemd/
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-gunicorn-and-nginx-on-centos-7
* https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04
