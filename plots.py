import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("experiment_comparison_table.csv")
df = df.dropna()

sns.set_theme(style="whitegrid", font_scale=1.1)
chunk_sizes = sorted(df["chunk_size"].unique())
overlaps = sorted(df["chunk_overlap"].unique())
colors = sns.color_palette("tab10", len(overlaps))

# Subplots
fig, axes = plt.subplots(len(chunk_sizes), 2, figsize=(14, 4 * len(chunk_sizes)), sharex=True)

for i, chunk_size in enumerate(chunk_sizes):
    subset = df[df["chunk_size"] == chunk_size]
    
    for j, metric in enumerate(["precision", "recall"]):
        ax = axes[i, j]
        
        for overlap, color in zip(overlaps, colors):
            data = subset[subset["chunk_overlap"] == overlap].sort_values("chunks_retieved")
            ax.plot(data["chunks_retieved"], data[metric], label=f"Overlap {overlap}", marker='o', color=color)
        
        ax.set_ylabel(metric.capitalize())
        if metric == "recall":
            ax.set_ylim(0.4, 1.01)  
        else:
            ax.set_ylim(bottom=0)  # auto top for precision to emphasize variation
        
        if i == len(chunk_sizes) - 1:
            ax.set_xlabel("Chunks Retrieved")
        ax.set_title(f"{metric.capitalize()} — Chunk Size: {chunk_size}")
        ax.grid(True)
        
        if i == 0 and j == 1:
            ax.legend(title="Chunk Overlap", bbox_to_anchor=(1.05, 1), loc="upper left")

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.suptitle("Precision and Recall Trends by Chunk Size and Overlap (Scaled Separately)", fontsize=16)
plt.show()