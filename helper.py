def greet(name):
    return f"Hello, {name}!"

def goodbye(name):
    return f"Goodbye, {name}!"

def get_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")
