import pymysql 

host = "localhost"
user = "root"
password = "123456"
db = "batch"
port = 3306

con = pymysql.connect(host, user, password, db, port)
c = con.cursor()

def select(fields, tables, where=None):

    global c 

    query = "SELECT" + fields + "FROM" + tables
    if (where):
        query = query + "WHERE" + where

    c.execute(query)
    return c.fetchall()

def insert(values, table, fields=None):

    global c, con

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
        query = query + " VALUES " + ", ".join(["("+ v +")" for v in values])

        c.execute(query)
        con.commit()

    print(query)
    
values = [
    "'1499', '86871053000101', 'Pedro', 'Actived', '1200'", 
    "'1500', '22588938000107', 'Maria', 'Actived', '1280'",
    "'1501', '68077847000108', 'João', 'Is not actived', '1600'",
    "'1502', '00701438000105', 'Rodrigo', 'Actived', '500'"]

insert(values, "tb_customer_account", fields="id_customer, cpf_cnpj, nm_customer, is_active, vl_total")
print(select("*", "tb_customer_account"))


def avg(fields, tables, where=None):

    global c
    i = 0
    query = " SELECT " + fields + " FROM " + tables + " WHERE " + where
    for i in where:
        average = where/2
    