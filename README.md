# ![](halo_brute_sprite.gif) bruteboard

Simple bruteforce app made in Python for Windows 10. Originally conceived as a clipboard-based utility, bruteboard has since been simplified to a tiny Python app.

## Installation

### Dependancies:
- Install GNU Make [http://gnuwin32.sourceforge.net/packages/make.htm](http://gnuwin32.sourceforge.net/packages/make.htm)
- Install Python [https://www.python.org/downloads/](https://www.python.org/downloads/)
- Install Pip [https://pip.pypa.io/en/stable/](https://pip.pypa.io/en/stable/)

Using Make, run `make deps` to install dependancies with pip.

### Usage:
- Use `make run` or
- Use `py run.py` (to specify Python version, `py -2 run.py`)

#### Advanced usage:
- To change the app name (default is Firefox), edit `run.py`
- To change the wait time between each attempt (default is 0.1 sec), edit `run.py`
- To change the bruteforce generation, edit `bruteboard.py`'s `getBruteforceItems` method located at the top of the file. Once the return value of this method are looped through completely, the program will exit.

## License

See [LICENSE](LICENSE).
