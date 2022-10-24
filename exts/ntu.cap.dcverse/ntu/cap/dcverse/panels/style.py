__all__ = ["main_window_style"]

from omni.ui import color as cl
from omni.ui import constant as fl
from omni.ui import url
import omni.kit.app
import omni.ui as ui
import pathlib

cl_actionlist_header_border_color=cl("#E0E0E0")
cl_actionlist_header_background_color=cl("#A8A8A800")
cl_attribute_hovered=cl("#575757")
cl_attribute_selected=cl("#9B9B9B")

main_window_style = {
    "Rectangle::actionlist_header":{
      "border_width": 1,
      "border_color": cl_actionlist_header_border_color,
      "background_color": cl_actionlist_header_background_color,
    },
    "Rectangle::actionlist_item_default:hovered": {
        "background_color": cl_attribute_hovered
    },
    "Rectangle::actionlist_item_seleted":{
        "background_color": cl_attribute_selected
    },
    "Rectangle::actiondetails":{
        "border_width": 1,
        "border_radius": 5,
        "border_color": cl_actionlist_header_border_color,
        "background_color": cl_actionlist_header_background_color,
    },
    "Label::actiondetails":{
        "alignment": ui.Alignment.LEFT_TOP,
        "margin": 5,
    },
    "Tooltip": {
        "border_width": 2,
        "border_radius": 5
    },
}
