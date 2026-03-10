# jupyterhub_config.py

# Use PAM authenticator (default)
c.JupyterHub.authenticator_class = 'pam'

# Set admin users
c.Authenticator.admin_users = {'admin'}

c.Authenticator.allow_all = True

#c.Authenticator.allowed_users = {'admin', 'group1', 'group2', 'group3'}

# Allow all users to login
c.PAMAuthenticator.open_sessions = True

# Base URL configuration
c.JupyterHub.bind_url = 'http://0.0.0.0:8000'

# Configure the hub to be accessible from the specified IP
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# Database configuration
c.JupyterHub.db_url = 'sqlite:///data/jupyterhub.sqlite'

# Cookie secret file
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/data/jupyterhub_cookie_secret'

# Allow named servers (optional)
c.JupyterHub.allow_named_servers = False

# Spawner configuration
c.Spawner.default_url = '/lab'
