## Papers by Adrian Pop
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
  title = &quot;{OpenModelica.jl: A modular and extensible Modelica compiler framework in Julia targeting ModelingToolkit.jl}&quot;,
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
<td>New Method to Perform Data Reconciliation with OpenModelica and ThermoSysPro</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/DanielBouskela">Daniel Bouskela</a>, <a href="/proceedings/authors/AudreyJardin">Audrey Jardin</a>, <a href="/proceedings/authors/ArunkumarPalanisamy">Arunkumar Palanisamy</a>, <a href="/proceedings/authors/LennartOchel">Lennart Ochel</a> and <a href="/proceedings/authors/AdrianPop">Adrian Pop</a></td>
</tr>
<tr><th>Abstract:</th>
<td>Data reconciliation aims at improving the accuracy of measurements by reducing the effect of random errors in the data. This is achieved by introducing redundancies on the measured quantities in the form of constraints based on fundamental physical laws such as mass, momentum and energy balance equations. These constraints are called the auxiliary conditions. Modelica is an equational language that was conceived to express models based on first principle physics for the purpose of behavioral simulation. This paper shows how to reuse such models for the purpose of data reconciliation. The novelty is to automatically extract the auxiliary conditions from the Modelica model. Then the reconciled values are computed using a least square method constrained by the auxiliary conditions, as specified by the VDI 2048 standard. The new method has been implemented in OpenModelica. A simple example built with ThermoSysPro illustrates the method in detail.</td></tr>
<tr><th>Keywords:</th>
<td>data reconciliation, Modelica, model reuse, cyber-physical systems, structural analysis</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181453">full paper</a> <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Bouskela:2021,
  title = &quot;{New Method to Perform Data Reconciliation with OpenModelica and ThermoSysPro}&quot;,
  author = {Daniel Bouskela and Audrey Jardin and Arunkumar Palanisamy and Lennart Ochel and Adrian Pop},
  pages = {453--462},
  doi = {10.3384/ecp21181453},
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
