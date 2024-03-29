# WSGI Handler sample configuration file.
#
# Change the appropriate settings below, in order to provide the parameters
# that would normally be passed in the command-line.
# (at least conf['addons_path'])
#
# For generic wsgi handlers a global application is defined.
# For uwsgi this should work:
#   $ uwsgi_python --http :9090 --pythonpath . --wsgi-file openerp-wsgi.py
#
# For gunicorn additional globals need to be defined in the Gunicorn section.
# Then the following command should run:
#   $ gunicorn odoo:service.wsgi_server.application -c openerp-wsgi.py

import odoo

#----------------------------------------------------------
# Common
#----------------------------------------------------------
odoo.multi_process = True # Nah!

# Equivalent of --load command-line option
odoo.conf.server_wide_modules = ['base', 'web']
conf = odoo.tools.config

# Path to the OpenERP Addons repository (comma-separated for
# multiple locations)
#conf['addons_path'] = './odoo/addons,./addons'

# Optional database config if not using local socket
# conf['db_name'] = 'defaultdb'
# conf['db_host'] = 'pg-10f39f27-bouraimaaremou-45c4.a.aivencloud.com'
# conf['db_user'] = 'avnadmin'
# conf['db_port'] = 14867
# conf['db_password'] = 'AVNS_4Q-IbnEybZFS-WEn_IL'

#----------------------------------------------------------
# Generic WSGI handlers application
#----------------------------------------------------------
application = odoo.http.root

odoo.service.server.load_server_wide_modules()

#----------------------------------------------------------
# Gunicorn
#----------------------------------------------------------
# Standard OpenERP XML-RPC port is 8069
bind = '127.0.0.1:8069'
pidfile = '.gunicorn.pid'
workers = 4
timeout = 240
max_requests = 2000
