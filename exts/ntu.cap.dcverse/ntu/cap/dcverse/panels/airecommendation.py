from ctypes import alignment
from logging.config import IDENTIFIER
import omni.kit.ui
import omni.ui as ui
from omni.ui import color as cl
import math

from .utils.model import Model
from .utils.delegate import Delegate
from .style import main_window_style


class AIRecommendationWindow(ui.Window):
  def __init__(self, title, menu_path):
    super().__init__(title, width=640, height=800)
    self._menu_path = menu_path
    self.frame.style = main_window_style
    self.actionlist = range(20)
    self.set_visibility_changed_fn(self._on_visibility_changed)
    self._build_ui()

  def on_shutdown(self):
    self._win = None

  def show(self):
    self.visible = True
    self.focus()

  def hide(self):
    self.visible = False

  def _build_ui(self):
    with self.frame:
      with ui.VStack():
        with ui.HStack(height=30, alignment=ui.Alignment.CENTER):
          # label = ui.Label("AI Recommendation", width=200, height=20)
          button_schedule = ui.Button("Schedule", height=20)
          button_recommend = ui.Button("Recommend Now", height=20)
        self._rtos_ui()
        with ui.VStack(height=300):
          with ui.HStack():
            self._actionlist_ui(self.actionlist)
            self._actiondetails_ui()
        self._potential_improvement_ui()

  def _rtos_ui(self):
    with ui.VStack(height=100):
      label_settings = ui.Label("Real-time Operation Settings", height=20)
      scrolling_serverlist = ui.ScrollingFrame(
          height=80, horizontal_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_OFF, vertical_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_ON)
      with scrolling_serverlist:
        with ui.VStack(height=0):
          for i in range(10):
            with ui.CollapsableFrame(f"CHWCAHU-{i+1}", collapsed=True, height=0):
              with ui.VStack(height=0):
                with ui.HStack(height=20):
                  ui.Label("Supply Temp", width=200, height=20)
                  ui.Label("14.92", width=100, height=20)
                with ui.HStack(height=20):
                  ui.Label("Return Temp", width=200, height=20)
                  ui.Label("22.94", height=20)
                with ui.HStack(height=20):
                  ui.Label("Flow Rate", width=200, height=20)
                  ui.Label("12379.17", height=20)

  def _actionlist_ui(self, actionlist):
    self._actionlist_items = []
    with ui.VStack(height=300):
      ui.Label("AI-recommended Actions", height=20)
      with ui.ZStack(height=40):
        ui.Rectangle(width=300, height=40, name="actionlist_header")
        with ui.HStack(height=40):
          # sheet header
          ui.Label("Time", width=100)
          ui.Label("Status", width=100)
          ui.Label("Category", width=100)
      scrolling_actionlist = ui.ScrollingFrame(
          horizontal_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_OFF, vertical_scrollbar_policy=ui.ScrollBarPolicy.SCROLLBAR_ALWAYS_ON)
      with scrolling_actionlist:
        with ui.VStack():
          # demo data
          for i, item in enumerate(actionlist):
            self._actionlist_additem(i)

  def _reset_actionlist_items(self):
    for i, item in enumerate(self._actionlist_items):
      self._actionlist_items[i].name = "actionlist_item_default"

  def _actionlist_additem(self, name):
    def _extend_actionlist(x, y, button, modifiers):
      self._reset_actionlist_items()
      self._action_details.text = f"Action Details{name}"
      actionlist_item_rect.name = "actionlist_item_seleted"
    with ui.ZStack():
      actionlist_item_rect = ui.Rectangle(width=300, height=40, name=f"actionlist_item_default")
      with ui.HStack(height=40, mouse_pressed_fn=_extend_actionlist, name=f"action{name}", tooltip="Click to view details"):
        ui.Label(str(22-name)+":00 Oct 18", width=100)
        ui.Label("Pending", width=100)
        ui.Label("Periodic", width=100)
      self._actionlist_items.append(actionlist_item_rect)

  def _actiondetails_ui(self):
    with ui.VStack(height=300):
      with ui.VStack(width=200):
        ui.Label("Action Details", height=20)
      with ui.HStack(height=30):
        ui.Button("Export")
        ui.Button("Deploy")
      with ui.ZStack():
        ui.Rectangle(name="actiondetails")
        self._action_details = ui.Label("No action selected",name="actiondetails")

  def _potential_improvement_ui(self):
    with ui.VStack(height=300):
      with ui.VStack(width=200):
        ui.Label("Potential Improvement", height=20)
      with ui.HStack(spacing=10):
        with ui.ZStack():
          ui.Rectangle(name="potentialimprovement")
        with ui.ZStack():
          ui.Rectangle(name="potentialimprovement")
        with ui.ZStack():
          ui.Rectangle(name="potentialimprovement")

  def _on_visibility_changed(self, visible):
    omni.kit.ui.get_editor_menu().set_value(self._menu_path, visible)

  # def _create_tooltip(self):
  #   with ui.VStack(width=200, style=tooltip_style):
  #     with ui.HStack(height=30):
  #       ui.Button("Export")
  #       ui.Button("Deploy")
  #     with ui.VStack(width=200, style=tooltip_style):
  #       ui.Label("Action Details", height=20)
  #       for i in range(5):
  #         ui.Label(f"{i+1}.Action Details", height=20)
