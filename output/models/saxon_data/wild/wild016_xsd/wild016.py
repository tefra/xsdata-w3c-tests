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
class E(B):
    """
    :ivar adam_com_attributes:
    """
    adam_com_attributes: Dict[QName, str] = field(
        default_factory=dict,
        metadata=dict(
            type="Attributes",
            namespace="http://abel.com/ http://adam.com/"
        )
    )


@dataclass
class Eden(E):
    class Meta:
        name = "eden"