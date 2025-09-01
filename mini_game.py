import random

def play_game():
    print("🎯 숫자 맞추기 게임에 오신 것을 환영합니다!")
    print("컴퓨터가 1부터 100 사이의 숫자를 선택했습니다.")

    secret_number = random.randint(1, 100) # 1부터 100까지 숫자 중에 랜덤 선택
    attempts = 0

    while True:
        try:
            guess = int(input("숫자를 입력하세요 (1~100): "))
            attempts += 1

            if guess == secret_number:
                print(f"축하합니다! 정답은 {secret_number}였습니다!")
                print(f"총 {attempts}번 만에 맞추셨네요!")
                print("당신은 천재입니다!")
                break
            elif guess < secret_number:
                print("틀렸습니다! 더 큰 숫자입니다.")
            else:
                print("틀렸습니다! 더 작은 숫자입니다.")
        except ValueError:
            print("숫자가 아닌 다른 문자는 입력할 수 없습니다. 다시 시도해주세요.")

# 게임 시작 및 재시작 로직
while True:
    play_game()
    play_again = input("\n게임을 다시 하시겠습니까? (예/아니오): ").lower()
    if play_again != '예':
        print("게임을 종료합니다. 다음에 또 만나요!")
        break