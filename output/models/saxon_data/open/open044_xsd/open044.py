from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict, Optional
from output.models.saxon_data.open.open044_xsd.open044x import (
    Alpha,
)


@dataclass
class Beta:
    """
    :ivar other_attributes:
    :ivar w3_org_xml_1998_namespace_attributes:
    """
    class Meta:
        name = "beta"

    other_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##other"
        )
    )
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
    :ivar w3_org_xml_1998_namespace_attributes:
    :ivar a:
    :ivar b:
    """
    class Meta:
        name = "doc"

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
