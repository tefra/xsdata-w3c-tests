from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Beta:
    class Meta:
        name = "beta"

    other_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        }
    )
    w3_org_xml_1998_namespace_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )


@dataclass
class Doc:
    class Meta:
        name = "doc"

    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
        }
    )
    w3_org_xml_1998_namespace_attributes: Dict = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "http://www.w3.org/XML/1998/namespace",
        }
    )
    a: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
    b: Optional[Beta] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "",
            "required": True,
        }
    )
