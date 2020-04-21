from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass
class E:
    """
    :ivar value:
    """
    class Meta:
        name = "e"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class E1:
    """
    :ivar any_element:
    """
    class Meta:
        name = "e1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class T:
    """
    :ivar www_w3_org_xml_2008_xsdl_exx_ns1_e1:
    :ivar e:
    :ivar e1:
    """
    www_w3_org_xml_2008_xsdl_exx_ns1_e1: Optional[E1] = field(
        default=None,
        metadata=dict(
            name="e1",
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1"
        )
    )
    e: Optional[E] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1"
        )
    )
    e1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1"
        )
    )


@dataclass
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
