import PySimpleGUI as sg

print(sg)
print('Hello World')
#Step 1 :Theme
#sg.theme("DarkAmber")
#Step 2: Layout
layout = [
    [sg.Text("Type Name Here:")],
    [sg.InputText("")],
    [sg.Text("Type Age Here:")],
    [sg.InputText("")],
    [sg.Text("Type Postion Here:")],
    [sg.InputText("")],
    [sg.Text("Add Notes Here:")],
    [sg.InputText("")],
    [sg.Button("Ok"), sg.Button("Cancel")]
]
#Step 3: Window
window = sg.Window("Form", layout)
#Step 4: While loop
while True:
    event, values = window.read()
    if (event == "Cancel") or (event == sg.WIN_CLOSED):
        break
    print(
        values[0], "\n",
        values[1], "\n",
        values[2], "\n",
        values[3])
input = [values[0], values[1], values[2], values[3], "\n"]
with open("info.txt", "a") as info:
    for line in input:
        info.write(line)
        info.write('\n')


