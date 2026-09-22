# Tarea 1 — MA3402 Estadística

(Falta: semilla-describir modelo-revisar la estructura-describir mejor las instrucciones)


Grupo: Miguel Astudillo-Nyx Butelmann-Benjamin Bravo-Gonzalo Castro

## Descripción
Modelo de call center (rellenar)

## Estructura
- `data/`: datos crudos y procesados
- `notebooks/`: los 4 notebooks de la tarea (uno por parte)
- `src/`: funciones auxiliares reutilizadas entre notebooks
- `results/`: gráficos y outputs generados

## Cómo ejecutar
1. Crear entorno virtual: `python -m venv venv`
2. Activar: `venv\Scripts\activate` (Windows) o `source venv/bin/activate` (Mac/Linux)
3. Instalar dependencias: `pip install -r requirements.txt`
4. Abrir los notebooks en `notebooks/` y ejecutar en orden

## Semilla
Se utiliza `np.random.default_rng(SEMILLA)` con semilla fija = [nuestro número] para reproducibilidad