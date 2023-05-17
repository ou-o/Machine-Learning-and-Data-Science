# Project 1
## Install 
### Ubuntu

- Setup the virtual environment
```bash
$ virtualenv -p python3 pyenv
$ ln -s pyenv/bin/activate envpy
$ . envpy
(pyenv) $ pip install -r requirements.txt
```

- Register the virtual environment in Jupyter, we'll call it "pymlds"
```bash
(pyenv) $ ipython kernel install --name pymlds --user
```

- Start Jupyter
```bash
(pyenv) $ jupyter notebook
```
