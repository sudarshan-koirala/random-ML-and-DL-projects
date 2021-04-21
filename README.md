# random machine learning and deep learning projects
Projects related to random topics in Machine Learning and Deep Learning

## Creating python environment and installing packages
Assuming you have python and pip installed

1. Install virtual environment -> `pip3 install virtualenv`
2. Create the virtual env -> `python3 -m virtualenv mlearning`
3. Activate the virutal env -> `source mlearning/bin/activate`
4. Install all the packages -> `pip3 install -r requirements.txt`
5. Run jupyterlab -> `jupyter lab`

### Creating custom conda environment 

1. Create new environment: `conda create -n mlearning python=3.8`
2. Activate the environment: `conda activate mlearning`
3. Install all libraries through pip: `pip install -r requirements.txt`
4. Create new ipython kernel: `ipython kernel install --user --name mlearning`

### Uninstall & Update the package if necessary
- Check which package needs update -> `pip-review` [pip-review GitHub link](https://github.com/jgonggrijp/pip-review)
- If uninstall needed -> `pip/pip3 uninstall <packagename>`
- If update is needed -> `pip/pip3 install <packagename> -U`
