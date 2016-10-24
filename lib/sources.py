from settings import env, WEBSITES_DIR
from fabric.api import lcd


def clone_repos(repos, dir_name):
    with lcd(WEBSITES_DIR):
        env.run('git clone '+repos+' '+dir_name)


def pull_repos(dir_name):
    print(WEBSITES_DIR + '/' + dir_name)
    with lcd(WEBSITES_DIR + '/' + dir_name):
        env.run('git stash')
        env.run('git pull')
