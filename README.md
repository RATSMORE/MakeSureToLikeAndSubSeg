# MakeSureToLikeAndSubSeg 
## What?
I'm glad you asked! This is a YouTube subscriber counter based on a 4-digit 7-segment display.
The python script periodically calls the Youtube API v3 to get the number of public subscribers a channel with a given
user handle has, and outputs the value onto the display.

## How do I use it?
To use this program, you need the dependencies listed on ```requirements.txt```, the python script ```MakeSureToLikeAndSubSeg.py```, 
and the configuration file ```cfg.txt```

The ```cfg.txt``` file simply has your key for the YouTube Data API in the first line, and the user handle (seen below a channel's username
when you open their page) in the second line.

Once the environment is set up and the configuration file is set, the program can be run using the following
```python3 MakeSureToLikeAndSubSeg.py```

