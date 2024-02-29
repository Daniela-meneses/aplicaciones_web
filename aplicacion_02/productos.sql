CREATE TABLE IF NOT EXISTS productos (
    nombre TEXT,
    descripcion TEXT,
    precio INTEGER,
    existencias INTEGER
);

INSERT INTO productos (nombre, descripcion, precio, existencias) VALUES
    ('Smartphone Samsung Galaxy S20', 'Smartphone con cámara de alta resolución y pantalla AMOLED.', 10000, 150),
    ('Televisor LG 4K 55 pulgadas', 'Televisor Ultra HD con tecnología HDR.', 15000, 100),
    ('Auriculares inalámbricos Sony', 'Auriculares con cancelación de ruido y larga duración de batería.', 3000, 300),
    ('Tablet Apple iPad Air', 'Tablet ligera y potente con pantalla Retina.', 12000, 120),
    ('Cámara digital Canon EOS Rebel T7', 'Cámara DSLR ideal para principiantes con lente incluido.', 8000, 80),
    ('Consola de videojuegos Xbox Series X', 'Consola de última generación con capacidad de reproducción en 4K.', 25000, 50),
    ('Impresora multifuncional Epson EcoTank', 'Impresora con sistema de tanque de tinta que reduce costos de impresión.', 6000, 90),
    ('Robot aspirador iRobot Roomba', 'Robot inteligente que aspira y limpia automáticamente pisos.', 9000, 70);
