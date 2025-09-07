"""exceptions_logging.py
Basic try/except and logging best practices.
"""
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")

def safe_div(a: float, b: float) -> float:
    try:
        return a / b
    except ZeroDivisionError:
        logging.exception("Division by zero!")
        return float('inf')

def main():
    logging.info("starting run")
    print(safe_div(10, 2))
    print(safe_div(1, 0))

if __name__ == "__main__":
    main()
