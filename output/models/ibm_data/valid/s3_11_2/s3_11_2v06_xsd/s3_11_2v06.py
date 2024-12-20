from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "a"


@dataclass
class DeptType:
    deptno: Optional[int] = field(
        default=None,
        metadata={
            "name": "Deptno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    dname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dname",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    loc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Loc",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )


@dataclass
class EmployeeType:
    empno: Optional[int] = field(
        default=None,
        metadata={
            "name": "Empno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    ename: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ename",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    sal: Optional[float] = field(
        default=None,
        metadata={
            "name": "Sal",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    deptno: Optional[int] = field(
        default=None,
        metadata={
            "name": "Deptno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "a",
            "required": True,
        },
    )


@dataclass
class Root:
    class Meta:
        name = "root"
        namespace = "a"

    dept: list[DeptType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    employee: list[EmployeeType] = field(
        default_factory=list,
        metadata={
            "name": "Employee",
            "type": "Element",
            "min_occurs": 1,
        },
    )
