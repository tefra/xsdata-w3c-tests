from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    number: list[int] = field(
        default_factory=list,
        metadata={
            "name": "Number",
            "type": "Element",
            "min_occurs": 1,
        },
    )
