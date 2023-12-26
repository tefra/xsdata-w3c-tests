from dataclasses import dataclass, field


@dataclass
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        },
    )
