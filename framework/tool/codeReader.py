import eventlet

with open(str(eventlet.__file__), "r") as f:
    print(f.read())