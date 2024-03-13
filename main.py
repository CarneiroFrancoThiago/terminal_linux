import subprocess

def change_terminal_colors():
    background_color = "'#1e1e1e'"
    text_color = "'#bfbfbf'"
    cursor_color = "'#4e4e4e'"

    command = f"gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$(gsettings get org.gnome.Terminal.ProfilesList default | awk '{{print $2}}')/ background-color {background_color}"
    subprocess.run(command, shell=True)

    command = f"gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$(gsettings get org.gnome.Terminal.ProfilesList default | awk '{{print $2}}')/ foreground-color {text_color}"
    subprocess.run(command, shell=True)

    command = f"gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$(gsettings get org.gnome.Terminal.ProfilesList default | awk '{{print $2}}')/ cursor-color {cursor_color}"
    subprocess.run(command, shell=True)

if __name__ == "__main__":
    change_terminal_colors()
