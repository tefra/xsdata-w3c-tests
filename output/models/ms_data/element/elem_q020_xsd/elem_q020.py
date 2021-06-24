from dataclasses import dataclass, field


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: str = field(
        default="Hello",
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: str = field(
        default="Hello",
        metadata={
            "name": "fooTest",
            "type": "Element",
        }
    )
