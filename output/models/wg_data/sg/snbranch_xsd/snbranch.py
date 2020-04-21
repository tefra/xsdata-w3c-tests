from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "http://www.w3.org/XML/2008/xsdl-exx/ns1"


@dataclass
class A:
    """
    :ivar value:
    """
    class Meta:
        name = "a"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class B:
    """
    :ivar value:
    """
    class Meta:
        name = "b"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class C:
    """
    :ivar value:
    """
    class Meta:
        name = "c"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


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
    :ivar n1:
    :ivar n:
    :ivar any_element:
    :ivar a:
    :ivar b:
    :ivar c:
    """
    s1: List[S1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            min_occurs=1,
            max_occurs=2,
            sequential=True
        )
    )
    s: List[S] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            min_occurs=1,
            max_occurs=2,
            sequential=True
        )
    )
    n1: List[N1] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            min_occurs=1,
            max_occurs=2,
            sequential=True
        )
    )
    n: List[N] = field(
        default_factory=list,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            min_occurs=1,
            max_occurs=2,
            sequential=True
        )
    )
    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )
    a: Optional[A] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            required=True
        )
    )
    b: Optional[B] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            required=True
        )
    )
    c: Optional[C] = field(
        default=None,
        metadata=dict(
            type="Element",
            namespace="http://www.w3.org/XML/2008/xsdl-exx/ns1",
            required=True
        )
    )


@dataclass
class Test(T):
    class Meta:
        name = "test"
        namespace = "http://www.w3.org/XML/2008/xsdl-exx/ns1"
