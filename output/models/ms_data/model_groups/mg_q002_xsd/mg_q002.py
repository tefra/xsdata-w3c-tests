from dataclasses import dataclass, field


@dataclass
class Foo:
    class Meta:
        name = "foo"

    e1: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 2,
            "max_occurs": 2,
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
