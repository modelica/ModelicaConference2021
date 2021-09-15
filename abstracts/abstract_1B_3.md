## Composing Modeling and Simulation with Machine Learning in Julia

**Chris Rackauckas, Ranjan Anantharaman, Alan Edelman, Shashi Gowda, Maja Gwozdz, Anand Jain, Chris Laughman, Yingbo Ma, Francesco Martinuzzi, Avik Pal, Utkarsh Rajput, Elliot Saba1 Viral B. Shah**

[&#8594; full paper](../proceedings/papers/Modelica2021session1B_paper3.pdf)

Abstract

In this paper we introduce JuliaSim, a high-performance
programming environment designed to blend traditional
modeling and simulation with machine learning. JuliaSim
can build accelerated surrogates from component-based
models, such as those conforming to the FMI standard,
using continuous-time echo state networks (CTESN). The
foundation of this environment, ModelingToolkit.jl, is an
acausal modeling language which can compose the trained
surrogates as components within its staged compilation
process. As a complementary factor we present the JuliaSim
model library, a standard library with differentialalgebraic
equations and pre-trained surrogates, which can
be composed using the modeling system for design, optimization,
and control. We demonstrate the effectiveness
of the surrogate-accelerated modeling and simulation approach
on HVAC dynamics by showing that the CTESN
surrogates accurately capture the dynamics of a HVAC
cycle at less than 4% error while accelerating its simulation
by 340x. We illustrate the use of surrogate acceleration
in the design process via global optimization
of simulation parameters using the embedded surrogate,
yielding a speedup of two orders of magnitude to find
the optimum. We showcase the surrogate deployed in a
co-simulation loop, as a drop-in replacement for one of
the coupled FMUs, allowing engineers to effectively explore
the design space of a coupled system. Together this
demonstrates a workflow for automating the integration of
machine learning techniques into traditional modeling and
simulation processes.

*Keywords: modeling, simulation, Julia, machine learning, surrogate modeling, acceleration, co-simulation, Functional Mock-up Interface*
