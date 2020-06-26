from plotly.subplots import make_subplots

from dataTransformations.kplot import KMeansPlot
from dataTransformations.silplot import SilhouettePlot


class Subplots:

    def subplots(self):

        fig = make_subplots(rows=2, cols=2, start_cell="bottom-left")

        fig.add_trace(KMeansPlot().kMeansPlot(),
                      row=1,
                      col=1)

        fig.add_trace(SilhouettePlot().silhouettePlot(),
                      row=1,
                      col=2)

        fig.update_layout(
            title_text="Multiple Subplots with Titles",
            #autosize=False,
            width=720,
            height=360,
            #margin=dict(l=50, r=50, b=100, t=100, pad=4),
            showlegend=False,
            #paper_bgcolor="LightSteelBlue",
        )

        return fig