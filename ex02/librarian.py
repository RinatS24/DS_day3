import os

def install_libs():
    os.system("pip install -r array_libs.txt")
    os.system("pip list")
    os.system("pip list > requirements.txt")


if __name__ == "__main__":
    if os.getenv("VIRTUAL_ENV") != None:
        install_libs()