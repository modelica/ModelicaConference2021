## Parallel Fast: An Efficient Coupling Approach for Co-Simulation with Different Coupling Step Sizes

**Franz Holzinger, Klaus Schuch, Martin Benedikt, Daniel Watzenig**

Abstract

The primary task of co-simulation is the synchronization
and exchange of data between the subsystems, e.g.,
FMUs, at certain coupling points. If the FMUs have different
step sizes, the synchronization of the FMUs is often
at the expense of the simulation duration of the cosimulation.
The presented parallel fast scheduling algorithm
is an effective approach to couple FMUs with different
coupling step sizes. Therefore, synchronization intervals
are introduced in which FMUs that finish their coupling
step are synchronized. This allows a high performance
of the coupling in terms of simulation duration.
The higher performance compared to other scheduling algorithms
is particularly evident in real-time applications,
i.e., HiL simulations. However, the synchronization intervals
are defined via a synchronization step size, which
can be set independently to the coupling step sizes of the
FMUs. This additional step size has a significant impact
on the simulation accuracy. An extrapolation measure is
introduced, which approximates the impact of the synchronization
step size on the extrapolation error and thus
on the simulation accuracy. Based on this, an optimization
approach is presented, which derives the optimal synchronization
step size to minimize the extrapolation measure.
parallel scheduling, synchronization step size, optimal
step size
