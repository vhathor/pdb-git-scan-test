"""Sample file for the Git-backed workspace scan test."""
import re
import requests
import yaml
from collections import Counter
from snowflake.snowpark import Session


def main():
    words = re.findall(r"\w+", "scan git workspace scan test")
    print(Counter(words).most_common(3))
    print(yaml.safe_dump({"ok": True}))


if __name__ == "__main__":
    main()
