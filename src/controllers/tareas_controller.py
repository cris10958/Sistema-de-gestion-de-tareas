import sqlite3

def agregar_tarea(titulo, descripcion, fecha_limite):
    conn = sqlite3.connect('data/tareas.dbo')
    cursor = conn.cursor()

    cursor.execute(
        '''INSERT INTO tareas (titulo, descripcion, fecha_limite)
            VALUES(?,?,?)
        ''',(titulo, descripcion, fecha_limite)
    )

    conn.commit()
    conn.close()
    print("Tarea registrada con exito")

def mostrar_tarea():
    conn = sqlite3.connect('data/tareas.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM tareas')
    tareas = cursor.fetchall()

    for tarea in tareas:
        print(f"ID: {tarea[0]}, titulo: {tarea[1]}, /
              descripcion: {tarea[2]}, fecha limite: /
              {tarea[3]}")

    conn.close()