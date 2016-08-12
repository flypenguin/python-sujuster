# The SUbtitle adJUSTER

Adjust subtitle start/stop timinigs with this script.


## Quickstart

Install with `pip install sujuster`. Then you can get a help with `sujust -h`


## Examples

    sujust subtitle_file.srt 1.5

... will make every subtitle in `subtitle_file.srt` appear 1.5 seconds later. Negative values are of course also supported.


## Caveat

You should actually [use PySRT](https://pypi.python.org/pypi/pysrt). I wrote this as a quick exercise, and then I thought "Maybe I'm not the only one" and googled. PySRT looks a whole lot more professional.

Still I did not want my 30 minutes work go to waste.