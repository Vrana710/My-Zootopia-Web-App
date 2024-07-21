import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal):
    output = '<li class="cards__item">\n'
    output += f'<div class="card__title">{animal["name"]}</div>\n'
    output += '<p class="card__text">\n'
    output += f'<strong>Location:</strong> {animal["locations"][0]}<br/>\n'
    if 'type' in animal:
        output += f'<strong>Type:</strong> {animal["type"]}<br/>\n'
    output += f'<strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
    output += '</p>\n'
    output += '</li>\n'
    return output

animals_data = load_data('animals_data.json')

output = ""
for animal in animals_data:
    output += serialize_animal(animal)

with open('animals_template.html', 'r') as file:
    template = file.read()

html_content = template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals.html', 'w') as file:
    file.write(html_content)
