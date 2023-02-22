import modules.create_json as cj
import turtle as tur
dict1 = {
    'name': 'Feliks',
    'surname': 'Novoselskyi',
    'age': '13'
}
dict2 = {}

cj.create_json("json\\new_json.json",dict1)
data = cj.read_json("json\\new_json.json")

dict2.update(data)

scr = tur.Screen()

tur.hideturtle()
tur.write(dict2["name"], move=False, align='left', font=('Arial', 20, 'normal'))
tur.penup()
tur.right(90)
tur.forward(50)
tur.write(dict2["surname"], move=False, align='left', font=('Arial', 20, 'normal'))

tur.forward(50)
tur.write(dict2["age"], move=False, align='left', font=('Arial', 20, 'normal'))

tur.done()
















