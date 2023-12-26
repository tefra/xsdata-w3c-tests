from dataclasses import dataclass, field


@dataclass
class E:
    class Meta:
        name = "e"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[-+]*",
        },
    )
