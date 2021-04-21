import tkinter as tk


def round_rectangle(canvas_obj: tk.Canvas, paddingx, paddingy, rectangle_width, rectangle_height, radius=25, **kwargs):
    """
    :param canvas_obj:
    :param paddingx:
    :param paddingy:
    :param rectangle_width:
    :param rectangle_height:
    :param radius:
    :param kwargs:
    """
    points = [paddingx + radius, paddingy,
              paddingx + radius, paddingy,
              rectangle_width - radius, paddingy,
              rectangle_width - radius, paddingy,
              rectangle_width, paddingy,
              rectangle_width, paddingy + radius,
              rectangle_width, paddingy + radius,
              rectangle_width, rectangle_height - radius,
              rectangle_width, rectangle_height - radius,
              rectangle_width, rectangle_height,
              rectangle_width - radius, rectangle_height,
              rectangle_width - radius, rectangle_height,
              paddingx + radius, rectangle_height,
              paddingx + radius, rectangle_height,
              paddingx, rectangle_height,
              paddingx, rectangle_height - radius,
              paddingx, rectangle_height - radius,
              paddingx, paddingy + radius,
              paddingx, paddingy + radius,
              paddingx, paddingy]

    return canvas_obj.create_polygon(points, **kwargs, smooth=True)
