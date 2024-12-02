from dataclasses import dataclass, field


@dataclass
class C1:
    e1: list["C1"] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "max_occurs": 10,
        },
    )


@dataclass
class Foo(C1):
    class Meta:
        name = "foo"
