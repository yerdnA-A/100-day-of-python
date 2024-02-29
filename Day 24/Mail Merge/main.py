PLACEHOLDER = '[name]'

with open('Day 24/Mail Merge/Input/Names/invited_names.txt', 'r') as names:
    invite_names = names.readlines()

with open('Day 24/Mail Merge/Input/Letters/starting_letter.txt', 'r') as file:
    invite_template = file.read()
    for name in invite_names:
        strip_name = name.strip()
        new_letter = invite_template.replace(PLACEHOLDER, strip_name)
        with open(f'Day 24/Mail Merge/Output/ReadyToSend/letter_for_{strip_name}.txt', 'w') as letter_comp:
            letter_comp.write(new_letter)


