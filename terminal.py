import subprocess
import keyboard


SECRET_COMMAND = "shadow"
SECRET_PASSWORD = "your_password"


def switch_account():
    print("Switching Windows account...")
    subprocess.run(
        "rundll32.exe user32.dll,LockWorkStation",
        shell=True
    )

# def check_for_all(inp):
#     if inp == 'all':
#         subprocess.Popen(
#             'start cmd /k runas /user:"your_windows_account" "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"',
#             shell=True
#         )
#     else

def launch_app_as_user():
    print("""
Available apps:
- chrome
- cmd
- notepad
""")

    app = input("> ")

    apps = {
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "cmd": "cmd.exe",
        "notepad": "notepad.exe"
    }

    if app in apps:
        subprocess.Popen(
            f'start cmd /k runas /user:"your_windows_account" "{apps[app]}"',
            shell=True
        )
    else:
        print("Unknown app.")

def check_exit_shortcut():
    if (
        keyboard.is_pressed("ctrl")
        and keyboard.is_pressed("alt")
        and keyboard.is_pressed("win")
        and keyboard.is_pressed("1")
        and keyboard.is_pressed("tab")
    ):
        print("\nEmergency exit activated.")
        exit()


def start_terminal():
    print("===============================================")
    print("                  JX TERMINAL                  ")
    print("===============================================")

    while True:

        check_exit_shortcut()

        command = input("> ")

        if command == "help":
            print("""
        Available commands:
        - status     : Check system status
        - vault      : Open private vault
        - about      : About this app
        - exit       : Close terminal
                    """)

        elif command == "status":
            print("System online.")

        elif command == "vault":
            print("Vault access requested.")

        elif command == "about":
            print("JX Terminal v1.0")

        elif command == "exit":
            print("Closing terminal...")
            break

        elif command == SECRET_COMMAND:
            print("""
        1. Launch app as your_windows_account
        2. Switch account
        """)

            choice = input("> ")

            if choice == "1":
                launch_app_as_user()

            elif choice == "2":
                switch_account()

            else:
                print("Cancelled.")

        else:
            print("Unknown command.")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_terminal()
    # open_secret_account()