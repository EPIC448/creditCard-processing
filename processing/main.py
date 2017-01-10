import sys, csv


def main_func(string):
    return string[::-1]


def get_content():
    try:
        # Open content from file passed as arg
        file_name = sys.argv[1]
        with open(file_name) as f:
            content = f.read()

    except IndexError:
        # Pass content in STDIN
        content = sys.stdin.read()

    return content


if __name__ == '__main__':

    content = get_content()

