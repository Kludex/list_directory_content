# List Directory Content

This is a simplified version of the list directory content command (**ls**).

## Installation
The environment management system used was
[conda](https://docs.conda.io/en/latest/). For those who prefer
[pipenv](https://github.com/pypa/pipenv) or other managers, there's a
[requirement file](requirements.txt) available.

We just need to clone the repository and create the environment.
```
git clone https://github.com/Kludex/list_directory_content
cd list_directory_content/

conda env create -f environment.yml
conda activate ls
```

To execute the command as `ls.py` instead of `./ls.py`, run:
```
export PATH=$PATH:$(pwd)
```

## Usage

The command to run this project is:

```
ls.py [OPTION] [FILE]
```

## Examples

There a few examples to help you to understand how to use it.

Using just the folder path.
```
ls.py /path/to/folder/
some_file
another_file
```

Using a prefix file.
```
ls.py /path/to/folder/som
some_file
```

Also, you can use the `-l` option.
```
ls.py -l /path/to/folder
rwxr--r--  2017-12-15 17:44 some_file
rwxr-xr-x  2017-12-15 17:44 another_file
```

## Collaborators
- Code: [Marcelo Trylesinski](https://github.com/Kludex)
- Challenge: [Sébastien Diemer](https://www.linkedin.com/in/sdiemer/?locale=en_US)