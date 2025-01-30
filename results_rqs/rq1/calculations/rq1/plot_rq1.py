import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from glob import glob

METADATA_ORDER = [
    'cff', 'readme', 'package', 'authors', 'contributors',
    'license', 'codemeta', 'zenodo', 'none'
]

data = {}
for file in glob('rq1_results_*.json'):
    with open(file) as f:
        json_data = json.load(f)
        cluster = list(json_data.keys())[0]
        data[cluster] = {k: json_data[cluster][k] for k in METADATA_ORDER}

df = pd.DataFrame(data).astype(float)

labels = {
    'cff': 'CFF File',
    'readme': 'README',
    'package': 'Package File',
    'authors': 'AUTHORS',
    'contributors': 'CONTRIBUTORS',
    'license': 'LICENSE',
    'codemeta': 'Codemeta.json',
    'zenodo': 'Zenodo.json',
    'none': 'None'
}

plt.figure(figsize=(12, 8))
ax = sns.heatmap(
    df.rename(index=labels),
    annot=True,
    fmt=".1f",
    cmap="YlGnBu",
    cbar_kws={'label': 'Percentage (%)'},
    linewidths=0.5,
    annot_kws={"size": 9}
)

plt.title('RQ1: Metadata Adoption Across Research Clusters', pad=20, fontsize=14)
plt.xlabel('Research Clusters', labelpad=15)
plt.ylabel('Metadata Files', labelpad=15)
ax.xaxis.tick_top()
plt.xticks(rotation=45, ha='left')
plt.yticks(rotation=0)

plt.tight_layout()
plt.show()