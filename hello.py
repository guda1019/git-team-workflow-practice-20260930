"""A minimal command-line greeting demo."""
import argparse

def greeting(name="World"):
    return f"Hello, {name}!"

def main():
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greeting(args.name))

if __name__ == "__main__":
    main()
