## Papers by Benoît Caillaud
<table><tr><th>Title:</th>
<td>Handling Multimode Models and Mode Changes in Modelica</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/AlbertBenveniste">Albert Benveniste</a>, <a href="/proceedings/authors/BenoitCaillaud">Benoît Caillaud</a> and <a href="/proceedings/authors/MathiasMalandain">Mathias Malandain</a></td>
</tr>
<tr><th>Abstract:</th>
<td>Since its version 3.3, the Modelica language offers the possibility to model multimode systems having different DAE-based dynamics in each mode, thanks to the introduction of state machines. When the differentiation index and structure varies with mode changes, compilers generate erroneous simulation code, often resulting in runtime exceptions.<br>

We propose in this paper amultimode structural analysis for both multiple modes and mode change events and we show how correct code for restarts can be generated. Our approach is illustrated on two simple but representative mechanical systems.</td></tr>
<tr><th>Keywords:</th>
<td>multimode DAE, structural analysis, mode change events</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181507">full paper</a> <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Benveniste:2021a,
  title = &quot;{Handling Multimode Models and Mode Changes in Modelica}&quot;,
  author = {Albert Benveniste and Beno{\^\i}t Caillaud and Mathias Malandain},
  pages = {507--517},
  doi = {10.3384/ecp21181507},
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
<td>A Reduced Index Mode-Independent Structure Model Transformation for Multimode Modelica Models</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/BenoitCaillaud">Benoît Caillaud</a>, <a href="/proceedings/authors/MathiasMalandain">Mathias Malandain</a> and <a href="/proceedings/authors/AlbertBenveniste">Albert Benveniste</a></td>
</tr>
<tr><th>Abstract:</th>
<td>Since its 3.3 release, Modelica offers the possibility to specify models of dynamical systems with multiple modes having different DAE-based dynamics. However, the handling of such models by the current Modelica tools is not satisfactory, with mathematically sound models yielding exceptions at runtime. In this article, we propose a systematic way of rewriting a multimode Modelica model, based on the results of an already implemented multimode structural analysis. The rewritten Modelica model is guaranteed to be correctly compiled by state-of-the-art Modelica tools. Simulation results are presented on a simple, yet meaningful, physical system whose original Modelica model is not correctly handled by state-of-the-art Modelica tools.</td></tr>
<tr><th>Keywords:</th>
<td>Modelica, multimode DAE, structural analysis, model transformations</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181519">full paper</a> <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Caillaud:2021,
  title = &quot;{A Reduced Index Mode-Independent Structure Model Transformation for Multimode Modelica Models}&quot;,
  author = {Beno{\^\i}t Caillaud and Mathias Malandain and Albert Benveniste},
  pages = {519--528},
  doi = {10.3384/ecp21181519},
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
<td>Compile-Time Impulse Analysis in Modelica</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/AlbertBenveniste">Albert Benveniste</a>, <a href="/proceedings/authors/BenoitCaillaud">Benoît Caillaud</a> and <a href="/proceedings/authors/MathiasMalandain">Mathias Malandain</a></td>
</tr>
<tr><th>Abstract:</th>
<td>Since its 3.3 release, Modelica offers the possibility to specify models of dynamical systems with multiple modes having different DAE-based dynamics. However, the handling of mode changes by the current Modelica tools is not satisfactory. <br>

An important difficulty is the occurrence of impulsive behavior at some mode changes, for some variables. In this paper, we propose a compile-time algorithm for identifying such impulsive behaviors and quantifying them in terms of their magnitude orders. Such algorithm can be used as an additional step of the structural analysis of Modelica models.</td></tr>
<tr><th>Keywords:</th>
<td>DAE, multimode DAE, structural analysis, impulsive behaviors</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181549">full paper</a> <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Benveniste:2021b,
  title = &quot;{Compile-Time Impulse Analysis in Modelica}&quot;,
  author = {Albert Benveniste and Beno{\^\i}t Caillaud and Mathias Malandain},
  pages = {549--559},
  doi = {10.3384/ecp21181549},
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
