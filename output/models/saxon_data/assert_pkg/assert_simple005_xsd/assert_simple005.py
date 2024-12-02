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


@dataclass
class Outer:
    class Meta:
        name = "outer"

    list_value: list[List] = field(
        default_factory=list,
        metadata={
            "name": "list",
            "type": "Element",
            "min_occurs": 1,
        },
    )
