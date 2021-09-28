## Papers by Philipp Mehrfeld
<table><tr><th>Title:</th>
<td>Underfloor heating system model for building performance simulations</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/StephanGobel">Stephan Göbel</a>, <a href="/proceedings/authors/ElaineSchmitt">Elaine Schmitt</a>, <a href="/proceedings/authors/PhilippMehrfeld">Philipp Mehrfeld</a> and <a href="/proceedings/authors/DirkMuller">Dirk Müller</a></td>
</tr>
<tr><th>Abstract:</th>
<td>The efficiency of heat pump systems is highly dependent on the temperature gap between the sink and the source side. Therefore, it is necessary to accurately model the sink side to enable the most accurate and holistic analysis of building energy systems.
In both residential and non-residential buildings, underfloor heating systems are becoming more and more widely used. Their application can reduce the flow temperature of the heating system compared to a radiator and thus increase the efficiency of a heat pump system.
This paper provides an underfloor heating system model including automatic parametrization according to prEN 1264-3:2020-02. Since the model represents a whole underfloor system, it consists at the system level of the distributor and several heating circuits and takes at the smallest level the heat transfer from a pipe element through different floor layers into account.
The model is verified for the system requirements according to prEN 1264-2:2020-02. A parameter study with a variety of different underfloor heating parameters and floor layers shows that reductions of heat transfer in the underfloor heating system are compensated primarily by increasing the supply temperature. The highest influence on the temperature level of the system is exerted by the pipe spacing T, which raises the flow temperature by up to 10.9 K, from 36.6 °C (T = 100 mm) to 47.5 °C (T = 400 mm).
The model is freely available on GitHub:
https://github.com/RWTHEBC/AixLib/tree/issue890_HOMProject_FloorHeating</td></tr>
<tr><th>Keywords:</th>
<td>Building performance simulation, EN 1264, automatic parametrization</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181343">full paper</a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Gobel:2021,
  title = {Underfloor heating system model for building performance simulations},
  author = {Stephan G\&quot;obel and Elaine Schmitt and Philipp Mehrfeld and Dirk M\&quot;uller},
  pages = {343--349},
  doi = {10.3384/ecp21181343},
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
<td>A Modular Model of Reversible Heat Pumps and Chillers for System Applications</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/FabianWullhorst">Fabian Wüllhorst</a>, <a href="/proceedings/authors/DavidJansen">David Jansen</a>, <a href="/proceedings/authors/PhilippMehrfeld">Philipp Mehrfeld</a> and <a href="/proceedings/authors/DirkMuller">Dirk Müller</a></td>
</tr>
<tr><th>Abstract:</th>
<td>Vapour compression machines such as heat pumps and chillers are vital for achieving climate goals.
Efficiency of both depend mostly on system integration.
In order to simulate coupled energy systems, fast and stable simulation models are required.<br>

Hence, we implement an open-source model for reversible vapour compression machines.
The black-box based refrigeration cycle is replaceable, additional inertia and losses are optional.
Furthermore, we model relevant safety controls of vapour compression machines.<br>

 To show validity of the presented approach, we first calibrate two different black-box models onto measured heat pump data.
The table-based model fits both measured temperature and power with minimal calibration effort.<br>

Second, we show influences of different model options onto coupled building performance simulations.
Computation time increases up to 50 % when enabling all model options.
Simultaneously, seasonal efficiency decreases by up to 23 % when modeling all safety controls.</td></tr>
<tr><th>Keywords:</th>
<td>Heat Pump, Chiller, Modular Model</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181561">full paper</a> / <a href="https://github.com/RWTH-EBC/X-HD/tree/issue01_VCLibDev">library</a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Wullhorst:2021,
  title = {A Modular Model of Reversible Heat Pumps and Chillers for System Applications},
  author = {Fabian W\&quot;ullhorst and David Jansen and Philipp Mehrfeld and Dirk M\&quot;uller},
  pages = {561--568},
  doi = {10.3384/ecp21181561},
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
<td>Examination of Reduced Order Building Models with Different Zoning Strategies to Simulate Larger Non-Residential Buildings Based on BIM as Single Source of Truth</td>
</tr>
<tr><th>Authors:</th>
<td>
<a href="/proceedings/authors/DavidJansen">David Jansen</a>, <a href="/proceedings/authors/VeronikaRichter">Veronika Richter</a>, <a href="/proceedings/authors/DiegoCordobaLopez">Diego Cordoba Lopez</a>, <a href="/proceedings/authors/PhilippMehrfeld">Philipp Mehrfeld</a>, <a href="/proceedings/authors/JeromeFrisch">Jérôme Frisch</a>, <a href="/proceedings/authors/DirkMuller">Dirk Müller</a> and <a href="/proceedings/authors/ChristophvanTreeck">Christoph van Treeck</a></td>
</tr>
<tr><th>Abstract:</th>
<td>Non-residential buildings are accountable for 11% of global energy-related CO2 emissions (United Nations Environment Programme 2018). To increase the performance in this sector, Building Energy Performance Simulation (BEPS) is one feasible approach. Therefore, there is need for reliable and fast simulation models. One feasible approach are so called Reduced Order Models (ROMs). Thus in this paper, a comparison between the results of the established BEPS tool EnergyPlus and a ROM in Modelica with a reduced number of resistances and capacities is applied at the use case of a non-residential building. A self-developed toolchain was used to create equal models for ROM and EnergyPlus based on the same Building Information Modeling (BIM) model. The comparison shows that the reduced model deviates by 10%in annual heating and cooling. To increase accuracy and decrease computational effort the zoning strategy of non-residential buildings is investigated. The investigation shows that using a suitable zoning approach can reduce the computational effort by up to 97 %.</td></tr>
<tr><th>Keywords:</th>
<td>BEPS, BIM, zoning, low order, RC</td></tr>
<tr><th>Paper:</th>
<td><a href="https://doi.org/10.3384/ecp21181665">full paper</a></td>
</tr>
<tr><th>Bibtex:</th>
<td><pre>
@InProceedings{modelica.org:Jansen:2021,
  title = {Examination of Reduced Order Building Models with Different Zoning Strategies to Simulate Larger Non-Residential Buildings Based on BIM as Single Source of Truth},
  author = {David Jansen and Veronika Richter and Diego Cordoba Lopez and Philipp Mehrfeld and J\&#x27;er\^ome Frisch and Dirk M\&quot;uller and Christoph van Treeck},
  pages = {665--672},
  doi = {10.3384/ecp21181665},
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
