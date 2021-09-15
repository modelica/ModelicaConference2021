## Power Flow Record Structures to Initialize OpenIPSL Phasor Time-Domain Simulations with Python

**Sergio A. Dorado-Rojas, Giuseppe Laera, Marcelo de Castro Fernandes, Tetiana Bogodorova, Luigi Vanfretti**

[&#8594; full paper](../proceedings/papers/Modelica2021session2A_paper4.pdf)

Abstract

This paper presents a tool to populate power flow results
for phasor time-domain simulations with the Open Instance
Power System Library (OpenIPSL). Our proposal
takes advantage of the object-oriented philosophy of Modelica
and introduces a data structure based on records to
handle power flow data for a given network model. Such
records constitute a user-friendly interface to change the
guess values used to solve the initial condition of a dynamical
simulation straightforwardly. Power flow calculations
are carried out by the open-source Python library GridCal.
We demonstrate the tool capabilities by generating power
flow results for several grid models and comparing them
with those obtained via proprietary tools such as PSS/E.
Moreover, we provide tutorial materials to ease integrating
the tool for a new/experienced OpenIPSL user.

*Keywords: GridCal, OpenIPSL, Power Flow, Python, Records*
