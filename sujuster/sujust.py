from argparse import ArgumentParser
from datetime import datetime, timedelta
from sys import stdout


config = None


def parse_args():
    """
    Parses the argument list.

    :return: None
    """
    global config
    parser = ArgumentParser()
    parser.add_argument("srt_file",
                        help="The subtitle file to adjust")
    parser.add_argument("offset",
                        type=float,
                        help="The offset of all subtitles. A positive number "
                             "means that the subtitle will be later, a "
                             "negative number that it will appear earlier. The "
                             "number is a floating point number (1.3) "
                             "representing seconds.")
    parser.add_argument("-o", "--outfile",
                        help="specify the output file. Default: output "
                             "to stdout",
                        default=None)
    config = parser.parse_args()


def get_subtitles(infile):
    """
    Generator which returns subtitles from a given already opened input file.

    Yields a list which is basically all lines between empty lines in the
    subtitles file.

    :param infile: The opened file-handle (or file-like object)
    :return: Yields [line1, line2, ...] of each subtitle block
    """
    line = "start"
    try:
        while line:
            line = infile.readline()
            if not line.strip(): continue
            st = [line.strip(), infile.readline().strip()]
            line = infile.readline()
            while line.strip():
                st.append(line.strip())
                line = infile.readline()
            yield st
    except UnicodeDecodeError as e:
        print("UNICODE ERROR on or after line: ", line)
        raise e


def adjust_subtitle(st, td):
    """
    Gets a list representing a subtitle. It expects the 'classic' .srt format
    with hours in the time stamps as the 2nd element of the list. Will then
    adjust the start and stop time by the given time delta object.

    :param st: The list containing the subtitle
    :param td: The timedelta object which is used to adjust
    :return: The processed list, although it is modified in-place.
    """
    # we only know microseconds, though the timestamp has milliseconds ...
    markers = [x + "000" for x in st[1].split(" --> ")]
    marker_objs = [datetime.strptime(x, "%H:%M:%S,%f") + td for x in markers]
    st[1] = "{} --> {}".format(
        marker_objs[0].strftime("%H:%M:%S,%f")[:-3],
        marker_objs[1].strftime("%H:%M:%S,%f")[:-3]
    )
    return st


def adjust_subtitles(outfile):
    """
    Opens config.srt_file as subtitle file, then iterates thorugh all subtitles
    and adjusts the start and stop times using the adjust_subtitle function.
    :param outfile: The output file handle (or any file-like object)
    :return: None
    """
    td = timedelta(seconds=config.offset)
    # see http://stackoverflow.com/a/2459793/902327
    with open(config.srt_file, "r", encoding='utf-8-sig') as infile:
        for num, st in enumerate(get_subtitles(infile)):
            adjust_subtitle(st, td)
            st_text = "\n".join(st) + "\n\n"
            outfile.write(st_text)


def start():
    """
    The starting point of everything.
    :return: None
    """
    parse_args()
    if config.outfile:
        with open(config.outfile, "w", encoding="utf-8") as outfile:
            adjust_subtitles(outfile)
    else:
        adjust_subtitles(stdout)
