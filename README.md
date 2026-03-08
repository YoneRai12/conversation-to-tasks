# Conversation to Tasks Converter

This repository provides a simple command‑line tool for extracting a list of tasks from free‑form conversations or meeting notes.

## Overview

When brainstorming or planning projects, conversations often contain actionable items hidden among ideas and discussion.  Turning those notes into a structured todo list can be tedious.  This tool reads plain text and extracts lines that look like tasks based on simple heuristics:

- Lines that start with common bullet characters (e.g. `-`, `*`, `•`).
- Numbered list entries (e.g. `1.`, `2)` etc.).
- Lines containing keywords such as `TODO:` or `task:`.

You can pass input via a file or directly through standard input.  The output is a newline‑separated list of extracted tasks.  Because it uses only regular expressions and no external libraries, it runs anywhere a standard Python interpreter is available.

## Installation

You don’t need to install anything; the script can be run directly with Python 3.  To make it easily available in your environment, you can copy `conversation_to_tasks.py` somewhere on your `PATH` or invoke it with an absolute path.

## Usage

```
python conversation_to_tasks.py                # Read from standard input
python conversation_to_tasks.py -f input.txt   # Read from the specified file
```

The script writes the extracted tasks to standard output.  If no tasks are found, the output will be empty.  For example:

```
$ cat example.txt
We discussed the following:

- Finish the ORA workbench prototype.
- Check GPU VRAM requirements.

Next steps:
1. Schedule a meeting with the design team.
2. Prepare the README and documentation.

$ python conversation_to_tasks.py -f example.txt
Finish the ORA workbench prototype.
Check GPU VRAM requirements.
Schedule a meeting with the design team.
Prepare the README and documentation.
```

## Testing

This repository includes a minimal test suite using the `unittest` module.  To run the tests:

```
python -m unittest discover -s tests
```

The tests cover the core extraction logic, verifying that bullet points, numbered lists and keyword lines are correctly recognized.

## License

This project is released under the MIT License.  See the `LICENSE` file for details.