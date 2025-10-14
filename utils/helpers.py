def convert_orientation(angle_degrees):
    """Convert angle in degrees to cardinal direction."""
    directions = ['North', 'North-East', 'East', 'South-East', 'South', 'South-West', 'West', 'North-West']
    idx = round(angle_degrees / 45) % 8
    return directions[idx]
