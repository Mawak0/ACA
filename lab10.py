import heapq


def get_frequencies(text):
    frequencies = {}

    for symbol in text:
        if symbol not in frequencies:
            frequencies[symbol] = 0
        frequencies[symbol] += 1

    return frequencies


def build_tree(frequencies):
    heap = []
    counter = 0

    for symbol in frequencies:
        heapq.heappush(heap, (frequencies[symbol], counter, symbol))
        counter += 1

    if not heap:
        return None

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        new_node = (left[2], right[2])
        heapq.heappush(heap, (left[0] + right[0], counter, new_node))
        counter += 1

    return heap[0][2]


def build_codes(tree):
    codes = {}

    def dfs(node, code):
        if isinstance(node, str):
            if code == "":
                codes[node] = "0"
            else:
                codes[node] = code
            return

        dfs(node[0], code + "0")
        dfs(node[1], code + "1")

    if tree is not None:
        dfs(tree, "")

    return codes


def huffman_encode(text):
    frequencies = get_frequencies(text)
    tree = build_tree(frequencies)
    codes = build_codes(tree)

    encoded = ""
    for symbol in text:
        encoded += codes[symbol]

    return encoded, codes, tree, frequencies


def huffman_decode(encoded, tree):
    if tree is None:
        return ""

    if isinstance(tree, str):
        return tree * len(encoded)

    decoded = ""
    node = tree

    for bit in encoded:
        if bit == "0":
            node = node[0]
        else:
            node = node[1]

        if isinstance(node, str):
            decoded += node
            node = tree

    return decoded


def print_codes(codes):
    for symbol in sorted(codes):
        print(repr(symbol), codes[symbol])


text = "huffman algorithm example"

encoded, codes, tree, frequencies = huffman_encode(text)
decoded = huffman_decode(encoded, tree)

print("Исходный текст:", text)
print("Частоты:", frequencies)

print("Словарь кодов:")
print_codes(codes)

print("Закодированный текст:", encoded)
print("Восстановленный текст:", decoded)
print("Длина исходного текста в битах:", len(text) * 8)
print("Длина закодированного текста в битах:", len(encoded))
print("Сложность: O(n + k * log(k)), где n - длина текста, k - количество различных символов")
