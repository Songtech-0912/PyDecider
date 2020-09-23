# PyDecider

![Image](markdown-images/Demo.png)

A simple Python app that gives a random yes or no answer, powered by `Eel`.

## Overview

PyDecider is very easy to use. Just launch it, and it will give you an answer of yes or no. I created it as a side project while learning the `Eel` library. And it's also free and open-source, so anyone can look through the source code and learn from it.

## Getting Started

To get PyDecider running on your machine, follow these easy steps:

### Prerequisites

* You must have `git` and `python3` installed

    * **Windows:** You can download `git` [here](https://git-scm.com/download/win)

    * **Mac:** You can download `git` [here](https://git-scm.com/download/mac)

    * **Linux:** `git` and `python3` are preinstalled on many distros. You can run the commmands `which git` and `which python` to check if they are installed. If you don't have it, use your package manager to get it.

* Install `pip` 

    * Download the `pip` installer from [here](https://bootstrap.pypa.io/get-pip.py)

    * Double-click on the `pip` installer or launch it with `python get-pip.py`

### Resolving dependencies

* Install `eel` like this:

```
pip install eel
```

### Run

* Get the source code with this command:

```
git clone https://github.com/Songtech-0912/PyDecider 
```

* To run PyInstaller, just open the `build` folder, and double-click on the `main.py` file, or enter this into your terminal:

```
python3 main.py
```

### Compiling executables

To compile executables, you must have `pyinstaller` installed. If you don't have it, you can get `pyinstaller` from `pip`:

```
pip install pyinstaller
```

Then, open a terminal in your PyDecider folder. Paste in this:

```
python -m eel main.py web-gui --onefile --noconsole --name PyDecider --exclude matplotlib --exclude scipy --exclude pandas --exclude numpy --exclude IPython --exclude tcl --exclude tk
```

By default, pyinstaller doesn't use UPX compression, which can reduce the file size of the executable. Assuming you have UPX installed, you can enable UPX compression with this flag:

```
--upx-dir <the-folder-where-you-installed UPX>
```

On Linux, this folder is usually `/usr/bin` but I can't say the same for Windows or Mac.

## Download

You can find pre-compiled executables of PyDecider on the releases page. Unfortunately, only Linux executables are available at the moment, but the compiling process should work the same on Mac or Windows.

## Problems

For now, the "try again" button doesn't work. This should be fixed in the next release.

In addition, the UI isn't fully responsive yet. Again, this will probably be fixed in the next release.

## Contributing

PyDecider's source code is filled with comments and should be easily understandable. To extend it or create your version, just create a pull request, fork the repo, make your changes, and I'll add your changes to the master branch.

## License

PyDecider is licensed under GNU GPLv3+. See LICENSE.md for further details.

---

Copyright (C) 2020  Yuxuan Song

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>

---
