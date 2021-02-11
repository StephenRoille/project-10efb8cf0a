"""Generate a config file with: jupyter-notebook --generate-config

https://www.codingforentrepreneurs.com/blog/jupyter-production-server-on-docker-heroku
"""
import os


# This function does not need to exist
# to start a password-protected jupyter notebook start the server with this command:
# jupyter-notebook --config=./config/jupyter.py
c = get_config()
# Kernel config
c.IPKernelApp.pylab = 'inline'  # if you want plotting support always in your notebook
# Notebook config
c.NotebookApp.notebook_dir = 'notebooks'
c.NotebookApp.allow_origin = u'https://love-unicorns.herokuapp.com/' # put your public IP Address here
c.NotebookApp.ip = '*'
c.NotebookApp.allow_remote_access = True
c.NotebookApp.open_browser = False
# run python -c "from notebook.auth import passwd; print(passwd())"
# type a password
# copy/paste the sha returned here
c.NotebookApp.password = u'sha1:99419d339fec:0de45b41731943f9b7a16dd85ffd9d1f0376d199'
c.NotebookApp.port = int(os.environ.get("PORT", 8888))
c.NotebookApp.allow_root = True
c.NotebookApp.allow_password_change = True
c.ConfigurableHTTPProxy.command = ['configurable-http-proxy', '--redirect-port', '80']

