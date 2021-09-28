## Papers by Michael Wetter
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
  location = {Link\&quot;{o}ping, Sweden},
  editor = {Martin Sj\&quot;{o}lund and Lena Buffoni and Adrian Pop and Lennart Ochel},
  isbn = {978-91-7929-027-6},
  issn = {1650-3740},
  month = sep,
  series = {Link\&quot;{o}ping Electronic Conference Proceedings},
  number = {181},
  publisher = {Modelica Association and Link\&quot;{o}ping University Electronic Press},
  year = {2021}
}
</pre></td></tr>
</table><br>

<table><tr><th>Title:</th>
<td>A Case Study on Condenser Water Supply Temperature Optimization with a District Cooling Plant</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/KathrynHinkelman">Kathryn Hinkelman</a>, <a href="/proceedings/authors/JingWang">Jing Wang</a>, <a href="/proceedings/authors/ChengliangFan">Chengliang Fan</a>, <a href="/proceedings/authors/WangdaZuo">Wangda Zuo</a>, <a href="/proceedings/authors/AntoineGautier">Antoine Gautier</a>, <a href="/proceedings/authors/MichaelWetter">Michael Wetter</a> and <a href="/proceedings/authors/NicholasLong">Nicholas Long</a></td>
</tr>
<tr><th>Abstract:</th>
<td>District cooling (DC) continues to proliferate due to increasing global cooling demands and economies of scale benefits; however, most district-scale modeling has focused on heating, and to the best of our knowledge, researchers have yet to model cooling plants featuring waterside economizers in DC settings. With the popular Modelica Buildings library expanding its capabilities to district scale, this study is one of the first to demonstrate how the open-source models can be used for detailed energy and control analysis of a DC plant. For a real-world case study, we developed and calibrated high-fidelity models for a DC system central plant at a college campus in Colorado, USA, and we optimized the condenser water supply temperature (CWST) setpoint for a DC plant across multiple time horizons using the Optimization library in Dymola. Results indicate that annual CWST optimization saves 4.7% annual plant energy, with less than 1% of additional energy savings gained through daily optimization. This confirms previous studies&#x27; findings that high frequency CWST optimizations are not necessary for the studied system.</td></tr>
<tr><th>Keywords:</th>
<td>District Cooling, Optimization, Chiller Plant, Waterside Economizer, Modelica Buildings Library</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181587">full paper</a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Hinkelman:2021,
  title = {A Case Study on Condenser Water Supply Temperature Optimization with a District Cooling Plant},
  author = {Kathryn Hinkelman and Jing Wang and Chengliang Fan and Wangda Zuo and Antoine Gautier and Michael Wetter and Nicholas Long},
  pages = {587--595},
  doi = {10.3384/ecp21181587},
  booktitle = {Proceedings of the 14th International Modelica Conference},
  location = {Link\&quot;{o}ping, Sweden},
  editor = {Martin Sj\&quot;{o}lund and Lena Buffoni and Adrian Pop and Lennart Ochel},
  isbn = {978-91-7929-027-6},
  issn = {1650-3740},
  month = sep,
  series = {Link\&quot;{o}ping Electronic Conference Proceedings},
  number = {181},
  publisher = {Modelica Association and Link\&quot;{o}ping University Electronic Press},
  year = {2021}
}
</pre></td></tr>
</table><br>
