
# UV and Python project management

## TL;DR: just use uv

[`uv`](https://docs.astral.sh/uv) is a very powerful and yet, starting to use it is very easy.
Unless you depend on a very specific feature of conda, just use `uv` from now on, that's my advice.

If you don't know where to start, just [install](https://docs.astral.sh/uv/getting-started/installation/) `uv` and instead of doing:

```bash
$ python my_program.py
```

do:

```bash
$ uv run my_program.py
```

## Who is this course for

I'm assuming that you already use Python because you find it useful, so this is not a Python seminar, this is a Python tooling seminar, we'll talk about tools that will make you pythoning more productive, but not about how to write better Python programs.

## Package management

Packages, libraries or modules are the true strength of any programming language, whether you do data analysis, create web services or UI applications you need them.

[`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)) has been so far the standard and [recommended](https://packaging.python.org/en/latest/guides/tool-recommendations/#installing-packages) tool to install Python packages.
In most Python package installation instructions you will see commands with the form:

```bash
$ pip install package_to_install
```

If you would run this command `pip` would download the package from PyPI and install it in your system Python.
Any package manager has to take into account package dependencies, for instance, [pandas](https://pandas.pydata.org/) requires [NumPy](https://numpy.org/), so in order to install pandas you first need to install NumPy, and that is something that the package manager would do for you.

Besides [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)), there are other package installers, like [`conda`](https://docs.conda.io/projects/conda/) or [`uv`](https://docs.astral.sh/uv/).
As we will see `conda`and `uv` have extra features not available in `pip`.

## PyPI

[PyPI](https://pypi.org/) (**Py**thon **P**ackaging **I**ndex) is the standard Python package repository, and `pip` has been, so fare, the most used tool to fetch packages from it.
PyPI, is the central repository where the Python community publishes and distributes open-source packages.
It serves as the default source for the pip installer, meaning that when a user runs *pip install numpy*, pip connects to PyPI, locates the NumPy package, downloads the appropriate archive, and installs it in the current environment.

PyPI hosts hundreds of thousands of packages covering nearly every domain of programming, from scientific computing and web development to natural language processing and bioinformatics.

Beyond being a distribution hub, PyPI plays a central role in the Python ecosystem’s reproducibility and collaboration. It provides a standardized way for developers to share code, manage versions, and integrate continuous delivery pipelines.

PyPI is a critical infrastructure that underpins nearly all modern Python development.

## conda

[`conda`](https://docs.conda.io/projects/conda/) was created to install complex packages often used in the scientific world.
It is common for these packages to include both Python and non-Python code and `conda` was built with these multi-language projects in mind. `conda`:

- Manages the installation of Python and non-Python tools (like R).
- It is quite good installing complex scientific packages like NumPy, SciPy, or TensorFlow.

`conda` has its own ecosystem, unlike `pip` or `uv`, `conda` does not work with the standard Python PyPI repository. 
`conda` tends to have specialized compilations of some popular scientific packages, but it has much less packages available that PyPI, and `conda` is not compatible with `pip`, so if you can't mix and match conda and non-conda packages.
Moreover, `uv` is much faster and it can also do the project management.

The [Anaconda Distribution](https://www.anaconda.com/) is a bundle that includes `conda` plus:

- A pre-installed collection of hundreds of scientific packages (NumPy, pandas, SciPy, matplotlib, Jupyter, etc.)
- Graphical tools (like Anaconda Navigator and Spyder IDE.)
- Commercial support options.

Anaconda:

- It’s big (5–7 GB installed) and it is slower than `uv`.
- Geared toward users who want an immediate, ready-to-use environment.

Although `conda` is free software, the anaconda distribution is [not free](https://legal.anaconda.com/policies/en/?name=terms-of-service) to use for medium and big companies.

## uv

[`uv`](https://docs.astral.sh/uv/) is a Swiss Army Knife that can replace many other tools. It can:

- Bootstrap the Python installation.
- Create and manage virtual environments.
- Run Python scripts taking care of its dependencies.
- Manage Python projects.

`uv` can replace totally or partially:
- Package installers like: `pip` or `conda`.
- Virtual environment tools like: [virtualenv](https://virtualenv.pypa.io/), [venv](https://docs.python.org/es/3.13/library/venv.html) or `conda`.
- Project management tools like: [Poetry](https://python-poetry.org/) or [PDM](https://pdm-project.org/).

While these tools remain viable options, `uv` integration and speed make it more convenient and fast.
Moreover, `uv` is multiplatform (Windows, Mac, and Linux), very fast, in most cases, does not require administrative privileges to be installed and it [free software](https://en.wikipedia.org/wiki/Free_and_open-source_software).

Install `uv` following its [installation](https://docs.astral.sh/uv/getting-started/installation/) instructions for your Operating System and remember that it has a quite comprehensive [documentation](https://docs.astral.sh/uv/).

Once you install it, run it to check that everything is OK:

```bash
$ uv self version
```

## Managing Python versions

`uv` can work with the Python software installed in your system, but it is not necessary to have any Python installed at all, if you don't have it `uv` will do it for you.
Nowadays, I usually don't have a system Python installed in my computer, I just use `uv`.

`uv` can discover the existing Python installations.
For example, to list all the Python versions that `uv`can detect in your system, as well as the ones ready to be installed, run the following command:

```bash
$ uv python list
```

To install a specific version just do:

```bash
$ uv python install 3.14
```

Now you can run *uv python list* again to check the installation location of the new Python.

If at any time you want to run any `uv` command with a specific Python version, you can.
For instance, we could run a specific REPL.

```bash
$ uv run --python 3.14 python
Python 3.14.0 (main, Oct 14 2025, 21:27:55) [Clang 20.1.4 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Hello')
```

## Running Python scripts

Let's run a very simple Python script, for that we use *uv run*.
Remember, *uv run* substitutes the standard `python`command.

```bash
$ uv run scripts/hello.py 
Hello world
```

That should have run without any problem, but now, let's try to run a script that depends on some libraries, like NumPy and matplotlib.

```bash
$ uv run scripts/mandelbrot.py 
Traceback (most recent call last):
  File "/home/jose/docencia/uv_seminar/scripts/mandelbrot.py", line 6, in <module>
    import matplotlib
ModuleNotFoundError: No module named 'matplotlib'
```

`uv` is trying to run the script for us, but it is not finding the matplotlib library.
If you are used to install your Python libraries in the system `python` using `pip` you might be tempted to run *pip install matplotlib* to fix the issue, but this is something that I wouldn't recommend at all and that wouldn't work with `uv`.
`uv` uses a virtual environment (more about that later) for each run, so installing matplotlib in the system `python` won't solve the issue.
Moreover, even if you would use your system `python` and `pip` you would still have a problem, if you would try to run this script in the future or in a different system you might not have the required libraries installed, and if you send the script to a colleague or a friend, it won't work unless he also installs the libraries, and that information is not included in the script.

How could we fix that issue? Enter [PEP 722](https://peps.python.org/pep-0722/).
Although this is something that you don't need to know for this seminar, just for your general Python general knowledge, a PEP is a [Python Enhancement Proposal](https://realpython.com/ref/glossary/pep/), a document that describes a feature implemented or proposed to be implemented in Python.
PEP 722 is already implemented, you you can use it, or as we'll see `uv` can use it.
It specifies how you should document the library requirements of a script in the same file.
If you would read PEP 722 you would realize that the right why to document that our script requires both NumPy and matplotlib is to write this comment:

```
# In order to run, this script needs the following 3rd party libraries
#
# Script Dependencies:
#    matplotlib
#    numpy
```

You might try to write this comment manually and you might try to run the script with ```python scripts/mandelbrot.py```, but that would fail, again.
Why? Because although the script now describes which are the dependencies, the `python` command will ignore the comment.
So, what's the point then? We'll, just use `uv` and everything will be fixed for you.

First, `uv` can add the dependencies to the file for us.





One very big advantage of uv is that in order to run Python software you don't need to install any Python or, if the code is well configure, even any package, uv will do it for you

Running scripts
Simple scripts with only standard library dependencies
Scripts with package dependencies
Virtualenvs
Installing a Python package involves, basically, copying the package contents to a location in which Python looks for files when trying to import modules. 
Also, in the case of packages that include non-Python code like pandas or NumPy the installer might have to copy compiled code or even might have to compile the code, a quite involved process.

Maybe you are used to installing packages by just opening a terminal and just running pip, don't do that.
Installing packages outside a virtual environment[https://docs.python.org/3/glossary.html#term-virtual-environment] is a very, very bad idea.
I repeat, if you care at all for the sanity of your system or for the reproducibility of your work, do not install packages outside a virtual environment.
What is a virtual environment
A Python virtual environment[https://docs.python.org/3/glossary.html#term-virtual-environment] is an isolated workspace that contains its own installation of Python and its own set of packages, independent from the system’s global Python. It allows you to manage project-specific dependencies without interfering with other projects or requiring administrator permissions. Each virtual environment keeps its own site-packages directory and can have different library versions, ensuring that software runs reproducibly.
Why do I need a virtualenv?
For a standard Python user, even for one not working on large projects, **virtual environments offer several practical advantages**:

1. **Avoid dependency conflicts:**
   Different projects often require different versions of the same package. A virtual environment keeps each project’s dependencies separate, so updating one package doesn’t break another project.

2. **Ensure reproducibility:**
   If you manage your environment using a list of dependencies (e.g., `requirements.txt` or `pyproject.toml`), your code will be able to run by others, or by you in the future, under the exact same conditions.

3. **Keep the system Python clean:**
   Installing packages globally can clutter or even damage the system Python (especially on Linux or macOS, where it’s used by the OS). Virtual environments prevent that risk by isolating installations. In fact, if you use uv you won't even need a system Python at all.

4. **Simplify deployment:**
   When you deploy a project, you will be able to create the same environment easily in a different machine. If you have just Python dependencies virtual environments will be everything you need, but if you have other dependencies, like non-Python command line tools you might want to familiarize yourself with container (using tools like Docker or Podman).

5. **Experiment safely:**
   You can try new packages, versions, or configurations without affecting your main setup. If something goes wrong, you just delete the environment and start fresh.

The best part is that uv manages your virtual environments for you, you can even forget about them.




Project management
Why do I need project management or single scripts with proper dependency management?

initializing and structuring Python projects

UV's lockfile approach ensures consistent environments across different systems
lock files to ensure reproducible environments

Dependency locking.

Initializing a new project

$ uv init explore-uv

The command will immediately create a new explore-uv directory with the following contents:
$ cd explore-uv
$ tree -a

Git is automatically initialized and main git-related files like .gitignore and an empty README.md are generated. .python-version file contains the Python version used for the project, while pyproject.toml serves as the main configuration file for project metadata and dependencies. A sample hello.py file is also created to help you get started quickly.

Do the option with library

Adding dependencies to the project.

Adding devel dependencies to the project

The first time you run the add command, UV creates a new virtual environment in the current working directory and installs the specified dependencies. Be aware this virtual environment will be automatically managed by uv, so just ignore it, and do not try to use pip in it.


This new environment doesn't have the dependencies listed in your pyproject.toml file, so you have to install them with the following command:
$ uv pip install -e .


Changing Python versions for the current project 

You can switch Python versions for your current UV project at any point as long as the new version satisfies the specifications in your pyproject.toml file
you can change the Python version in .python-version file to any version above, like 3.11.7. Afterwards, call uv sync.

When you run uv add commands to install dependencies, UV automatically generates and updates a uv.lock file. This lock file serves several critical purposes:
- It records the exact versions of all dependencies and their sub-dependencies that were installed.
- It ensures reproducible builds by "locking" dependency versions across different environments.
- It helps prevent "dependency hell" by maintaining consistent package versions.
- It speeds up installations since UV can use the locked versions instead of resolving dependencies again.

Lock files are essential for development to maintain reproducible builds and prevent dependency conflicts.
UV manages the lock file automatically - you don't need to manually edit it. The lock file should be committed to version control to ensure all developers use the same dependency versions.

Requirements.txt files are better suited for deployment scenarios or when sharing code with users who may not use UV
You can maintain both files by using UV's lock file for development while generating a requirements.txt for deployment. To generate a requirements.txt from a UV lock file, use the following command:
$ uv export -o requirements.txt

Updating dependencies
The add command can be used again in these and any other scenario where you need to change the constraints or versions of existing dependencies.

1. Installing the latest version of a package:
$ uv add requests

2. Installing a specific version:
$ uv add requests=2.1.2

3. Change the bounds of a package's constraints:
$ uv add 'requests<3.0.0'

Adding optional dependencies

Dependency groups



https://www.datacamp.com/tutorial/python-uv

https://realpython.com/python-uv/

https://realpython.com/python-virtual-environments-a-primer/

https://www.bitecode.dev/p/a-year-of-uv-pros-cons-and-should

https://www.saaspegasus.com/guides/uv-deep-dive/

https://realpython.com/uv-vs-pip/

https://medium.com/@digitalpower/comparing-the-best-python-project-managers-46061072bc3f

https://martynassubonis.substack.com/p/python-project-management-primer

https://martynassubonis.substack.com/p/python-project-management-primer-a55

https://realpython.com/python-pyproject-toml/

https://dagster.io/blog/python-project-best-practices

https://bury-thomas.medium.com/mastering-python-project-management-with-uv-part-4-ci-cd-docker-ed4128fdd0c1
https://snarky.ca/why-it-took-4-years-to-get-a-lock-files-specification/
