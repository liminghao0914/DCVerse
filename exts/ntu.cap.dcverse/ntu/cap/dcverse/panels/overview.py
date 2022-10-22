import omni.kit.ui
import omni.ui as ui


class OverviewWindow(ui.Window):
    def __init__(self, title, menu_path):
        super().__init__(title, width=640, height=480)
        self._menu_path = menu_path
        self.set_visibility_changed_fn(self._on_visibility_changed)
        self._build_ui()
        self._count = 0

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
              label = ui.Label("")

              def on_click():
                self._count += 1
                label.text = f"count: {self._count}"
                omni.kit.commands.execute('CreatePrimWithDefaultXform',
                                          prim_type='Cube',
                                          attributes={'size': 100, 'extent': [(-50, -50, -50), (50, 50, 50)]})

              def on_reset():
                self._count = 0
                label.text = "empty"

              on_reset()

              with ui.HStack():
                ui.Button("Add", clicked_fn=on_click)
                ui.Button("Reset", clicked_fn=on_reset)

    def _on_visibility_changed(self, visible):
        omni.kit.ui.get_editor_menu().set_value(self._menu_path, visible)
