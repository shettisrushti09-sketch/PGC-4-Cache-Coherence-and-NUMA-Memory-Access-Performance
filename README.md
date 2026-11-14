# Experiment 4: Cache Coherence and NUMA Memory Access Performance

## Overview

This experiment analyzes cache coherence protocols and studies how false sharing and NUMA memory placement affect memory access performance in multi-core systems.

It focuses on three cache coherence protocols — MSI, MESI and MOESI — and compares adjacent and padded memory layouts to understand false sharing. It also examines local and remote memory access in NUMA systems.

## Objectives

- Study MSI, MESI and MOESI cache coherence protocols.
- Understand how cache coherence maintains consistency between processor caches.
- Compare coherence traffic using simulation.
- Analyze false sharing using adjacent and padded counters.
- Examine local and remote NUMA memory access.
- Understand correctness, execution time and scalability.

## Technologies and Tools

- VMware Workstation
- Ubuntu 22.04 LTS
- GCC Compiler
- OpenMP
- Python 3
- numactl
- hwloc

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
├── .gitignore
├── experiment_report.md
└── README.md
```

## Software Installation

Install the required packages in Ubuntu:

```bash
sudo apt update
sudo apt install build-essential numactl hwloc python3 -y
```

Verify the compiler and NUMA configuration:

```bash
gcc --version
numactl --hardware
lscpu
```

## Programs

| Program | Description |
|---|---|
| `coherence_sim.py` | Simulates MSI, MESI and MOESI cache coherence protocols |
| `false_sharing.c` | Compares adjacent and padded counters |
| `numa_sweep.c` | Studies NUMA memory access performance |
| `compare_numa.c` | Combines false-sharing and memory-sweep comparisons |

## Execution Instructions

Open the Ubuntu terminal and navigate to the experiment's source directory:

```bash
cd Experiment_4_Cache_Coherence_NUMA/src
```

### 1. Cache Coherence Simulation

```bash
python3 coherence_sim.py 1000
```

This program simulates the MSI, MESI and MOESI protocols and compares their coherence traffic.

### 2. False Sharing

Compile:

```bash
gcc -O2 false_sharing.c -fopenmp -o false_sharing
```

Run adjacent counters:

```bash
./false_sharing
```

Run padded counters:

```bash
./false_sharing padded
```

### 3. NUMA Memory Sweep

Compile:

```bash
gcc -O2 numa_sweep.c -fopenmp -o numa_sweep
```

Run:

```bash
./numa_sweep
```

Local and remote memory placement can be tested using `numactl`, depending on the available NUMA nodes.

### 4. Combined Comparison

Compile:

```bash
gcc -O2 compare_numa.c -fopenmp -o compare_numa
```

Run:

```bash
./compare_numa
```

## Experiment Screenshots

### 1. Cache Coherence Simulation

![Cache Coherence Simulation](images/01_coherence_simulation.png)

### 2. False Sharing

![False Sharing](images/02_false_sharing.png)

### 3. NUMA Memory Sweep

![NUMA Memory Sweep](images/03_numa_sweep.png)

### 4. Combined NUMA Comparison

![Combined NUMA Comparison](images/04_compare_numa.png)

### 5. Remote NUMA Simulation

![Remote NUMA Simulation](images/05_remote_numa_simulation.png)

## Cache Coherence Comparison

The following chart compares bus transactions for adjacent and padded layouts across MSI, MESI and MOESI.

![Bus Transactions Comparison](images/bus_transactions.png)

## Observations

| Case | Observation |
|---|---|
| MSI | Requires an upgrade transaction before the first write to a private shared line |
| MESI | Supports a silent Exclusive-to-Modified transition |
| MOESI | Allows an owner cache to supply a dirty line directly to another cache |
| Adjacent counters | Can cause false sharing and additional coherence traffic |
| Padded counters | Reduce false sharing by separating counters across cache lines |
| Local NUMA memory | Provides a reference for memory access time |
| Remote NUMA memory | Can have higher access time, particularly on multi-socket systems |

## Conclusion

This experiment demonstrates how cache coherence protocols maintain consistency between processor caches and how memory layout affects performance.

MSI, MESI and MOESI differ in the amount of coherence traffic they generate. False sharing can reduce performance when multiple threads modify different variables on the same cache line, while padding helps reduce this effect.

NUMA memory placement also influences memory access performance, with remote memory access typically having higher latency on multi-socket systems.

## Experiment Report

For detailed theory, methodology, program explanations, observations and conclusion, refer to:

[View Experiment Report](experiment_report.md)

## Note on Results

Execution timings depend on the processor, number of cores, operating system and virtual-machine configuration. Hardware timing results should be interpreted according to the system on which the experiment was executed. Reference outputs and screenshots should be clearly identified as reference material rather than personal measurements.
