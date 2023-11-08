import sqlite3 as sql

class Conexion:
    def __init__(self, cleansa):
        self.cleansa = cleansa
        self.conexion = sql.connect(cleansa)
        self.cursor = self.conexion.cursor()


# Creación de tablas ---------------------------------------------------------------------
    def crear_tablas(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS categoria
                                      (id INTEGER PRIMARY KEY, nombre TEXT NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS direccion
                                     (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                     ciudad TEXT NOT NULL,
                                     calle TEXT NOT NULL,
                                     numero INTEGER NOT NULL,
                                     codigo_postal INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS ficha (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              nombre TEXT NOT NULL,
                              apellido TEXT NOT NULL,
                              dni INTEGER,
                              cuil INTEGER,
                              telefono INTEGER NOT NULL,
                              mail TEXT NOT NULL,
                              fecha_nacimiento DATE NOT NULL,
                              fk_id_direccion INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS proveedor (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              fk_id_ficha INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS usuario (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nombre_usuario VARCHAR(30) NOT NULL,
                            contrasena VARCHAR(20) NOT NULL,
                            rol VARCHAR(20) NOT NULL,
                            fk_id_ficha INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              fk_id_ficha INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS metodo_pago (
                              id INTEGER NOT NULL,
                              nombre VARCHAR(30) NOT NULL,
                              PRIMARY KEY (id))''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS venta (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              precio_total REAL NOT NULL,
                              fecha DATE NOT NULL,
                              fk_id_cliente INTEGER NOT NULL,
                              fk_id_metodo_pago INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS producto (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              nombre VARCHAR(40) NOT NULL,
                              marca VARCHAR(30) NOT NULL,
                              descripcion TEXT NOT NULL,
                              precio REAL NOT NULL,
                              stock INTEGER NOT NULL,
                              fecha_vencimiento DATE NOT NULL,
                              fk_id_categoria INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS etiqueta (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              nombre VARCHAR(40) NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS venta_producto (
                              cantidad_producto INTEGER NOT NULL,
                              fk_id_venta INTEGER NOT NULL,
                              fk_id_producto INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS compra (
                              id INTEGER PRIMARY KEY AUTOINCREMENT,
                              precio_total REAL NOT NULL,
                              fecha DATE NOT NULL,
                              fk_id_metodo_pago INTEGER NOT NULL,
                              fk_id_proveedor INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS compra_producto (
                              cantidad_producto INTEGER NOT NULL,
                              fk_id_compra INTEGER NOT NULL,
                              fk_id_producto INTEGER NOT NULL)''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS etiqueta_producto (
                              fk_id_etiqueta INTEGER NOT NULL,
                              fk_id_producto INTEGER NOT NULL)''')

        self.conexion.commit()



# Insertar datos ----------------------------------------------------------------------------------------------------

    def insertar_datos_categoria(self, datos):
        self.cursor.executemany("INSERT INTO categoria(id, nombre) VALUES (?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_direccion(self, datos):
        self.cursor.executemany("INSERT INTO direccion (id, ciudad, calle, numero, codigo_postal) VALUES (?, ?, ?, ?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_ficha(self, datos):
        self.cursor.executemany("INSERT INTO ficha (id, nombre, apellido, dni, cuil, telefono, mail, fecha_nacimiento, fk_id_direccion) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_proveedor(self, datos):
        self.cursor.executemany("INSERT INTO proveedor (id, fk_id_ficha) VALUES (?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_usuario(self, datos):
        self.cursor.executemany("INSERT INTO usuario (id, nombre_usuario, contrasena, rol, fk_id_ficha) VALUES (?, ?, ?, ?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_cliente(self, datos):
        self.cursor.executemany("INSERT INTO cliente (id, fk_id_ficha) VALUES (?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_metodo_pago(self, datos):
        self.cursor.executemany("INSERT INTO metodo_pago (id, nombre) VALUES (?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_producto(self, datos):
        self.cursor.executemany("INSERT INTO producto (id, nombre, marca, descripcion, precio, stock, fecha_vencimiento, fk_id_categoria) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_etiqueta(self, datos):
        self.cursor.executemany("INSERT INTO etiqueta (id, nombre) VALUES (?, ?)", datos)
        self.conexion.commit()

    def insertar_datos_etiqueta_producto(self, datos):
        self.cursor.executemany("INSERT INTO etiqueta_producto (fk_id_etiqueta, fk_id_producto) VALUES (?, ?)", datos)
        self.conexion.commit()




    def cerrar_bd(self):
        self.conexion.close()




# Ejecutar ()
if __name__ == '__main__':
    db_name = 'cleansa.db'
    conexion = Conexion(db_name)
    #conexion.crear_tablas()

    datos_categoria = [
        (1, 'Para superficies'),
        (2, 'Desinfectantes'),
        (3, 'Para cristales y vidrios'),
        (4, 'Para suelos'),
        (5, 'Jabones para cuerpo'),
        (6, 'Shampoo'),
        (7, 'Detergentes'),
        (8, 'Para limpieza industrial'),
        (9, 'Para joyas'),
        (10, 'Para cocina'),
        (11, 'Para calzado'),
        (12, 'Multiusos'),
        (13, 'Para baños'),
        (14, 'Para electrodomésticos'),
        (15, 'Para piscinas y jacuzzis'),
        (16, 'Para mascotas'),
        (17, 'Ambientadores'),
        (18, 'Para limpieza automotriz'),
        (19, 'Para ropa')
    ]

    datos_direccion = [
        (1, 'Buenos Aires', 'Avenida Rivadavia', 1500, 1040),
        (2, 'Buenos Aires', 'Florida', 1685, 1005),
        (3, 'Buenos Aires', 'Avenida Corrientes', 2000, 1046),
        (4, 'Buenos Aires', 'Avenida Santa Fe', 2500, 1123),
        (5, 'Buenos Aires', 'Lavalle', 1451, 1047),
        (6, 'Buenos Aires', 'Avenida 9 de Julio', 3000, 1047),
        (7, 'Buenos Aires', 'Belgrano', 3500, 1092),
        (8, 'Buenos Aires', 'Reconquista', 100, 1003),
        (9, 'Buenos Aires', 'Callao', 200, 1024),
        (10, 'Buenos Aires', 'Córdoba', 1800, 1054),
        (11, 'Buenos Aires', 'Maipú', 2800, 1006),
        (12, 'Buenos Aires', 'Avenida Pueyrredón', 1600, 1118),
        (13, 'Buenos Aires', 'Avenida Jujuy', 2451, 1247),
        (14, 'Buenos Aires', 'Sarmiento', 3262, 1041),
        (15, 'Buenos Aires', 'Boedo', 3321, 1206),
        (16, 'Buenos Aires', 'Entre Ríos', 2133, 1236),
        (17, 'Buenos Aires', 'Humberto Primo', 2023, 1103),
        (18, 'Buenos Aires', 'San Juan', 666, 1232),
        (19, 'Buenos Aires', 'San Martín', 888, 1004),
        (20, 'Buenos Aires', 'Avenida Independencia', 1789, 1099),
        (21, 'Buenos Aires', 'Defensa', 1987, 1065),
        (22, 'Buenos Aires', 'Avenida Montes de Oca', 3456, 1270),
        (23, 'Buenos Aires', 'Avenida Caseros', 3216, 1264),
        (24, 'Buenos Aires', 'Brandsen', 1234, 1161),
        (25, 'Buenos Aires', 'Avenida Almirante Brown', 1254, 1155),
        (26, 'Buenos Aires', 'Bolívar', 1616, 1066),
        (27, 'Buenos Aires', 'Avenida San José', 2323, 1147),
        (28, 'Buenos Aires', 'Balcarse', 2529, 1064),
        (29, 'Buenos Aires', 'Avenida Vélez Sársfield', 1050, 1407),
        (30, 'Buenos Aires', 'General Paz', 2060, 1406),
        (31, 'Buenos Aires', 'Avenida Eva Perón', 3040, 1405),
        (32, 'Buenos Aires', 'Carlos Pellegrini', 1544, 1011),
        (33, 'Buenos Aires', 'Avenida Juan B Justo', 1624, 1416),
        (34, 'Buenos Aires', 'Paseo Colón', 1022, 1063),
        (35, 'Buenos Aires', 'Avenida San Martín', 2268, 1408),
        (36, 'Buenos Aires', 'San José de Calasanz', 2589, 1419),
        (37, 'Buenos Aires', 'Avenida Francisco Beiró', 2547, 1408),
        (38, 'Buenos Aires', 'Mosconi', 1689, 1407),
        (39, 'Buenos Aires', 'Avenida Donato Álvarez', 3489, 1406),
        (40, 'Buenos Aires', 'Artigas', 2222, 1416),
        (41, 'Buenos Aires', 'Avenida Chivilcoy', 2200, 1213)
    ]

    datos_ficha = [
        (1, 'Silvia', 'Flores', 62816632, None, 91157503883, 'silvia@gmail.com', '1983-09-25', 1),
        (2, 'Cecilia', 'Acosta', 20031591, None, 91184651699, 'cecilia@gmail.com', '2007-02-05', 2),
        (3, 'Mirta', 'Garcia', 30520674, None, 91172465305, 'mirta@gmail.com', '1993-10-21', 3),
        (4, 'Raúl', 'Suarez', 44447290, None, 91144700460, 'raul@gmail.com', '1997-12-20', 4),
        (5, 'Ricardo', 'Gonzalez', 49799921, None, 91149168533, 'ricardo@gmail.com', '1973-02-12', 5),
        (6, 'Natalia', 'Ramirez', 45774559, None, 91193680837, 'natalia@gmail.com', '1987-04-11', 6),
        (7, 'Víctor', 'Romero', 11447048, None, 91168902473, 'victor@gmail.com', '1994-11-15', 7),
        (8, 'Mónica', 'Diaz', 76746518, None, 91110595411, 'monica@gmail.com', '1986-10-03', 8),
        (9, 'Julio', 'Fernandez', 48924118, None, 91165635003, 'julio@gmail.com', '1973-05-27', 9),
        (10, 'Mario', 'Medina', 39816257, None, 91196833623, 'mario@gmail.com', '1976-07-15', 10),
        (11, 'Claudio', 'Lopez', 28306848, None, 91161212362, 'claudio@gmail.com', '2006-06-26', 11),
        (12, 'Miguel', 'Aguirre', 91236168, None, 91113030504, 'miguel@gmail.com', '1992-07-08', 12),
        (13, 'Valeria', 'Santana', 66022244, None, 91104413097, 'valeria@gmail.com', '1991-02-21', 13),
        (14, 'Alicia', 'Gomez', 38605690, None, 91160756888, 'alicia@gmail.com', '1981-05-13', 14),
        (15, 'Graciela', 'Sanchez', 54727961, None, 91114395799, 'graciela@gmail.com', '1986-06-29', 15),
        (16, 'Nélida', 'Perez', 56350188, None, 91150260702, 'nelida@gmail.com', '1999-12-21', 16),
        (17, 'Patricia', 'Herrera', 74388343, None, 91101847813, 'patricia@gmail.com', '1978-11-11', 17),
        (18, 'Mauricio', 'Puente', 15707217, None, 91101313852, 'mauricio@gmail.com', '1972-03-10', 18),
        (19, 'Hugo', 'Sosa', 72997404, None, 91122417443, 'hugo@gmail.com', '1978-12-08', 19),
        (20, 'Salvador', 'Guerra', 87256899, None, 91113734929, 'salvador@gmail.com', '1990-12-05', 20),
        (21, 'Marta', 'Rubio', 16307614, None, 91110060202, 'marta@gmail.com', '1988-11-21', 21),
        (22, 'Iván', 'Abreu', None, 20173362966, 91197840081, 'ivan@gmail.com', '1994-04-21', 22),
        (23, 'Anahí', 'Carvajal', None, 22440707966, 91135187561, 'anahi@gmail.com', '2001-11-29', 23),
        (24, 'Lorena', 'Falcon', None, 28262242088, 91153834931, 'lorena@gmail.com', '1993-05-21', 24),
        (25, 'Jorge', 'Aguilar', None, 23434106144, 91161221905, 'jorge@gmail.com', '1986-03-18', 25),
        (26, 'Josep', 'Brito', None, 21199851755, 91103187705, 'josep@gmail.com', '1971-08-08', 26),
        (27, 'Carlos', 'Ortiz', None, 26628864633, 91152557940, 'carlos@gmail.com', '1973-01-04', 27),
        (28, 'Jennifer', 'Dos Santos', None, 22576525200, 91134441673, 'jennifer@gmail.com', '2003-07-08', 28),
        (29, 'Juana', 'Castellano', None, 25159050944, 91164265684, 'juana@gmail.com', '1999-03-09', 29),
        (30, 'Rosa', 'Espinosa', None, 27936401399, 91154000255, 'rosa@gmail.com', '2000-04-21', 30),
        (31, 'Roinner', 'Nuñez', None, 20635947866, 91149183528, 'roinner@gmail.com', '2001-01-22', 31),
        (32, 'Susana', 'Navas', None, 22976618000, 91185062599, 'susana@gmail.com', '1977-10-22', 32),
        (33, 'Martin', 'Chacon', None, 21598320822, 91167402802, 'martin@gmail.com', '1993-04-14', 33),
        (34, 'Luis', 'Salazar', None, 21708125699, 91128433442, 'luis@gmail.com', '1996-02-23', 34),
        (35, 'Walter', 'Lucena', None, 22765290122, 91104673180, 'walker@gmail.com', '2002-08-13', 35),
        (36, 'Rogelio', 'Melendez', None, 24519533499, 91139335076, 'rogelio@gmail.com', '2001-06-25', 36),
        (37, 'Leonardo', 'Rivera', None, 27553483099, 91166659502, 'leonardo@gmail.com', '1987-09-09', 37),
        (38, 'Emilia', 'Macias', None, 20421075855, 91146136694, 'emilia@gmail.com', '1971-04-21', 38),
        (39, 'Eugenia', 'Palma', None, 23190450755, 91112956999, 'eugenia@gmail.com', '2003-05-30', 39),
        (40, 'Sheila', 'Moreno', None, 21887016966, 91197133899, 'sheila@gmail.com', '1989-05-12', 40),
        (41, 'Abraham', 'Pons', None, 20369216255, 91149034747, 'abraham@gmail.com', '1988-06-05', 41)

    ]

    datos_proveedor = [
        (1, 22),
        (2, 23),
        (3, 24),
        (4, 25),
        (5, 26),
        (6, 27),
        (7, 28),
        (8, 29),
        (9, 30),
        (10, 31),
        (11, 32),
        (12, 33),
        (13, 34),
        (14, 35),
        (15, 36),
        (16, 37),
        (17, 38),
        (18, 39),
        (19, 40),
        (20, 41)
    ]

    datos_usuario = [(1, 'SilviaFlores', '12345', 'Administrador', 1)]

    datos_cliente = [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), (9, 10), (10, 11), (11, 12),
                     (12, 13), (13, 14), (14, 15), (15, 16), (16, 17), (17, 18), (18, 19), (19, 20), (20, 21)]

    datos_metodo_pago = [(1, 'Efectivo'), (2, 'Tarjeta de débito'), (3, 'Tarjeta de crédito'),
                         (4, 'Transferencia bancaria'), (5, 'Cheque')]

    datos_producto = [(1, 'Lysol Desinfectante Multiusos', 'Lysol', 'Elimina gérmenes y bacterias en superficies', 1820,50, '2028-05-10', 1),
                      (2, 'Clorox Desinfectante en Spray', 'Clorox', 'Desinfectante para todo tipo de superficies', 4500,46, '2029-09-11', 2),
                      (3, 'Dettol Desinfectante para Superficies', 'Dettol', 'Mata el 99.9% de los gérmenes', 3000, 33,'2030-10-01', 1),
                      (4, 'Windex Limpiador de Cristales', 'Windex', 'Deja los cristales y vidrios relucientes', 2500,66, '2025-11-02', 3),
                      (5, 'Glass Plus Limpiador de Vidrios', 'Glass Plus', 'Limpia sin dejar rayas', 2900, 37,'2030-11-25', 3),
                      (6, 'Lysoform Desinfectante para Suelos', 'Lysoform', 'Elimina gérmenes y malos olores', 4456, 48,'2031-04-06', 13),
                      (7, 'Mr. Músculo Limpiador de Pisos', 'Mr. Músculo', 'Limpieza profunda para todo tipo de suelos',1600, 55, '2028-08-01', 4),
                      (8, 'Dove Jabón de Baño', 'Dove', 'Hidrata y cuida la piel', 1000, 20, '2030-09-05', 5),
                      (9, 'Nivea Gel de Ducha', 'Nivea', 'Limpia suavemente la piel', 999, 15, '2026-05-22', 5),
                      (10, 'Skip Detergente en Polvo', 'Skip', 'Elimina las manchas difíciles', 2650, 100, '2035-09-10',19),
                      (11, 'Ariel Jabón en Barra', 'Ariel', 'Limpia y refresca la ropa', 455, 87, '2027-01-22', 19),
                      (12, 'Head & Shoulders Shampoo Anticaspa', 'Head & Shoulders','Elimina la caspa y fortalece el cabello', 1200, 92, '2025-06-15', 6),
                      (13, 'Pantene Shampoo Hidratante', 'Pantene', 'Hidrata y suaviza el cabello', 2230, 14,'2029-04-08', 6),
                      (14, 'Ace Detergente Líquido', 'Ace', 'Limpieza profunda para la ropa', 3699, 58, '2027-07-26', 7),
                      (15, 'Ala Detergente en Polvo', 'Ala', 'Elimina las manchas difíciles', 1265, 60, '2025-04-07', 7),
                      (16, 'IndustrialClean Limpiador Industrial', 'IndustrialClean','Ideal para limpieza en entornos industriales', 4700, 44, '2024-03-04', 8),
                      (17, 'ProClean Desengrasante Industrial', 'ProClean','Elimina la grasa y la suciedad más resistente', 6999, 65, '2026-07-16', 8),
                      (18, 'Hagerty Limpiador de Joyas', 'Hagerty', 'Devuelve el brillo a las joyas', 5875, 37,'2028-06-29', 9),
                      (19, 'SilverClean Limpiador de Plata', 'SilverClean', 'Especial para joyas de plata', 10000, 15,'2029-06-10', 9),
                      (20, 'Cif Limpiador de Cocina', 'Cif', 'Elimina la grasa y los residuos de la cocina', 1500, 20,'2027-05-22', 10),
                      (21, 'Mr. Músculo Desengrasante para Cocina', 'Mr. Músculo', 'Elimina la grasa incrustada', 2360,23, '2027-08-11', 10),
                      (22, 'Kiwi Crema para Zapatos', 'Kiwi', 'Nutre y protege el calzado', 650, 46, '2026-07-18', 11),
                      (23, 'Saphir Limpiador de Calzado', 'Saphir', 'Limpieza profunda para todo tipo de calzado', 1600,35, '2025-09-26', 11),
                      (24, 'Mr. Clean Limpiador Multiusos', 'Mr. Clean', 'Limpieza versátil para el hogar', 3999, 61,'2028-09-23', 12),
                      (25, 'Ajax Limpiador Multiusos', 'Ajax', 'Limpieza efectiva en todas las superficies', 1455, 18,'2027-04-30', 12),
                      (26, 'Domestos Limpiador de Baños', 'Domesticos', 'Elimina gérmenes y desinfecta', 2050, 33,'2029-05-21', 13),
                      (27, 'Harpic Limpiador de Inodoro', 'Harpic', 'Limpieza profunda para el inodoro', 980, 45,'2030-02-02', 13),
                      (28, 'Finish Limpiador de Lavavajillas', 'Finish','Mantiene el lavavajillas limpio y sin residuos', 699, 48, '2030-06-11', 14),
                      (29, 'Easy-Off Limpiador de Horno', 'Easy-Off', 'Elimina la grasa acumulada en el horno', 2800, 16,'2026-08-25', 14),
                      (30, 'Clorotec Desinfectante para Piscinas', 'Clorotec','Mantiene el agua de la piscina limpia y cristalina', 4100, 33, '2027-06-29', 15),
                      (31, 'PoolShock Tratamiento para Piscinas', 'PoolShock', 'Elimina bacterias y algas en la piscina',9750, 12, '2026-07-19', 15),
                      (32, 'Pedigree Champú para Perros', 'Pedigree', 'Cuida la piel y el pelaje de tu mascota', 1600,14, '2025-12-22', 16),
                      (33, 'Domestos Limpiador de Cañerías', 'Domesticos','Elimina obstrucciones y malos olores en las cañerías', 9850, 17, '2029-11-27', 13),
                      (34, 'Easy-Off Limpiador de Microondas', 'Easy-Off', 'Elimina residuos y olores en el microondas',2145, 25, '2027-02-29', 14),
                      (35, 'Glade Ambientador en Aerosol', 'Glade', 'Fragancia fresca para el hogar', 650, 31,'2027-10-10', 17),
                      (36, 'Air Wick Ambientador Eléctrico', 'Air Wick', 'Aromatiza automáticamente tu casa', 1950, 61,'2028-11-17', 17),
                      (37, 'Sonax Limpiador de Tapicería', 'Sonax', 'Limpieza profunda para el interior del automóvil',3900, 45, '2029-07-08', 18),
                      (38, 'Turtle Wax Limpiador de Carrocería', 'Turtle Wax','Brillo y protección para la pintura del coche', 4500, 11, '2033-02-02', 18),
                      (39, 'Meguiars Limpiador de Llantas', 'Meguiars', 'Limpieza y brillo para las llantas', 3900, 35,'2032-01-01', 18),
                      (40, 'Desinfectante Antibacterial', 'Genérico', 'Elimina bacterias y virus en superficies', 500,11, '2028-04-17', 2)
                      ]

    datos_etiqueta = [(1, 'Peligroso'),
                      (2, 'Biodegradable'),
                      (3, 'Sin fragancia'),
                      (4, 'En oferta'),
                      (5, 'Con descuento'),
                      (6, '3 x 1'),
                      (7, '2 x 1'),
                      (8, 'Tóxico'),
                      (9, 'Agotado'),
                      (10, 'Con fragancia')
                      ]

    datos_etiqueta_producto = [(1, 1),
                               (2, 2),
                               (3, 3),
                               (4, 4),
                               (5, 5),
                               (6, 6),
                               (7, 7),
                               (8, 8),
                               (9, 9),
                               (10, 10),
                               (1, 11),
                               (2, 12),
                               (3, 13),
                               (4, 14),
                               (5, 15),
                               (6, 16),
                               (7, 17),
                               (8, 18),
                               (9, 19),
                               (10, 20),
                               (1, 21),
                               (2, 22),
                               (3, 23),
                               (4, 24),
                               (5, 25),
                               (6, 26),
                               (7, 27),
                               (8, 28),
                               (9, 29),
                               (10, 30),
                               (1, 31),
                               (2, 32),
                               (2, 33),
                               (3, 34),
                               (6, 35),
                               (8, 36),
                               (8, 37),
                               (10, 38),
                               (8, 39),
                               (4, 40)
                               ]


    # conexion.insertar_datos_categoria(datos_categoria)
    # conexion.insertar_datos_direccion(datos_direccion)
    # conexion.insertar_datos_ficha(datos_ficha)
    # conexion.insertar_datos_proveedor(datos_proveedor)
    # conexion.insertar_datos_usuario(datos_usuario)
    # conexion.insertar_datos_cliente(datos_cliente)
    # conexion.insertar_datos_metodo_pago(datos_metodo_pago)
    # conexion.insertar_datos_producto(datos_producto)
    # conexion.insertar_datos_etiqueta(datos_etiqueta)
    # conexion.insertar_datos_etiqueta_producto(datos_etiqueta_producto)



    conexion.cerrar_bd()
