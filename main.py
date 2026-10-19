def main():
    with open("words.txt", encoding="utf-8") as f:
        words = [w.strip() for w in f if w.strip()]
    print("Hello World!")
    print(f"Total words: {len(words)}")
    for w in words:
        print("-", w)


if __name__ == "__main__":
    main()
