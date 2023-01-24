def add_score(subject_score, subject, score):
    subject_score[f'{subject}'] = score
    return subject_score
print(add_score({'python': 50}, 'calculus', 60))

def calc_average_score():
    add_score