import datetime

def timestamp_to_date(timestamp):
    """Convierte un timestamp Unix en una fecha y hora legibles."""
    return datetime.datetime.fromtimestamp(int(timestamp)).strftime('%Y-%m-%d %H:%M:%S')

