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


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
