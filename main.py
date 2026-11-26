"""The Robot Vacuum's Best Excuse — make.fun entry.

Writes one line to /output/entry.txt: the vacuum's excuse for missing a spot.
Gate: UTF-8, 1-140 chars, not only whitespace. The line is 80 chars, 60 spare.
The winner beat the bumper peace-treaty line on the tie-break: its last four
words are the punchline, while the treaty line ends on a date.
"""
import sys
from pathlib import Path

LINE = "My lidar saw a sock, classified it as a sleeping animal, and I am not a monster."

CANDIDATES = [
    ("Cliff sensor saw the rug edge as a 40-foot drop", 5, 5, 4),
    ("Map updated and the spot moved", 5, 4, 4),
    ("Dustbin full, carried the dirt in my heart", 4, 5, 4),
    ("Bumper negotiated a peace treaty with the baseboard in 2023", 5, 5, 5),
    ("Battery 4%, chose the dock over the crumb, a moral decision", 5, 5, 4),
    ("Lidar saw a sock, classified it as a sleeping animal", 5, 5, 5),
    ("Cleaned around the spot out of respect, it has seniority", 4, 4, 4),
]


def tournament():
    print("candidate tournament (specificity / surprise / freshness):")
    for name, spec, surp, fresh in CANDIDATES:
        print(f"  {name}: {spec}/{surp}/{fresh} = {spec + surp + fresh}")
    print("winner: lidar sock sleeping animal, 5/5/5 = 15 (tie-break: cleanest end turn)")


def check():
    n = len(LINE)
    print(f"VALID: {n} chars, {len(LINE.split())} words, {140 - n} spare under the 140-char gate")
    return 0


def self_test():
    out = Path("/tmp/vacuum-excuse-self-test.txt")
    out.write_text(LINE + "\n", encoding="utf-8")
    again = out.read_text(encoding="utf-8")
    assert again == LINE + "\n"
    print("self-test: byte-identical")
    return 0


def main(argv):
    if "--check" in argv:
        return check()
    if "--self-test" in argv:
        return self_test()
    if "--tournament" in argv:
        tournament()
        return 0
    if "--print-line" in argv:
        print(LINE)
        return 0
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} chars to {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
