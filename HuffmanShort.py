import heapq

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq, self.symbol, self.left, self.right, self.huff = freq, symbol, left, right, ''
    def __lt__(self, nxt):
        return self.freq < nxt.freq

def printNodes(node, val=''):
    newVal = val + str(node.huff)
    if node.left: printNodes(node.left, newVal)
    if node.right: printNodes(node.right, newVal)
    if not node.left and not node.right: print(f"{node.symbol} -> {newVal}")

def encode_text(text, huffman_tree):
    encoding_map = {}
    def traverse_tree(node, code=''):
        if node.left: traverse_tree(node.left, code + '0')
        if node.right: traverse_tree(node.right, code + '1')
        if not node.left and not node.right: encoding_map[node.symbol] = code
    traverse_tree(huffman_tree)
    return ''.join(encoding_map[char] for char in text)

def decode_text(encoded_text, huffman_tree):
    decoded_text, current_node = '', huffman_tree
    for bit in encoded_text:
        current_node = current_node.left if bit == '0' else current_node.right
        if not current_node.left and not current_node.right:
            decoded_text += current_node.symbol
            current_node = huffman_tree
    return decoded_text

chars, freq = input().split(), map(int, input().split())
nodes = [Node(f, c) for f, c in zip(freq, chars)]
while len(nodes) > 1:
    left, right = heapq.heappop(nodes), heapq.heappop(nodes)
    left.huff, right.huff = '0', '1'
    heapq.heappush(nodes, Node(left.freq + right.freq, left.symbol + right.symbol, left, right))
printNodes(nodes[0])
huffman_tree = nodes[0]
print("Decoded text:", decode_text(input(), huffman_tree))
print("Encoded binary text:", encode_text(input(), huffman_tree))
