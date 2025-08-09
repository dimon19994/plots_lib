import base64
from io import BytesIO

from PIL import Image


def configure_bg_image(background_image):
    if not background_image:
        return []

    try:
        with Image.open(background_image) as img:
            width, height = img.size

            buffered = BytesIO()
            img.save(buffered, format="JPEG")

            img_bytes = buffered.getvalue()
            encoded_image = base64.b64encode(img_bytes).decode()

        return [
            {
                "source": f"data:image/png;base64,{encoded_image}",
                "xref": "x",
                "yref": "y",
                "x": -0.5,
                "y": height + 0.5,
                "sizex": width,
                "sizey": height,
                "sizing": "stretch",
                "opacity": 0.8,
                "layer": "below",
                "name": "background",
            }
        ]
    except Exception as e:
        print(f"Error loading background image: {e}")
        return []


def configure_title(text, title_data):
    title = {"text": text}
    if title_data:
        title.update(title_data)
    return title


def configure_xaxis(text, equal, xaxis_data):
    xaxis = {"title": {"text": text}}
    if equal:
        xaxis["scaleanchor"] = "y"
    if xaxis_data:
        xaxis.update(xaxis_data)
    return xaxis


def configure_yaxis(text, equal, yaxis_data):
    yaxis = {"title": {"text": text}}
    if equal:
        yaxis["scaleanchor"] = "x"
    if yaxis_data:
        yaxis.update(yaxis_data)
    return yaxis


def configure_font(font_data):
    font = {"size": 12, "color": "Black"}
    if font_data:
        font.update(font_data)
    return font


def configure_margins(margin_data, title):
    margins = {"l": 5, "r": 5, "t": 30 if title else 5, "b": 5}
    if margin_data:
        margins.update(margin_data)
    return margins


def configure_legend(legend_data):
    return legend_data if legend_data else {}
