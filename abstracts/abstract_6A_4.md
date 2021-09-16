## New Method to Perform Data Reconciliation with OpenModelica and ThermoSysPro

**Daniel Bouskela, Audrey Jardin, Arunkumar Palanisamy, Lennart Ochel, Adrian Pop**

[&#8594; full paper](../proceedings/papers/Modelica2021session6A_paper4.pdf)

Abstract

Data reconciliation aims at improving the accuracy of measurements by
reducing the effect of random errors in the data. This is achieved by
introducing redundancies on the measured quantities in the form of
constraints based on fundamental physical laws such as mass, momentum
and energy balance equations. These constraints are called the
auxiliary conditions. Modelica is an equational language that was
conceived to express models based on first principle physics for the
purpose of behavioral simulation. This paper shows how to reuse such
models for the purpose of data reconciliation. The novelty is to
automatically extract the auxiliary conditions from the Modelica
model. Then the reconciled values are computed using a least square
method constrained by the auxiliary conditions, as specified by the
VDI 2048 standard. The new method has been implemented in
OpenModelica. A simple example built with ThermoSysPro illustrates the
method in detail.

*Keywords: data reconciliation, Modelica, model reuse, cyber-physical systems, structural analysis*
