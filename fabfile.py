from settings import *
from lib.db import *
from lib.sources import *
from lib.general import *


def deploy_all():
    confs = get_websites_confs()
    for website in confs:
        if os.path.isdir(WEBSITES_DIR + '/' + confs[website]['dir_name']):
            pull_repos(confs[website]['dir_name'])
        else:
            clone_repos(confs[website]['ssh_repos'], confs[website]['dir_name'])
        drop_database(confs[website]['dir_name'])
        create_database(confs[website]['mysql_db'], confs[website]['mysql_login'])
        import_database(confs[website]['mysql_db'],
                        WEBSITES_DIR + '/' + confs[website]['dir_name'] + '/db/export.sql')
