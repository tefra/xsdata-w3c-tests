from dataclasses import dataclass, field


@dataclass
class B:
    class Meta:
        name = "b"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class Ext(B):
    class Meta:
        name = "ext"


@dataclass
class Doc(Ext):
    class Meta:
        name = "doc"
