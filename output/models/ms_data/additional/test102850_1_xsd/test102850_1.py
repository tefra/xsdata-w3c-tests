from dataclasses import dataclass, field


@dataclass
class Root:
    a: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 4,
            "sequence": 1,
        },
    )
    b: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 2,
            "sequence": 1,
        },
    )
