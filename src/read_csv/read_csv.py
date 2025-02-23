import csv
import os


def read_csv(flags: dict[str, str]) -> dict[str, list]:
    """
    Reads a CSV file and returns its content as a dictionary. The keys of the dictionary are the column headers, and the values are lists of values in each column.

    :param:
        file_path (str): The path to the CSV file.

    :return:
        dict[str, list]: A dictionary where each key is a column header and the value is a list of values in that column.
    """
    if "file" in flags:
        file_path = flags["file"]
    elif "f" in flags:
        file_path = flags["f"]
    else:
        raise ValueError("No file path provided. Use --file or -f to specify the file path.")

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")

    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        headers_prep = next(reader)
        headers = []
        if flags["mode"] == "physics" or flags["m"] == "physics":
            for header in headers_prep:
                if header in ["time", "position", "velocity", "acceleration"]:
                    headers.append(header)
                else:
                    tmp = header.split(" ")[0].lower()
                    if tmp in ["time", "position", "velocity", "acceleration"]:
                        headers.append(tmp)
                    else:
                        headers.append(tmp.split("\"")[1].lower())
        data = {header: [] for header in headers}
        for row in reader:
            for header, value in zip(headers, row):
                if value == "":
                    data[header].append(None)
                else:
                    data[header].append(float(value))

    return data