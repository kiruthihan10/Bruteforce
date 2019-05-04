def main(n):
    n = int(n)
    uni = []
    for i in range(0,n):
        uni.append(32)
    words = []
    word = ''
    while word.count('~')!=n:
        uni.reverse()
        x=1
        i=uni[0]
        if i == 126:
            i=33
            uni[1]=uni[1]+1
        else:
            i=i+1
        uni[0]=i
        
        for i in uni[1:]:
            if i > 126:
                i=33
                uni[x]=i
                uni[x+1]=uni[x+1]+1
            x+=1
        if 32 in uni:
            zero = uni.index(32)
            zero = n-1-zero
        else:
            zero = -1
        uni.reverse()
        word = ''
        for i in uni[zero+1:]:
            word+=chr(i)
        print (word)
        words.append(word)
    print(len(words))
    print(list(set(words)).sort() == words.sort())
import time
start = time.time()
main(3)
print(time.time()-start)
