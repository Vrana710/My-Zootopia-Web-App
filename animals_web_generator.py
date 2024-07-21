import json

def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

output = ""
for animal in animals_data:
    output += '<li class="cards__item">\n'
    output += f"Name: {animal['name']}<br/>\n"
    output += f"Diet: {animal['characteristics']['diet']}<br/>\n"
    output += f"Location: {animal['locations'][0]}<br/>\n"
    if 'type' in animal:
        output += f"Type: {animal['type']}<br/>\n"
    output += '</li>\n'

with open('animals_template.html', 'r') as file:
    template = file.read()

html_content = template.replace('__REPLACE_ANIMALS_INFO__', output)

with open('animals.html', 'w') as file:
    file.write(html_content)
