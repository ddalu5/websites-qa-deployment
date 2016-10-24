from settings import env, MYSQL_ADMIN_LOGIN, MYSQL_ADMIN_PASSWORD


def mysql_execute(command):
    """
    execute MySQL command
    :param command: string
    """
    env.run('mysql -u ' + MYSQL_ADMIN_LOGIN +
            ' --password=' + MYSQL_ADMIN_PASSWORD +
            ' --execute="' + command + '"')


def create_database(db_name, db_user):
    """
    Create database and grant all privileges on it to <db_user>
    :param db_name: string
    :param db_user: string
    """
    mysql_execute('create database ' + db_name + ';')
    mysql_execute('grant all privileges on ' + db_name + '.* to ' +
                  db_user + '@\'localhost\';')


def drop_database(db_name):
    """
    Drop database
    :param db_name: string
    """
    mysql_execute('drop database ' + db_name + ';')


def import_database(db_name, db_filepath):
    """
    Import backup in <db_name>
    :param db_name: string
    :param db_filepath: string
    """
    env.run('mysql -u ' + MYSQL_ADMIN_LOGIN +
            ' --password=' + MYSQL_ADMIN_PASSWORD +
            ' ' + db_name + ' < ' + db_filepath + ';')
