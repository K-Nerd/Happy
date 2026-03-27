item = [115,65,97,88,55,110,100,90,67,75,80,84,70,110,120,92,103] # 115,65,97,88,55,110,100,90,67,75,80,84,70,110,120,92,103
answer=""   # A B A C B A A C B C C C B A A B A 
            # A B A C B A A C B C C C B A A B A
            # AABBACABAABACBBACCCBCBBAABABBA
            # AABBACABABABBACCCBCBCABABBA
for x in item:
    if x>110 :
        answer+='A'
    elif x<70:
        answer+='B'
    elif x<=90:
        answer+='C'
    if x%3==1:
        answer+='A'
    elif x%4<3:
        answer+='B'
    else:
        answer+='C'

print(answer)
    