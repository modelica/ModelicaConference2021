## Papers by John Tinnerholm
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
<td><a href="https://doi.org/10.3384/ecp21181109">full paper</a> <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a></td>
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
