from dataclasses import dataclass, field


@dataclass
class FooTest:
    class Meta:
        name = "fooTest"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"

    foo_test: list[FooTest] = field(
        default_factory=list,
        metadata={
            "name": "fooTest",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 2,
        },
    )
