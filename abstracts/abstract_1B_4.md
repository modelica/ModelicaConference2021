## OpenModelica.jl: A modular and extensible Modelica compiler framework in Julia targeting ModelingToolkit.jl

**John Tinnerholm, Adrian Pop, Andreas Heuermann, Martin Sjölund**

Abstract

This paper presents current work on our Modelica Compiler
framework in Julia: OpenModelica.jl.1 We provide a
brief overview of this novel framework and its features,
and we also present the latest addition to the possible
backend options. We target ModelingToolkit.jl (MTK), a
framework for symbolic-numerical computation and scientific
machine learning. We evaluated the performance
of our new backend using the ScalableTestsuite, a benchmark
suite for Modelica Compilers. In our experiment,
we demonstrate that MTK can be used as a backend with
competitive simulation performance. In addition, using
the scientific machine learning features of the Modeling
toolkit, we were able to approximate models in the ScalableTestsuite
using surrogate techniques and how such
techniques can be used to accelerate the solving of nonlinear
algebraic loops during tearing.
Based on our experiments, we propose using this new
framework to automatically generate surrogate components
of a Modelica model during the simulation to increase
performance. The experimental work presented
here provides one of the first investigations concerning
the integration of the symbolic-numerical abilities of Julia
within a Modelica tool.

**Keywords: Modelica, OpenModelica, Julia, Equationbased modeling, Compiler-construction**
