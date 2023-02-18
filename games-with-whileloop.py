def flatten_list(arr: list) -> list:
    flattened = []
    app = [sub_val if type(val) is list else "" for val in arr for sub_val in val]
    print(app)
    return flattened


def main():
    print(flatten_list([1, [2, 3], 4, 5, [6, 7]]))


if __name__ == "__main__":
    main()
