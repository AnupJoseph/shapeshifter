# Internal
from xml.dom import minidom
import re

# External
import numpy as np

# Project

# Project Specific Configuration


def grab_points(infile: str):
    doc = minidom.parse(infile)
    path_strings = [path.getAttribute("d") for path in doc.getElementsByTagName("path")]
    pattern = r"\bQ .*? L\b"
    matches = re.findall(pattern, path_strings[0])
    svgpath = matches[0].replace("Q ", "").replace(" L", "")
    svgpath = [[float(j) for j in i.split(",")] for i in svgpath.split()]
    return np.array(svgpath)
