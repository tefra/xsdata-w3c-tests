from dataclasses import dataclass, field
from typing import List, Optional

__NAMESPACE__ = "a"


@dataclass
class DeptType:
    """
    :ivar deptno:
    :ivar dname:
    :ivar loc:
    :ivar id:
    """
    deptno: Optional[int] = field(
        default=None,
        metadata={
            "name": "Deptno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    dname: Optional[str] = field(
        default=None,
        metadata={
            "name": "Dname",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    loc: Optional[str] = field(
        default=None,
        metadata={
            "name": "Loc",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )


@dataclass
class EmployeeType:
    """
    :ivar empno:
    :ivar ename:
    :ivar sal:
    :ivar deptno:
    :ivar id:
    """
    empno: Optional[int] = field(
        default=None,
        metadata={
            "name": "Empno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    ename: Optional[str] = field(
        default=None,
        metadata={
            "name": "Ename",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    sal: Optional[float] = field(
        default=None,
        metadata={
            "name": "Sal",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    deptno: Optional[int] = field(
        default=None,
        metadata={
            "name": "Deptno",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )
    id: Optional[int] = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "a",
            "required": True,
        }
    )


@dataclass
class Root:
    """
    :ivar dept:
    :ivar employee:
    """
    class Meta:
        name = "root"
        namespace = "a"

    dept: List[DeptType] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    employee: List[EmployeeType] = field(
        default_factory=list,
        metadata={
            "name": "Employee",
            "type": "Element",
            "min_occurs": 1,
        }
    )
