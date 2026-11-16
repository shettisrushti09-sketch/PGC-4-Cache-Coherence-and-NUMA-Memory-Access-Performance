# Experiment 4: Cache Coherence Protocols (MSI, MESI, MOESI) and NUMA Memory Access Performance

## Executive Summary

This experiment studies cache coherence protocols in multi-core systems and analyzes the effects of false sharing and Non-Uniform Memory Access (NUMA) on memory performance.

It covers three cache coherence protocols — MSI, MESI and MOESI — and compares adjacent and padded memory layouts to understand false sharing. It also investigates local and remote NUMA memory access.

The experiment combines Python-based simulation, C implementations, and performance visualizations to understand cache coherence, memory access behavior, and parallel performance.

---

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

- Study MSI, MESI, and MOESI cache coherence protocols.
- Understand how cache coherence maintains consistent data across processor caches.
- Simulate and compare cache coherence protocol transactions.
- Analyze false sharing using adjacent and padded counters.
- Examine local and remote NUMA memory access.
- Understand the effects of memory placement and cache coherence on performance.

## 2. Technologies and Tools

| Technology | Purpose |
|---|---|
| VMware Workstation | Virtual machine environment |
| Ubuntu 22.04 LTS | Operating system |
| GCC Compiler | C program compilation |
| OpenMP | Parallel programming |
| Python 3 | Cache coherence simulation |
| numactl | NUMA configuration and inspection |
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
│   ├── compare_numa.c
│   ├── false_sharing.c
│   └── numa_sweep.c
│
├── .gitignore
├── README.md
└── experiment_report.md
```

## 4. Theoretical Background

### 4.1 Cache Coherence Protocols

Cache coherence protocols ensure that multiple processor caches maintain a consistent view of shared memory.

| Protocol | Description |
|---|---|
| MSI | Uses Modified, Shared, and Invalid states. |
| MESI | Extends MSI by adding the Exclusive state. |
| MOESI | Extends MESI by adding the Owned state. |

**Cache States:**

- **Modified (M):** Cache line has been modified and differs from main memory.
- **Exclusive (E):** Cache line is held exclusively and is clean.
- **Shared (S):** Cache line may be present in multiple caches.
- **Invalid (I):** Cache line contains invalid data.
- **Owned (O):** Cache holds a modified shared line and is responsible for supplying its data.

### 4.2 False Sharing

False sharing occurs when multiple threads modify different variables that occupy the same cache line.

- Adjacent counters may cause unnecessary cache coherence traffic.
- Padded counters separate frequently modified variables.
- Padding can reduce false sharing and improve parallel performance.

### 4.3 NUMA Architecture

Non-Uniform Memory Access (NUMA) is a memory architecture in which memory access time depends on the location of memory relative to the processor.

| Memory Type | Description |
|---|---|
| Local Memory | Memory connected to the processor's own NUMA node. |
| Remote Memory | Memory connected to another NUMA node. |

Remote memory access can have higher latency than local memory access, particularly in multi-socket systems.

## 5. Source Code and Programs

All implementation files are located in the `src/` directory.

| Program | Description |
|---|---|
| `coherence_sim.py` | Simulates MSI, MESI, and MOESI cache coherence protocols. |
| `false_sharing.c` | Compares adjacent and padded counters to study false sharing. |
| `numa_sweep.c` | Studies NUMA memory access performance. |
| `compare_numa.c` | Performs combined NUMA and memory performance comparisons. |
| `generate_charts.py` | Generates experiment performance visualizations. |

## 6. Execution Instructions

### 6.1 Install Dependencies

Open the Ubuntu terminal and install the required packages:

```bash
sudo apt update

sudo apt install build-essential \
    numactl hwloc python3 python3-matplotlib -y
```

Verify the environment:

```bash
gcc --version
python3 --version
numactl --hardware
lscpu
```

### 6.2 Navigate to the Project

```bash
cd Experiment_4_Cache_Coherence_NUMA
```

### 6.3 Cache Coherence Simulation

Navigate to the source directory:

```bash
cd src
```

Execute:

```bash
python3 coherence_sim.py
```

This program simulates the MSI, MESI, and MOESI cache coherence protocols.

### 6.4 False Sharing Experiment

Compile the C program:

```bash
gcc -O2 -fopenmp false_sharing.c -o false_sharing
```

Execute:

```bash
./false_sharing
```

The program is used to study the performance effects of false sharing through adjacent and padded counters.

### 6.5 NUMA Memory Sweep

Compile:

```bash
gcc -O2 -fopenmp numa_sweep.c -o numa_sweep
```

Execute:

```bash
./numa_sweep
```

This program examines memory access performance under different NUMA-related configurations.

### 6.6 Combined NUMA Comparison

Compile:

```bash
gcc -O2 -fopenmp compare_numa.c -o compare_numa
```

Execute:

```bash
./compare_numa
```

This program performs additional memory performance comparisons.

**Note:** Actual NUMA-specific execution depends on the available hardware and memory nodes. Virtual machines may expose limited NUMA functionality.

## 7. Experiment Screenshots

The following screenshots document the experiment outputs and visualizations.

### 7.1 Cache Coherence Simulation

![Cache Coherence Simulation](./images/01_coherence_simulation.png)

### 7.2 False Sharing Analysis

![False Sharing](./images/02_false_sharing.png)

### 7.3 NUMA Memory Sweep

![NUMA Memory Sweep](./images/03_numa_sweep.png)

### 7.4 Combined NUMA Comparison

![Combined NUMA Comparison](./images/04_compare_numa.png)

### 7.5 Remote NUMA Simulation

![Remote NUMA Simulation](./images/05_remote_numa_simulation.png)

### 7.6 Bus Transactions Comparison

![Bus Transactions Comparison](./images/bus_transactions.png)

## 8. Comparison and Observations

### 8.1 Cache Coherence Comparison

The experiment compares the behavior of MSI, MESI, and MOESI protocols using simulated bus transactions.

![Bus Transactions Comparison](./images/bus_transactions.png)

### 8.2 Key Observations

| Case | Observation |
|---|---|
| MSI | Uses Modified, Shared, and Invalid states. |
| MESI | Exclusive state can avoid an unnecessary upgrade transaction. |
| MOESI | Owned state allows a cache to retain a modified shared line. |
| Adjacent Counters | Can cause false sharing and additional coherence traffic. |
| Padded Counters | Can reduce false sharing by separating counters across cache lines. |
| Local NUMA Memory | Provides a reference for memory access performance. |
| Remote NUMA Memory | May introduce additional memory access latency. |

## 9. Conclusion

This experiment demonstrates the importance of cache coherence and memory architecture in multi-core computing systems.

MSI, MESI, and MOESI use different cache states and transitions to maintain data consistency. False sharing can introduce unnecessary cache coherence traffic, while padding can help reduce this effect.

The NUMA analysis highlights how memory placement influences access performance. Overall, the experiment provides practical insight into cache coherence protocols, memory hierarchy, and parallel performance optimization.

## 10. Experiment Report

For detailed theoretical explanations, implementation methodology, program descriptions, observations, and results, refer to the complete experiment report:

[View Experiment Report](./experiment_report.md)

---

**Note:** Execution time and hardware performance depend on the processor, available cores, operating system, and virtual machine configuration. Actual measurements should be recorded from the system used to execute the experiment. Simulated results should be distinguished from hardware measurements.
