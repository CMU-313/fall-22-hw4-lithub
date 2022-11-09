# Student prediction Microservice

This repository represent a ML microservice that predicts if a student is good or not (G3 Grade > 15).
The features used by the ML model are: 
- Dalc : Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
- Walc : Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
- absences : The number of school absences (numeric: from 0 to 93). Higher number of absences tend to correlate with a lower final grade.
- activities: Extra-curricular activities (binary: yes or no).
- failures : Number of past class failures (numeric: n if 1<=n<3, else 4). Lower failures indicate higher final grade
- higher : Whether student wants to take higher education (binary: yes or no). "Yes" typically indicates a bettter candidate.
- studytime : Weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours). Higher studytime correlated with higher final grade.
- traveltime : Home to school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour).
- reason : Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference or 'other')


The model performs with an F1 score of 0.878, which is much higher than the baseline model (which had an F1 score of approximately 0.5). We changed the columns that are included in the dataframe that the model is trained on to include only the above features, which we felt were more correlated with the G3 variable and would improve the performance of the model. We used the get_dummies command to convert the categorical variables ('activies', 'higher', and and 'reason') to numerical columns, which allowed us to use a random forest classifier model to determine if a student with particular statistics is good or not. The model outputs 1 if yes and 0 if no, as shown in the "Example Usage" section of the notebook.


# HW4 Starter Code and Instructions

Please consult the [homework assignment](https://cmu-313.github.io//assignments/hw4) for additional context and instructions for this code.

## pipenv

[pipenv](https://pipenv.pypa.io/en/latest) is a packaging tool for Python that solves some common problems associated with the typical workflow using pip, virtualenv, and the good old requirements.txt.

### Installation

#### Prereqs

- The version of Python you and your team will be using (version greater than 3.8)
- pip package manager is updated to latest version
- For additional resources, check out [this link](https://pipenv-fork.readthedocs.io/en/latest/install.html#installing-pipenv)

#### Mac OS

To install pipenv from the command line, execute the following:

```terminal
sudo -H pip install -U pipenv
```

#### Windows OS

The same instructions for Mac OS **should** work for windows, but if it doesn't, follow the instructions [here](https://www.pythontutorial.net/python-basics/install-pipenv-windows).

### Usage

#### Downloading Packages

The repository contains `Pipfile` that declares which packages are necessary to run the `model_build.ipnyb`.
To install packages declared by the Pipfile, run `pipenv install` in the command line from the root directory.

You might want to use additional packages throughout the assignment.
To do so, run `pipenv install [PACKAGE_NAME]`, as you would install python packages using pip.
This should also update `Pipfile` and add the downloaded package under `[packages]`.
Note that `Pipfile.lock` will also be updated with the specific versions of the dependencies that were installed.
Any changes to `Pipfile.lock` should also be committed to your Git repository to ensure that all of your team is using the same dependency versions.

#### Virtual Environment

Working in teams can be a hassle since different team members might be using different versions of Python.
To avoid this issue, you can create a python virtual environment, so you and your team will be working with the same version of Python and PyPi packages.
Run `pipenv shell` in your command line to activate this project's virtual environment.
If you have more than one version of Python installed on your machine, you can use pipenv's `--python` option to specify which version of Python should be used to create the virtual environment.
If you want to learn more about virtual environments, read [this article](https://docs.python-guide.org/dev/virtualenvs/#using-installed-packages).
You can also specify which version of python you and your team should use under the `[requires]` section in `Pipfile`.

## Jupyter Notebook

You should run your notebook in the virtual environment from pipenv.
To do, you should run the following command from the root of your repository:

```terminal
pipenv run jupyter notebook
```

## API Endpoints

You should also use pipenv to run your Flask API server.
To do so, execute the following commands from the `app` directory in the pip venv shell.


Set an environment variable for FLASK_APP.
For Mac and Linux:
```terminal
export FLASK_APP=app.py
```

For Windows:
```terminal
set FLASK_APP=app
```

To run:
```terminal
pipenv run flask run
```

Or if you're in the pipenv shell, run:
```terminal
flask run
```

You can alter the port number that is used by the Flask server by changing the following line in `app/app.py`:

```python
app.run(host="0.0.0.0", debug=True, port=80)
```

## Testing

To run tests, execute the following command from the `app` directory:

```terminal
pytest
```

If you're not in the Pipenv shell, then execute the following command from the `app` directory:

```terminal
pipenv run pytest
```
