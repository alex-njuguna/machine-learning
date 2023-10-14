from graphing import create_chart
from data_storage import read_column


user_menu = """pick a choice from the following options:

- "c" to chart a new graph.
- "q" to quit.

Your selection: """

charting_menu = "Enter the column you would like to chart: "

filename_prompt = "Enter your desired file name: "

def handle_chart():
    column = int(input(charting_menu))
    x = read_column(-1)
    y = [float(n) for n in read_column(column)]

    filename = input(filename_prompt)
    create_chart(x, y, filename.strip())

while True:
    user_selection = input(user_menu)

    if user_selection == "q":
        break
    elif user_selection == "c":
        handle_chart()
    else:
        print(f"Sorry, '{user_selection}' is not a valid option.")



