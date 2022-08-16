import numpy as np
import pandas as pd

loanstats = pd.DataFrame(pd.read_excel(
    r"C:\Users\win\Desktop\loan_stats.xlsx"))

member_grade = pd.DataFrame(pd.read_excel(
    r"C:\Users\win\Desktop\member_grade.xlsx"))

# loan_inner = pd.merge(member_grade, loanstats,  how='inner')

# loan_left = pd.merge(loanstats, member_grade,  how='left')

# loan_right = pd.merge(loanstats, member_grade, how='right')

loan_outer = pd.merge(loanstats, member_grade, how='outer')

print(loan_outer)
