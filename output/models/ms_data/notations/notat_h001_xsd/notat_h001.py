from dataclasses import dataclass, field


@dataclass
class Foo:
    class Meta:
        name = "foo"

    foo_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://foo",
        },
    )
