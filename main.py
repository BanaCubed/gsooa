from nicegui import ui
from typing import TypedDict


# region Setup
class State(TypedDict):
    running: bool
    seed: int


state: State = {
    "running": False,
    "seed": 0,
}
# endregion

# region Rendering
with ui.element("div").classes(
    "w-full h-full flex-col gap-4 flex items-center"
    " justify-center bg-gray-200 max-w-xl p-4 rounded-lg m-auto"
):
    with ui.element("h1").classes("text-2xl font-bold"):
        ui.label("gsooA")
    with ui.button(
        "Start",
        on_click=lambda: state.update({"running": True}),
        icon="play_arrow"
    ).bind_visibility_from(state, "running", value=False):
        pass
    ui.label(" ").bind_text_from(state, "running", backward=lambda x: "Yes" if x else "No")
# endregion

ui.run()
