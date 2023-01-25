def add_score(subject_score, student, subject, score):
    if student not in subject_score:
        subject_score[student] = {}
    subject_score[student][subject] = score
    return subject_score
dic = add_score({'65010001': {'python': 50}}, '65010001', 'calculus', 60)
id_student = []
subject = []
score = []

for key, value in dic.items():
    id_student.append(key)
    subject.append(value)
    
for i in range(0, len(subject)):
    for key, value in subject[i].items():
        score.append(value)

def calc_average_score(dic):
    new_dict = {}
    score_total = sum(score)
    average = f'{score_total/2:.2f}'
    for i in range(len(id_student)):
        new_dict[id_student[i]] = average
    return new_dict
print(calc_average_score(dic))