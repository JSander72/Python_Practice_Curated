"""io_files.py
Read/write text files safely with context managers.
"""
from pathlib import Path

def main():
    p = Path("example.txt")
    p.write_text("Hello file!\nLine 2\n", encoding="utf-8")
    text = p.read_text(encoding="utf-8")
    print(text.strip().splitlines())

if __name__ == "__main__":
    main()
