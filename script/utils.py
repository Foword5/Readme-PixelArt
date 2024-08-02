def print_colored_text_hex(hex_color, text):
    hex_color = hex_color.lstrip('#')
    r, g, b = int(hex_color[:2], 16), int(hex_color[2:4], 16), int(hex_color[4:], 16)
    
    ansi_code = f"\033[38;2;{r};{g};{b}m"
    
    print(f"{ansi_code}{text}\033[0m", end="")