# About this repository
Represent famous number sequences as colors and music

## :hammer_and_wrench: Setup/ Preparation
```bash
pipenv install --ignore-pipfile --skip-lock --python 3.7
pipenv shell
git submodule init
git submodule update --remote --merge
```
Make sure the following packages are installed and edit `timidity.cfg` to use freepats as the default source config.
```
sudo apt-get install freepats
sudo apt-get install timidity
```

If faced by `UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.`
```bash
sudo apt-get install python3.7-tk
```
