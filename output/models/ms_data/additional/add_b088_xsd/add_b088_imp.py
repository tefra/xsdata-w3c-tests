from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://importedXSD"


@dataclass
class Any1:
    """
    :ivar local_element:
    :ivar bbb:
    :ivar ccc:
    """
    class Meta:
        name = "any1"

    local_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##local",
        }
    )
    bbb: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://importedXSD",
        }
    )
    ccc: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://importedXSD",
        }
    )


@dataclass
class Imp:
    """
    :ivar att1:
    :ivar att2:
    """
    class Meta:
        name = "imp"
        namespace = "http://importedXSD"

    att1: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
    att2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class Doc1:
    """
    :ivar elem1:
    :ivar elem2:
    """
    class Meta:
        name = "doc1"
        namespace = "http://importedXSD"

    elem1: List[Any1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100,
        }
    )
    elem2: List[Any1] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 100,
        }
    )
