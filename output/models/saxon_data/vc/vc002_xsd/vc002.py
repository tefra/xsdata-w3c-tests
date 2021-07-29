from dataclasses import dataclass, field


@dataclass
class Temp:
    class Meta:
        name = "temp"

    value: str = field(
        default="",
        metadata={
            "pattern": r"2008.*",
        }
    )
