from dataclasses import dataclass, field


@dataclass
class Root:
    class Meta:
        name = "root"
        nillable = True

    e: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
