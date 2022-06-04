from prettytable import PrettyTable
res_table = PrettyTable()

res_table.add_rows(["R2 = ", result.rsquared,
                    "R2 adj. = ", result.rsquared_adj, 
                    "F-statistic = ", result.fvalue,
                    "Prob (F-statistic) = ", result.f_pvalue,
                    "Condition number = ", result.condition_number])

print(res_table)
