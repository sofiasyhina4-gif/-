# TODO импортировать необходимые молули

import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"

def task() -> None:
    file = open(INPUT_FILENAME, "r", encoding="utf-8")
    lines = file.read().split("\n")
    file.close()
    headers = lines[0].split(",")

    result = []
    for line in lines[1:]:
        if line == "":
            continue
        values = line.split(",")
        row = {}
        for i in range(len(headers)):
            row[headers[i]] = values[i]
        result.append(row)
    # TODO считать содержимое csv файла

    out = open(OUTPUT_FILENAME, "w", encoding="utf-8")
    json.dump(result, out, ensure_ascii=False, indent=4)
    out.close()
    # TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")