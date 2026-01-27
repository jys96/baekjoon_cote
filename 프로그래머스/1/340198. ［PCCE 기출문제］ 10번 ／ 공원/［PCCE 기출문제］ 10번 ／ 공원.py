def solution(mats, park):
    answer = -1
    
    width = len(park)
    height = len(park)
    
    for mat in mats:
        for h in range(height):
            for w in range(width):
                target = park[h][w:w+mat]
                
                if target.count("-1") >= mat:
                    chk = False
                    end = h + mat
                    if end <= height:
                        for i in range(h, end):
                            h_target = park[i][w:w+mat]

                            if h_target.count("-1") >= mat:
                                chk = True
                            else:
                                chk = False
                                break
                            
                    if chk:
                        if answer < mat:
                            answer = mat
    
    return answer