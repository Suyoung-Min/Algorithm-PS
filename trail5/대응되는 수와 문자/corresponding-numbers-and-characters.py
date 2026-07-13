n, m = map(int, input().split())

# Note: Using 1-based indexing for words as per C++ code
words = [""] + [input() for _ in range(n)]
queries = [input() for _ in range(m)]

words2int = {}
int2words = {}

tidx = 0

for word in words:
    words2int[word] = tidx
    tidx += 1

int2words = {str(v):k for k, v in words2int.items()}


for query in queries:
    if query.isdigit():
        print(int2words[query])
    else:
        print(words2int[query])