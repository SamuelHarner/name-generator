# name-generator
Name generation using simple probablistic model for next letter generation based on previous letter. Works by probablistically selecting a first letter and then subsequent letters until the next letter chosen is a blank space.

Model should be trained on a dataset of names containing only english letters.

## How to run
Run in terminal using command in the following format:

```
python name_generator.py < ./datasets/biotech_companies.txt
```