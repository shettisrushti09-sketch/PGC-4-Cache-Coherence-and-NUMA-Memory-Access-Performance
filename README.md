# Experiment 4: Cache Coherence and NUMA Memory Access Performance

## Overview

This experiment studies how cache coherence protocols maintain consistency between multiple processor caches and how false sharing and NUMA memory placement affect performance.

The experiment covers three cache coherence protocols:

- **MSI** – Modified, Shared, Invalid
- **MESI** – Modified, Exclusive, Shared, Invalid
- **MOESI** – Modified, Owned, Exclusive, Shared, Invalid

It also examines adjacent and padded memory layouts to understand false sharing, along with local and remote memory access in NUMA systems.

## Objectives

- Understand the MSI, MESI and MOESI cache coherence protocols.
- Compare coherence traffic using a two-core simulation.
- Study false sharing using adjacent and padded counters.
- Examine NUMA local and remote memory access.
- Understand correctness, execution time and scalability.

## Repository Structure

```text
Experiment_4_Cache_Coherence_NUMA/
│
├── images/
│   ├── 01_coherence_simulation.png
│   ├── 02_false_sharing.png
│   ├── 03_numa_sweep.png
│   ├── 04_compare_numa.png
│   ├── 05_remote_numa_simulation.png
│   └── bus_transactions.png
│
├── scripts/
│   └── generate_charts.py
│
├── src/
│   ├── coherence_sim.py
│   ├── false_sharing.c
│   ├── numa_sweep.c
│   └── compare_numa.c
│
├── experiment_report.md
└── .gitignore
```

## Software Requirements

- VMware Workstation
- Ubuntu 22.04 LTS
- GCC compiler
- OpenMP
- Python 3
- numactl
- hwloc

Install the required packages on Ubuntu:

```bash
sudo apt update
sudo apt install build-essential numactl hwloc python3 -y
```

## Programs

| Program | Description |
|---|---|
| `coherence_sim.py` | Simulates MSI, MESI and MOESI protocols |
| `false_sharing.c` | Compares adjacent and padded counters |
| `numa_sweep.c` | Examines NUMA memory access performance |
| `compare_numa.c` | Combines false-sharing and memory-sweep comparisons |

## Execution

Navigate to the source directory:

```bash
cd src
```

### 1. Cache Coherence Simulation

```bash
python3 coherence_sim.py 1000
```

### 2. False Sharing

```bash
gcc -O2 false_sharing.c -fopenmp -o false_sharing
./false_sharing
```

### 3. NUMA Memory Sweep

```bash
gcc -O2 numa_sweep.c -fopenmp -o numa_sweep
```

Run the compiled program according to the NUMA configuration of the system.

### 4. Combined Comparison

```bash
gcc -O2 compare_numa.c -fopenmp -o compare_numa
./compare_numa
```

## Expected Observations

- MSI requires an upgrade transaction even for a private line's first write.
- MESI can move from Exclusive to Modified without a bus transaction.
- MOESI allows an owner cache to supply a dirty line to another cache.
- False sharing can reduce performance when threads update different variables on the same cache line.
- Padding can reduce false sharing.
- Remote NUMA access is typically slower on multi-socket systems; results can vary on a single-socket machine or virtual machine.

## Screenshots and Report

The `images/` directory contains experiment-related screenshots and the bus-transactions chart.

The detailed experiment report is available in [`experiment_report.md`](experiment_report.md).

## Note on Results

Execution timings depend on the processor, number of cores, operating system and virtual-machine configuration. Hardware performance results should be interpreted in the context of the machine on which the programs were executed. Reference outputs, if included, should be identified as reference results rather than personal measurements.

## Conclusion

The experiment illustrates how cache coherence protocols, false sharing and NUMA memory placement influence memory-system performance. It highlights the importance of reducing unnecessary coherence traffic and placing data efficiently in multi-core systems.
