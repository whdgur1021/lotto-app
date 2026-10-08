import tkinter as tk
import random


# 번호 구간에 맞는 로또 공 색상 반환
def get_ball_color(number):
    if number <= 10:
        return "#FBC400"  # 노랑
    elif number <= 20:
        return "#69C8F2"  # 파랑
    elif number <= 30:
        return "#FF7272"  # 빨강
    elif number <= 40:
        return "#AAAAAA"  # 회색
    else:
        return "#B0D840"  # 초록


# 로또 번호 생성 버튼을 눌렀을 때 실행
def generate_lotto_numbers():
    if len(number_sets) >= 5:
        message_label.config(text="최대 5세트까지 만들었어요. 초기화 후 다시 생성하세요.")
        return

    # 1~45 중 중복 없이 6개를 뽑고 오름차순으로 정렬
    numbers = sorted(random.sample(range(1, 46), 6))
    number_sets.append(numbers)

    # 번호 세트를 표시할 한 줄 만들기
    row = tk.Frame(result_frame)
    row.pack(pady=5)

    set_label = tk.Label(row, text=f"{len(number_sets)}세트", width=6)
    set_label.pack(side="left", padx=5)

    # 번호를 색깔 공으로 표시
    for number in numbers:
        ball = tk.Canvas(
            row,
            width=42,
            height=42,
            highlightthickness=0
        )
        ball.pack(side="left", padx=3)

        color = get_ball_color(number)
        ball.create_oval(2, 2, 40, 40, fill=color, outline="")
        ball.create_text(
            21,
            21,
            text=str(number),
            font=("Arial", 12, "bold")
        )

    message_label.config(text="")


# 초기화 버튼을 눌렀을 때 실행
def reset_lotto_numbers():
    number_sets.clear()

    # 화면에 표시된 번호 세트 모두 지우기
    for widget in result_frame.winfo_children():
        widget.destroy()

    message_label.config(text="번호를 다시 생성할 수 있어요.")


# 프로그램 창 만들기
window = tk.Tk()
window.title("로또 번호 생성기")
window.geometry("430x450")

title_label = tk.Label(
    window,
    text="로또 번호 생성기",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)

# 버튼을 나란히 배치할 프레임
button_frame = tk.Frame(window)
button_frame.pack(pady=10)

generate_button = tk.Button(
    button_frame,
    text="로또번호 생성",
    font=("Arial", 12),
    command=generate_lotto_numbers
)
generate_button.pack(side="left", padx=5)

reset_button = tk.Button(
    button_frame,
    text="초기화",
    font=("Arial", 12),
    command=reset_lotto_numbers
)
reset_button.pack(side="left", padx=5)

message_label = tk.Label(window, text="")
message_label.pack()

result_frame = tk.Frame(window)
result_frame.pack(pady=10)

# 생성한 번호 세트를 저장하는 목록
number_sets = []

window.mainloop()