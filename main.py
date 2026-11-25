"""Copy entry.txt to the output directory for the make.fun entry.

The entry is one line of awkward small talk between two robots
riding an elevator together, at most 200 characters.
The robot logic shows through: notifications, firmware, and the
forced politeness of a machine that has no idea what to say next.
The awkwardness is the joke — the pause, the doors closing,
and a question neither robot really wants answered.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
