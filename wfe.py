import sys
import subprocess

# Get the language code from the command line arguments
language_code = sys.argv[1]

# Substitute the language code into the first bash script
bash_script_1 = "wget -np -r --accept-regex 'https://dumps.wikimedia.org/{}wiki/latest/{}wiki-latest-pages-articles*' https://dumps.wikimedia.org/{}wiki/latest/".format(language_code, language_code, language_code)

# Execute the first bash script
subprocess.run(bash_script_1, shell=True)

# Substitute the language code into the second bash script
bash_script_2 = "./gather_wordfreq.py dumps.wikimedia.org/{}wiki/latest/*.bz2 > {}_wordfreq.txt".format(language_code, language_code)

# Execute the second bash script
subprocess.run(bash_script_2, shell=True) 
