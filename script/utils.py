def show_progress(percentage, bar_length=40):
    if not 0 <= percentage <= 100:
        raise ValueError("Percentage must be between 0 and 100.")

    # Calculate the number of filled characters
    filled_length = int(bar_length * percentage // 100)
    
    # Create the bar
    bar = '█' * filled_length + '-' * (bar_length - filled_length)
    
    # Display the bar
    print(f'\r|{bar}| {percentage}% ', end="")

def print_colored_text_hex(hex_color, text):
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
    
    ansi_code = f"\033[38;2;{r};{g};{b}m"
    
    print(f"{ansi_code}{text}\033[0m", end="")