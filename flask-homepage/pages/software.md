title: Software

Here you can find a few software packages that I've developed. Since I'm a big
supporter of the [open source initiative](http://opensource.org/) all the
packages are available under permissive open source licenses. If you want to have
a full overview of my coding activities check out my repositories:

- [bitbucket](https://bitbucket.org/lukaszmentel)
- [github](https://github.com/lmmentel)

## [Batch Calculator][bc]

A GUI app based on [wxPython](https://wxpython.org/) for calculating the correct amount of 
reactants (batch) for a particular composition given by the molar ratio of its components. It is
designed to assist chemical synthesis when it requires batch preparation. Besides offering a 
quick and easy way of calculating the desired masses (or moles) it can also store information
about chemicals, components and syntheses and generate lab reports in pdf format. You can find
more information in the [github repository][bc].

<div class="row">
    <img class="img-responsive center-block" width=700px src="{{ url_for('static', filename='img/BC_014.png') }}">
</div>

## [mendeleev]

[mendeleev] is my attempt to
develop a database of atomic properties with an easy to use python API with
convenient methods to formulate complex querries, tranfer data to
[numpy] and [pandas](http://pandas.org) objects and visualize
various properties is color mapped periodic tables (using [bokeh](http://bokeh.pydata.org/en/latest/)).

All the atomic properties are listed in the [data page](http://mendeleev.readthedocs.io/en/
latest/data.html) of the documentation with their respective references. A particularly 
interesting feature is that the package includes 10 different electronegativity
scales that are available directly or can be generated using appropriate functions from
other stored properties.

For more information visit:

* [PYPI page](https://pypi.python.org/pypi/mendeleev)
* [project repository](http://bitbucket.org/lukaszmentel/mendeleev)
* [documentaion][mendeleev]

<div class="row">
    <img class="img-responsive center-block" width=700px src="{{ url_for('static', filename='img/mendeleev.png') }}">
</div>

Similar (python) efforts can be found on the web:

* [periodic](https://github.com/luisnaranjo733/periodic)
* [periodictable](http://www.reflectometry.org/danse/elements.html)
* [elements](http://www.lfd.uci.edu/~gohlke/) by Christoph Gohlke 

## [panther]

A Package for ANharmonic THERmochemistry - a python implementation for calculating
anharmonic corrections to thermochemical functions in the independent mode approximation for 
molecules and solids. The package was developed in collaboration with the
[group of Prof J. Sauer](https://www.chemie.hu-berlin.de/de/forschung/quantenchemie)
in Berlin during my stay there and evolved from the work of G. Piccini. It is interfaced with
the [Atomic Simulation Environment (ASE)][ase] and should
work with most of the programs supported by it.

<div class="row">
    <img class="img-responsive center-block" width=700px src="{{ url_for('static', filename='img/mode1-animation.gif') }}">
</div>

For more information visit:

- [panther repository](https://bitbucket.org/lukaszmentel/panther)
- [panther documentation][panther]

## [zefram](https://bitbucket.org/lukaszmentel/zefram)

Is a convenience package for accessing various properties of zeolite frameworks combining
the data available from:

* [IZA database of zeolite structures](http://www.iza-structure.org/databases/)
* [ZEOMICS](http://helios.princeton.edu/zeomics/)

in a python package allowing easy access to the stored data.
You can find more details on the [project page](https://bitbucket.org/lukaszmentel/zefram).

## [chemtools]

[chemtools] package evolved from a set of modules and scripts intended to help with
automation of various tasks common in electronic structure calculations. 

It provides a quite powerful [BasisSet class](http://chemtools.readthedocs.io/en/latest/_reference/chemtools.basisset.html) that allows one-particle basis sets to be handled efficiently. Some
of the features include: 

* conversion between various basis set formats
    - input: [GamessUS][gamessus], [Molpro][molpro] and [Gaussian][gaussian]
    - output: [GamessUS][gamessus], [Molpro][molpro], [Gaussian][gaussian], [NWChem][nwchem], [CFour/AcesII][cfour], [Dalton][dalton]
* optimization of primitive exponents using a wrapper around
  [scipy.optimize](http://docs.scipy.org/doc/scipy/reference/optimize.html) module
* plotting basis set completeness profiles

Another unique feature are the tools for writing, reading and parsing the files associated with
[GamessUS][gamessus] calculations contained in the [calculators](http://chemtools.readthedocs.io/en/latest/_reference/chemtools.calculators.html) subpackage, it supports:

- writing the input files,
- parsing the standard `log` files,
- parsing various parts of the `PUNCH` or `.dat` file
- reading the (direct access binary) dictionary file`.F10` records into [numpy] arrays
- reading the (sequential unformatted binary) files with two-electron integrals (`.F08`, `.F09`), elements
  of the reduced two-particle density matrix (`.F15`, `.F16`), CI coefficients (`.F12`) into [numpy] arrays

More information:

- [chemtools repository][chemtools]
- [chemtools documentation](http://chemtools.readthedocs.io/en/latest/index.html)


## [ase-espresso][ase-espresso]

[ase-espresso][ase-espresso] provides a Python interface compatible with
[Atomic Simulation Environment (ASE)][ase] for manging calculations with [Quantum Espresso] - 
the widely used open source package for plane wave Density Functional Theory (DFT) and molecular
dynamics calculations.

The current version started from a fork from [vossjo][vossjo-ae] and since then considerably diverged
offering various improvements over the original version, the most important ones include:

- python 3.x compatible
- installable through [pip] and [setuptools]
- documentation available through [sphinx] with a lot of docstrings updated
- the `site.cfg` was replaced by a new `SiteConfig` class that dynamically gathers information about the execution environment 
- the old `espresso` class is now split into two: `Espresso` preserving the standard functionality and
  `iEspresso` responsible for dynamic/interactive jobs with a custom version of `pw.x`
- the `Espresso` class were restructured according to [ase] guidelines regarding calculator objects to
  support full compatibility with [ase]
- most of the system call are now handled by [pexpect] and [subprocess] instead of the old `os.system`,
  `os.popen()`, `os.popen2()`, `os.popen3()`
- tests were added
- code style and readability were improved

## [colorcif]

A small utility python script based on [Atomistic Simulation Environment][ase]
to generate high-quality images from [cif](https://en.wikipedia.org/wiki/Crystallographic_Information_File)
files with symmetry unique atoms colored with different colors:

<div style="text-align: center">
<img style="width:200px" src="https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_RdYlGn_T.png">
<img style="width:200px" src="https://bytebucket.org/lukaszmentel/colorcif/raw/tip/example/gfx/ton_gist_rainbow_O.png">
</div>

More details are given on the [project page][colorcif].

[ase-espresso]: https://github.com/lmmentel/ase-espresso
[ase]: https://wiki.fysik.dtu.dk/ase/index.html
[bc]: https://github.com/lmmentel/batchcalculator
[cfour]: http://www.cfour.de/
[chemtools]: https://bitbucket.org/lukaszmentel/chemtools
[colorcif]: https://bitbucket.org/lukaszmentel/colorcif
[dalton]: http://www.daltonprogram.org/
[gamessus]: http://www.msg.ameslab.gov/GAMESS/
[gaussian]: http://www.gaussian.com/
[mendeleev]: http://mendeleev.readthedocs.org
[molpro]: http://www.molpro.net/
[numpy]: http://numpy.org
[nwchem]: http://www.nwchem-sw.org/index.php/Main_Page
[panther]: http://panther.readthedocs.io
[pexpect]: https://pexpect.readthedocs.io/en/stable
[pip]: https://pip.pypa.io/en/stable/
[sphinx]: http://www.sphinx-doc.org/en/stable/
[vossjo-ae]: https://github.com/vossjo/ase-espresso
[Quantum Espresso]: http://www.quantum-espresso.org/
[wiki]: https://github.com/vossjo/ase-espresso/wiki