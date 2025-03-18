from nicegui import ui
from state import unstableState


# region Rendering
with ui.element("div").classes(
    "w-full h-full flex-col gap-4 flex items-center"
    " justify-center bg-gray-200 max-w-xl p-4 rounded-lg m-auto"
):
    with ui.element("h1").classes("text-2xl font-bold"):
        ui.label("gsooA")
    ui.button(
        "Start",
        on_click=lambda: unstableState.update({"running": True}),
        icon="play_arrow"
    ).bind_visibility_from(unstableState, "running", value=False)
# endregion

ui.run()
