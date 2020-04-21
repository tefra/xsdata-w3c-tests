from dataclasses import dataclass, field
from lxml.etree import QName
from typing import Dict


@dataclass
class B:
    """
    :ivar any_attributes:
    """
    any_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="##any"
        )
    )


@dataclass
class R(B):
    """
    :ivar eve_com_attributes:
    """
    eve_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://eve.com/"
        )
    )


@dataclass
class Eden(R):
    class Meta:
        name = "eden"
