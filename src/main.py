import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.environ.get("API_KEY")
print(f"API key: {api_key}")


def main():
    print("Hello from python-for-ml!")


if __name__ == "__main__":
    main()
