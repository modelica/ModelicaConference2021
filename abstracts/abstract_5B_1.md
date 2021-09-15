## A Cloud-native Implementation of the Simulation as a Service-Concept Based on FMI

**Moritz Stüber, Georg Frey**

Abstract

Providing modelling and simulation capabilities as a service
promises to increase their value by improving accessibility
for non-expert users and software agents as well as
by leveraging cloud-computing technology to scale simulation
performance beyond the capabilities of a single
computer. In order to reach this potential, implementations
must align their design with the architectural styles
of cloud computing applications and the web in general.
We present an open-source, cloud-native Simulation as
a Service (SIMaaS)-implementation that gives access to
models and allows simulating them on the web. The implementation
uses Functional Mockup Units (FMUs) for
co-simulation as an executable form of a model and relies
on FMPy for simulation. It is realized as a microservice in
the form of a REST-based HTTP-API. Functionality and
performance are demonstrated by using the service to create
ensemble forecasts for PV systems and to search for an
optimal parameter set using a genetic algorithm. Conceptual
limitations and the resulting opportunities for further
work are summarized.

*Keywords: simulation as a service, cloud-native simulation, service-oriented software architecture, FMI 2.0*
