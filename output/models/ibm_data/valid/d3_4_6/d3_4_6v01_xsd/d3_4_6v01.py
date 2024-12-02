from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass
class Nametest:
    ele: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "a",
            "min_occurs": 1,
        },
    )


@dataclass
class Root(Nametest):
    class Meta:
        name = "root"
        namespace = "a"
