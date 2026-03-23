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

    # CSS for widgets
    display(HTML("""
    <style>
    .output_area, .jupyter-widgets, .widgets-vbox, .widgets-hbox, .p-Widget {
        background-color: #1e1e1e !important; border: none !important;
    }
    .dark-slider .widget-label { color: #e0e0e0 !important;
                                font-size: 18px !important;
                                font-family: monospace !important;
                                font-weight: bold !important; }
    .dark-slider .widget-readout { color: #e0e0e0 !important; font-family: monospace !important; font-size: 18px !important; font-weight: bold !important; }
    .dark-slider .noUi-target { background: #2a2a2a !important; border: none !important; }
    .dark-slider .noUi-connect { background: #4dabf7 !important; }
    .dark-slider .noUi-handle { background: #cccccc !important; border: none !important; }
    .dark-slider .noUi-handle:hover { background: #ffffff !important; }
    img { background-color: #1e1e1e !important; }
    </style>
    """))