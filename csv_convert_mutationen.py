import csv
import datetime


def main():
    source_file_name = "studien.csv"
    target_file_name = "studien_modMolMarker.csv"
    mapping_file_name = "MolMarkerMapping.csv"
    log_file_name = "error.log"

    mapping_dictionary = {}
    with open(mapping_file_name, 'r', encoding="utf-8", newline="") as mapping_file:
        mapping_reader = csv.reader(mapping_file, delimiter=";")
        next(mapping_reader, None)  # skip first line
        for row in mapping_reader:
            mapping_dictionary.update({row[0]: [item.strip() for item in row[1].split('#')]})

    with open(source_file_name, 'r', encoding="utf-8", newline="") as source_file:
        csv_reader = csv.reader(source_file, delimiter=";")
        data = list(csv_reader)

    with open(log_file_name, 'a', encoding="utf-8") as log_file:
        log_file.write("started logging - " + str(datetime.datetime.now()) + "\n")
        for row in data[1:]:  # skip first line for changes
            if len(row[17]) > 0:
                tokenized_items = row[17].split('#')
                replacement_items = []
                for item in tokenized_items:
                    translation = mapping_dictionary.get(item.strip())
                    if translation is None:
                        log_file.write("missing translation: \"" + item + "\"\n")
                    elif len(translation) == 0:
                        pass  # empty translation shouldn't cause an error.log line
                    else:
                        replacement_items.extend(translation)
                row[17] = '#'.join(replacement_items)
        log_file.write("finished logging - " + str(datetime.datetime.now()) + "\n")

    with open(target_file_name, 'w', encoding="utf-8", newline="") as target_file:
        csv_writer = csv.writer(target_file, delimiter=";")
        csv_writer.writerows(data)


if __name__ == "__main__":
    main()
