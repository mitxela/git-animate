# git-animate

Reads through a git repo and turns each commit into a series of vim keystrokes. The result is a pseudo-timelapse which almost looks like it's being typed out by a real person. Results vary depending on how frequent the commits were. It's also still only doing linewise diffs, so even a single byte change means the whole line is re-typed.

Only works on a single file. If the repo has multiple files being changed in it, you will probably need to alter this script to filter out the one you want. It is a good idea to rebase any merge commits so that the history reads as if it was written by a single author.

`pip install -r requirements.txt`

`process.py` reads the git history and outputs the patches as a list of tuples representing changes. E.g. `python process.py > allpatches.txt` 

`playback.py` reads the patches file and turns it into keystrokes. Run the script and then focus on a new terminal window. Hold esc to abort.

These scripts were used to produce [this video](https://www.youtube.com/watch?v=i08S5qolgvc).
