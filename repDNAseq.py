new1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
fin = []
for i in range(len(new1)):
    print(new1[i:i+10])
    fin.append(new1[i:i+10])


seqs = {}
res = []
for i in range(len(new1)-9):
    seq = new1[i:i+10]
    if seq in seqs:
        seqs[seq] += 1
        if seqs[seq] == 2:
            res.append(seq)
    else:
        seqs[seq] == 1
print(res)
