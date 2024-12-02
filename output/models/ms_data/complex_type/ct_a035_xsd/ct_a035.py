from dataclasses import dataclass, field


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
