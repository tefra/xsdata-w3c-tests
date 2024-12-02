from dataclasses import dataclass, field


@dataclass
class B:
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        },
    )


@dataclass
class R(B):
    pass


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
