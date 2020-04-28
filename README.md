QuickDiff

A Qt wrapper around 'gvim -d' allowing the user to quickly drag files into the UI and launch a diff.

Features three convenience buttons:

* 'Swap Files' simply swaps the file order in the diff

* 'Toggle On Top' allows the user to toggle the window's 'Stay on top' behavior when needed.  The default state is 'on'.

* 'Diff' launches gvim with the current diff.  Assumes gvim is in your system PATH.

Should be cross-platform but so far only tested on Windows 10.
