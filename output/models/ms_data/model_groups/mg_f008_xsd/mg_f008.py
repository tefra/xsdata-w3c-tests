from dataclasses import dataclass, field


@dataclass
class Foo:
    class Meta:
        name = "foo"

    w3_org_1999_xhtml_element: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "http://www.w3.org/1999/xhtml",
            "process_contents": "skip",
        },
    )


@dataclass
class Doc(Foo):
    class Meta:
        name = "doc"
