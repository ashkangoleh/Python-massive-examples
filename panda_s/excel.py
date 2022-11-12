import pandas as pd

# df = pd.read_excel('/external/test_proj/panda_s/file_example_XLS_1000.xls')
# print("==>> df: ", df)

df = pd.DataFrame({"name": ['Kelly', 'David', 'Mandy', "John"], "description": ["age: 12 gender:female hobbies: loves to read",
                  "age:16, gender:male, hobbies: play soccer", "age: 15, gender:female, hobbies: cooking", "18, male, reading"]})


print("==>> df: ", df)
