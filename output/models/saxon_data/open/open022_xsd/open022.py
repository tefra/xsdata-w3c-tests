from dataclasses import dataclass, field


@dataclass
class B:
    open_com_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://open.com/",
        },
    )


@dataclass
class R(B):
    pass


@dataclass
class Doc(R):
    class Meta:
        name = "doc"
