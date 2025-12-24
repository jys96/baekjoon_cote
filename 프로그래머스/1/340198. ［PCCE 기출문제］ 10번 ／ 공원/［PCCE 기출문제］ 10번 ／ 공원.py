def solution(mats, park):
    
    mats.sort(reverse=True)
    
    rows = len(park)      
    cols = len(park[0])   
    
    for size in mats:
        
        for i in range(rows - size + 1):
            for j in range(cols - size + 1):
                
                
                can_place = True
                
                
                for r in range(size):
                    for c in range(size):
                        
                        if park[i + r][j + c] != "-1":
                            can_place = False
                            break
                    if not can_place:
                        break
                
                if can_place:
                    return size
    
    return -1