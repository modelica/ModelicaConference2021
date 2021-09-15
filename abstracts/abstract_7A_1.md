Handling Multimode Models and Mode Changes in Modelica
Albert Benveniste1 Benoît Caillaud1 Mathias Malandain1

Abstract
Since its version 3.3, the Modelica language offers the
possibility to model multimode systems having different
DAE-based dynamics in each mode, thanks to the introduction
of state machines. When the differentiation index
and structure varies with mode changes, compilers generate
erroneous simulation code, often resulting in runtime
exceptions. We propose in this paper a multimode structural
analysis for both multiple modes and mode change
events and we show how correct code for restarts can be
generated. Our approach is illustrated on two simple but
representative mechanical systems.
Keywords: multimode DAE, structural analysis
