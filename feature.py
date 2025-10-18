import platform

def system_info():
    return f"Running on: {platform.system()} {platform.release()}"

if __name__ == "__main__":
    print(system_info())
