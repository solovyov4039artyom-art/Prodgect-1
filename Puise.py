
APP_NAME ="PULSE"
notes_count = 0
notes_text = ""

print(f"=== {APP_NAME} v0.1 ===")


while True:
    print("\n1 — Добавить заметку")
    print("2 — Показать заметки")
    print("q — Выход")
    cmd=input("Введите команду: ")
    if cmd == "1":
        text = "Заметка " + str(notes_count + 1)
        notes_count += 1
        notes_text += f"\n{text} "
        notes_text += input("Введите текст заметки: ")
        print(f"Добавлено: {text}")
    elif cmd == "2":
        if notes_count == 0 :
            print ("заметок нет ")
        else:
            print(notes_text)
    elif cmd == "q":
        print("Пока!")
        break
    else:
        print("Неизвестная команда")
        print()
