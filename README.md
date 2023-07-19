# Python_Package
# Random Password Generator

This is a simple Python script that generates random passwords. The passwords will be a combination of lowercase letters, uppercase letters, and digits. The script will exclude certain names from the generated passwords based on the contents of two CSV files: `names.csv` and `places.csv`.

## How to Use

1. Clone the repository to your local machine.

2. Make sure you have Python installed on your system.

3. Create two CSV files named `names.csv` and `places.csv` in the same directory as the script.

4. Add the names of people to `names.csv` and the names of places to `places.csv`, each in a separate row. These names will be excluded from the generated passwords.

5. Run the script by uncommenting the following lines at the end of the script:

python <br/>  password = genPass()<br/>  print(password)
