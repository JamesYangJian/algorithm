
def insert_sort_rec(seq, i):
    if i == 0:
        return
    
    insert_sort_rec(seq, i-1)
    
    j = i
    while j>0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        
        j -= 1
        
    return
    
def insert_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j>0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j], seq[j-1]
            j -= 1
            
    return
    
    
def select_sort_rec(seq, i):
    if i == 0:
        return
    
    start = i-1
    max_pos = start

    for j in range(start):
        print(j)
        if seq[j] > seq[max_pos]:
            max_pos = j
    
    if max_pos != start:
        seq[start], seq[max_pos] = seq[max_pos], seq[start]
        
    start = i-1
        
    select_sort_rec(seq, start)
    
def select_sort(seq):
    for i in range(len(seq)-1, 0, -1):
        max_pos = i
        for j in range(i):
            if seq[j] > seq[max_pos]:
                max_pos = j
        if max_pos != i:
            seq[i], seq[max_pos] = seq[max_pos], seq[i]
            
            
    return

    