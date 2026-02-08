from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class FooTest:
    class Meta:
        name = "fooTest"

    my_elem_1: str = field(
        metadata={
            "name": "myElem_1",
            "type": "Element",
            "namespace": "",
        }
    )
    my_elem_2: int = field(
        metadata={
            "name": "myElem_2",
            "type": "Element",
            "namespace": "",
        }
    )
    my_attr: None | str = field(
        default=None,
        metadata={
            "name": "myAttr",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"

    foo_test: FooTest = field(
        metadata={
            "name": "fooTest",
            "type": "Element",
        }
    )
