# My Zootopia Web Application

Welcome to the My Zootopia Web Application project! This repository contains a Python script that reads animal data from a JSON file and generates an HTML page displaying this data in a formatted way.

## Project Structure

- `animals_data.json`: Contains data on various types of foxes.
- `animals_template.html`: An HTML template where animal data will be inserted.
- `animals_web_generator.py`: A Python script that processes the JSON data and updates the HTML template.

## Getting Started

Follow these steps to set up and run the project on your local machine:

### 1. Clone the Repository

Clone the repository from GitHub:

```bash
git clone https://github.com/Vrana710/My-Zootopia-Web-App.git
cd My-Zootopia-Web-App
```

### 2. Python Environment

Ensure you have Python installed. No additional packages are required beyond the standard library.

### 3. Running the Script

To generate the HTML file, run the `animals_web_generator.py` script:

```bash
python animals_web_generator.py
```

This will read data from `animals_data.json`, process it, and generate `animals.html` based on the `animals_template.html`.

### 4. Viewing the Output

Open `animals.html` in a web browser to view the generated HTML page. You can open it directly or serve it using a local web server if needed.

## Project Details

### Git Preparation

1. **Initialize Git Repository:**

   ```bash
   git init
   ```

2. **Add Files and Commit:**

   ```bash
   git add .
   git commit -m "First commit"
   ```

3. **Connect to GitHub Repository:**

   ```bash
   git remote add origin https://github.com/Vrana710/My-Zootopia-Web-App.git
   git branch -M main
   git push -u origin main
   ```

### Step-by-Step Breakdown

#### Step 1 - Print Data From File

- **Objective:** Read and print data from `animals_data.json`.
- **File:** `animals_web_generator.py`
- **Function:** `print_animal_data()`

#### Step 2 - Writing HTML

- **Objective:** Generate and write animal data to `animals.html` using `animals_template.html`.
- **Function:** `generate_animal_html()`, `update_html_template()`

#### Step 3 - Making It Nice

- **Objective:** Improve HTML formatting by using proper HTML tags and classes.
- **Updated Function:** `generate_animal_html()`

#### Step 4 - Like A Pro

- **Objective:** Finalize the HTML design with enhanced formatting.
- **Updated Function:** `generate_animal_html()`

### Commit History

- **First Commit:** Initialized repository and added files.
- **Access Data from JSON File:** Read and printed data from `animals_data.json`.
- **Bring Animal Data into HTML:** Integrated data into HTML template.
- **Generate Card Item for Every Animal:** Enhanced HTML output with animal card design.
- **Improve Card Item HTML:** Finalized HTML design for animal cards.

## Additional Information

- Includes improved HTML & CSS formatting and Python filtering based on `skin_type`.
- Feel free to explore the code and modify it according to your needs.
- If you have any questions or issues, please open an issue on the GitHub repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, please contact [ranavarsha710@gmail.com](mailto:ranavarsha710@gmail.com).
