from output.models.ms_data.model_groups.mg_q007_xsd.mg_q007 import Bar
from output.models.ms_data.model_groups.mg_q007_xsd.mg_q007 import Doc


obj = Doc(
    e1="yo",
    e2=Bar(
        e1="This is different"
    )
)
