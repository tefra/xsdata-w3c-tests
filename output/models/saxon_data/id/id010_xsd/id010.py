from dataclasses import dataclass, field


@dataclass
class Para:
    class Meta:
        name = "para"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    id: str = field(
        default="para001",
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    para: list[Para] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
