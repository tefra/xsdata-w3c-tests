from dataclasses import dataclass, field


@dataclass
class Elem:
    class Meta:
        name = "elem"

    value: str = field(
        default="",
        metadata={
            "white_space": "collapse",
            "pattern": r"Hello world",
        },
    )
