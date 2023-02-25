from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://importedXSD"


@dataclass
class Any1:
    class Meta:
        name = "any1"

    local_element_or_bbb_or_ccc: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "wildcard": True,
                    "type": object,
                    "namespace": "##local",
                },
                {
                    "name": "bbb",
                    "type": object,
                    "namespace": "http://importedXSD",
                },
                {
                    "name": "ccc",
                    "type": object,
                    "namespace": "http://importedXSD",
                },
            ),
        }
    )


@dataclass
class Imp:
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
