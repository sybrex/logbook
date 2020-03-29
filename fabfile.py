from fabric.tasks import task


SYSTEMD_SERVICE = 'logbook'
USERNAME = 'deployer'
TARGET_DIRECTORY = '/srv/www/logbook'
GIT_REPOSITORY = 'git@github.com:sybrex/logbook.git'
GIT_KEY = '~/.ssh/github-deployer'


@task
def install(c):
    """
    Install project
    pipenv run fab install --hosts ip
    """
    c.run(f'mkdir {TARGET_DIRECTORY}')
    with c.cd(TARGET_DIRECTORY):
        c.run(f'git clone {GIT_REPOSITORY} .')
        c.run('export PIPENV_VENV_IN_PROJECT="enabled" && pipenv install')


@task
def upload(c, local, remote):
    """
    Upload file
    pipenv run fab upload --local /path/to/local/file.txt --remote relative/path/to/file.txt --hosts ip
    """
    c.put(local, f'{TARGET_DIRECTORY}/{remote}')


@task
def download(c, remote, local):
    """
    Download file
    pipenv run fab download --remote relative/path/to/file.txt --local /path/to/local/file.ini --hosts ip
    """
    c.get(f'{TARGET_DIRECTORY}/{remote}', local)


@task
def deploy(c, branch='master', migrate=True, deps=True, collectstatic=False):
    """
    Deploy updates to server
    pipenv run fab deploy --branch master --migrate --deps --collectstatic --hosts ip
    """
    with c.cd(TARGET_DIRECTORY):
        print('Update code')
        c.run(f'git fetch origin && git checkout {branch} && git pull origin {branch}')
        if deps:
            print('Installing dependencies')
            c.run('pipenv install')
        if migrate:
            print('Migrating database')
            c.run('pipenv run python manage.py migrate')
        if collectstatic:
            print('Running collectstatic')
            c.run('pipenv run python manage.py collectstatic')
        c.run(f'sudo service {SYSTEMD_SERVICE} restart')
