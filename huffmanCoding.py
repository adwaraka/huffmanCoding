from collections import Counter
import heapq

class Node(object):

    def __init__(self, frequency, symbol, left=None, right=None):
        self.frequency = frequency
        self.symbol = symbol              # alphabets/alphanumeric chars
        self.huffmanEncoding = ''         # 0 or 1
        self.left = left
        self.right = right

    def __lt__(self, node):
        return self.frequency < node.frequency


def returnCode(node, code='', mapping={}):
    newCode = code + str(node.huffmanEncoding)
    if node.left:
        left = returnCode(node.left, newCode, mapping)

    if node.right:
        right = returnCode(node.right, newCode, mapping)

    if node.left is None and node.right is None:
        # print("{} -> {}".format(node.symbol, newCode))
        mapping[node.symbol] = newCode
        return mapping
    return {**left, **right}


def huffmanEncoding(freqChar):
    nodes = []
    for node in freqChar:
        heapq.heappush(nodes, Node(int(node[1]), node[0], None, None))

    while len(nodes) > 1:
        leftNode = heapq.heappop(nodes)
        rightNode = heapq.heappop(nodes)

        leftNode.huffmanEncoding = 0
        rightNode.huffmanEncoding = 1

        newNode = Node(leftNode.frequency + rightNode.frequency,
                       '',  # The new node need not have any symbol attached to it
                       leftNode,
                       rightNode
                       )

        heapq.heappush(nodes, newNode)
    # print(nodes[0].frequency)
    return nodes, returnCode(nodes[0])  # there should only be 1 node left


def huffmanDecoding(codedStr, nodeRoot):
    # print(codedStr)
    decoded, curr = "", nodeRoot
    for bit in codedStr:
        # print(bit)
        if bit == '0':
            curr = curr.left
        elif bit == '1':
            curr = curr.right
        if curr.left is None and curr.right is None:
            decoded+=curr.symbol
            curr = nodeRoot
    return decoded


if __name__ == "__main__":
    def main():
        arr = []
        with open('test.txt', 'r', encoding='utf-8') as fp:
            count = Counter(fp.read())
        for (i, j) in zip(count.keys(), count.values()):
            arr.append((i, j))
        nodes, _ = huffmanEncoding(arr)
        # print(coded)
        testString = (
            "0001110100100001111000010011101111110010"
            "01111010000010100011010"
            )
        print("Decoded string: {}".format(huffmanDecoding(testString, nodes[0])))
    main()
