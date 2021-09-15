## Detailed White-Box Non-Linear Model Predictive Control for Scalable Building HVAC Control

**Filip Jorissen, Damien Picard, Kristoff Six, Lieve Helsen**

[&#8594; full paper](../proceedings/papers/Modelica2021session4B_paper1.pdf)

Abstract

Grey-box and black-box MPC approaches for building
HVAC applications often use lumped, low-order models
with a low level of detail. While such models require
smaller computation times, their accuracy is limited and
there are practical constraints related to data collection,
how to deal with multi-zone buildings and they often do
not explicitly model the building HVAC equipment. In
this paper we present an alternative approach based on detailed
white-box models. TACO, a custom toolchain that
builds upon physics-based Modelica models and JModelica,
is used to efficiently solve the resulting optimisation
problems. This paper presents a realistic case study model
of 79 zones and OCP results for this case study are discussed,
demonstrating the feasibility of the approach and
the underestimated potential of detailed white-box MPC.

*Keywords: Optimal control of hybrid systems, HVAC, white-box modelling, building automation, TACO, JModelica, MPC*
