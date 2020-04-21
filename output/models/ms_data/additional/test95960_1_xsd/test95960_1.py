from dataclasses import dataclass, field


@dataclass
class Employees:
    """
    :ivar employee:
    :ivar dept:
    """
    employee: int = field(
        default=1,
        metadata=dict(
            name="Employee",
            type="Element",
            namespace="",
            required=True
        )
    )
    dept: int = field(
        default=9,
        metadata=dict(
            name="Dept",
            type="Attribute",
            required=True
        )
    )
