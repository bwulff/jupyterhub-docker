# jupyterhub_config.py

# Network configuration
c.JupyterHub.hub_ip = '0.0.0.0'
c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000
c.JupyterHub.bind_url = 'http://localhost:8000'

# Authenticator configuration
c.JupyterHub.authenticator_class = 'pam'
c.Authenticator.admin_users = {'admin'}
#c.Authenticator.allowed_users = {'admin', 'group1', 'group2', 'group3'}
# Allow all users to login
c.PAMAuthenticator.open_sessions = True
c.Authenticator.allow_all = True

# System configuration
c.JupyterHub.db_url = 'sqlite:///data/jupyterhub.sqlite'
c.JupyterHub.cookie_secret_file = '/srv/jupyterhub/data/jupyterhub_cookie_secret'
c.JupyterHub.allow_named_servers = False

# Spawner configuration
c.Spawner.default_url = '/lab'
