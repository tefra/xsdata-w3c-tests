from dataclasses import dataclass, field


@dataclass
class FooType:
    class Meta:
        name = "fooType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
    any_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##any",
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
