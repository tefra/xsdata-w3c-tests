from dataclasses import dataclass, field
from typing import List, Optional, Union
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
        }
    )
    dob: Optional[object] = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        }
    )


@dataclass
class ChildTypeDerived:
    class Meta:
        name = "childTypeDerived"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dob: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        }
    )


@dataclass
class CtAlt1:
    class Meta:
        name = "ctAlt1"

    child: List[ChildTypeDerived] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
    number_of_children: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfChildren",
            "type": "Attribute",
        }
    )


@dataclass
class CtAlt2:
    class Meta:
        name = "ctAlt2"

    child: List[ChildTypeBase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    number_of_children: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfChildren",
            "type": "Attribute",
        }
    )


@dataclass
class CtBase:
    class Meta:
        name = "ctBase"

    child: List[ChildTypeBase] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
        }
    )
    number_of_children: Optional[int] = field(
        default=None,
        metadata={
            "name": "numberOfChildren",
            "type": "Attribute",
        }
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    person: List[Union[CtBase, CtAlt1, CtAlt2]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
