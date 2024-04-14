'''try:
    file = open("Day 30/a_file.txt")
    a_dictionary = {"key" : "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("Day 30/a_file.txt", 'w')
    file.write("File create")
except KeyError as error_msg:
    print(f"The key {error_msg} does't jexists")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("I create this")'''

altura = float(input("Altura:"))
peso = float(input("Peso:"))

imc = peso / altura ** 2

if altura > 2.5:
    raise ValueError("A sua altura não deve ultrapassar 2.50")
else:
    print(imc)