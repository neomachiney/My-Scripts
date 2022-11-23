#!/usr/bin/python3
from termcolor import colored
from argparse import ArgumentParser

from lib.Globals import sql_dict, Color
from lib.PathFunctions import urler, ender
from lib.Functions import starter, connector, print_sql_dict

parser = ArgumentParser(description=colored("Store and update passwords!",color='yellow'))
group = parser.add_mutually_exclusive_group()
parser.add_argument('-H', '--host', type=str, help="Host")
parser.add_argument('-U', '--username', type=str, help="Username")
parser.add_argument('-E', '--email', type=str, help="Email")
parser.add_argument('-P', '--password', type=str, help="Password")
parser.add_argument('-A', '--two-factor', type=str, help="2FA keys")
parser.add_argument('-B', '--backup', type=str, help="Backup data")
parser.add_argument('-O', '--other', type=str, help="Other")
group.add_argument('-c', '--config', action="store_true", help="Fetch from config file (optional, not implemented)")
group.add_argument('-a', '--argv', action="store_true", help="Fetch from command line (optional, not implemented)")
group.add_argument('-i', '--input', action="store_true", help="Fetch from input (optional, not implemented)")
argv = parser.parse_args()

mode = starter(argv)

def sql_argv(argv):
    global sql_dict
    sql_dict['HOST'] = formurl(argv.host)
    sql_dict['USERNAME'] = argv.username
    sql_dict['EMAIL'] = argv.email
    sql_dict['PASSWORD'] = argv.password
    sql_dict['2FA'] = argv.two_factor
    sql_dict['BACKUP'] = argv.backup
    sql_dict['OTHER'] = argv.other

def sql_input():
    global sql_dict
    sql_dict['HOST'] = formurl(input(f"{Color.information} Enter Host: "))
    sql_dict['USERNAME'] = input(f"{Color.information} Enter Username: ")
    sql_dict['EMAIL'] = input(f"{Color.information} Enter Email: ")
    sql_dict['PASSWORD'] = input(f"{Color.information} Enter Password: ")
    sql_dict['2FA'] = input(f"{Color.information} Enter 2FA: ")
    sql_dict['BACKUP'] = input(f"{Color.information} Enter Backup: ")
    sql_dict['OTHER'] = input(f"{Color.information} Enter other data: ")

try:
    conn, cursor = connector()
except Exception as E:
    print(E)

def insert_mysql():
    statement = "INSERT INTO password (HOST, USERNAME, EMAIL, PASSWORD, 2FA, BACKUP, OTHER) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    values = (
            formurl(sql_dict['HOST']),
            sql_dict['USERNAME'],
            sql_dict['EMAIL'],
            sql_dict['PASSWORD'],
            sql_dict['2FA'],
            sql_dict['BACKUP'],
            sql_dict['OTHER']
    )
    cursor.execute(statement, values)
    conn.commit()

def fetch_mysql(host = ""):
    if not host:
        statement = "SELECT * from password"
    elif host:
        statement = "SELECT * from password where HOST = '%s'" % host
    else:
        pass
    cursor.execute(statement)
    data = cursor.fetchall()
    return data

def update_mysql(host):
    data = fetch_mysql()
    where = ""
    for i in data:
        if i[1] == host:
            where = i[0]
            data = i[1:]
            break

    statement = "UPDATE password SET HOST = %s, USERNAME = %s, EMAIL = %s, PASSWORD = %s, 2FA = %s, BACKUP = %s, OTHER = %s WHERE ID = %s"
    values = (
            formurl(sql_dict['HOST']),
            sql_dict['USERNAME'],
            sql_dict['EMAIL'],
            sql_dict['PASSWORD'],
            sql_dict['2FA'],
            sql_dict['BACKUP'],
            sql_dict['OTHER'],
            int(where))
    cursor.execute(statement, values)
    conn.commit()

def fetch_print(host = ""):
    query_res = fetch_mysql(host)
    for _ in query_res:
        _ = _[1:]
        _host, remainder = _[0], "|".join(_[1:])
        print(f"{Color.good} Host: {colored(_host, color='red', attrs=['bold'])} {colored(remainder, color='yellow', attrs=['bold'])}")
    print(f"{Color.good} Fetched!")
    exit()

def input_and_check():
    global sql_dict
    if mode == 'argv':
        sql_argv(argv)
    elif mode == "input":
        sql_input()
    print_sql_dict(sql_dict)
    cont = input(f"{Color.information} Press Y to continue and N to re-edit the data (Y/N)")
    if cont != "Y":
        sql_dict = input_and_check()
    else:
        return sql_dict

def formurl(u):
    if 'www.' in u:
        u = u.split('www.')[-1]
    u = ender(urler(u), '/').replace("http://", "https://")
    return u

def main():
    global sql_dict
    const = input(f"{Color.information} Create data (C) or Edit data (E) or Get data (C/E/G)? ")
    if const == "G":
        print("Press enter to get all")
        fp = input(f" {Color.information} Enter host name to get: ")
        if fp:
            fp = formurl(fp)
        fetch_print(fp)
    elif const == "C":
        sql_dict = input_and_check()
        insert_mysql()
    elif const == "E":
        sql_dict = input_and_check()
        up = formurl(input(f"{Color.information} Enter hostname to update: "))
        update_mysql(up)
    else:
        print("Wrong data, enter again")
        return True

if __name__ == '__main__':
    while True:
        m = main()
        if not m:
            break
