# 두 정수 A와 B를 입력받은 다음, A/B를 출력하는 프로그램을 작성하시오.
# 수작업

A, B = map(int, input().split())

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)









# 함수 풀이
# 함수들을 먼저 정의합니다.
def Add(A, B):
    print(A + B)

def Sub(A, B):
    print(A - B)

def Multi(A, B):
    print(A * B)

def Split(A, B):
    print(A // B)

def Resume(A, B):
    print(A % B)

def main():
    # 1. 입력을 받습니다.
    A, B = map(int, input().split())

    # 2. 각 함수에 A와 B를 전달하며 '호출'합니다.
    Add(A, B)
    Sub(A, B)
    Multi(A, B)
    Split(A, B)
    Resume(A, B)

# 프로그램을 실행합니다.
if __name__ == "__main__":
    main() 