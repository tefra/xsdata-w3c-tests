from dataclasses import dataclass, field


@dataclass
class Employees:
    employee: int = field(
        default=1,
        metadata={
            "name": "Employee",
            "type": "Element",
            "namespace": "",
            "required": True,
        },
    )
    dept: int = field(
        default=9,
        metadata={
            "name": "Dept",
            "type": "Attribute",
        },
    )
