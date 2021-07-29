from dataclasses import dataclass, field


@dataclass
class Value:
    class Meta:
        name = "value"

    value: str = field(
        default="",
        metadata={
            "required": True,
        }
    )
