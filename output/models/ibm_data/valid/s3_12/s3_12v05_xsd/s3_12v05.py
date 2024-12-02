from dataclasses import dataclass, field
from typing import Any, Optional, Union

from xsdata.models.datatype import XmlDate

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class ChildTypeBase:
    class Meta:
        name = "childTypeBase"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    dob: Optional[object] = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        },
    )


@dataclass
class ChildTypeDerived(ChildTypeBase):
    class Meta:
        name = "childTypeDerived"

    dob: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        },
    )


@dataclass
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
    number_of_children: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfChildren",
            "type": "Attribute",
        },
    )


@dataclass
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


@dataclass
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


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    person: list[Union[CtBase, CtAlt1, CtAlt2]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        },
    )
