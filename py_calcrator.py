import PySimpleGUI as sg
import numpy as np

layout =[[sg.Output(size=(50,1),key="-log-")],
        [sg.Output(size=(50,7),key="-output-")],
        [sg.Button('7',key="-7-",size = (7,5)), sg.Button('8',key="-8-",size = (7,5)), sg.Button('9',key="-9-",size = (7,5)),sg.Button('÷',key="-/-",size = (7,5)) ],
        [sg.Button('4',key="-4-",size = (7,5)), sg.Button('5',key="-5-",size = (7,5)), sg.Button('6',key="-6-",size = (7,5)),sg.Button('x',key="-x-",size = (7,5)) ],
        [sg.Button('1',key="-1-",size = (7,5)), sg.Button('2',key="-2-",size = (7,5)), sg.Button('3',key="-3-",size = (7,5)),sg.Button('-',key="---",size = (7,5)) ],
        [sg.Button(' ',key="- -",size = (7,5)),sg.Button('0',key="-0-",size = (7,5)),sg.Button(' ',key="- -",size = (7,5)),sg.Button('+',key="-+-",size = (7,5))]
]

window = sg.Window('Calculator', layout,size=(400,600))

num_1 = ""
oparator = ""
num_2 = ""
num_3 = 0
num_4 = 0


while True:
    event, values = window.read()
    if event == "-9-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "9"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-8-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "8"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-7-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "7"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-6-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "6"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-5-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "5"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-4-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "4"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-3-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "3"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-2-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "2"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-1-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "1"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-0-":
        window["-output-"].update("")
        num_1 = num_2
        num_2 = "0"
        num_2 += num_1
        print(num_2[::-1])
    if event == "-+-":
        window["-output-"].update("")
        window["-log-"].update(num_2[::-1])
        num_4 = num_3
        num_3 = int(num_2[::-1])
        window["-output-"].update("")
        window["-log-"].update(num_4 + num_3)
        num_3 += num_4
        num_2 = ""
    if event == sg.WIN_CLOSED:
        break



