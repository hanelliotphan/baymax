# BayMax Simulation
Simulation of Baymax from Disney Big Hero 6 using Python, Pyttsx3 voice engine 
and Google speech recognition

## Development Status
`IN PROGRESS`

## Installations
First, we need to install `portaudio` from Homebrew. This package is required
for Python library `pyaudio`

```bash
$ brew install portaudio
```

Then, we install packages in `requirements.txt`
```bash
$ pip3 install -r requirements.txt
```

**NOTE**: If errors related to `#include "portaudio.h"` occurred when running `pip install pyaudio`, like this:
```bash
#include "portaudio.h"

         ^
1 error generated.
error: command '/usr/bin/clang' failed with exit status 1
``` 
Then we need to run the command separately in the Terminal below:
```bash
$ CFLAGS="-I/opt/homebrew/include -L/opt/homebrew/lib" python3 -m pip install pyaudio
```

We need to install FLAC in order to recognize speech with the command below:
```bash
$ sudo port install flac
```
If you have not installed Macports, please download Macports from [this link](https://www.macports.org/install.php)

Then, we run
```bash
$ python3 src/main.py
```

**NOTE**: If you face the `KeyError: 'VoiceAge'` problem, please go to the 
`nsss.py` in your folder (the full error message should display the full path),
and remove the `attr['VoiceAge']` line code

## Dedications
I dedicate this hard work commitment to my mom, whom has sacrificed everything for my better future. I hope I have 
made you proud!
