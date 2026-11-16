# Experiment 4: Cache Coherence Protocols (MSI, MESI, MOESI) & NUMA Memory Access Performance

## Executive Summary

This experiment investigates cache coherence mechanisms in multi-core systems and analyzes how false sharing and NUMA memory placement influence memory access performance.

The study covers three cache coherence protocols — MSI, MESI, and MOESI — and compares adjacent and padded memory layouts to understand false sharing. It also examines local and remote NUMA memory access.

The experiment combines Python-based protocol simulation, C implementations, and performance visualizations to understand memory consistency, coherence traffic, and memory access behavior.

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
- Understand how cache coherence maintains consistency between processor caches.
- Compare coherence transactions through simulation.
- Analyze false sharing using adjacent and padded counters.
- Examine local and remote NUMA memory access.
- Understand the relationship between memory placement, coherence traffic, and performance.

## 2. Technologies and Tools

| Technology | Purpose |
|---|---|
| VMware Workstation | Virtual machine environment |
| Ubuntu 22.04 LTS | Operating system |
| GCC Compiler | C program compilation |
| OpenMP | Multi-threaded execution |
| Python 3 | Cache coherence simulation |
| numactl | NUMA memory configuration and inspection |
| hwloc | Hardware topology inspection |

---

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

---

## 4. Theoretical Background

### 4.1 Cache Coherence Protocols

Cache coherence protocols ensure that multiple processor caches maintain a consistent view of shared memory.

The three protocols studied are:

| Protocol | Description |
|---|---|
| MSI | Uses Modified, Shared, and Invalid states. |
| MESI | Extends MSI by introducing the Exclusive state. |
| MOESI | Extends MESI by introducing the Owned state. |

**Important Cache States:**

- **Modified (M):** Cache line has been modified and differs from main memory.
- **Exclusive (E):** Cache line is held exclusively and is clean.
- **Shared (S):** Cache line may be present in multiple caches.
- **Invalid (I):** Cache line contains invalid data.
- **Owned (O):** Cache holds a modified shared line and is responsible for supplying its data.

### 4.2 False Sharing

False sharing occurs when multiple threads modify different variables that occupy the same cache line.

- Adjacent counters may cause unnecessary cache coherence traffic.
- Padded counters separate frequently modified variables into different cache lines.
- Padding can reduce false sharing and improve parallel performance.

### 4.3 NUMA Architecture

Non-Uniform Memory Access (NUMA) is a memory architecture in which memory access time depends on the location of memory relative to the processor.

| Memory Type | Description |
|---|---|
| Local Memory | Memory attached to the processor's own NUMA node. |
| Remote Memory | Memory attached to another NUMA node. |

Remote memory access can have higher latency than local memory access, particularly in multi-socket systems.

---

## 5. Source Code and Programs

All implementation files are organized inside the `src/` directory.

| File | Description |
|---|---|
| `coherence_sim.py` | Simulates MSI, MESI, and MOESI cache coherence protocols. |
| `false_sharing.c` | Compares adjacent and padded counters to study false sharing. |
| `numa_sweep.c` | Studies NUMA memory access performance. |
| `compare_numa.c` | Performs combined memory performance comparisons. |
| `generate_charts.py` | Generates experiment performance visualizations. |

---

## 6. Execution Instructions

### 6.1 Install Dependencies

Open the Ubuntu terminal and install the required packages:

```bash
sudo apt update

sudo apt install build-essential numactl hwloc python3 python3-matplotlib -y
```

Verify the installed tools:

```bash
gcc --version
python3 --version
numactl --hardware
lscpu
```

### 6.2 Navigate to the Project Directory

```bash
cd Experiment_4_Cache_Coherence_NUMA
```

Navigate to the source directory:

```bash
cd src
```

### 6.3 Cache Coherence Simulation

Execute the Python simulation:

```bash
python3 coherence_sim.py 1000
```

This program simulates the MSI, MESI, and MOESI cache coherence protocols and compares their behavior.

### 6.4 False Sharing Experiment

Compile the C program:

```bash
gcc -O2 -fopenmp false_sharing.c -o false_sharing
```

Execute the program:

```bash
./false_sharing
```

Execute the padded-counter configuration:

```bash
./false_sharing padded
```

This experiment compares adjacent and padded counters to understand the impact of false sharing on parallel performance.

### 6.5 NUMA Memory Sweep

Compile:

```bash
gcc -O2 -fopenmp numa_sweep.c -o numa_sweep
```

Execute:

```bash
./numa_sweep
```

This program studies memory access performance under different NUMA-related configurations.

### 6.6 Combined NUMA Comparison

Compile:

```bash
gcc -O2 -fopenmp compare_numa.c -o compare_numa
```

Execute:

```bash
./compare_numa
```

This program performs additional comparisons related to memory access and performance.

**Note:** NUMA-specific execution depends on the available hardware, memory nodes, and virtual machine configuration. A virtual machine may expose limited NUMA functionality.

---

## 7. Experiment Screenshots

The following screenshots illustrate the program outputs and experiment visualizations.

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

---

## 8. Comparison and Observations

### 8.1 Cache Coherence Comparison

The following visualization compares bus transactions across the MSI, MESI, and MOESI cache coherence protocols.

![Bus Transactions Comparison](./images/bus_transactions.png)

### 8.2 Key Observations

| Case | Observation |
|---|---|
| MSI | Uses Modified, Shared, and Invalid states to maintain cache consistency. |
| MESI | Exclusive state can avoid unnecessary upgrade transactions. |
| MOESI | Owned state allows a cache to share a modified cache line. |
| Adjacent Counters | Can cause false sharing and additional coherence traffic. |
| Padded Counters | Can reduce false sharing by separating counters across cache lines. |
| Local NUMA Memory | Provides a reference for memory access performance. |
| Remote NUMA Memory | May have higher access latency than local memory. |

### 8.3 Performance Analysis

The experiment highlights three important aspects of multi-core memory performance:

1. **Cache Coherence:** Different protocols use different cache states and transactions to maintain data consistency.
2. **False Sharing:** Memory layout can influence cache coherence traffic when multiple threads access different variables in the same cache line.
3. **NUMA Access:** Memory placement can influence access latency depending on whether memory is local or remote to the processor.

Actual performance depends on the hardware architecture and execution environment.

---

## 9. Conclusion

This experiment demonstrates the importance of cache coherence protocols and memory architecture in multi-core computing systems.

MSI, MESI, and MOESI use different cache states and transitions to maintain memory consistency. False sharing can introduce unnecessary cache coherence traffic, while padding helps reduce this effect.

The NUMA analysis highlights how memory placement influences memory access performance. Overall, the experiment provides practical insight into cache coherence, memory hierarchy, and parallel performance optimization.

---

## 10. Experiment Report

For detailed theoretical explanations, implementation methodology, program descriptions, experimental observations, and conclusions, refer to the complete experiment report:

**[View Complete Experiment Report](./experiment_report.md)**

---

**Note:** Execution times and hardware performance depend on the processor, available cores, operating system, and virtual machine configuration. Actual measurements should be recorded from the system used to execute the experiment. Simulated results should be clearly distinguished from actual hardware measurements.
