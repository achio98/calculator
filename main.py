import PySimpleGUI as sg

sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Output(size=(23, 2), key='-OUTPUT-')],
          [sg.Button('7'), sg.Button('8'), sg.Button('9'), sg.Button('/')],
          [sg.Button('4'), sg.Button('5'), sg.Button('6'), sg.Button('*')],
          [sg.Button('1'), sg.Button('2'), sg.Button('3'), sg.Button('-')],
          [sg.Button('0'), sg.Button('.'), sg.Button('='), sg.Button('+')],
          [sg.Button('CE'), sg.Button('C')]]

# Create the Window
window = sg.Window('Calculator', layout)
# Event Loop to process "events" and get the "values" of the inputs
expression = []
value = ''
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # if user closes window or clicks cancel
        break
    if event.isdigit() or event is '.':
        if len(expression) > 1:
            if expression[1].isdigit():
                del expression[0]
                print(expression)
        value = value + event
        window['-OUTPUT-'].update(value)
    elif event == 'C':
        if len(expression) == 2:
            event = ''
            expression.pop()
        elif len(expression) > 0:
            expression.pop()
        window['-OUTPUT-'].update('')
        value = ''
    elif event == 'CE':
        expression = []
        value = ''
        window['-OUTPUT-'].update('')
    else:
        expression.append(value)
        expression.append(event)
        value = ''
        if expression[1] == '=':
            del expression[1]
        if '' in expression:
            expression.remove('')
    print(expression)
    if len(expression) > 3:
        score = eval(f"{expression[0]}{expression[1]}{expression[2]}")
        window['-OUTPUT-'].update(score)
        if event != '=':
            expression = [score, event]
        else:
            expression = [score]
        print(expression)

window.close()