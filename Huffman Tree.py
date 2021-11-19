import heapq
# Node class for the tree
class Node:
    def __init__(self, value, num, left=None, right=None):
        self.value = value
        self.num = num
        self.left = left
        self.right = right

    # A "less-than" function
    def __lt__(self, other):
        return self.num < other.num

# Putting codes into a dictionary
def getCodes(binTree, code, dic):
    if binTree == None:
        return
    if binTree.value != '':
        dic[binTree.value] = code
        return

    #codepath going right or left
    getCodes(binTree.left, code + '0', dic)
    getCodes(binTree.right, code + '1', dic)

# Main method for calculations
def huffman(content):
    d = {}
    for character in content:
        if character in d:
            d[character] += 1
        else:
            d[character] = 1

    pq = []
    for chars in d:
        heapq.heappush(pq, Node(chars, d[chars]))
    # Min heap while loop
    while len(pq) > 1:
        min = heapq.heappop(pq)
        min2 = heapq.heappop(pq)

        heapq.heappush(pq, Node('', min.num + min2.num, min, min2))

    binCodes = {}
    getCodes(pq[0], "", binCodes)
    return binCodes

# Turning lists into strings to be taken
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
numbers = [77, 37, 32, 42, 120, 24, 17, 50, 76, 4, 7, 42, 24, 67, 67, 20, 5, 59, 67, 85, 17, 12, 22, 4, 22, 2]
freqxlen = [77, 37, 32, 42, 120, 24, 17, 50, 76, 4, 7, 42, 24, 67, 67, 20, 5, 59, 67, 85, 17, 12, 22, 4, 22, 2, 3290]

res = []
for i, x in enumerate(letters): # by enumerating you get both the item and its index
    res += x * numbers[i] # add the next item to the result list
join = ' '.join(str(e) for e in res)
content = join.replace(" ", "")

# Sorting in alphabetical order
binCodes = huffman(content)
binCodes2 = sorted(binCodes, key=lambda x: x[0], reverse=False)

print('       Letter   Frequency   Code   Length   Freq X Len ')
print('      -------- ----------- ------ -------- ------------  ')
for chars in binCodes2:
    Length = len(binCodes[chars])
    FreqxLen = Length * (content.count(chars))
    print('%10s %10s %10s %5s %10s' % (chars, content.count(chars), binCodes[chars], Length, FreqxLen))
total = 0
list_size = len(freqxlen)
loop_counter = 0
while loop_counter < list_size:
    total = total + freqxlen[loop_counter]
    loop_counter = loop_counter + 1
print("\nThe weighted minimum path length is: ", total)
