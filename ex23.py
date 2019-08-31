import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        # interesting... calling the "main" functino inside itself
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    # this just works as an line skip "\n"
    next_lang = line.strip
    #this is for decoding bytes
    raw_bytes = next_lang.encode(encoding, errors=errors)
    #this is for enconding strings
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # here we print the out both of them
    print(raw_bytes, "<===>", cooked_string)

# this is for opening the langauges.txt file
languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error)
