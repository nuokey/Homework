tag = input()

tags = ["a", "abbr", "b", "body", "caption", "cite","code", "div", "form", "h1", "h2", "h3", "h4", "h5", "h6", "header", "i", "s"]
if tag in tags:
    s = input()
    print(f"<{tag}>{s}</{tag}>")
else:
    print("Введен неверный тэг")