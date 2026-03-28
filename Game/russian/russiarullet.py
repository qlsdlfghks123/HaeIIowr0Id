import random
import time


class Game:
    def game_start(self):

        print("\n게임이 시작되었습니다. 러시안 룰렛은 뭔지 아시죠?\n"
              "6발의 장탄수를 가지는 리볼버에 1개의 총알만 넣고 실린더를 돌린 뒤\n"
              "서로 돌아가며 총을 자기 머리에 대고 방아쇠를 당기는 복불복 결투게임입니다.\n\n"
              "상대는 컴퓨터입니다. 끝까지 살아남기를 바랍니다..\n")

        self.bullet = [0, 0, 0, 0, 0, 1]
        random.shuffle(self.bullet)

        print("운명은 정해졌습니다.\n")
        return self.bullet

    def select_you(self):
        try:
            answer = int(input("먼저 하실건가요? 당신이 고르세요.\n1.컴퓨터부터 2.나부터 \n\n대답:"))
            self.turn = answer
            if answer <= 0 or answer > 2:
                raise ValueError
            self.main_game()

        except ValueError:
            print("\n잘못 된 값을 입력하셨습니다. 다시 입력하세요.\n")
            self.select_you()

    def main_game(self):
        while len(self.bullet) > 0:
            shot = self.bullet.pop(0)
            if self.turn == 1:
                print("\n[컴퓨터의 차례]. 탄창을 확인 중입니다...")
                time.sleep(2)
                input("엔터를 누르면 컴퓨터가 방아쇠를 당깁니다!")
                time.sleep(1.5)
                if shot == 1:
                    print("빵!!!\nYou win!")
                    break
                else:
                    print("아쉽게도 당신의 차례가 되었습니다.")
                    print(f"남은 탄창:{len(self.bullet)}")
                    time.sleep(1)
                    self.turn = 2

            elif self.turn == 2:
                print("\n[당신의 차례] 방아쇠를 확인 중입니다...")
                time.sleep(2)
                input("준비가 되었으면 엔터를 누르세요!")
                time.sleep(1.5)
                if shot == 1:
                    print("빵!!!\n당신은 죽었습니다...")
                    break
                else:
                    print("운이 좋네요. 다음 게임으로 가시죠.")
                    print(f"남은 탄창:{len(self.bullet)}")
                    time.sleep(1)
                    self.turn = 1


if __name__ == "__main__":
    strat = Game()
    strat.game_start()
    strat.select_you()
