from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(kw_only=True)
class Test:
    class Meta:
        name = "test"

    complex_att1: None | int = field(
        default=None,
        metadata={
            "name": "complexAtt1",
            "type": "Attribute",
        },
    )
    complex_att2: None | int = field(
        default=None,
        metadata={
            "name": "complexAtt2",
            "type": "Attribute",
        },
    )
    global_att1: None | int = field(
        default=None,
        metadata={
            "name": "globalAtt1",
            "type": "Attribute",
        },
    )
    item1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    item2: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    global_att2: None | int = field(
        default=None,
        metadata={
            "name": "globalAtt2",
            "type": "Attribute",
        },
    )
    foo1: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    foo2: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    global_att3: None | int = field(
        default=None,
        metadata={
            "name": "globalAtt3",
            "type": "Attribute",
        },
    )
    foo3: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    item3: None | int = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    complex_att3: None | int = field(
        default=None,
        metadata={
            "name": "complexAtt3",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    test: Test = field(
        metadata={
            "type": "Element",
        }
    )
