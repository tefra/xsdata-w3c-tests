from output.models.ms_data.wildcards.test328873_xsd.test328873 import Sub2


obj = Sub2(
    other_attributes={
        "att2": "bc",
        "{b}att3": "foo",
        "{x}att4": "val",
        "att": "a",
    },
    target_namespace_local_b_c_attributes={
        "{a}att1": "abc",
    }
)
