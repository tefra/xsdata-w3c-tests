from dataclasses import dataclass, field

__NAMESPACE__ = "a"


@dataclass
class C:
    class Meta:
        name = "c"

    a: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
    b: list[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )


@dataclass
class Root(C):
    class Meta:
        name = "root"
        namespace = "a"
