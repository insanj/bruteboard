# ![](halo_brute_sprite.gif) bruteboard

Simple bruteforce app made in Python for Windows 10. Originally conceived as a clipboard-based utility, bruteboard has since been simplified to a tiny Python app.

## Installation

### Dependancies:
- Install Make [http://gnuwin32.sourceforge.net/packages/make.htm](http://gnuwin32.sourceforge.net/packages/make.htm)
- Install Conda [https://conda.io/miniconda.html](https://conda.io/miniconda.html), which should handle python, pip, and other dependencies

Using Make, run `make setup` to install dependancies with pip.

### Usage:
- Use `make run` to run without setup or cleanup steps, or `make all` to fresh install
- Manually use `py run.py`

#### Advanced usage:
- To change the app name (default is Firefox), provide an app name in the `brute.force()` method location in `run.py`
- To change the cooldown between each keypress (default is 0.2 sec), provide a cooldown in the `brute.force()` method located in `run.py`
- To change what keys are sent (default is every number for 0-2000), change the `make()` method located in `brutemaker.py`

Note: you can always interrupt bruteboard by pressing CONTROL+C in the command prompt window.

### Todo:
- Improve bruterunner to work as a dependancy injection system, taking in the helper, maker, client, and tower as params
- Allow for complex configuration within the `run.py` file itself, taking in numerous options:
   - Customize app name
   - Customize cooldown
   - Customize bruteforce item generation (what keypresses get sent) by supplying a method or closure
   - Enlist the brutetower to find a specific app by name
   - Choose an app from a list of running processes using brutetower
- Create basic UI using Python-based libraries
- Create cross-platform Makefile and `bruteclient`/`brutetower` to support Mac OS X, Linux

## License

See [LICENSE](LICENSE).
