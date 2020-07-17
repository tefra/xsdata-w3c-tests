from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, List, Optional
from output.models.saxon_data.open.open045_xsd.open045x import (
    Alpha,
)


@dataclass
class Beta:
    """
    :ivar w3_org_xml_1998_namespace_attributes:
    """
    class Meta:
        name = "beta"

    w3_org_xml_1998_namespace_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )


@dataclass
class Doc:
    """
    :ivar content:
    :ivar w3_org_xml_1998_namespace_attributes:
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "doc"

    content: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            mixed=True,
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    w3_org_xml_1998_namespace_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://www.w3.org/XML/1998/namespace"
        )
    )
    a: Optional[Alpha] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
    b: Optional[Beta] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="",
            required=True
        )
    )
