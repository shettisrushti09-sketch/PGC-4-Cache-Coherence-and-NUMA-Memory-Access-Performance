# Experiment 4: Cache Coherence Protocols (MSI, MESI, MOESI) & NUMA Memory Access Performance

## Executive Summary

This experiment investigates cache coherence mechanisms in multi-core systems and analyzes how false sharing and NUMA memory placement influence memory access performance.

The study covers three cache coherence protocols — MSI, MESI and MOESI — and compares adjacent and padded memory layouts to understand false sharing. It also examines local and remote NUMA memory access.

The experiment combines protocol simulation, C implementations and performance visualizations to understand memory consistency, coherence traffic and memory access behavior.

## Table of Contents

1. [Experiment Objectives](#1-experiment-objectives)
2. [Technologies and Tools](#2-technologies-and-tools)
3. [Repository Structure](#3-repository-structure)
4. [Theoretical Background](#4-theoretical-background)
5. [Source Code and Programs](#5-source-code-and-programs)
6. [Execution Instructions](#6-execution-instructions)
7. [Experiment Screenshots](#7-experiment-screenshots)
8. [Comparison and Observations](#8-comparison-and-observations)
9. [Conclusion](#9-conclusion)
10. [Experiment Report](#10-experiment-report)

---

## 1. Experiment Objectives

- Study MSI, MESI and MOESI cache coherence protocols.
- Understand how cache coherence maintains consistency between processor caches.
- Compare coherence traffic through simulation.
- Analyze false sharing using adjacent and padded counters.
- Examine local and remote NUMA memory access.
- Understand correctness, execution time and scalability.

## 2. Technologies and Tools

| Technology | Purpose |
|---|---|
| VMware Workstation | Virtual machine environment |
| Ubuntu 22.04 LTS | Operating system |
| GCC Compiler | C program compilation |
| OpenMP | Multi-threaded execution |
| Python 3 | Cache coherence simulation |
| numactl | NUMA memory configuration |
| hwloc | Hardware topology inspection |

## 3. Repository Structure

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

## 4. Theoretical Background

### 4.1 Cache Coherence Protocols

Cache coherence protocols ensure that multiple processor caches maintain a consistent view of shared memory.

| Protocol | Description |
|---|---|
| MSI | Uses Modified, Shared and Invalid states |
| MESI | Adds the Exclusive state to MSI |
| MOESI | Adds the Owned state to MESI |

**Important Cache States:**

- **Modified (M):** Cache line has been modified and differs from main memory.
- **Exclusive (E):** Cache line is held exclusively and is clean.
- **Shared (S):** Cache line may be present in multiple caches.
- **Invalid (I):** Cache line contains invalid data.
- **Owned (O):** Cache holds a modified shared line and is responsible for supplying it.

### 4.2 False Sharing

False sharing occurs when multiple threads modify different variables that occupy the same cache line.

- Adjacent counters may cause unnecessary cache coherence traffic.
- Padded counters separate data across cache lines.
- Padding can reduce false sharing and improve parallel performance.

### 4.3 NUMA Architecture

Non-Uniform Memory Access (NUMA) is a memory architecture in which memory access time depends on the location of memory relative to the processor.

| Memory Type | Description |
|---|---|
| Local Memory | Memory attached to the processor's NUMA node |
| Remote Memory | Memory attached to another NUMA node |

Remote memory access can have higher latency than local memory access, particularly in multi-socket systems.

## 5. Source Code and Programs

All implementation files are located in the `src/` directory.

| Program | Description |
|---|---|
| `coherence_sim.py` | Simulates MSI, MESI and MOESI protocols |
| `false_sharing.c` | Compares adjacent and padded counters |
| `numa_sweep.c` | Studies NUMA memory access performance |
| `compare_numa.c` | Combines false-sharing and memory-sweep comparisons |

## 6. Execution Instructions

### 6.1 Software Installation

Install the required packages in Ubuntu:

```bash
sudo apt update
sudo apt install build-essential numactl hwloc python3 -y
```

Verify the environment:

```bash
gcc --version
numactl --hardware
lscpu
```

### 6.2 Cache Coherence Simulation

Navigate to the source directory:

```bash
cd Experiment_4_Cache_Coherence_NUMA/src
```

Execute:

```bash
python3 coherence_sim.py 1000
```

This program simulates MSI, MESI and MOESI cache coherence protocols.

### 6.3 False Sharing

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

### 6.4 NUMA Memory Sweep

Compile:

```bash
gcc -O2 numa_sweep.c -fopenmp -o numa_sweep
```

Execute:

```bash
./numa_sweep
```

### 6.5 Combined NUMA Comparison

Compile:

```bash
gcc -O2 compare_numa.c -fopenmp -o compare_numa
```

Execute:

```bash
./compare_numa
```

**Note:** NUMA-specific execution depends on the memory nodes and hardware resources available in the system or virtual machine.

## 7. Experiment Screenshots

The following screenshots illustrate the program outputs and experiment visualizations.

### 7.1 Cache Coherence Simulation

Simulation output for MSI, MESI and MOESI protocols.

![Cache Coherence Simulation](./images/01_coherence_simulation.png)

### 7.2 False Sharing Analysis

Comparison of adjacent and padded counter execution.

![False Sharing](./images/02_false_sharing.png)

### 7.3 NUMA Memory Sweep

NUMA memory access performance analysis.

![NUMA Memory Sweep](./images/03_numa_sweep.png)

### 7.4 Combined NUMA Comparison

Combined comparison of memory access and false-sharing behavior.

![Combined NUMA Comparison](./images/04_compare_numa.png)

### 7.5 Remote NUMA Simulation

Illustration of remote NUMA memory access behavior.

![Remote NUMA Simulation](./images/05_remote_numa_simulation.png)

## 8. Comparison and Observations

### 8.1 Cache Coherence Comparison

The following visualization compares bus transactions across cache coherence protocols and memory layouts.

![Bus Transactions Comparison](./images/bus_transactions.png)

### 8.2 Key Observations

| Case | Observation |
|---|---|
| MSI | Requires an upgrade transaction before the first write to a private shared line |
| MESI | Supports a silent Exclusive-to-Modified transition |
| MOESI | Allows an owner cache to supply a dirty line directly to another cache |
| Adjacent Counters | Can cause false sharing and additional coherence traffic |
| Padded Counters | Reduce false sharing by separating counters across cache lines |
| Local NUMA Memory | Provides a reference for memory access time |
| Remote NUMA Memory | Can have higher access time, particularly on multi-socket systems |

## 9. Conclusion

This experiment demonstrates the importance of cache coherence and memory architecture in multi-core computing systems.

MSI, MESI and MOESI use different cache states and transitions to maintain memory consistency. False sharing can introduce unnecessary coherence traffic, while padding helps reduce this effect.

The NUMA analysis highlights how memory placement influences access performance. Overall, the experiment provides practical insight into cache coherence, memory hierarchy and parallel performance optimization.

## 10. Experiment Report

For detailed theory, methodology, program explanations, observations and conclusion, refer to the complete experiment report:

[View Experiment Report](./experiment_report.md)

---

**Note:** Execution times and hardware performance depend on the processor, available cores, operating system and virtual-machine configuration. Actual measurements should be recorded from the system used to execute the experiment. Reference outputs should be clearly identified as reference material.
