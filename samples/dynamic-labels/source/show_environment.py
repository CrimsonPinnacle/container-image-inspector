import os

if __name__ == "__main__":
    for key, value in sorted(os.environ.items()):
        print(f'{key}={value}')