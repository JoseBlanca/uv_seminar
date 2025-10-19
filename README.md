
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

`uv` allows us to specify the dependencies when we run a script.

```bash
$ uv run --with "numpy, matplotlib" scripts/mandelbrot.py 
Installed 11 packages in 38ms
Saved image to mandelbrot.png
```

That has solved our problem, but it is not an ideal solution because we need to remember to add the dependencies to the command every time we try to run the script.
How could we fix that issue? Enter [PEP 722](https://peps.python.org/pep-0722/).

Although this is something that you don't need to know for this seminar, just for your general Python general knowledge, a PEP is a [Python Enhancement Proposal](https://realpython.com/ref/glossary/pep/), a document that describes a feature implemented or proposed to be implemented in Python.
PEP 722 is already implemented, you you can use it, or as we'll see `uv` can use it.
It specifies how you should document the library requirements of a script in the same file.

If you would read PEP 722 you would realize that the right why to document that our script requires both NumPy and matplotlib is to write a comment similar to:

```
# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "matplotlib",
#     "numpy",
# ]
# ///
```

You might try to write this comment manually (not a trivial thing to do) and you might try to run the script with ```python scripts/mandelbrot.py```, but that would fail, again.
Why? Because although the script now describes which are the dependencies, the `python` command will ignore the comment.
So, what's the point then? We'll, just use `uv` and everything will be fixed for you.

First, `uv` can add the dependencies to the file for us.

```bash
$ uv add --script scripts/mandelbrot.py 'matplotlib' 'numpy'
Updated `scripts/mandelbrot.py`
```

Now uv has added the dependencies comment for us to the file and moreover, if we run the script using uv, it will get and use the required libraries for us.
*`uv` add* is the way to add dependencies to a script or project.

```bash
$ uv run scripts/mandelbrot.py
Installed 11 packages in 20ms
Saved image to mandelbrot.png
```

The first time that you run the script it might take a while because it might have to download the libraries, but don't worry, the second time it'll be much faster because `uv`[caches](https://en.wikipedia.org/wiki/Cache_(computing)) the libraries.

## Virtual environments

Installing a Python package involves, basically, copying the package contents to a location in which Python looks for files when trying to import modules. 
Also, in the case of packages that include non-Python code like pandas or NumPy the installer might have to copy compiled code or even might have to compile the code, a quite involved process.
In any case, should be copied to some location in which the Python interpreter will be able to find them when they are required.

You don't need to do this, and you don't need to know which are these location, but if you are curious, you can ask the Python interpreter to show you these locations.

```bash
$ uv run python
Python 3.14.0 (main, Oct 14 2025, 21:27:55) [Clang 20.1.4 ] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> print(sys.path)
['', '/home/jose/.local/share/uv/python/cpython-3.14.0-linux-x86_64-gnu/lib/python314.zip', '/home/jose/.local/share/uv/python/cpython-3.14.0-linux-x86_64-gnu/lib/python3.14', '/home/jose/.local/share/uv/python/cpython-3.14.0-linux-x86_64-gnu/lib/python3.14/lib-dynload', '/home/jose/.local/share/uv/python/cpython-3.14.0-linux-x86_64-gnu/lib/python3.14/site-packages']
```

In my case these locations are all managed by `uv` because I have run *uv run python* and not just the system Python, but the result will vary with your Python installation.

In any case, if you don't use `uv` be very aware that, if you don't use virtual environments, pip will install the Python packages in system wide directories that will be used by all your projects and that implies some problems.

### Incompatible library versions

Python libraries often add incompatible changes between versions, for instance, they might first deprecate and then remove some features.

Let's try to run the `legacy_emoji.py` script:

```bash
$ uv run --with emoji scripts/legacy_emoji.py 
Installed 1 package in 15ms
Traceback (most recent call last):
  File "/home/jose/docencia/uv_seminar/scripts/legacy_emoji.py", line 4, in <module>
    print(emoji.emojize("Python is :thumbs_up:", use_aliases=True))
          ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: emojize() got an unexpected keyword argument 'use_aliases'
```

We could run this code with an old version of the library:

```bash
$ uv run --with "emoji<1.0" scripts/legacy_emoji.py 
      Built emoji==0.6.0
Installed 1 package in 0.33ms
Python is 👍
```

So, we might think that installing the old version at the system level would solve our problem, but that, obviously, is not a great idea.
One problem is that projects that depend of modern version would not work.

```bash
$ uv run --with "emoji<1.0" scripts/modern_emoji.py 
Traceback (most recent call last):
  File "/home/jose/docencia/uv_seminar/scripts/modern_emoji.py", line 4, in <module>
    print(emoji.emojize("Python is :thumbs_up:", language="alias"))
          ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: emojize() got an unexpected keyword argument 'language'
```

We could run the modern code with a modern version of the library:

```bash
$ uv run --with "emoji>2.0" scripts/modern_emoji.py 
Python is 👍
```

So, if we install an old version of the library, the modern code won't work and if we install a modern version, the old code won't work.
Are we in an insolvable catch-22 situation? If we only had the system Python and system wide library installs we would, but, fortunately we can use virtual environments to isolate projects and library installations, so we can have different versions of the same library installed for different projects.

You might be thinking that the example that I have just shown is contrived and that that would not happen usually, but if you do, you better think twice.
Libraries are removing old code and, especially, old APIs all the time. For instance, NumPy and pandas hav done it recently. So if you created a project that depends on Numpy or pandas a year or a couple of years ago, that code might not run anymore with the current versions of the library.

If you install packages by just opening a terminal and running pip, you work might be not reproducible. For once, you are not being explicit of the libraries upon which your current project depends, and moreover, library versions for different projects might be incompatible.

 Installing packages outside a virtual environment[https://docs.python.org/3/glossary.html#term-virtual-environment] is a very, very bad idea.
I repeat, if you care at all for the sanity of your system or for the reproducibility of your work, do not install packages outside a virtual environment.

### What is a virtual environment

A Python virtual environment[https://docs.python.org/3/glossary.html#term-virtual-environment] is an isolated workspace that contains its own installation of Python and its own set of packages, independent from the system’s global Python. It allows you to manage project-specific dependencies without interfering with other projects or requiring administrator permissions. Each virtual environment keeps its own site-packages directory and can have different library versions, ensuring that software runs reproducibly.

For a standard Python user, even for one not working on large projects, virtual environments offer several **practical advantages**:

1. **Avoid dependency conflicts:**
   Different projects often require different versions of the same package. A virtual environment keeps each project’s dependencies separate, so updating one package doesn’t break another project.

2. **Keep the system Python clean:**
   Installing packages globally can clutter or even damage the system Python (especially on Linux or macOS, where it’s used by the OS). Virtual environments prevent that risk by isolating installations. In fact, if you use uv you won't even need a system Python at all.

3. **Experiment safely:**
   You can try new packages, versions, or configurations without affecting your main setup. If something goes wrong, you just delete the environment and start fresh.


## Projects

Virtual environments are great, but it would be even better avoid managing them because when you install your packages manually you are not being explicit about which packages are installed in the environment and which versions are you using.
So, the most reproducible approach is to list the requirements of every project in a file and let a tool, like `uv` manage the environment for you following your explicit declaration of the library requirements.
This automatic management: 

1. **Ensures reproducibility:**
   If you manage your environment using a list of dependencies (e.g., `requirements.txt` or `pyproject.toml`), your code will be able to run by others, or by you in the future, under the exact same conditions.

2. **Simplifies deployment:**
   When you deploy a project, you will be able to create the same environment easily in a different machine. If you have just Python dependencies virtual environments will be everything you need, but if you have other dependencies, like non-Python command line tools you might want to familiarize yourself with container (using tools like Docker or Podman).

And the best part is that uv manages your virtual environments for you, you can even forget about them.

## Project management

A project is just a directory with some files that indicate some essential information about it, like, for instance, the library requirements.
Let's create a project with `uv`:

```bash
$ uv init legacy_libraries
Initialized project `legacy-libraries` at `/home/jose/docencia/uv_seminar/legacy_libraries`
$ ls legacy_libraries/
main.py  pyproject.toml  README.md
```

`uv` has created a new directory *legacy_libraries* with some files in it:

- *main.py* and README.md are just some stubs.
- *.python_version* just states the default Python version to use in your project.
- *pyproject.toml* will hold, among other configurations, the list of library dependencies.

Copy the *legacy_emoji.py* file to the project directory and try to run it.

```bash
$ cp scripts/legacy_emoji.py legacy_libraries/
$ cd legacy_libraries/
legacy_libraries$ uv run legacy_emoji.py 
Using CPython 3.14.0
Creating virtual environment at: .venv
Traceback (most recent call last):
  File "/home/jose/docencia/uv_seminar/legacy_libraries/legacy_emoji.py", line 1, in <module>
    import emoji
ModuleNotFoundError: No module named 'emoji'
```

It fails because we haven't added the emoji library to the project. Let's fix that problem.

```bash
$ uv add "emoji<1.0"
Resolved 2 packages in 86ms
Prepared 1 package in 233ms
Installed 1 package in 11ms
 + emoji==2.15.0
```

`uv` has added the *emoji* dependency to the *pyproject.toml* file.

```toml
dependencies = [
    "emoji<1.0",
]
```

`uv` has also created a virtual environment and has installed the library in it.

```bash
$ ls .venv/
bin  CACHEDIR.TAG  lib  lib64  pyvenv.cfg
```

This will be the virtual environment that `uv` will use to run the code in that project.
The first time you run the add command, UV creates a new virtual environment in the current working directory and installs the specified dependencies. Be aware this virtual environment will be automatically managed by uv, so just ignore it, and do not try to use pip in it.
`uv` and `pip` should not be used at the same time in the same environment, and moreover, `uv` might decide to remove or update the virtual environment directory at any time.

Finally, `uv` has created a new important file: *uv.lock*.
This file includes the exact version or the libraries that are installed in the environment and the source of the code installed. So, this file is critical for reproducibility and you have to included it in your `git` repository. (If you don't know or you don't use a source [version control](https://en.wikipedia.org/wiki/Version_control) system, you need to study that.)

Try to run the code again.

```bash
$ uv run legacy_emoji.py 
Python is 👍
```

Now, not only the code works, but you can be sure that it will run in the future or in any other system.

As an exercise create another project to run the modern version of the emoji code: "modern_emoji.py".

### Adding the own project library

In many cases you'll need to install the library that you are developing to the virtual environment of the project. You can do that.

```bash
$ uv pip install -e .
```

### Requirements.txt

If you need to create a requirement.txt file `uv` can do it for you, for instance because somebody that you work with is not using `uv`, you can do it with:

```bash
$ uv export -o requirements.txt
```


## Other features

We have just scratched the surface of what `uv` is able to do or of what you can configure in it.
Remember that `uv` has an extensive [documentation](https://docs.astral.sh/uv/) that is updated all the time.

## Additional documentation


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
