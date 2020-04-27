import os
from configparser import RawConfigParser
from fabric.tasks import task


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
env = RawConfigParser()
env.read(BASE_DIR + '/logbook/env.ini')

SYSTEMD_SERVICE = env['project']['systemd_service']
USERNAME = env['project']['username']
PROJECT_PATH = env['project']['path']
GIT_REPOSITORY = env['project']['git_repository']
GIT_KEY = env['project']['git_key']


@task
def install(c):
    """
    Install project
    pipenv run fab install --hosts ip
    """
    c.run(f'mkdir {PROJECT_PATH}')
    with c.cd(PROJECT_PATH):
        c.run(f'git clone {GIT_REPOSITORY} .')
        c.run('export PIPENV_VENV_IN_PROJECT=1 && pipenv install')


@task
def upload(c, local, remote):
    """
    Upload file
    pipenv run fab upload --local /path/to/local/file.txt --remote relative/path/to/file.txt --hosts ip
    """
    c.put(local, f'{PROJECT_PATH}/{remote}')


@task
def download(c, remote, local):
    """
    Download file
    pipenv run fab download --remote relative/path/to/file.txt --local /path/to/local/file.txt --hosts ip
    """
    c.get(f'{PROJECT_PATH}/{remote}', local)


@task
def deploy(c, branch='master', migrate=True, deps=True, collectstatic=False):
    """
    Deploy updates to server
    pipenv run fab deploy --branch master --migrate --deps --collectstatic --hosts ip
    """
    with c.cd(PROJECT_PATH):
        print('Update code')
        c.run(f'git fetch origin && git checkout {branch} && git pull origin {branch}')
        if deps:
            print('Installing dependencies')
            c.run('pipenv install')
        if migrate:
            print('Migrating database')
            c.run('pipenv run python logbook/manage.py migrate')
        if collectstatic:
            print('Running collectstatic')
            c.run('pipenv run python logbook/manage.py collectstatic')
        service(c, SYSTEMD_SERVICE, 'restart')


@task
def service(c, name="nginx", action="restart"):
    """
    System service status|start|stop|restart
    pipenv run fab service --name nginx --action stop --hosts ip
    """
    c.run(f'sudo service {name} {action}')
