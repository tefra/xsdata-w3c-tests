from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class ComplexfooType:
    class Meta:
        name = "complexfooType"

    comp_foo: bool = field(
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )


@dataclass(kw_only=True)
class SimpleTest:
    class Meta:
        name = "simpleTest"

    value: bool = field()


@dataclass(kw_only=True)
class ComplexTest(ComplexfooType):
    class Meta:
        name = "complexTest"


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    complex_test: ComplexTest = field(
        metadata={
            "name": "complexTest",
            "type": "Element",
        }
    )
    simple_test: SimpleTest = field(
        metadata={
            "name": "simpleTest",
            "type": "Element",
        }
    )
