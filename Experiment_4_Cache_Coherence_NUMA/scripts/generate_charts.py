import matplotlib.pyplot as plt
import numpy as np

protocols = ["MSI", "MESI", "MOESI"]

data = {
    "Adjacent": [4000, 3999, 3999],
    "Padded": [4, 2, 2]
}

x = np.arange(len(protocols))
width = 0.35

plt.figure(figsize=(9, 5))

plt.bar(x - width / 2, data["Adjacent"], width, label="Adjacent")
plt.bar(x + width / 2, data["Padded"], width, label="Padded")

plt.xlabel("Cache Coherence Protocol")
plt.ylabel("Total Bus Transactions")
plt.title("Bus Transactions: Adjacent vs Padded Layout")
plt.xticks(x, protocols)
plt.legend()
plt.grid(axis="y", linestyle="--", alpha=0.5)

plt.tight_layout()
plt.savefig("bus_transactions.png", dpi=300)
plt.show()
