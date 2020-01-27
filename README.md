# leoturtle

A turtlegraphics class for jupyter based on [ipcanvas](https://github.com/martinRenou/ipycanvas).

## Installation

We recommend using the Python 3 version of anaconda. You can [download it here](https://www.anaconda.com/distribution/)

If you have git installed you can clone this repository

```bash
git clone https://github.com/cedricvogel/leoturtle.git
```

Otherwise just [download](https://github.com/cedricvogel/leoturtle/archive/master.zip) and unpack it.

inside the leoturtle folder run


```bash
conda env create -f enviromnt.yml
```

You can now activate the conda environment including all the dependencies with

```bash
conda activate leoturtle
```

If you want to use jupyterlab you will have to install the extension for ipycanvas.

```bash
jupyter labextension install @jupyter-widgets jupyterlab-manager ipycanvas
```

You can now use jupyterlab with 

```bash
jupyter lab
```