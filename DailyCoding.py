'''
# Daily coding challenge
Given hash table : 
1 - a
2 - b
...
26 - z

input: string of number
output: num ways that encode the message
'''

def counting(data, k, mem):
    #base case 1: data.length = 0
    if k == 0:
        return 1

    #base case 2: data[start] = 0
    startIndex = len(data) - k
    if data[startIndex] == '0':
        return 0
    if mem[k] != -1:
        return mem[k]

    #always decode the first character
    res = counting(data, k - 1,mem)
    
    #if data[start:start+2] can be decoded
    if k>=2 and int(data[startIndex:startIndex+2]) <= 26:
        res+= counting(data, k - 2, mem)
    mem[k] = res
    return res

def finalCount(data):
    mem = [-1 for x in range(len(data) + 1)]
    return counting(data, len(data), mem)

testCase = ["129","122222","01111111","","9999"]
for x in range(len(testCase)):
    print(finalCount(testCase[x]))

'''
output:
2
13
0
1
1
'''