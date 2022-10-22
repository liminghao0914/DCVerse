import omni.ext
import omni.ui as ui
import omni.kit.commands

from .panels.overview import OverviewWindow
from .panels.airecommendation import AIRecommendationWindow
from .panels.trendreports import TrendReportsWindow
from .panels.datahalltwin import DataHallTwinWindow

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class MyExtension(omni.ext.IExt):
  def on_startup(self, ext_id):
    print("[ntu.cap.dcverse] MyExtension startup")

    # Note the "Window" part of the path that directs the new menu item to the "Window" menu.
    self._menu_path_overview = f"DCVerse/OPTIMISATION/Overview"
    self._window_overview = None
    self._menu_overview = omni.kit.ui.get_editor_menu().add_item(
        self._menu_path_overview, self._open_overview, True)

    self._menu_path_airecommendation = f"DCVerse/OPTIMISATION/AI Recommendation"
    self._window_airecommendation = None
    self._menu_airecommendation = omni.kit.ui.get_editor_menu().add_item(
        self._menu_path_airecommendation, self._open_airecommendation, True)

    self._menu_path_trendreports = f"DCVerse/OPTIMISATION/Trend Reports"
    self._window_trendreports = None
    self._menu_trendreports = omni.kit.ui.get_editor_menu().add_item(
        self._menu_path_trendreports, self._open_trendreports, True)

    self._menu_path_datahalltwin = f"DCVerse/SIMULATION/Data Hall Twin"
    self._window_datahalltwin = None
    self._menu_datahalltwin = omni.kit.ui.get_editor_menu().add_item(
        self._menu_path_datahalltwin, self._open_datahalltwin, True)

  def on_shutdown(self):
    print("[ntu.cap.dcverse] MyExtension shutdown")

    omni.kit.ui.get_editor_menu().remove_item(self._menu_overview)
    if self._window_overview is not None:
      self._window_overview.destroy()
      self._window_overview = None

    omni.kit.ui.get_editor_menu().remove_item(self._menu_airecommendation)
    if self._window_airecommendation is not None:
      self._window_airecommendation.destroy()
      self._window_airecommendation = None

    omni.kit.ui.get_editor_menu().remove_item(self._menu_trendreports)
    if self._window_trendreports is not None:
      self._window_trendreports.destroy()
      self._window_trendreports = None

    omni.kit.ui.get_editor_menu().remove_item(self._menu_datahalltwin)
    if self._window_datahalltwin is not None:
      self._window_datahalltwin.destroy()
      self._window_datahalltwin = None

  def _open_overview(self, menu, toggled):
    """Handles showing and hiding the window from the 'Windows' menu."""
    if toggled:
      if self._window_overview is None:
        self._window_overview = OverviewWindow("Overview", self._menu_path_overview)
      else:
        self._window_overview.show()
    else:
      if self._window_overview is not None:
        self._window_overview.hide()

  def _open_airecommendation(self, menu, toggled):
    """Handles showing and hiding the window from the 'Windows' menu."""
    if toggled:
      if self._window_airecommendation is None:
        self._window_airecommendation = AIRecommendationWindow(
            "AI Recommendation", self._menu_path_airecommendation)
      else:
        self._window_airecommendation.show()
    else:
      if self._window_airecommendation is not None:
        self._window_airecommendation.hide()

  def _open_trendreports(self, menu, toggled):
    """Handles showing and hiding the window from the 'Windows' menu."""
    if toggled:
      if self._window_trendreports is None:
        self._window_trendreports = TrendReportsWindow("Trend Reports", self._menu_path_trendreports)
      else:
        self._window_trendreports.show()
    else:
      if self._window_trendreports is not None:
        self._window_trendreports.hide()

  def _open_datahalltwin(self, menu, toggled):
    """Handles showing and hiding the window from the 'Windows' menu."""
    if toggled:
      if self._window_datahalltwin is None:
        self._window_datahalltwin = DataHallTwinWindow("Data Hall Twin", self._menu_path_datahalltwin)
      else:
        self._window_datahalltwin.show()
    else:
      if self._window_datahalltwin is not None:
        self._window_datahalltwin.hide()