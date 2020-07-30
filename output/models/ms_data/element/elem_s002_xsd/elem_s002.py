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


@dataclass
class FrValid(Cs):
    class Meta:
        name = "fr_valid"
        namespace = "http://xsdtesting"


@dataclass
class Fr1Valid(Cc):
    class Meta:
        name = "fr1_valid"
        namespace = "http://xsdtesting"


@dataclass
class Root:
    """
    :ivar fr1_valid:
    :ivar fr_valid:
    """
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    fr1_valid: Optional[Fr1Valid] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
    fr_valid: Optional[FrValid] = field(
        default=None,
        metadata=dict(
            type="Element",
            required=True
        )
    )
