from dataclasses import dataclass, field

__NAMESPACE__ = "IdConstrDefs/fields"


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "IdConstrDefs/fields"

    number: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
