from PySimpleGUI import *


layout = [
    [Txt( "" * 10 )],
    [Text("", size = (15, 1), font = ("Helvetica", 18),
        text_color = "black", key = "input")],
    [ReadFormButton("1"), ReadFormButton("2"), ReadFormButton("3"), ReadFormButton("+"), ReadFormButton("-")],
    [ReadFormButton("4"), ReadFormButton("5"), ReadFormButton("6"), ReadFormButton("*"), ReadFormButton("/")],
    [ReadFormButton("7"), ReadFormButton("8"), ReadFormButton("9"), ReadFormButton("("), ReadFormButton(")")],
    [ReadFormButton("."), ReadFormButton("0"), ReadFormButton("del"), ReadFormButton("="), ReadFormButton("c")]
]

form = FlexForm("Calculator", default_button_element_size=(5, 2),
    auto_size_buttons=False, grab_anywhere=False)

form.Layout(layout)

result = ""
temp = ""
Answer = ""

def sub():
    x = float(result)
    y = float(temp)
    z = y-x
    result = z
    form.FindElement("input").Update(result)

def add():
    x = float(result)
    y = float(temp)
    z = y+x
    result = z
    form.FindElement("input").Update(result)

def mult():
    x = float(result)
    y = float(temp)
    z = y*x
    result = z
    form.FindElement("input").Update(result)

def div():
    x = float(result)
    y = float(temp)
    z = y/x
    result = z
    form.FindElement("input").Update(result)


while True:
    button, value =form.read()
    if (button == "del"):
        result = result[:-1]
        form.FindElement("input").Update(result)
    elif (button == "c"):
        result = ""   
        form.FindElement("input").Update(result)
    #elif (button == "-") or (button == "+") or (button == "*") or (button == "/"):
     #   temp = result
      #  result = ""
       # form.FindElement("input").Update(result)
    elif (button == "="):
        Answer = eval(result)
        Answer = str(round(float(Answer), 5))
        form.FindElement("input").Update(Answer)
        Answer = result
    elif len(result) == 16:
        pass
    else:
        result += button
        form.FindElement("input").Update(result)
    event, value = form.read()
    if (event == WIN_CLOSED):
        break
    


