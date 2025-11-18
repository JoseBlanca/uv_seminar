
# UV and Python project management

## TL;DR: just use uv

[`uv`](https://docs.astral.sh/uv) is very powerful and yet, starting to use is very easy.
Unless you depend on a very specific feature of conda, like using non-Python conda supported software, just use `uv` from now on, that's my advice.
If you normally use `pip install`, start using `uv` and don't look back.

If you don't know where to start, just [install](https://docs.astral.sh/uv/getting-started/installation/) `uv` and instead of doing:

```bash
$ python my_program.py
```

do:

```bash
$ uv run my_program.py
```

## Who is this seminar for

I'm assuming that you already use Python, so this is not a Python seminar, this is a Python tooling seminar, we'll talk about tools that will make you pythoning more productive, but not about how to write better Python programs.

You will need a computer in which to [install `uv`](https://docs.astral.sh/uv/getting-started/installation/) and that's about it.

Finally, I'm also assuming that you don't know `uv`, if you already do, this introduction is not for you.

What you don't need is previous knowledge about [virtual environments](https://docs.python.org/3/glossary.html#term-virtual-environment), project management or Python packages.

## Objectives

After this seminar you will be able to:

- Install and update Python with uv.
- Understand what virtual environments and [lock files](https://peps.python.org/pep-0751/) are.
- Run scripts with isolated dependencies.
- Create and manage reproducible projects.

## PyPI

Packages, libraries or modules are the true strength of any programming language, whether you do data analysis, create web services or UI applications you need them.

[PyPI](https://pypi.org/) (**Py**thon **P**ackaging **I**ndex) is the standard Python package repository.
PyPI, is the central repository where the Python community publishes and distributes open-source packages.
It serves as the default source for the pip installer, meaning that when a user runs *pip install numpy*, pip connects to PyPI, locates the NumPy package, downloads the appropriate archive, and installs it in the current environment.

PyPI hosts hundreds of thousands of packages covering nearly every domain of programming, from scientific computing and web development to natural language processing and bioinformatics.

Beyond being a distribution hub, PyPI plays a central role in the Python ecosystem’s reproducibility and collaboration. It provides a standardized way for developers to share code, manage versions, and integrate continuous delivery pipelines.

PyPI is a critical infrastructure that underpins nearly all modern Python development.

## Package management

Before `uv` the main package management tool was [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)).
In fact `pip`has been almost the standard and [recommended](https://packaging.python.org/en/latest/guides/tool-recommendations/#installing-packages) tool to install Python packages.
In most Python package installation instructions you will see commands with the form:

```bash
$ pip install package_to_install
```

If you would run this command `pip` would download the package from PyPI and install it in your system Python.
Any package installer has to take into account package dependencies, for instance, [pandas](https://pandas.pydata.org/) requires [NumPy](https://numpy.org/), so in order to install pandas you first need to install NumPy, and that is something that the package installer would do for you.

Besides [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)), there are other package installers, like [`conda`](https://docs.conda.io/projects/conda/) or [`uv`](https://docs.astral.sh/uv/).
As we will see `conda`and `uv` have extra features not available in `pip`.

## conda

[`conda`](https://docs.conda.io/projects/conda/) was created to install complex packages often used in the scientific world.
It is common for these packages to include both Python and non-Python code and `conda` was built with these multi-language projects in mind. `conda`:

- Manages the installation of Python and non-Python tools (like R).
- It is quite good installing complex scientific packages like NumPy, SciPy, or TensorFlow.

`conda` has its own ecosystem, unlike `pip` or `uv`, `conda` does not work with the standard Python PyPI repository. 
`conda` tends to have specialized compilations of some popular scientific packages, but it has much less packages available that PyPI, and `conda` is not compatible with `pip`, so if you can't mix and match conda and non-conda packages in the same project.
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
- Run Python scripts taking care of its dependencies.
- Manage Python projects.
- Reproduce working environments.
- Create and manage virtual environments.

`uv` can replace totally or partially:
- Package installers like: [`pip`](https://en.wikipedia.org/wiki/Pip_(package_manager)) or [`conda`](https://docs.conda.io/projects/conda/).
- Virtual environment tools like: [virtualenv](https://virtualenv.pypa.io/), [venv](https://docs.python.org/es/3.13/library/venv.html) or `conda`.
- Project management tools like: [Poetry](https://python-poetry.org/) or [PDM](https://pdm-project.org/).

While these tools remain viable options, `uv` integration and speed make it more convenient and fast.
Moreover, `uv` is multiplatform (Windows, Mac, and Linux), very fast, in most cases, does not require administrative privileges to be installed and it is [free software](https://en.wikipedia.org/wiki/Free_and_open-source_software).

| Tool    | Strengths                   | Weaknesses               |
| ------- | --------------------------- | ------------------------ |
| `pip`   | Ubiquitous, standard        | No project management    |
| `conda` | Handles non-Python dependencies     | Slow, separate ecosystem |
| `uv`    | Fast, unified, reproducible | It doesn't handle non-Python dependencies |


### uv installation

Install `uv` following its [installation](https://docs.astral.sh/uv/getting-started/installation/) instructions for your Operating System and remember that it has a quite comprehensive [documentation](https://docs.astral.sh/uv/).

Once you install it, run it to check that everything is OK:

```bash
$ uv self version
```

To update `uv` to the latest version run:

```
$ uv self update
```

## Managing Python versions

There are many ways of installing Python.
You can go to [python.org](https://www.python.org/) download the latest Python version and install it,
you can get it using the software package manager or software store of your Operating System, or you can use other tools, and now you get a new way, the one that I consider the simplest and most convenient and the one that I now recommend: `uv`.

`uv` can work with the `python` versions installed in your system, but it is not necessary to have any `python` installed at all, if you don't have it `uv` will do it for you.
Nowadays, I usually don't have a system Python installed in my computer, I just use `uv`.

`uv` can discover the existing Python installations.
For example, to list all the Python versions that `uv`can detect in your system, as well as the ones ready to be installed, run the following command:

```bash
$ uv python list
```

Be aware that this list will depend on the `uv` version, so be sure that you have the latest `uv` if you want to have an updated `python` version list.

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

`uv`can install Python:

- In the same way across any Operating System.
- Without administrative privileges.
- Independently of the Python system.
- Managing different Python versions without conflicts between them.

All that being said, you don't need to install Python using `uv` in order to use any of the other `uv` capabilities, `uv` will work with almost any Python available, independently of how you have installed it.

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
This will fail even if you have previously installed matplotlib in other project or at the system level.

`uv` isolates the environment in which runs every project, or in this case, every script.
`uv` uses a virtual environment (more about that later) for each run, so installing matplotlib in the system `python` won't solve the issue.

This is a good practice that you should follow and that `uv` enforces.
Even if you would use your system `python` and `pip` you would still have a problem, if you would try to run this script in the future or in a different system you might not have the required libraries installed, and if you send the script to a colleague or a friend, it won't work unless he also installs the libraries, and that information is not included in the script.

`uv` allows us to specify the dependencies when we run a script.

```bash
$ uv run --with "numpy, matplotlib" scripts/mandelbrot.py 
Installed 11 packages in 38ms
Saved image to mandelbrot.png
```

That has solved our problem, but it is not an ideal solution because we need to remember to add the dependencies, by using the `--with` parameter, to the command every time we try to run the script.
How could we fix that issue? Enter [PEP 722](https://peps.python.org/pep-0722/).

Although this is something that you don't need to know for this seminar, just for your general Python general knowledge, a PEP is a [Python Enhancement Proposal](https://realpython.com/ref/glossary/pep/), a document that describes a feature implemented or proposed to be implemented in Python.
PEP 722 is already implemented, so you can use it, or as we'll see `uv` can use it.
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

You might try to write this comment manually (not a trivial thing to do), just use `uv` and everything will be fixed for you.
`uv` can add the dependencies to the file for us.

```bash
$ uv add --script scripts/mandelbrot.py 'matplotlib' 'numpy'
Updated `scripts/mandelbrot.py`
```

*`uv` add* is the way to add dependencies to a script or project.
Now `uv` has added the dependencies comment for us to the file and, if we run the script using `uv`, it will get and use the required libraries for us.


```bash
$ uv run scripts/mandelbrot.py
Installed 11 packages in 20ms
Saved image to mandelbrot.png
```

The first time that you run the script it might take a while because it might have to download the libraries, but don't worry, the second time it'll be much faster because `uv`[caches](https://en.wikipedia.org/wiki/Cache_(computing)) the libraries.

## Virtual environments

![Not using virtual environments, this is fine](is_fine.jpg)

### Incompatible library versions

[Virtual environments](https://docs.python.org/3/glossary.html#term-virtual-environment) allow you to create isolated environments that might use different versions of libraries or, even, of `python` itself. 
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

So, we might think that installing the old version at the system level would solve our problem, but that is not a great idea.
One problem is that projects that depend of modern versions of the library would not work.

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
Are we in an insolvable catch-22 situation? If we only had the system `python` and system wide library installs we would, but, fortunately we can use virtual environments to isolate projects and library installations, so we can have different versions of the same library installed for different projects.

You might be thinking that the example that I have just shown is contrived and that that would not happen usually, but if you do, you better think twice.
Libraries are removing old code and, especially, old APIs all the time. For instance, NumPy and pandas have done it recently. So if you created a project that depends on Numpy or pandas a year or a couple of years ago, that code might not run anymore with the current versions of the library.

If you install packages by just opening a terminal and running pip, you work might be not reproducible. For once, you are not being explicit of the libraries upon which your current project depends, and moreover, library versions for different projects might be incompatible.

Installing packages outside a virtual environment is a very, very bad idea.
I repeat, if you care at all for the sanity of your system or for the reproducibility of your work, do not install packages outside a virtual environment.

### What is a virtual environment

A Python [virtual environment](https://docs.python.org/3/glossary.html#term-virtual-environment) is an isolated workspace that contains its own installation of Python and its own set of packages, independent from the system’s global Python. It allows you to manage project-specific dependencies without interfering with other projects or requiring administrator permissions. Each virtual environment keeps its own site-packages directory and can have different library versions, ensuring that software runs reproducibly.

For a standard Python user, even for one not working on large projects, virtual environments offer several **practical advantages**:

1. **Avoid dependency conflicts:**
   Different projects often require different versions of the same package. A virtual environment keeps each project’s dependencies separate, so updating one package doesn’t break another project.

2. **Keep the system Python clean:**
   Installing packages globally can clutter or even damage the system `python` (especially on Linux or macOS, where it’s used by the OS). Virtual environments prevent that risk by isolating installations. In fact, if you use `uv` you won't even need a system `python` at all.

3. **Experiment safely:**
   You can try new packages, versions, or configurations without affecting your main setup. If something goes wrong, you just delete the environment and start fresh.

Installing a Python package involves, basically, copying the package contents to a location in which `python` looks for files when trying to import modules. 
This location might be a general, system-wide, one or a different place for every project.
A virtual environment is just a folder with several subfolders in it that will hold a symlink to a `python` executable along with any library that you install in that environment, and usually you have one such environment for every project.
This environments keep each project isolated from every other project and from the system-wide Python installation.

You don't need to know where your packages are installed, but if you are curious, you can ask the `python` interpreter to show you these locations.

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


## Projects

Virtual environments are great, they allow us to isolate dependencies, but it would be even better avoid managing them, to be able to automatically install in a reproducible way the environments in which we are working.
When you install your packages manually you are not being explicit about which packages are installed in the environment and which versions are you using.
So, the most reproducible approach is to list the requirements of every project in a file and let a tool, like `uv` manage the environment for you following your explicit declaration of the library requirements.
This automatic management: 

1. **Ensures reproducibility:**
   If you manage your environment using a list of dependencies (e.g., `requirements.txt` or `pyproject.toml`), your code will be able to run by others, or by you in the future, under the exact same conditions.

2. **Simplifies deployment:**
   When you deploy a project, you will be able to create the same environment easily in a different machine. If you have just Python dependencies virtual environments will be everything you need, but if you have other dependencies, like non-Python command line tools you might want to familiarize yourself with container technologies (using tools like [docker](https://www.docker.com/) or [podman](https://podman.io/)).

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
The first time you run the add command, `uv` creates a new virtual environment in the current working directory and installs the specified dependencies. Be aware this virtual environment will be automatically managed by uv, so just ignore it, and do not try to use pip in it.
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

### Adding the project library as a dependency

In many cases you'll need to install the library that you are developing to the virtual environment of the project.
This is mostly needed when your own code should be importable as a package, e.g. for testing or using a CLI entry point.
You can do that.

```bash
$ uv pip install -e .
```

### Dependency tree

You can see the library dependency tree of your project with:

```{bash}
$ uv pip tree
matplotlib v3.10.7
├── contourpy v1.3.3
│   └── numpy v2.3.4
├── cycler v0.12.1
├── fonttools v4.60.1
├── kiwisolver v1.4.9
├── numpy v2.3.4
├── packaging v25.0
├── pillow v12.0.0
├── pyparsing v3.2.5
└── python-dateutil v2.9.0.post0
    └── six v1.17.0
```

You can also `ask uv pip tree` to show you which are the rules that has followed to decide to install these package versions and to show you which ones are outdated.

```{bash}
$ uv pip tree --show-version-specifiers --outdated
matplotlib v3.10.7
├── contourpy v1.3.3 [required: >=1.0.1]
│   └── numpy v2.3.4 [required: >=1.25]
├── cycler v0.12.1 [required: >=0.10]
├── fonttools v4.60.1 [required: >=4.22.0]
├── kiwisolver v1.4.9 [required: >=1.3.1]
├── numpy v2.3.4 [required: >=1.23]
├── packaging v25.0 [required: >=20.0]
├── pillow v12.0.0 [required: >=8]
├── pyparsing v3.2.5 [required: >=3]
└── python-dateutil v2.9.0.post0 [required: >=2.7]
    └── six v1.17.0 [required: >=1.5]
```

### Requirements.txt

If you need to create a requirement.txt file `uv` can do it for you, for instance because somebody that you work with is not using `uv`, you can generate it with:

```bash
$ uv export -o requirements.txt
```

## Other features

We have just scratched the surface of what `uv` is able to do or of what you can configure in it.
Remember that `uv` has an extensive [documentation](https://docs.astral.sh/uv/) that is updated all the time.

## Exercises

### Install and update uv

Install uv and check its version.

<details>
<summary>💡 Click to show solution</summary>

```{bash}
$ uv -V
```

</details>

Update uv to the latest version.

<details>
<summary>💡 Click to show solution</summary>

```{bash}
$ uv self update
info: Checking for updates...
success: You're on the latest version of uv (v0.9.7)
```

</details>

### Use different Python versions

Run the primers.py script using a standard Python version (like 3.14.0) and the corresponding [free-threaded](https://docs.python.org/3/howto/free-threading-python.html) one (like 3.14.0t).
(`uv` documentation regarding running scripts with different [Python versions](https://docs.astral.sh/uv/guides/scripts/#using-different-python-versions).)

<details>
<summary>💡 Click to show solution</summary>

```{bash}
$ uv run --python 3.14.0 scripts/primes.py 
1 threads → 664579 primes in 18.58s
4 threads → 664579 primes in 18.33s
$ uv run --python 3.14.0t scripts/primes.py 
1 threads → 664579 primes in 21.45s
4 threads → 664579 primes in 9.04s
```

</details>

### Run a script with dependencies

Try to run the rich_print.py script.
It will fail.
([Running scripts](https://docs.astral.sh/uv/guides/scripts/) section in `uv`'s documentation).

<details>
<summary>💡 Click to show solution</summary>
```{bash}
$ uv run scripts/rich_print.py 
ModuleNotFoundError: No module named 'rich'
```
</details>

Now running adding to the command the required dependency using the `--with` argument.

<details>
<summary>💡 Click to show solution</summary>
```{bash}
$ uv run --with rich scripts/rich_print.py 
```

</details>

Add the `rich` requirement to the [script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/#inline-script-metadata) using `uv add` and check the way in which this changes the script.

<details>
<summary>💡 Click to show solution</summary>
```{bash}
$ uv add --script scripts/rich_print.py 'rich'
Updated `scripts/rich_print.py`
```

</details>

Now you can run the script without the `--with` argument. You could even send the script to a colleague that will be able to running without caring for its dependencies, by just using `uv`.

<details>
<summary>💡 Click to show solution</summary>

```{bash}
$ uv run scripts/rich_print.py 
```
</details>

### Create and manage a project

Create a project named mandelbrot and copy in it the `mandelbrot.py` script.
Check the [projects](https://docs.astral.sh/uv/guides/projects/) section in the `uv` documentation.

<details>
<summary>💡 Click to show solution</summary>

```{bash}
$ uv init mandelbrot
Initialized project `mandelbrot` at `~/edu/uv_seminar/mandelbrot`
```
</details>

Take a look at the contents of the `.python-version`, and `pyproject.toml` files.

Now add the `matplotlib` and `numpy` dependencies to the project.

<details>
<summary>💡 Click to show solution</summary>

```{bash}
$ cd mandelbrot
~/edu/mandelbrot$ uv add matplotlib numpy
Initialized project `mandelbrot` at `~/edu/uv_seminar/mandelbrot`
```
</details>

Checkout the lines added to the `pyproject.toml` file, the newly created `uv.lock` file and the virtual environment directory `.venv`, and then run the mandelbrot script.

Now to check that `uv` is capable of regenerating the virtual environment directory at any time delete the `.venv` directory, run the mandelbrot script again and take a look at the regenerated `.venv` directory.

<details>
<summary>💡 Click to show solution</summary>

```{bash}
$ cd mandelbrot
~/edu/mandelbrot$ rm -r .venv
~/edu/mandelbrot$ ls .venv
~/edu/mandelbrot$ uv run mandelbrot.py
~/edu/mandelbrot$ ls .venv
```
</details>

Upgrade all project library dependencies to the latest versions using `uv sync --upgrade`.

<details>
<summary>💡 Click to show solution</summary>

```{bash}
~/edu/mandelbrot$ uv sync --upgrade
```
</details>

Now install the project as editable to be able to run tests and import any library that you would create.
To do it run:

```{bash}
~/edu/mandelbrot$ uv add --dev --editable .
```

Now open a python terminal and check that you can import mandelbrot.

```{bash}
~/edu/mandelbrot$ uv run python
>>> import mandelbrot
```

### Install a tool using uvx

With `uv` can directly use Python [tools](https://docs.astral.sh/uv/concepts/tools/) like [ruff](https://docs.astral.sh/ruff/) or [ty](https://docs.astral.sh/ty/).

Try to run ruff on the `mandelbrot.py` file.

```{bash}
$ uvx ruff check mandelbrot.py
All checks passed!
```

## Additional documentation

The official [`uv` documentation](https://docs.astral.sh/uv/).

The [Real Python](https://realpython.com/) [`uv` tutorial](https://realpython.com/python-uv/).

[`uv` introduction](https://www.datacamp.com/tutorial/python-uv) at datacamp.

If you want to learn more about virtual environments and, specially, if you want to manage them manually (something seldom required if you use uv) take a look at the comprehensive Real Python [virtual environment primer](https://realpython.com/python-virtual-environments-a-primer/).

Another [introduction](https://www.saaspegasus.com/guides/uv-deep-dive/) to `uv`.

More information about the [pyproject.toml](https://realpython.com/python-pyproject-toml/) file.

## Stay up to date

A great way to knowing about the latests Python developments and trends is to listen to the excellent [PythonBytes](https://pythonbytes.fm/) podcast.
