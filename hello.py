"""A minimal command-line greeting demo."""
import argparse

def greeting(name="World"):
    normalized_name = name.strip() or "World"
    return f"Hello, {normalized_name}!"

def main():
    parser = argparse.ArgumentParser(description="Print a friendly greeting.")
    parser.add_argument("--name", default="World", help="Name to greet")
    args = parser.parse_args()
    print(greeting(args.name))

if __name__ == "__main__":
    main()
