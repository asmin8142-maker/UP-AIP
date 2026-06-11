CSV_PATH = 'data/dataset.csv'

DATE_COL = 'time'

NUMERIC_COLS = {
    'Температура': 'temperature_2m (°C)',
    'Влажность': 'relative_humidity_2m (%)',
    'Осадки': 'precipitation (mm)',
    'Скорость ветра': 'wind_speed_10m (km/h)'
}

DEFAULT_COL = 'temperature_2m (°C)'

STYLE = 'seaborn-v0_8-whitegrid'

PALETTE = [
    '#2563EB',
    '#0891B2',
    '#7C3AED',
    '#059669',
    '#DC2626'
]

TITLE = 'Климат Астаны: как меняется погода'

FIG_SIZE = (18, 10)

HIST_BINS = 25
SCATTER_ALPHA = 0.5
PIE_BINS = 4