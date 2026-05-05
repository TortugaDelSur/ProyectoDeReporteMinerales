-- Crear tabla de precios históricos
CREATE TABLE IF NOT EXISTS precios_commodities (
    id SERIAL PRIMARY KEY,
    nombre_commodity VARCHAR(50) NOT NULL, -- Ejemplo: 'Cobre', 'Litio'
    precio DECIMAL(12, 4) NOT NULL,         -- Usamos decimal para precisión financiera
    moneda VARCHAR(10) DEFAULT 'USD',      -- Divisa de referencia
    unidad VARCHAR(20),                    -- Ejemplo: 'libra', 'tonelada'
    fuente_dato VARCHAR(100),              -- URL o nombre del sitio web
    fecha_extraccion TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índice para acelerar las consultas por tiempo (muy útil para reportes)
CREATE INDEX IF NOT EXISTS idx_fecha_commodity ON precios_commodities (nombre_commodity, fecha_extraccion DESC);