from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    value: str = field(
        default="",
        metadata={
            "required": True,
            "min_length": 5,
        }
    )
