## Papers by Martin Sjölund
<table><tr><th>Title:</th>
<td>OpenModelica.jl: A modular and extensible Modelica compiler framework in Julia targeting ModelingToolkit.jl</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/JohnTinnerholm">John Tinnerholm</a>, <a href="/proceedings/authors/AdrianPop">Adrian Pop</a>, <a href="/proceedings/authors/AndreasHeuermann">Andreas Heuermann</a> and <a href="/proceedings/authors/MartinSjolund">Martin Sjölund</a></td>
</tr>
<tr><th>Abstract:</th>
<td>This paper presents current work on our Modelica Compiler framework in Julia: OpenModelica.jl.
We provide a brief overview of this novel framework and its features, and we also present the latest addition to the possible backend options.
We target ModelingToolkit.jl (MTK), a framework for symbolic-numerical computation and scientific machine learning. 
We evaluated the performance of our new backend using the ScalableTestsuite, a benchmark suite for Modelica Compilers.
In our experiment, we demonstrate that MTK can be used as a backend with competitive simulation performance. 
In addition, using the scientific machine learning features of the Modeling toolkit,  
we were able to approximate models in the ScalableTestsuite using surrogate techniques and how such techniques can be used to accelerate 
the solving of nonlinear algebraic loops during tearing.<br>

Based on our experiments, we propose using this new framework to automatically generate surrogate components of a Modelica model during the simulation to increase performance.
The experimental work presented here provides one of the first investigations concerning the integration of the symbolic-numerical abilities of Julia within a Modelica tool.</td></tr>
<tr><th>Keywords:</th>
<td>Modelica, OpenModelica, Julia, Equation-based modeling, Compiler-construction</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181109">full paper</a> <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Tinnerholm:2021,
  title = {{OpenModelica.jl: A modular and extensible Modelica compiler framework in Julia targeting ModelingToolkit.jl}},
  author = {John Tinnerholm and Adrian Pop and Andreas Heuermann and Martin Sj\&quot;olund},
  pages = {109--117},
  doi = {10.3384/ecp21181109},
  booktitle = {Proceedings of the 14th International Modelica Conference},
  location = {Link\&quot;oping, Sweden},
  editor = {Martin Sj\&quot;olund and Lena Buffoni and Adrian Pop and Lennart Ochel},
  isbn = {978-91-7929-027-6},
  issn = {1650-3740},
  month = sep,
  series = {Link\&quot;oping Electronic Conference Proceedings},
  number = {181},
  publisher = {Modelica Association and Link\&quot;oping University Electronic Press},
  year = {2021}
}
</pre></td></tr>
</table><br>

<table><tr><th>Title:</th>
<td>Evaluating a Tree Diff Algorithm for Use in Modelica Tools</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/MartinSjolund">Martin Sjölund</a></td>
</tr>
<tr><th>Abstract:</th>
<td>Modelica tools change the formatting of the source code when performing operations in the graphical user interface.
These unintended changes cause problems for source code management where during a code review you will mostly see changes that do not perform anything.
The intent of this work is to present a workflow where edits from an interactive environment do not contain these unintended changes when using the source code management system.<br>

A diff tool that can merge two Modelica files and produce a merged copy is presented and evaluated.
The diff algorithm works by comparing syntax subtrees of Modelica code and having some domain knowledge about which subtrees belong together, speeding up the diff algorithm.
The result is a merged file by taking formatting of the first file and the semantics from the second file.
This works very well for smaller changes (a single edit) and scales with file size (making the user interface faster for smaller files).
To test the algorithm on a larger set of changes, a conversion script was applied to a set of libraries and the performance was analyzed.
The results are very promising especially for Modelica libraries that are split into multiple files rather than a large single file.
Having a single large file takes slightly longer to process and produces additional formatting changes to a library developed as a set of smaller files.</td></tr>
<tr><th>Keywords:</th>
<td>Modelica, diff, file comparison, conversion script, interactive user interface</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181529">full paper</a> <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Sjolund:2021,
  title = {{Evaluating a Tree Diff Algorithm for Use in Modelica Tools}},
  author = {Martin Sj\&quot;olund},
  pages = {529--537},
  doi = {10.3384/ecp21181529},
  booktitle = {Proceedings of the 14th International Modelica Conference},
  location = {Link\&quot;oping, Sweden},
  editor = {Martin Sj\&quot;olund and Lena Buffoni and Adrian Pop and Lennart Ochel},
  isbn = {978-91-7929-027-6},
  issn = {1650-3740},
  month = sep,
  series = {Link\&quot;oping Electronic Conference Proceedings},
  number = {181},
  publisher = {Modelica Association and Link\&quot;oping University Electronic Press},
  year = {2021}
}
</pre></td></tr>
</table><br>
