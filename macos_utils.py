import subprocess

def get_mac_info():
    try:
        result = subprocess.run(['sw_vers'], capture_output=True, text=True)
        return result.stdout
    except:
        return "Не удалось получить информацию о macOS"
