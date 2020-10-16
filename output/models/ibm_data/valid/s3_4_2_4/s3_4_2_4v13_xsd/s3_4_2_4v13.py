from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xstest-tns/schema11_S3_4_2_4"


@dataclass
class AttrGoupType:
    """
    :ivar default_attr1:
    :ivar default_attr2:
    """
    class Meta:
        name = "attrGoupType"

    default_attr1: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultAttr1",
            "type": "Attribute",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
            "required": True,
        }
    )
    default_attr2: Optional[bool] = field(
        default=None,
        metadata={
            "name": "defaultAttr2",
            "type": "Attribute",
            "namespace": "http://xstest-tns/schema11_S3_4_2_4",
            "required": True,
        }
    )


@dataclass
class Root(AttrGoupType):
    class Meta:
        name = "root"
        namespace = "http://xstest-tns/schema11_S3_4_2_4"
