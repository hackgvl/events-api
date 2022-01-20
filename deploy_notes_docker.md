1. Open a Command Prompt / Terminal / Shell, either:
   1. On your local computer / localhost
   1. Or, if you develop on a remote server then SSH into the remote machine.

1. Execute the following commands:
   	1. (Optional) For Production or Remote Servers Only
		1. `sudo useradd usernamehere -s /bin/bash && passwd usernamehere`
		2. `sudo mkdir /home/usernamehere/public_html && chown -Rf usernamehere:groupnamehere /home/usernamehere/public_html`
   	1. (Optional) Install Git on your operating system, assuming you don't already have it installed:
		1. RedHat / CentOS / Fedora: `sudo update yum` && `sudo yum install git`
		1. Ubuntu / Debian: `sudo apt-get update` && `sudo apt-get install git`
		1. Mac: `sudo brew install git`
	1. `cd` to change the directory to where you want the git repository / application to be downloaded
	2. Clone the GitHub repository
		1. Using the SSH protocol: `git clone git@github.com:codeforgreenville/upstate_tech_cal_service.git`
		2. Or, using the HTTPS protcol: `git clone https://github.com/codeforgreenville/upstate_tech_cal_service.git`
   	1. `cd upstate_tech_cal_service`
   	2. Install Docker and Docker Compose on your operating system: https://docs.docker.com/compose/install/
      	1. Alternatively, install Docker Desktop: https://docs.docker.com/desktop/

2. Create a local config.ini file, if one does not exist.
	3. `cp config.ini.example-docker config.ini && nano config.ini`
	4. Fill in the placeholder values in your `config.ini` with the real values for the following, `nano config.ini`
		1. Register your own [Eventbrite token](https://www.eventbrite.com/support/articles/en_US/How_To/how-to-locate-your-eventbrite-api-user-key?lg=en_US)
		2. Flask secret can be any long random string
		3. (No longer needed) Version 3 of the Meetup.com API requires an Oauth Key. However, as of Oct 2019, we're using only public GET API endpoints that require not authentication. It's not necessary to register a Meetup.com API key unless/until the app needs access to an authenticated endpoint, at which point the key could be added to the config file
	
3. Create a local logging_config.ini file
   1. `cp logging_config.ini.example-docker logging_config.ini`
   2. `mkdir logs`

4. Test with gunicorn WSGI Server on a localhost port
   1. Run the following to generate / update the `all_meetings.json` file in your application directory.
   2. `docker-compose up --build` or `docker-compose up -d --build` to run the container in detatched mode
   3. View logs with `docker-compose logs` or follow logs with `docker-compose logs -f`
   4. Visit the localhost application in your web browser, and see if it works: `http://127.0.0.1:8000/api/gtc?tags=1`

5. (Optional) On Remote or Production Servers - Setup a cronjob to generate the all_meetings.json, for example, at :35 after every hour
   1. `crontab -e -u usernamehere`
   2. `35 * * * * source $HOME/.bashrc; cd ~/upstate_tech_cal_service && docker-compose restart`

6. (Optional) Configure hosting via a real Web Server, like Apache or Nginx
   1. Configure an Nginx or Apache to "talk" to the container via the respective "proxy" directive(s)
      	1. Apache Example
		~~~
		<VirtualHost *:443>

		UseCanonicalName On

		ServerName events.openupstate.org

		DocumentRoot /home/eventapi/public_html
		DirectoryIndex index.html
		ErrorLog /var/log/httpd/events.openupstate.org_error_log
		CustomLog /var/log/httpd/events.openupstate.org_access_log combined

		ProxyPass /api/ http://127.0.0.1:8000|http://events.openupstate.org/api/

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
	1. Nginx Virtual Host Example - [modified from Boban, and not tested](https://serverfault.com/q/892944)
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
				proxy_pass http://127.0.0.1:8000;
			}
		}
		~~~
	1. If hosting Nginx or Apache through a Docker container on the same [Docker network](https://docs.docker.com/compose/networking/), you can replace `127.0.0.1` with the container name, and remove the `127.0.0.1:8000` port mapping in `docker-compose.yml`.


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
