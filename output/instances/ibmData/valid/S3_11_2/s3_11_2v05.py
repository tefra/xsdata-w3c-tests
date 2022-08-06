from output.models.ibm_data.valid.s3_11_2.s3_11_2v05_xsd.s3_11_2v05 import DeptType
from output.models.ibm_data.valid.s3_11_2.s3_11_2v05_xsd.s3_11_2v05 import EmployeeType
from output.models.ibm_data.valid.s3_11_2.s3_11_2v05_xsd.s3_11_2v05 import Root


obj = Root(
    dept=[
        DeptType(
            deptno=10,
            dname="Accounting",
            loc="Dallas"
        ),
        DeptType(
            deptno=20,
            dname="Production",
            loc="New York"
        ),
    ],
    employee=[
        EmployeeType(
            empno=1001,
            ename="Jag",
            sal=2500.0,
            deptno=10
        ),
        EmployeeType(
            empno=1002,
            ename="Win",
            sal=2600.0,
            deptno=20
        ),
    ]
)
