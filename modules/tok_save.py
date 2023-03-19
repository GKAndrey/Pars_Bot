import os

PATH = os.path.abspath(__file__+"/../..")

def toks(t):
    with open(os.path.join(os.path.join(PATH, "modules"), "tokns.py"), "w") as f:
        f.write(f"tok = {t}")