from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class CInvalid:
    """
    :ivar any_element:
    """
    class Meta:
        name = "c_invalid"

    any_element: Optional[object] = field(
        default=None,
        metadata=dict(
            type="Wildcard",
            namespace="##any",
            required=True
        )
    )


@dataclass
class Cs:
    """
    :ivar value:
    :ivar a:
    """
    class Meta:
        name = "cs"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            min_length=1,
            max_length=4
        )
    )
    a: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )


@dataclass
class Fe1Valid:
    """
    :ivar value:
    """
    class Meta:
        name = "fe1_valid"
        namespace = "http://xsdtesting"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            min_length=1,
            max_length=4
        )
    )


@dataclass
class FeValid:
    """
    :ivar value:
    """
    class Meta:
        name = "fe_valid"
        namespace = "http://xsdtesting"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True,
            max_length=4
        )
    )


@dataclass
class Root:
    """
    :ivar fe1_valid:
    :ivar fe_valid:
    """
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    fe1_valid: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True,
            min_length=1,
            max_length=4
        )
    )
    fe_valid: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True,
            max_length=4
        )
    )


@dataclass
class Cc(Cs):
    """
    :ivar b:
    """
    class Meta:
        name = "cc"

    b: Optional[str] = field(
        default=None,
        metadata=dict(
            type="Attribute"
        )
    )
