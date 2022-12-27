# Usage of this tool

`wwf.py` is a Python script that takes a language code as an input argument and substitutes it into two bash scripts. The first bash script downloads the latest pages and articles for the specified language from Wiktionary, and the second bash script processes the downloaded data to generate a word frequency file.

## Prerequisites

Before running `wwf.py`, make sure that you have the following installed:

- wget
- Python 3

## Running the script

To run `wwf.py`, open a terminal and navigate to the directory where the script is located. Then, run the following command:

`python `wwf.py` [language code]`

Replace `[language code]` with the language code of the Wiktionary data you want to download. For example, to download Hungarian Wiktionary data, you would use the following command:

e.g.: `python `wwf.py` hu`

This will execute the two bash scripts with the language code `hu` substituted into them, resulting in the latest pages and articles for Hungarian Wiktionary being downloaded and a word frequency file for Hungarian being generated.

## Output

After running `wwf.py`, you should see a new directory called `dumps.wikimedia.org` in the current directory, with a subdirectory for the specified language. The downloaded data will be stored in this subdirectory.

You should also see a new file called `[language code]_wordfreq.txt` in the current directory, containing the word frequency data for the specified language.

## Notes

- The script may take some time to run, depending on the size of the data being downloaded.
- The script may generate a large amount of output in the terminal, which can be safely ignored.
- The downloaded data and word frequency file may be quite large, so make sure you have enough storage space available.