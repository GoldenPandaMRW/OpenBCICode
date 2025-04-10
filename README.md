# OpenBCICode
Includes scripts to read EEG signals and plot it visually.

“bcitest.py” was run with the following flags: “python bcitest.py --serial-port COM6 –-board-id 2”

# Installing
1. Fork
0. Make venv (if you don't have one): `python -m venv .venv`
0. Activate venv:
    - Windows: `.venv\bin\activate.bat`
    - Linux/Max: `.venv/bin/activate`
0. `pip install -r requirements.txt`

# Running
Make sure your venv is active (see above).

Currently assumes `--serial-port COM6 –-board-id 2`