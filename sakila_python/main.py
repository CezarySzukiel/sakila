from psycopg2 import connect, OperationalError, sql, DatabaseError

try:
    cnx = connect(
        user='postgres',
        password='coderslab',
        host='localhost',
        port='5433',
        database='postgres',
    )

    cursor = cnx.cursor()
    print('connected')
except OperationalError as err:
    print('Connection error:')
    raise ValueError(f'Connection error: {err}')

query_create_tb_user = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id SERIAL,
        name VARCHAR(120),
        email VARCHAR(60) UNIQUE,
        password VARCHAR(60) DEFAULT 'ala',
        PRIMARY KEY (id)
    );
""").format(table_name=sql.Identifier('User'))

query_create_tb_address = sql.SQL("""
    CREATE TABLE IF NOT EXISTS {table_name} (
        id SERIAL PRIMARY KEY,
        city VARCHAR(120),
        street VARCHAR(60),
        notes TEXT,
        user_id SMALLINT,
        FOREIGN KEY (user_id) REFERENCES {table_name_foreign}(id)
    )
""").format(table_name=sql.Identifier('Address'), table_name_foreign=sql.Identifier('User'))

query_insert_user_tb = sql.SQL("""
    INSERT INTO {table_name} (name, email, password)
    VALUES (%s, %s, %s)
    """).format(table_name=sql.Identifier('User'))

query_update_user_tb = sql.SQL("""
    UPDATE {table_name} SET password= %s WHERE id = %s
    """).format(table_name=sql.Identifier('User'))

query_delete_user_tb = sql.SQL("""
    DELETE FROM {table_name} WHERE name = %s
    """).format(table_name=sql.Identifier('User'))

query_alter = sql.SQL("""
    ALTER TABLE {table_name} ADD COLUMN price DECIMAL(7,2) DEFAULT 0
    """).format(table_name=sql.Identifier('User'))

query_alter2 = sql.SQL("""
    ALTER TABLE {table_name} ADD COLUMN date_of_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    """).format(table_name=sql.Identifier('Address'))

query_select = sql.SQL("""
    SELECT * FROM {table_name}
    """).format(table_name=sql.Identifier('User'))

with cnx:
    # try:
    #     cursor.execute(query_create_tb_user)
    #     print('Table user created')
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_create_tb_address)
    #     print('Table address created')
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_insert_user_tb, ('Jan', 'a@a.pl', 'tajne'))
    #     print('User inserted')
    # except DatabaseError as error:
    #     print(error)
    # try:
    #     cursor.execute(query_update_user_tb, ('bardzotajne', 1))
    #     print('password changed')
    # except DatabaseError as error:
    #     print(error)
    #
    # try:
    #     cursor.execute(query_delete_user_tb, ('Jan',))
    #     print('User deleted')
    # except DatabaseError as error:
    #     print(error)

    # try:
    #     cursor.execute(query_alter)
    #     print('Column added')
    # except DatabaseError as error:
    #     print(error)

    # try:
    #     cursor.execute(query_alter2)
    #     print('Column date_of_created added')
    # except DatabaseError as error:
    #     print(error)

    try:
        cursor.execute(query_select)
        print('Table user')
        print(cursor.fetchall())
    except DatabaseError as error:
        print(error)
