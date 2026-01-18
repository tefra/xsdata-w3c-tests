from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(kw_only=True)
class Base1:
    foo: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Base2:
    foo: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class Base3:
    foo: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    local_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##local",
        },
    )


@dataclass(kw_only=True)
class Derived1(Base1):
    foo: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Derived2(Base2):
    local_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    bar: None | object = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class Derived3(Base3):
    local_attributes: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Doc:
    class Meta:
        name = "doc"

    elem1: Derived1 = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    elem2: Derived2 = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    elem3: Derived3 = field(
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
