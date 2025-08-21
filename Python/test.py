myText = ['ahmed', 'mohamed', 'ali']

def format_text(text):
    return f'- {text.title().capitalize()} -'
myFormatedData = map(format_text, myText)

for name in myFormatedData:
    print(name)