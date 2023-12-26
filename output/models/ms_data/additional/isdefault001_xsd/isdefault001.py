from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"

    value: str = field(
        init=False,
        default="abc",
        metadata={
            "required": True,
        },
    )
