score_list = []
sum = 0

score_list.append(int(input()))
score_list.append(int(input()))
score_list.append(int(input()))
score_list.append(int(input()))
score_list.append(int(input()))

for score in score_list:
    if score < 40:
        sum += 40
    else:
        sum += score

print(sum // len(score_list))