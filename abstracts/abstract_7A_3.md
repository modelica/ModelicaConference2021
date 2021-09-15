Evaluating a Tree Diff Algorithm for Use in Modelica Tools
Martin Sjölund1

Abstract
Modelica tools change the formatting of the source code
when performing operations in the graphical user interface.
These unintended changes cause problems for
source code management since a code review would
mostly go through changes that do not change any semantics.
The intent of this work is to present a workflow where
edits from an interactive graphical user interface does not
contain these unintended changes when using the source
code management system.
A diff tool that can merge two Modelica files and produce
a merged copy is presented and evaluated. The diff
algorithm works by comparing syntax subtrees of Modelica
code and having some domain knowledge about which
subtrees belong together, speeding up the diff algorithm.
The result is a merged file by taking formatting of the first
file and the semantics from the second file. This works
very well for smaller changes (a single edit) and scales
with file size (making the user interface faster for smaller
files).
To test the algorithm on a larger set of changes, a conversion
script was applied to a set of libraries. The effect
of applying a conversion script is a set of automated edit
operations, which cause unintended changes in the formatting
of the source code. The diff algorithm with applied to
these changes and the performance was analyzed.
The results are very promising especially for Modelica
libraries that are split into multiple files rather than a
large single file. Having a single large file takes slightly
longer to process and produces additional unintended formatting
changes compared to a library developed as a set
of smaller files.
Keywords: Modelica, diff, file comparison, conversion
script, interactive user interface
