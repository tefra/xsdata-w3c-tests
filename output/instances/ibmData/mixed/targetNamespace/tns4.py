from output.models.ibm_data.mixed.target_namespace.tns4_xsd.tns4 import X
from output.models.ibm_data.mixed.target_namespace.tns4_xsd.tns4_imp import A
from output.models.ibm_data.mixed.target_namespace.tns4_xsd.tns4_imp import Y


obj = X(
    y=Y(
        a=[
            A(
                value=1
            ),
            A(
                value=2
            ),
        ]
    )
)
