from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: list[float] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: float = field()


@dataclass(kw_only=True)
class ComplexTest(ComplexfooType):
    class Meta:
        name = "complexTest"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    complex_test: list[ComplexTest] = field(
        default_factory=list,
        metadata={
            "name": "complexTest",
            "type": "Element",
            "min_occurs": 1,
        },
    )
    simple_test: list[SimpleTest] = field(
        default_factory=list,
        metadata={
            "name": "simpleTest",
            "type": "Element",
            "min_occurs": 1,
        },
    )
