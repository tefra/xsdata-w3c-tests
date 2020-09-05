from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional, Union

__NAMESPACE__ = "http://xsdtesting"


@dataclass
class Ct1:
    """
    :ivar att1:
    """
    class Meta:
        name = "CT1"

    att1: Optional[Union[bool, float, int, "Ct1.Value"]] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )

    class Value(Enum):
        """
        :cvar X:
        :cvar Y:
        """
        X = "x"
        Y = "y"


@dataclass
class Ct2:
    """
    :ivar att1:
    """
    class Meta:
        name = "CT2"

    att1: Optional[int] = field(
        default=None,
        metadata=dict(
            type="Attribute",
            namespace="http://xsdtesting"
        )
    )


@dataclass
class E1:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://xsdtesting"

    value: Optional[Union[bool, float, int, "E1.Value"]] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )

    class Value(Enum):
        """
        :cvar X:
        :cvar Y:
        """
        X = "x"
        Y = "y"


@dataclass
class E2:
    """
    :ivar value:
    """
    class Meta:
        namespace = "http://xsdtesting"

    value: Optional[int] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class E3(Ct2):
    class Meta:
        namespace = "http://xsdtesting"


@dataclass
class Root:
    """
    :ivar e2:
    :ivar e1:
    :ivar e3:
    """
    class Meta:
        name = "root"
        namespace = "http://xsdtesting"

    e2: List[E2] = field(
        default_factory=list,
        metadata=dict(
            name="E2",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e1: List[E1] = field(
        default_factory=list,
        metadata=dict(
            name="E1",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
    e3: List[E3] = field(
        default_factory=list,
        metadata=dict(
            name="E3",
            type="Element",
            min_occurs=0,
            max_occurs=9223372036854775807
        )
    )
