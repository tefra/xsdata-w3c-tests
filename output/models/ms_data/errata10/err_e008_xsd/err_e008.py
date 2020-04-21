from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.tempuri.org"


@dataclass
class TestToken:
    """
    :ivar value:
    """
    class Meta:
        name = "testToken"
        namespace = "http://www.tempuri.org"

    value: Optional[str] = field(
        default=None,
        metadata=dict(
            required=True
        )
    )


@dataclass
class Root:
    """
    :ivar test_token:
    """
    class Meta:
        name = "root"
        namespace = "http://www.tempuri.org"

    test_token: Optional[TestToken] = field(
        default=None,
        metadata=dict(
            name="testToken",
            type="Element",
            required=True
        )
    )
