import os


def main():
    output_path = os.environ["GITHUB_OUTPUT"]

    with open(output_path, "a") as f:
        f.write("test=false")


if __name__ == '__main__':
    main()
