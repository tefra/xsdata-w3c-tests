from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://xstest-tns/ibms3_3_6_v04"


@dataclass
class Elem0:
    """
    :ivar value:
    """
    class Meta:
        name = "elem0"
        namespace = "http://xstest-tns/ibms3_3_6_v04"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Elem1:
    """
    :ivar value:
    """
    class Meta:
        name = "elem1"
        namespace = "http://xstest-tns/ibms3_3_6_v04"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Elem2:
    """
    :ivar value:
    """
    class Meta:
        name = "elem2"
        namespace = "http://xstest-tns/ibms3_3_6_v04"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class Elem3:
    """
    :ivar value:
    """
    class Meta:
        name = "elem3"
        namespace = "http://xstest-tns/ibms3_3_6_v04"

    value: Optional[str] = field(
        default=None,
        metadata={
            "required": True,
        }
    )


@dataclass
class RootType:
    """
    :ivar elem3:
    :ivar elem2:
    :ivar elem0:
    :ivar elem1:
    """
    class Meta:
        name = "rootType"

    elem3: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/ibms3_3_6_v04",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    elem2: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/ibms3_3_6_v04",
            "min_occurs": 1,
            "max_occurs": 2,
            "sequential": True,
        }
    )
    elem0: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/ibms3_3_6_v04",
            "required": True,
        }
    )
    elem1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://xstest-tns/ibms3_3_6_v04",
            "required": True,
        }
    )


@dataclass
class Root(RootType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/ibms3_3_6_v04"
