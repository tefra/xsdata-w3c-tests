from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://xstest-tns"


@dataclass(kw_only=True)
class ChildTypeBase:
    class Meta:
        name = "childTypeBase"

    name: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dob: None | object = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class ChildTypeDerived(ChildTypeBase):
    class Meta:
        name = "childTypeDerived"

    dob: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CtBase:
    class Meta:
        name = "ctBase"

    child: list[ChildTypeBase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        },
    )
    number_of_children: None | int = field(
        default=None,
        metadata={
            "name": "numberOfChildren",
            "type": "Attribute",
        },
    )


@dataclass(kw_only=True)
class CtAlt1(CtBase):
    class Meta:
        name = "ctAlt1"

    child: list[ChildTypeDerived] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )


@dataclass(kw_only=True)
class CtAlt2(CtBase):
    class Meta:
        name = "ctAlt2"

    child: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )


@dataclass(kw_only=True)
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    person: list[CtBase | CtAlt1 | CtAlt2] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
