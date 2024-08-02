def hex_to_rgb(hex_color):
    """Convert hex color to an RGB tuple."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def print_text_with_hex_color(hex_color, text):
    """Print text with the given hex color."""
    r, g, b = hex_to_rgb(hex_color)
    print(f"\033[38;2;{r};{g};{b}m{text}\033[0m", end="")