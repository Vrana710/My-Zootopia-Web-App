import json

def load_data(file_path):
    """
    Load a JSON file from the specified file path.

    Args:
        file_path (str): The path to the JSON file.

    Returns:
        dict: The data loaded from the JSON file.
    """
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)

def generate_animal_html(data):
    """
    Generate an HTML string for the animal data provided.

    Args:
        data (list): A list of dictionaries, each representing an animal.

    Returns:
        str: The HTML string representing the animals.
    """
    output = ''
    for animal in data:
        output += '<li class="cards__item">\n'
        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'
        output += '  <p class="card__text">\n'
        if "locations" in animal and animal["locations"]:
            output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'
        if "type" in animal:
            output += f'    <strong>Type:</strong> {animal["type"]}<br/>\n'
        if "characteristics" in animal:
            characteristics = animal["characteristics"]
            if "diet" in characteristics:
                output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
            if "group" in characteristics:
                output += f'    <strong>Group:</strong> {characteristics["group"]}<br/>\n'
            if "lifespan" in characteristics:
                output += f'    <strong>Lifespan:</strong> {characteristics["lifespan"]}<br/>\n'
            if "training" in characteristics:
                output += f'    <strong>Training:</strong> {characteristics["training"]}<br/>\n'
            if "temperament" in characteristics:
                output += f'    <strong>Temperament:</strong> {characteristics["temperament"]}<br/>\n'
            if "distinctive_feature" in characteristics:
                output += f'    <strong>Distinctive feature:</strong> {characteristics["distinctive_feature"]}<br/>\n'
            if "average_litter_size" in characteristics:
                output += f'    <strong>Average litter size:</strong> {characteristics["average_litter_size"]}<br/>\n'
            if "common_name" in characteristics:
                output += f'    <strong>Common name:</strong> {characteristics["common_name"]}<br/>\n'
            if "slogan" in characteristics:
                output += f'    <strong>Slogan:</strong> {characteristics["slogan"]}<br/>\n'
        output += '  </p>\n'
        output += '</li>\n'
    return output

def update_html_template(template_path, output_path, animals_html):
    """
    Update the HTML template with the provided animal data.

    Args:
        template_path (str): The path to the HTML template file.
        output_path (str): The path to save the updated HTML file.
        animals_html (str): The HTML string representing the animals.
    """
    with open(template_path, "r", encoding="utf-8") as file:
        html_content = file.read()
    
    html_content = html_content.replace('__REPLACE_ANIMALS_INFO__', animals_html)
    
    with open(output_path, "w", encoding="utf-8") as file:
        file.write(html_content)

    print("Website has been generated successfully!")

def main():
    """
    Main function to load data, generate animal HTML, and update the HTML template.
    """
    animals_data = load_data('animals_data.json')
    animals_html = generate_animal_html(animals_data)
    update_html_template('animals_template.html', 'animals.html', animals_html)

if __name__ == "__main__":
    main()
