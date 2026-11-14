# Experiment 4: Cache Coherence and NUMA Memory Access Performance

## 1. Objective

To study how cache coherence protocols (MSI, MESI and MOESI) maintain consistency among the caches of a multi-core processor and to understand the performance effects of false sharing and NUMA memory placement.

The experiment uses two threads, each incrementing its own counter. The counters are arranged either on the same cache line (adjacent layout) or on separate cache lines (padded layout).

## 2. Software Requirements

| Software / Tool | Purpose |
|---|---|
| VMware Workstation Pro | Virtualization |
| Ubuntu 22.04 LTS | Guest operating system |
| GCC Compiler | Compiling C programs |
| OpenMP | Parallel programming |
| numactl and hwloc | NUMA topology and memory binding |
| Python 3 | Cache coherence simulation |

## 3. Theory

### 3.1 Cache Coherence

In a multi-core processor, each core has its own private cache. When multiple cores access the same memory location, they may hold separate copies of the data.

If one core modifies its copy, other copies may become outdated. Cache coherence protocols ensure that all cores maintain a consistent view of memory.

### 3.2 MSI Protocol

MSI uses three cache states:

- **Modified (M):** The cache has the only valid, modified copy.
- **Shared (S):** Multiple caches may hold a clean copy.
- **Invalid (I):** The cache copy is not valid.

### 3.3 MESI Protocol

MESI adds the Exclusive (E) state to MSI.

- **Exclusive (E):** A cache holds the only clean copy.
- A write to an Exclusive line changes its state to Modified without requiring a bus transaction.

This reduces bus traffic for private data.

### 3.4 MOESI Protocol

MOESI adds the Owned (O) state.

- **Owned (O):** A cache holds a modified line that may also be shared with other caches.
- The owner can supply data directly to other caches without first writing it back to memory.

This helps reduce memory write-back traffic.

### 3.5 False Sharing

False sharing occurs when two threads modify different variables that happen to occupy the same cache line.

Even though the variables are different, the cache coherence mechanism operates on the entire cache line. This causes the line to move between cores repeatedly.

Padding or alignment separates the variables into different cache lines and reduces this unnecessary coherence traffic.

### 3.6 NUMA

NUMA stands for Non-Uniform Memory Access.

In a NUMA system, memory is divided among different nodes. Accessing memory attached to the local node is generally faster than accessing memory attached to another node.

The `numactl` utility can control CPU and memory placement using CPU-node binding and memory-node binding.

## 4. Programs Included

The repository contains four source programs:

| Program | Description |
|---|---|
| `coherence_sim.py` | Simulates MSI, MESI and MOESI protocols |
| `false_sharing.c` | Compares adjacent and padded counters |
| `numa_sweep.c` | Performs a NUMA memory sweep |
| `compare_numa.c` | Combines false-sharing and memory-sweep comparisons |

## 5. Protocol Simulation Results

The following values are the sample output provided in the experiment reference PDF for 1,000 iterations.

| Layout | Protocol | Bus Transactions | BusRd | BusUpgr | Invalidations | Write-back | C2C |
|---|---|---:|---:|---:|---:|---:|---:|
| Adjacent | MSI | 4000 | 2000 | 2000 | 1999 | 1999 | 0 |
| Adjacent | MESI | 3999 | 2000 | 1999 | 1999 | 1999 | 0 |
| Adjacent | MOESI | 3999 | 2000 | 1999 | 1999 | 0 | 1999 |
| Padded | MSI | 4 | 2 | 2 | 0 | 0 | 0 |
| Padded | MESI | 2 | 2 | 0 | 0 | 0 | 0 |
| Padded | MOESI | 2 | 2 | 0 | 0 | 0 | 0 |

C2C = Cache-to-cache transfer.

### Graph: Bus Transactions

![Bus Transactions Comparison](../images/bus_transactions.png)

The graph compares bus transactions for adjacent and padded layouts across the three protocols.

## 6. Performance Results

Execution-time values depend on the processor, virtual machine and number of threads. No hardware execution measurements have been recorded for this report.

### 6.1 False Sharing Results

| Layout | Threads | Final Count | Correctness | Time (s) |
|---|---:|---:|---|---|
| Adjacent | 1 | 100000000 | Expected: Correct | Not measured |
| Padded | 1 | 100000000 | Expected: Correct | Not measured |
| Adjacent | 2 | 100000000 | Expected: Correct | Not measured |
| Padded | 2 | 100000000 | Expected: Correct | Not measured |
| Adjacent | 4 | 100000000 | Expected: Correct | Not measured
