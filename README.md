# About this repository
Represent famous number sequences as colors and music

## :hammer_and_wrench: Setup/ Preparation
```bash
pipenv install --ignore-pipfile --skip-lock --python 3.7
pipenv shell
git submodule init
git submodule update --remote --merge
```
If faced by "fluidsynth file not found" on some linux environment, try the following.
```bash
sudo apt-get install fluid-soundfont-gm
```

If faced by `UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.`
```bash
sudo apt-get install python3.7-tk
```
## :rocket: Usage examples
Example: Play the sequence of Pi digits mapped to the chromatic musical scale with C4 root and length of 12
```bash
python play_numbers.py -n Pi -m Chromatic -r C -s 4 -l 12
```
Example: Play the sequence of Prime numbers mapped to the Major musical scale with A3 root and length of 14 against all integers as a backing track
```bash
python play_numbers.py -n Primes -m Major -r A -s 3 -l 14 -b
```
:information_source: Use the `--help` option to display and explain all the options
```bash
python play_numbers.py ---help
```
