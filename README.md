# wikipedia-word-frequency
 
 
Yet, the simpliest usage is as the following:

1. Download the latest wikipedia dump from [the Wikipedia dumps](https://dumps.wikimedia.org/huwiki/latest/) for a selected language (e.g. Hungarian Language in this minimal example):


`wget -np -r --accept-regex 'https:\/\/dumps\.wikimedia\.org\/huwiki\/latest\/huwiki-latest-pages-articles*' https://dumps.wikimedia.org/huwiki/latest/
`

2. Once the wikipedia dump is downloaded to the `dumps.wikimedia.org` forlder, use `gather_wordfreq.py` to obtain the list of words with their number of occurrences within the given wikipedia dump:

`./gather_wordfreq.py dumps.wikimedia.org/huwiki/latest/*.bz2 > hu_wordfreq.txt
`
