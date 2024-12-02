from dataclasses import dataclass, field


@dataclass
class N:
    class Meta:
        name = "n"

    value: str = field(default="")


@dataclass
class Outer:
    class Meta:
        name = "outer"

    n: list[N] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
