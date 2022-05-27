# coords = [
#     [3562, 2231], [3644, 2174], [3635, 2079],
#     [3545, 2040], [3462, 2096], [3471, 2191], [3562, 2231]
# ]
#
# x, y = 0.3562, 0.2231
# x1, y1 = 0.3644, 0.2174
# x2, y2 = 0.3635, 0.2079
# x3, y3 = 0.3545, 0.2040
# x4, y4 = 0.3462, 0.2096
# x5, y5 = 0.3471, 0.2191


def draw_tile(coords, file_name, cairo):
    with cairo.SVGSurface(f"/home/eugene/Documents/tiles/{file_name}.svg", 400, 400) as surface:
        context = cairo.Context(surface)
        context.scale(400, 400)
        context.set_line_width(0.005)
        for coord in coords:
            draw_polygon(coord, context)


def draw_polygon(coords, context):
    context.move_to(coords[0][0]/10000, coords[0][1]/10000)
    final_coord = None
    for coord in coords:
        if not final_coord:
            final_coord = coord
            continue
        context.line_to(coord[0]/10000, coord[1]/10000)
    context.line_to(final_coord[0]/10000, final_coord[1]/10000)
    context.stroke()
