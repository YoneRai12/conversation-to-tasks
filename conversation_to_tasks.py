#!/usr/bin/env python3
"""
conversation_to_tasks.py
========================

Extract tasks from free‑form conversation text.  Tasks are detected based on simple
heuristics: lines beginning with bullet markers (`-`, `*`, `•`), numbered
list entries (e.g. `1.`, `2)`), or lines containing the keywords `TODO:` or
`task:` (case insensitive).  The script outputs each detected task on its own line.

Usage
-----

    python conversation_to_tasks.py            # Read from standard input
    python conversation_to_tasks.py -f path/to/file.txt

The tool prints the extracted tasks to standard output.  If no tasks are
found, nothing is printed.

Limitations
-----------

This extractor uses simple regular expressions and does not understand
context.  It may occasionally include lines that are not truly tasks or miss
tasks expressed in very informal language.  For complex workflows you may
want to integrate with a full natural language processing pipeline.
"""

import argparse
import re
from typing import Iterable, List


def extract_tasks(lines: Iterable[str]) -> List[str]:
    """Extract task lines from an iterable of text lines.

    A line is considered a task if it matches one of the following patterns:

    * Begins with optional whitespace followed by a bullet character (`-`, `*`, `•`).
    * Begins with optional whitespace followed by a number and a period or right
      parenthesis (e.g. ``"1."`` or ``"2)"``).
    * Contains the keywords ``"TODO:"`` or ``"task:"`` (case insensitive).

    Leading bullet markers and numbering are stripped from the extracted
    tasks, and surrounding whitespace is removed.

    Parameters
    ----------
    lines : Iterable[str]
        The lines of text to scan.

    Returns
    -------
    List[str]
        A list of normalized task descriptions.
    """
    task_patterns = [
        re.compile(r"^\s*[-*•]\s+(.*)$"),
        re.compile(r"^\s*\d+[\.)]\s+(.*)$"),
        re.compile(r"^.*\b(TODO:|task:)\s*(.*)$", re.IGNORECASE),
    ]

    tasks: List[str] = []
    for line in lines:
        stripped = line.rstrip("\n\r")
        for pattern in task_patterns:
            match = pattern.match(stripped)
            if match:
                # The relevant text is in the last capturing group.
                task_text = match.group(match.lastindex).strip()
                if task_text:
                    tasks.append(task_text)
                break  # Stop checking patterns once a match is found
    return tasks


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract tasks from conversation text")
    parser.add_argument(
        "-f",
        "--file",
        type=str,
        help="Path to input file (if omitted, reads from standard input)",
    )
    args = parser.parse_args()

    if args.file:
        try:
            with open(args.file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except FileNotFoundError:
            parser.error(f"Input file not found: {args.file}")
    else:
        lines = []
        try:
            for line in iter(input, ""):
                lines.append(line)
        except EOFError:
            pass

    tasks = extract_tasks(lines)
    for task in tasks:
        print(task)


if __name__ == "__main__":
    main()