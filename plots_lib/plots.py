from pathlib import Path

import plotly.graph_objects as go

from .utils import *


def display_plot(
    data,
    title="",
    filename=None,
    img=False,
    html=False,
    s_json=False,
    equal=False,
    xaxis=None,
    yaxis=None,
    background_image=None,
    font=None,
    width=None,
    height=None,
    margins=None,
    save_path=None,
    legend=None,
    title_data=None,
    xaxis_data=None,
    yaxis_data=None,
):
    fig = go.Figure()
    generate_lines(fig, data)

    fig.update_layout(
        images=configure_bg_image(background_image),
        title=configure_title(title, title_data),
        xaxis=configure_xaxis(xaxis, equal, xaxis_data),
        yaxis=configure_yaxis(yaxis, equal, yaxis_data),
        font=configure_font(font),
        margin=configure_margins(margins, title),
        legend=configure_legend(legend),
        width=width,
        height=height,
    )

    if filename and save_path:
        save_path = Path(save_path)
        save_path.mkdir(parents=True, exist_ok=True)

        if img:
            fig.write_image(
                save_path / f"{filename}.png", width=width, height=height, scale=5
            )
        if html:
            fig.write_html(save_path / f"{filename}.html")
        if s_json:
            fig.write_json(save_path / f"{filename}.json")

    return fig


def generate_lines(fig, data):
    for plot_data in data:
        plot, markers, label, color, style, visible = plot_data
        fig.add_trace(
            go.Scatter(
                x=plot[0],
                y=plot[1],
                mode=markers,
                name=label,
                showlegend=bool(label),
                marker_color=color,
                text=[str(i + 1) for i in range(len(plot[0]))],
                line=style.get("line"),
                marker=style.get("marker"),
                visible=None if visible else "legendonly",
                textposition=style.get("textposition"),
            )
        )
