# Program of the Day: Huffman Coding

import heapq
from collections import Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):
    heap = [HuffmanNode(char, freq) for char, freq in freq_table.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(node, code="", huffman_codes={}):
    if node is not None:
        if node.char is not None:
            huffman_codes[node.char] = code
        build_huffman_codes(node.left, code + "0", huffman_codes)
        build_huffman_codes(node.right, code + "1", huffman_codes)

    return huffman_codes

# Example usage
text = "hello world"
frequency_table = Counter(text)
huffman_tree_root = build_huffman_tree(frequency_table)
huffman_codes = build_huffman_codes(huffman_tree_root)

print("Huffman Codes:")
for char, code in huffman_codes.items():
    print(char, ":", code)
