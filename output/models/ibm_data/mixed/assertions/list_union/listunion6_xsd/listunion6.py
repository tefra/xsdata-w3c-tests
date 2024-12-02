from dataclasses import dataclass, field


@dataclass
class List:
    class Meta:
        name = "list"

    value: list[int] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
