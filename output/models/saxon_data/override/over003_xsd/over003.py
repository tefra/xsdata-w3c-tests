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


@dataclass
class Para2:
    class Meta:
        name = "para2"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "pattern": r"[0-9]+-[0-9]+-[0-9]+",
        },
    )
