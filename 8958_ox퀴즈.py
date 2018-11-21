def QuizScore(s):
    score=0
    l=s.split("X")
    if "" in l:l.remove("")
    for i in l:
        numO=len(i)
        score+=numO*(numO+1)/2
    return score

a=int(input())
for c in range(a):
    quiz=input()
    print(int(QuizScore(quiz)))