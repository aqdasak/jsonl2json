from pathlib import Path
import sys

import json
import jsonlines


def main():
    if len(sys.argv) != 3:
        print("Usage: jl2j input_file output_file")
        exit()

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    if not Path(input_filename).exists():
        print(f"{input_filename} does not exist")
        exit()

    json_object = []
    try:
        with jsonlines.open(input_filename) as reader:
            for obj in reader:
                json_object.append(obj)
    except Exception as e:
        print(e)
        exit(1)

    with open(output_filename, "w") as output:
        json.dump(json_object, output, indent=2)


if __name__ == "__main__":
    main()
