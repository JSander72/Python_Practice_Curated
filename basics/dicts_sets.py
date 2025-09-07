"""dicts_sets.py
Dictionaries and sets with common operations.
Run: python dicts_sets.py
"""
def main():
    person = {"name": "James", "role": "Software Engineer"}
    person["stack"] = ["Python", "JS"]  # add key

    # .get avoids KeyError and lets you set a default
    print("city:", person.get("city", "unknown"))

    # set removes duplicates, supports math set ops
    tags = {"python", "dev", "algorithms"}
    more = {"dev", "leetcode", "practice"}
    print("union:", tags | more)
    print("intersection:", tags & more)
    print("difference:", tags - more)

if __name__ == "__main__":
    main()
