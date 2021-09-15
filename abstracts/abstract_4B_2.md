## Software Architecture and Implementation of Modelica Buildings Library Coupling for Spawn of EnergyPlus

*Michael Wetter, Kyle Benne, Baptiste Ravache*

Abstract

Spawn of EnergyPlus is a next-generation energy simulation
engine that targets control design and implementation
workflows. Spawn reuses the weather, lighting, loads, and
envelope modules from EnergyPlus through a precompiled
library and couples them with HVAC and control
models implemented in Modelica. Thus, for Spawn, the
EnergyPlus HVAC models are removed. Spawn has been
designed to perform coupled simulation with any number
of EnergyPlus models, supporting simulation of a single
building or multiple buildings as part of a district energy
system.
This paper describes how the Modelica objects are implemented
and synchronized to allow the modular specification
at the Modelica-level that uses a Functional Mockup
Unit (FMU) that contains the EnergyPlus model. A key
feature of our implementation is that multiple instances
of Modelica models call C functions, which jointly build
a data structure that defines parameters, inputs and outputs
of the EnergyPlus model. This data structure is used
during the initialization to generate an FMU that contains
a fully configured EnergyPlus model. This FMU is then
accessed by all Modelica models to exchange with EnergyPlus
values for parameters, inputs and outputs during
the simulation. This setup allows the Modelica models to
be instantiated in a modular, object-oriented manner, as is
typical for Modelica, yet they jointly construct and use an
FMU that contains EnergyPlus.
Compared to an HVAC and envelope simulation that
uses a native Modelica building model of comparable level
of detail, the Modelica-EnergyPlus model translates about
35% faster and simulates about 50% faster.

*Keywords: Modelica Buildings Library, Spawn of Energy-Plus, Modelica External Object, FMI*
