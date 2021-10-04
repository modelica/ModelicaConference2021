## Papers by Shashi Gowda
<table><tr><th>Title:</th>
<td>Composing Modeling and Simulation with Machine Learning in Julia</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/ChrisRackauckas">Chris Rackauckas</a>, <a href="/proceedings/authors/RanjanAnantharaman">Ranjan Anantharaman</a>, <a href="/proceedings/authors/AlanEdelman">Alan Edelman</a>, <a href="/proceedings/authors/ShashiGowda">Shashi Gowda</a>, <a href="/proceedings/authors/MajaGwozdz">Maja Gwozdz</a>, <a href="/proceedings/authors/AnandJain">Anand Jain</a>, <a href="/proceedings/authors/ChrisLaughman">Chris Laughman</a>, <a href="/proceedings/authors/YingboMa">Yingbo Ma</a>, <a href="/proceedings/authors/FrancescoMartinuzzi">Francesco Martinuzzi</a>, <a href="/proceedings/authors/AvikPal">Avik Pal</a>, <a href="/proceedings/authors/UtkarshRajput">Utkarsh Rajput</a>, <a href="/proceedings/authors/ElliotSaba">Elliot Saba</a> and <a href="/proceedings/authors/ViralShah">Viral Shah</a></td>
</tr>
<tr><th>Abstract:</th>
<td>In this paper we introduce JuliaSim, a high-performance programming environment designed to blend traditional modeling and simulation with machine learning. JuliaSim can build accelerated surrogates from component-based models, such as those conforming to the FMI standard, using continuous-time echo state networks (CTESN). The foundation of this environment, ModelingToolkit.jl, is an acausal modeling language which can compose the trained surrogates as components within its staged compilation process. As a complementary factor we present the JuliaSim model library, a standard library with differential-algebraic equations and pre-trained surrogates, which can be composed using the modeling system for design, optimization, and control. We demonstrate the effectiveness of the surrogate-accelerated modeling and simulation approach on HVAC dynamics by showing that the CTESN surrogates accurately capture the dynamics of a HVAC cycle at less than 4\% error while accelerating its simulation by 340x. We illustrate the use of surrogate acceleration in the design process via global optimization of simulation parameters using the embedded surrogate, yielding a speedup of two orders of magnitude to find the optimum. We showcase the surrogate deployed in a co-simulation loop, as a drop-in replacement for one of the coupled FMUs, allowing engineers to effectively explore the design space of a coupled system. Together this demonstrates a workflow for automating the integration of machine learning techniques into traditional modeling and simulation processes.</td></tr>
<tr><th>Keywords:</th>
<td>Julia, machine learning, surrogate modeling, acceleration, co-simulation, Functional Mock-up Interface</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp2118197">full paper</a> <a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/80x15.png" /></a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Rackauckas:2021,
  title = &quot;{Composing Modeling and Simulation with Machine Learning in Julia}&quot;,
  author = {Chris Rackauckas and Ranjan Anantharaman and Alan Edelman and Shashi Gowda and Maja Gwozdz and Anand Jain and Chris Laughman and Yingbo Ma and Francesco Martinuzzi and Avik Pal and Utkarsh Rajput and Elliot Saba and Viral Shah},
  pages = {97--107},
  doi = {10.3384/ecp2118197},
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
