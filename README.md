# OpenBCICode
Includes scripts to read EEG signals and plot it visually.

“bcitest.py” was run with the following flags: “python bcitest.py --serial-port COM6 –-board-id 2”

# Installing
1. Fork the repo
0. Make venv (if you don't have one):
    - Windows: `python -m venv .venv`
    - Linux/Mac: `python3 -m venv .venv`
0. Activate venv:
    - Windows:
        - If running on powershell: `.venv\Scripts\activate.ps1`
        - Otherwise: `.venv\Scripts\activate.bat`
    - Linux/Mac: `.venv/bin/activate`
0. `pip install -r requirements.txt`

# Running
**Make sure your venv is active (see above).**

Wherever you run the above activate script, that's where
you need to run the script, so that means *__DON'T USE THE
RUN BUTTON ON PYCHARM__*

Currently assumes `--serial-port COM6 –-board-id 2`