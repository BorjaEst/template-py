<p align="center">
  <a href="" rel="noopener">
    <img width=601px height=203px src="project_logo.png" alt="Project logo">
  </a>
</p>

<h2 align="center">template-py</h3>

<!-- <div align="center">

  [![Build Status]()]()
  [![Documentation Status]()]()
  [![pipeline status]()]()
  [![coverage status]()]()
  [![License]()]()
  [![Status]()]() 

</div> -->

---

<p align="center"> > WRITE HERE YOUR pROJECT DESCRIPTION <
    <br> 
</p>

# 📝 Table of Contents
- [About](#about)
- [Documentation]()
- [Build using docker](#build)
- [Run using udocker](#deployment)
- [Testing](#testing)
- [Authors](#authors)
- [TODO]()

# About <a name = "about"></a>
> Write here your Project about lines

This project aims to provide all the tools to start a python project.
It includes utilities like:

- [**sqa**](https://indigo-dc.github.io/sqa-baseline) Tools and tutorial to implement Software Quality Assurance based on EOSC Research Projects. 
- [**TDD**](https://en.wikipedia.org/wiki/Test-driven_development) Tools and tutorial to develop using Test Driven Development.
- [**vscode**](https://code.visualstudio.com/docs/languages/python) basic configuration to run, containerize and debug python code with vscode.
- [**docs**](https://www.sphinx-doc.org/en/master) extended documentation folder template for sphinx with rst-cheatsheet and tutorials.
- [**GPLv3**](https://www.gnu.org/licenses/gpl-3.0.en.html) this software is free licensed under GNU umbrella, we encourage you to reuse the license for your project. 
- [**docker**](https://www.docker.com/) necessary tools to containerize your application with docker.
- [**setup**](https://setuptools.readthedocs.io/en/latest) tools configuration to build your python package.
- [**git**](https://git-scm.com) with the necessary .gitignore file to keep clean your python python project repository.
- [**tox**](https://tox.readthedocs.io/en/latest) automation testing configuration template file to easily test your code and get rich pep8 and coverage reports.


## Prerequisites
> Write here your Project prerequisites

To use this template you need at lease the following knowledge:
- Python programming. To create basic Python projects.
- Git basics. Although if you are not an expert, I recommend you to use [ungit](https://github.com/FredrikNoren/ungit) .


# Documentation <a name = "doc"></a>
> Point here where to find the project documentation or how to build it

**This project contains useful tutorial on its documentation that you can use to build your project.** <br>
To build them you can use [sphinx](https://www.sphinx-doc.org/en/master) instructions.
```sh
$ pip install sphinx sphinx_rtd_theme
...
Installing collected packages: sphinx, sphinx-rtd-theme
Successfully installed sphinx-3.4.3 sphinx-rtd-theme-0.5.1
$ cd docs
$ make html
Running Sphinx ...
...
build succeeded.

The HTML pages are in _build/html.
```

Or use the tox automation environment already defined as template to build and test it:
```sh
$ tox -e docs
...
build succeeded.

The HTML pages are in docs/_build/html.
________________________________________________________________________________________________________ summary _________________________________________________________________________________________________________
  docs: commands succeeded
  congratulations :)
```

Now you can read the the documentation using your browser using the [index.html](./docs/_build/html/index.html) at in `docs/_build/html`.


# Built using docker <a name = "build"></a>
> Write here how to run your container with docker 

Normally you would perform this step using on shell:

```sh
$ docker build -t <dockerhub_user>/<dockerhub_repo>:<version> --build-arg arg=value .
Sending build context to Docker daemon  235.9MB
Step 1/24 : ARG version=...
...
Successfully built a42fdf57588a
Successfully <dockerhub_user>/<dockerhub_repo>:<version>
```


# Run using udocker <a name = "deployment"></a>
> Write here how to run using udocker.

To deploy the the application using __udocker__ at the __Runtime machine__ you need:
 - Input path with data to be mounter on `/app/data` inside the container.
 - Output path for results to be mounted on `/app/output` inside the container.
 - Configuration files and other on `/app/<config_file>` inside the container.

Once the requirement are completed, pull the image from the image registry.
```sh
$ udocker pull <registry>/<image>:<version>
...
Downloading layer: sha256:a3ed95caeb02ffe68cdd9fd84406680ae93d633cb16422d00e8a7c22955b46d4
...
```

Once the repository is added and the image downloaded, create the local container: 
```sh
$ udocker create --name=<container-name> <registry>/<image>:<version>
fa42a912-b0d4-3bfb-987f-1c243863802d
```

Finally, run the container. Note normally the described _data_, _output_ and _<config_file>_ have to be provided. 
Also it is needed to specify the user (in this template _application_) that should run inside the container:
```sh
$ udocker run \
  --user=application \
  --volume=${PWD}/<config_file>:/app/<config_file> \
  --volume=${PWD}/data:/app/data \
  --volume=${PWD}/output:/app/output \
  <container-name> {container-arguments}
...
executing program 
...
```

# Testing <a name = "testing"></a>
> Write here how to test your project

Testing is based on [sqa-baseline](https://indigo-dc.github.io/sqa-baseline/) criteria. On top, [tox](https://tox.readthedocs.io/en/latest/) automation is used to simplify the testing process.

You can run unit and functional tests with coverage using:
```sh
$ tox
```

# Authors <a name = "authors"></a>
> Write here the authors and contributors

- [@B.Esteban](https://git.scc.kit.edu/zr5094)

