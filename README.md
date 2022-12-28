# name-generator
Name generation using simple probablistic model (first order Markov model) for next letter generation based on previous letter. Works by probablistically (based on trend in data) selecting a first letter and then subsequent letters until the next letter chosen is a blank space.

Model should be trained on a dataset that is a list of names containing only english letters (no spaces).

## How to run
**Library requirement:** NumPy

Run in terminal using command in the following format:

```
python name_generator.py < ../datasets/biotech_companies.txt
```

## Example outputs
### Biotech companies dataset
```
Geriviote
Ata
Allerin
Ironat
Geletrel
```

### Countries dataset
```
Trugu
Atoka
Caol
Ianmimey
Conora
```