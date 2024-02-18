from dataclasses import dataclass, field


@dataclass
class MyType:
    class Meta:
        name = "myType"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class FooType(MyType):
    class Meta:
        name = "fooType"

    value: str = field(
        init=False,
        default="CA",
        metadata={
            "required": True,
        },
    )


@dataclass
class Root(FooType):
    class Meta:
        name = "root"
