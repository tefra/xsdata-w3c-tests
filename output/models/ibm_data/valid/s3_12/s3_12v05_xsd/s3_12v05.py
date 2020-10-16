from dataclasses import dataclass, field
from typing import List, Optional, Union

__NAMESPACE__ = "http://xstest-tns"


@dataclass
class ChildTypeBase:
    """
    :ivar name:
    :ivar dob:
    """
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
    """
    :ivar name:
    :ivar dob:
    """
    class Meta:
        name = "childTypeDerived"

    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    dob: Optional[str] = field(
        default=None,
        metadata={
            "name": "DOB",
            "type": "Attribute",
        }
    )


@dataclass
class CtAlt1:
    """
    :ivar child:
    :ivar number_of_children:
    """
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
    """
    :ivar child:
    :ivar number_of_children:
    """
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
    """
    :ivar child:
    :ivar number_of_children:
    """
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
    """
    :ivar person:
    """
    class Meta:
        name = "root"
        namespace = "http://xstest-tns"

    person: List[Union[CtAlt1, CtAlt2, CtBase]] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "",
            "min_occurs": 1,
        }
    )
