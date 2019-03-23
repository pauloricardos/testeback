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

    query = "SELECT " + fields + " FROM " + tables
    if (where):
        query = query + "WHERE " + where

    c.execute(query)
    return c.fetchall()

def insert(values, table, fields=None):
     
    global c, con

    query2 = "DELETE FROM  " + table
    c.execute(query2)

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
        query = query + " VALUES " + ", ".join(["("+ v +")" for v in values])

        c.execute(query)
        con.commit()

    
values = [
    "'1499', '86871053000101', 'Pedro', 'Actived', '1200'", 
    "'1500', '22588938000107', 'Maria', 'Actived', '1280'",
    "'1501', '68077847000108', 'Joao', 'Is not actived', '1600'",
    "'1502', '00701438000105', 'Rodrigo', 'Actived', '500'"]

insert(values, "tb_customer_account", fields="id_customer, cpf_cnpj, nm_customer, is_active, vl_total")
print(select("*", "tb_customer_account"))


def orderBySalary(table):
    
    global c
    
    salaries = select("vl_total", table)
    print(salaries)
orderBySalary("tb_customer_account")

# select avg(vl_total) from tb_customer_account where id_customer >= 1500 and vl_total > 560;
# select vl_total from tb_customer_account where id_customer >= 1500 and vl_total > 560;
# select count(*) from tb_customer_account where id_customer >= 1500 and vl_total > 560;
# select * from tb_customer_account

def average(fields, table):

    global c

    numbers = []
    for vl_total in table:
        numbers.append("vl_total")
        listSum = sum(numbers)
        print (listSum)

average("vl_total", "tb_customer_account")    