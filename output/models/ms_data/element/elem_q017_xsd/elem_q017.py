from dataclasses import dataclass, field


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: str = field(
        init=False,
        default="Hello"
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: str = field(
        init=False,
        default="Hello",
        metadata={
            "name": "fooTest",
            "type": "Element",
            "required": True,
        }
    )
