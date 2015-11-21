from fabric.api import local
import os

from fabvenv import virtualenv
from fabric.context_managers import cd



from fabric.api import put, run, settings, sudo
from fabric.operations import prompt
from fabric.contrib import django

from fabric.api import *
from fabtools import require
import fabtools



## Usage 
## 		fab -R master <method_name> 
## 
## Before execution 
##	 1. Define server IP in roles
## 	 2. Provide git repo 
## 	 3. Provide repo name 



env.user						= 'root'
env.key_filename				= '/home/sid/.ssh/deploy_open_ssh'
env.VIRTUALENV 					= '/webapps/'+{{ project_name }}+'/myenv/'
#VIRTUALENV 						= '/webapps/myenv/'
env.app_dir						= '/webapps/'+{{ project_name }}+'/'
env.app_code_dir				= '/webapps/'+{{ project_name }}+'/code'
env.app_root_dir				= '/webapps/'

db_name							= os.getenv('DATABASE_NAME', {{ project_name }}+"_db")
db_user							= os.getenv('DATABASE_USER', {{ project_name }}+"_user")
db_password						= os.getenv('DATABASE_PASSWORD', "password")




env.roledefs = {
#	'master' : [' 192.241.245.23'], 
#	'test' : ['128.199.167.207'],	# The dev  server 
	#'staging' : ['1.1.1.1'],
}

## Setup repo name here 
# env.repo						= 'https://gitlab.com/Vija/somerepo.git'
# env.repo_name 					='reponame'

env.warn_only 					= True

def check():
	''' Test Fab '''
	sudo('pwd');


## Setup server

def setup_server():
	sudo('')
	sudo(' sudo apt-get update')
	sudo(' sudo apt-get -y upgrade ')



def update_upgrade():

	sudo('  apt-get update')
	sudo('  apt-get -y upgrade --force-yes')

	# create vitual env
	sudo('sudo apt-get -y install python-virtualenv --force-yes')
	


def webserver():

	# Nginx
	require.nginx.server()	

def postgres():
	# Postgres packages
	sudo('apt-get -y install python-psycopg2 libpq-dev python-virtualenv git python-dev' )
	# Create system level user for postgres role

	# install postgress server,user and database
	require.postgres.server()
	require.postgres.user(db_user, db_password)
	require.postgres.database(db_name, db_user)



def app_install():

	# Create directory structure
	sudo('mkdir -p %s' % env.app_dir)
	sudo('git clone %s %s' % (env.repo,env.app_code_dir))

	# Install virtual environement
	sudo('sudo apt-get install python-virtualenv')
	sudo('mkdir -p %s' % env.VIRTUALENV )
	sudo ('virtualenv %s' % env.VIRTUALENV)

	# Install python packages via vitualenv
	with cd(env.app_code_dir):
		with virtualenv(env.VIRTUALENV):
			run('pip install -r requirements.txt')
