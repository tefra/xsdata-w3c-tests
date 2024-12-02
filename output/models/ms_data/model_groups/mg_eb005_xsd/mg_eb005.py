from dataclasses import dataclass, field


@dataclass
class Foo:
    class Meta:
        name = "foo"

    t1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
            "max_occurs": 8,
        },
    )


@dataclass
class Root(Foo):
    class Meta:
        name = "root"
