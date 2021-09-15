Portable runtime environments for Python-based FMUs:
Adding Docker support to UniFMU
Thomas Schranz1 Christian Møldrup Legaard2 Daniella Tola2 Gerald Schweiger1

Abstract
Co-simulation is a means to combine and leverage the
strengths of different modeling tools, environments and
formalisms and has been applied successfully in various
domains. The Functional Mock-Up Interface (FMI) is
the most commonly used standard for co-simulation. In
this paper we extend UniFMU, a tool that allows users
to build Functional Mock-Up Units (FMUs) in virtually
any programming language, to support execution within
Docker. As a result the generated FMUs can be distributed
in an environment containing all runtime dependencies.
To describe the process of creating Dockerized FMUs using
UniFMU, we show how to model and co-simulate
a robotic arm and a controller using two Python-based
FMUs.
Keywords: FMI, Co-Sim, Python, Tool-Coupling, Docker
