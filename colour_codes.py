colours = {
    "blue":{"HTML":"0000FF","RGB":"(0,0,255)"},
    "red":{"HTML":"FF0000", "RGB":"(255,0,0)"},
    "yellow":{"HTML":"FFFF00","RGB":"(255,255,0)"},
    "green":{"HTML":"008000","RGB":"(0,128,0)"},
    "purple":{"HTML":"800080","RGB":"(128,0,128)"},
    "orange":{"HTML":"FFA500","RGB":"(255,165,0)"}}
    
while True:
    print(list(colours.keys()))
    colour_choice = input("Choose a colour (or 'stop' when done): ")
    if colour_choice == 'stop':
        break
    print(list(colours["blue"].keys()))
    code_choice = input("Choose a code: ")
    print(colours[colour_choice][code_choice])