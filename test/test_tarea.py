import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

import unittest
from src.controllers.tareas_controller import agregar_tarea, mostrar_tarea
import sqlite3

class TestTareas(unittest.TestCase):
    #Esre metodo se ejecuta antes de todas las pruebas
    def setUp(self):
        #bd en memoria para pruebas
        self.conn = sqlite3.connect(':memory')
        self.cursor = self.conn.cursor()

        self.cursor.execute('''
             CREATE TABLE tareas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                fecha_limite TEXT 
            )''')
        self.conn.commit()
    
    #Este metodo se ejecuta despues de cada prueba
    def tearDown(self):
        #cierre de conexion de bd
        self.conn.close()

    def test_agregar_tarea(self):
        #insertar una tarea de pruebas
        agregar_tarea('Tarea test','Descripcion test','2025-03-03')
        #se verifica que la tarea se haya registrado
        self.cursor.execute('SELECT * FROM tareas where titulo = ?',('Tarea test'))
        tarea = self.cursor.fetchone()
        self.assertIsNotNone(tarea)
        self.assertEqual(tarea[1],'Tarea test')
        self.assertEqual(tarea[2],'Descripcion test')
        self.assertEqual(tarea[3],'2025-03-03')

#Ejecucion:
#Se ejecuta el archivo de la prueba
