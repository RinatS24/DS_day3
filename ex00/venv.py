import os

def env():
    print(f"Your current virtual env is {os.getenv("VIRTUAL_ENV")}")


if __name__ == "__main__":
    env()