def add_score(subject_score, subject, score):
    subject_score[f'{subject}'] = score
    return subject_score
dic = add_score({'python': 50}, 'calculus', 60)
def calc_average_score(dic):
    score_total = 0
    for key, value in dic.items():
        score_total += value
    average = score_total/2
    return(f'{average:.2f}')
    
print(calc_average_score(dic))