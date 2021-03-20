import pandas

data = pandas.read_csv("C:/Users/domin/OneDrive/Desktop/Python/100 days of code/Proyectos Profesionales/C Morse/morse.csv")
df = pandas.DataFrame(data)
dictionary = df.to_dict()

morse_dict= {dictionary["letter"][n]: dictionary["code"][n] for n in dictionary["letter"]}

word = input("What is you word?\n").upper()

pal_list = [morse_dict[n] for n in list(word) if n in morse_dict]     

print(f'{word} = {(pal_list)}')

