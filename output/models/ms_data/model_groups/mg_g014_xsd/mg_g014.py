from dataclasses import dataclass, field


@dataclass
class Foo:
    class Meta:
        name = "foo"

    e1: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 999999999,
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
