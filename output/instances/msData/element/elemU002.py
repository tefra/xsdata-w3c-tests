from output.models.ms_data.element.elem_u002_xsd.elem_u002 import Root


obj = Root(
    r=[
        "Chapter 1",
        "Chapter&#10;2",
        "Chapter&#10;2",
        "Chapter&#9;3",
    ]
)
