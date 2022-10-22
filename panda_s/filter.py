from functools import reduce
import pandas as pd


industry_skills = pd.read_csv(
    '/external/test_proj/panda_s/industry_skills.csv')

df = pd.DataFrame(industry_skills)
df = df[(df.skill_group_category == 'Soft Skills')
        & (df.industry_name == 'Oil & Energy')]
print("==>> df: ", df)

