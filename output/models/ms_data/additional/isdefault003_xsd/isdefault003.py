from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    value: str = field(
        default="abc",
        metadata={
            "required": True,
        },
    )
