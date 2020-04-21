from dataclasses import dataclass, field
from typing import List, Optional

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
class N:
    """
    :ivar value:
    """
    class Meta:
        name = "n"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class N1:
    """
    :ivar value:
    """
    class Meta:
        name = "n1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class S:
    """
    :ivar value:
    """
    class Meta:
        name = "s"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class S1:
    """
    :ivar value:
    """
    class Meta:
        name = "s1"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class T:
    """
    :ivar s1:
    :ivar s:
    :ivar n:
    :ivar any_element:
    """
    s1: Optional[S1] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            required=True
        )
    )
    s: Optional[S] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            required=True
        )
    )
    n: Optional[N] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            required=True
        )
    )
    any_element: List[object] = field(
        default_factory=list,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )


@dataclass
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
