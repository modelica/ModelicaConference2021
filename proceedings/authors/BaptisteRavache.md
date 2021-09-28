## Papers by Baptiste Ravache
<table><tr><th>Title:</th>
<td>Software Architecture and Implementation of Modelica Buildings Library Coupling for Spawn of EnergyPlus</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/MichaelWetter">Michael Wetter</a>, <a href="/proceedings/authors/KyleBenne">Kyle Benne</a> and <a href="/proceedings/authors/BaptisteRavache">Baptiste Ravache</a></td>
</tr>
<tr><th>Abstract:</th>
<td>Spawn of EnergyPlus is a next-generation energy simulation engine that targets control design and implementation workflows. Spawn reuses the weather, lighting, loads, and envelope modules from EnergyPlus implemented in C++. It couples these with HVAC and control models implemented in Modelica. Spawn has been designed to perform coupled simulation with any number of EnergyPlus envelope models, supporting simulation of a single building or multiple buildings as part of a district energy system.<br>

This paper describes how these Modelica objects are implemented and synchronized to allow the modular specification at the Modelica-level that uses a shared Functional Mockup Unit (FMU) for envelope simulation. A key feature of our implementation is that multiple instances of Modelica models call C functions, which jointly build a data structure that defines the configuration of the whole building model. This data structure is then used to generate a FMU that 
contains a fully configured EnergyPlus model. This FMU is then accessed by all these Modelica models to exchange with EnergyPlus values for parameters, inputs and outputs during the simulation. This setup allows the Modelica models to be instantiated in a modular, object-oriented manner, as is typical for Modelica, yet they jointly construct and use a shared building model.<br>

When compared to a native Modelica building envelope simulation of comparable level of detail, the coupled Modelica-EnergyPlus model translates about 35% faster and simulates about 50% faster.</td></tr>
<tr><th>Keywords:</th>
<td>Modelica Buildings Library, Spawn of EnergyPlus, Modelica External Object</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181325">full paper</a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Wetter:2021,
  title = {Software Architecture and Implementation of Modelica Buildings Library Coupling for Spawn of EnergyPlus},
  author = {Michael Wetter and Kyle Benne and Baptiste Ravache},
  pages = {325--334},
  doi = {10.3384/ecp21181325},
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
