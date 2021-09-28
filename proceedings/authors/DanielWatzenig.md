## Papers by Daniel Watzenig
<table><tr><th>Title:</th>
<td>Parallel Fast: An Efficient Coupling Approach for Co-Simulation with Different Coupling Step Sizes</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/FranzHolzinger">Franz Holzinger</a>, <a href="/proceedings/authors/KlausSchuch">Klaus Schuch</a>, <a href="/proceedings/authors/MartinBenedikt">Martin Benedikt</a> and <a href="/proceedings/authors/DanielWatzenig">Daniel Watzenig</a></td>
</tr>
<tr><th>Abstract:</th>
<td>The primary task of co-simulation is the synchronization and exchange of data between the subsystems, e.g., FMUs, at certain coupling points. If the FMUs have different step sizes, the synchronization of the FMUs is often at the expense of the simulation duration of the co-simulation. The presented parallel fast scheduling algorithm is an effective approach to couple FMUs with different coupling step sizes. Therefore, synchronization intervals are introduced in which FMUs that finish their coupling step are synchronized. This allows a high performance of the coupling in terms of simulation duration. The higher performance compared to other scheduling algorithms is particularly evident in real-time applications, i.e., HiL simulations. However, the synchronization intervals are defined via a synchronization step size, which can be set independently to the coupling step sizes of the FMUs. This additional step size has a significant impact on the simulation accuracy. An extrapolation measure is introduced, which approximates the impact of the synchronization step size on the extrapolation error and thus on the simulation accuracy. Based on this, an optimization approach is presented, which derives the optimal synchronization step size to minimize the extrapolation measure.</td></tr>
<tr><th>Keywords:</th>
<td>parallel scheduling, synchronization step size, optimal step size</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181649">full paper</a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Holzinger:2021,
  title = {Parallel Fast: An Efficient Coupling Approach for Co-Simulation with Different Coupling Step Sizes},
  author = {Franz Holzinger and Klaus Schuch and Martin Benedikt and Daniel Watzenig},
  pages = {649--658},
  doi = {10.3384/ecp21181649},
  booktitle = {Proceedings of the 14th International Modelica Conference},
  location = {Link\&quot;{o}ping, Sweden},
  editor = {Martin Sjölund and Lena Buffoni and Adrian Pop and Lennart Ochel},
  isbn = {978-91-7929-027-6},
  issn = {1650-3740},
  month = sep,
  series = {Linköping Electronic Conference Proceedings},
  number = {181},
  publisher = {Modelica Association and Linköping University Electronic Press},
  year = {2021}
}
</pre></td></tr>
</table><br>
