from dataclasses import dataclass, field


@dataclass
class Elt1:
    class Meta:
        name = "elt1"

    any_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )


@dataclass
class Elt2:
    class Meta:
        name = "elt2"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    elt1: list[Elt1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
