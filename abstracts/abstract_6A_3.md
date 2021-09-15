A Portable and Secure Package Format for Executable Simulation
Modules based on WebAssembly
Moritz Allmaras*1 Andrés Botero Halblaub2 Harald Held2 Tim Schenk2

Abstract
We propose a new format (Digital Twin Assembly –
dtasm) for self-contained executable co-simulation modules
that is portable and sandboxed, yet offers performance
close to native machine code and is sufficiently
lightweight for running on embedded devices. Dtasm is
based on WebAssembly, a standardized bytecode format
for a stack-based virtual machine originally developed
for high-performance computations in web browsers. A
language-independent binary interface for such modules
is described that is functionally comparable to FMI for cosimulation
but not tied to a particular programming language.
We discuss the benefits and drawbacks of this approach
and how it can address some specific issues for executable
simulation modules running in parallel with the
operation of real systems.
Keywords: Simulation Modularization, Portability, Sandboxing,
WebAssembly
