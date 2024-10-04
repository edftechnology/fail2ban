import subprocess

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
        print(f"Command executed successfully: {command}")
    except subprocess.CalledProcessError:
        print(f"Failed to execute command: {command}")

def main():
    # Lista de comandos para instalar e configurar Tex Live e fazer a limpeza do sistema
    commands = [
        "sudo apt clean",
        "sudo apt autoclean",
        "sudo apt autoremove -y",
        "sudo apt update",
        "sudo apt --fix-broken install",
        "sudo apt clean",
        "sudo apt list --upgradable",
        "sudo apt full-upgrade -y",
        "sudo apt install fail2ban -y",
        "sudo systemctl status fail2ban",
        "sudo systemctl start fail2ban",
        "sudo systemctl enable fail2ban",
        "sudo systemctl status fail2ban"
    ]

    for command in commands:
        run_command(command)

    print("Fail2Ban installation and system maintenance are complete.")

if __name__ == "__main__":
    main()

# [1] OPENAI.
# ***Monitoramento de acesso no linux.***
# Disponível em: <https://chat.openai.com/c/7772a507-88e7-46c8-ad7a-64a2d9011843> (texto adaptado).
# ChatGPT.
# Acessado em: 21/02/2024 12:00.
