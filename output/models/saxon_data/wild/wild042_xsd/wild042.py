from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class Computer:
    """
    :ivar www_w3_org_2001_xmlschema_instance_attributes:
    """
    class Meta:
        name = "computer"

    www_w3_org_2001_xmlschema_instance_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://www.w3.org/2001/XMLSchema-instance",
            required=True
        )
    )
