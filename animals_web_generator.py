import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

def generate_animal_html(data):
    """ Generate HTML string for animals with final design """
    output = ''
    for animal in data:
        output += '<li class="cards__item">\n'
        output += f'  <div class="card__title">{animal.get("name", "N/A")}</div>\n'
        output += '  <p class="card__text">\n'
        output += f'    <strong>Location:</strong> {animal.get("locations", [])[0] if animal.get("locations") else "N/A"}<br/>\n'
        output += f'    <strong>Type:</strong> {animal.get("type", "N/A")}<br/>\n'
        output += f'    <strong>Diet:</strong> {animal.get("characteristics", {}).get("diet", "N/A")}<br/>\n'
        output += f'    <strong>Group:</strong> {animal.get("characteristics", {}).get("group","N/A")}<br/>\n'
        output += f'    <strong>Lifespan:</strong> {animal.get("characteristics", {}).get("lifespan","N/A")}<br/>\n'
        output += f'    <strong>Training:</strong> {animal.get("characteristics", {}).get("training","N/A")}<br/>\n'
        output += f'    <strong>Temperament:</strong> {animal.get("characteristics", {}).get("temperament","N/A")}<br/>\n'
        output += f'    <strong>Distinctive_feature:</strong> {animal.get("characteristics", {}).get("distinctive_feature","N/A")}<br/>\n'
        output += f'    <strong>Average_litter_size:</strong> {animal.get("characteristics", {}).get("average_litter_size","N/A")}<br/>\n'
        output += f'    <strong>Common_name:</strong> {animal.get("characteristics", {}).get("common_name","N/A")}<br/>\n'
        output += f'    <strong>Slogan:</strong> {animal.get("characteristics", {}).get("slogan","N/A")}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'
    return output


def update_html_template(template_path, output_path, animals_html):
    """ Update HTML template with animal data """
    with open(template_path, "r") as file:
        html_content = file.read()
    
    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', animals_html)
    
    with open(output_path, "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    animals_data = load_data('animals_data.json')
    animals_html = generate_animal_html(animals_data)
    update_html_template('animals_template.html', 'animals.html', animals_html)
