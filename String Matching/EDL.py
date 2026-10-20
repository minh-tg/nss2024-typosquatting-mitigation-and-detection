KEYBOARD = {
    "1": ["Q", "2"],
    "2": ["1", "3", "Q", "W"],
    "3": ["2", "4", "W", "E"],
    "4": ["3", "5", "E", "R"],
    "5": ["4", "6", "R", "T"],
    "6": ["5", "7", "T", "Y"],
    "7": ["6", "8", "Y", "U"],
    "8": ["7", "9", "U", "I"],
    "9": ["8", "0", "I", "O"],
    "0": ["9", "-", "O", "P"],

    "Q": ["1", "2", "A", "W"],
    "W": ["2", "3", "Q", "E", "A", "S"],
    "E": ["3", "4", "W", "R", "S", "D"],
    "R": ["4", "5", "E", "T", "D", "F"],
    "T": ["5", "6", "R", "Y", "F", "G"],
    "Y": ["6", "7", "T", "U", "G", "H"],
    "U": ["7", "8", "Y", "I", "H", "J"],
    "I": ["8", "9", "U", "O", "J", "K"],
    "O": ["9", "0", "I", "P", "K", "L"],
    "P": ["0", "-", "O", "L"],

    "A": ["Q", "W", "S", "Z"],
    "S": ["W", "E", "A", "D", "Z", "X"],
    "D": ["E", "R", "S", "F", "X", "C"],
    "F": ["R", "T", "D", "G", "C", "V"],
    "G": ["T", "Y", "F", "H", "V", "B"],
    "H": ["Y", "U", "G", "J", "B", "N"],
    "J": ["U", "I", "H", "K", "N", "M"],
    "K": ["I", "O", "J", "L", "M"],
    "L": ["O", "P", "K", "."],

    "Z": ["A", "S", "X"],
    "X": ["Z", "S", "D", "C"],
    "C": ["X", "D", "F", "V"],
    "V": ["C", "F", "G", "B"],
    "B": ["V", "G", "H", "N"],
    "N": ["B", "H", "J", "M"],
    "M": ["N", "J", "K"],
    "-": ["0", "P", "_"],
    "_": ["-"],
    ".": ["L"],
    "@": [],
    "/": [],
    "!": [],
    "(": [],
    ")": [],
    "~": [],
    "'": [],
    "*": []
}


def near(source, destination):
    """Are two keys neighbors? A key counts as its own neighbor."""
    if source == destination:
        return True
    if not (source.isascii() and destination.isascii()):
        return False
    x, y = source.upper(), destination.upper()
    return x in KEYBOARD and y in KEYBOARD and (x == y or x in KEYBOARD[y])


def distance(target, candidate):
    """EDL distance from the legitimate name (target) to the candidate."""
    h, w = len(target), len(candidate)
    d = [[0] * (w + 1) for _ in range(h + 1)]

    def insert(i, y):
        # Insertion: 0.5 next to the previous target key, 2 otherwise.
        if not target:
            return 4
        return 1 if near(target[i - 1] if i else target[0], y) else 4

    for i in range(h + 1):
        d[i][0] = i                                     # deletion 0.5, also at the start
    for j, y in enumerate(candidate, 1):
        d[0][j] = d[0][j - 1] + insert(0, y)            # insertion before the first letter
    for i, x in enumerate(target, 1):
        for j, y in enumerate(candidate, 1):
            substitute = 0 if x == y else (1 if near(x, y) else 4)
            d[i][j] = min(d[i - 1][j] + 1,              # deletion 0.5
                          d[i][j - 1] + insert(i, y),   # insertion 0.5 / 2
                          d[i - 1][j - 1] + substitute) # match 0, substitution 0.5 / 2
            if i > 1 and j > 1 and target[i - 2] == y and candidate[j - 2] == x:
                d[i][j] = min(d[i][j], d[i - 2][j - 2] + 1)  # adjacent transposition 0.5
    return d[h][w] / 2


if __name__ == "__main__":
    for a, b, want in [("react", "reactr", 0.5), ("react", "reacto", 2), ("react", "reqct", 0.5),
                       ("react", "regct", 2), ("react", "rect", 0.5), ("react", "raect", 0.5)]:
        print(f"{a} -> {b}: {distance(a, b)} (paper: {want})")
