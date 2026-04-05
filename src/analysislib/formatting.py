# Import necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.display import display, HTML

def format_notebook():
    # Theme Setup
    sns.set_theme(style="darkgrid", context="talk")

    plt.rcParams.update({
        "figure.facecolor": "#1e1e1e",
        "axes.facecolor": "#1e1e1e",
        "axes.edgecolor": "#cccccc",
        "axes.labelcolor": "#e0e0e0",
        "text.color": "#e0e0e0",
        "xtick.color": "#cccccc",
        "ytick.color": "#cccccc",
        "grid.color": "#444444",
        "grid.alpha": 0.3,
        "legend.facecolor": "#2a2a2a",
        "legend.edgecolor": "#aaaaaa",
        "axes.titleweight": "bold",
        "font.family": "monospace",
        "font.size": 12,
        "savefig.facecolor": "#1e1e1e"
    })

    display(HTML("""<style>
        .widget-label { color: #cccccc !important; font-family: monospace !important; }
        .jupyter-widgets { background: transparent !important; }
    </style>"""))