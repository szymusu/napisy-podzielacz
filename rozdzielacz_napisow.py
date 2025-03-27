def read_file(filename):
    with open(filename) as file:
        lines = file.readlines()

    subs = []

    i = 0
    while i < len(lines):
        index = int(lines[i])
        i += 1
        time = lines[i].strip()
        i += 1
        text = lines[i].strip()
        i += 2

        subs.append((index, time, text))
    return subs


def write_file(filename, subs):
    with open(filename, 'w') as file:
        for sub in subs:
            text = split_text(sub[2])
            file.write(f"{sub[0]}\n{sub[1]}\n{text}\n\n")


def split_text(text: str) -> str:
    if len(text) < 40:
        return text

    i = text.rfind(" ", 0, len(text) // 2)
    if text[i - 2] == " ":
        i -= 2
    return "\n".join([text[:i], text[i + 1:]])


if __name__ == '__main__':
    subs = read_file("adamczyk dzwiek.srt")
    print(subs)

    write_file("adamczyk dzwiek rozdzielone.srt", subs)