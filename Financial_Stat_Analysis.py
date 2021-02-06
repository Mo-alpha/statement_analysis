import pandas as pd

def file_select():
	from tkinter import Tk
	from tkinter.filedialog import askopenfilename

	Tk().withdraw()
	filename = askopenfilename()
	return filename

inputfile1 = "data\\Balance-Sheet.xlsx"
inputfile2 = "data\\Income-Statement.xlsx"
inputfile3 = "data\\Statement-of-Cash-Flows.xlsx"

col_names = ['2020', '2019',  '2018', '2017',  '2016', '2015']
bal_sheet = pd.read_excel(inputfile1, index_col=0, header=None, names=col_names,)
income_statement = pd.read_excel(inputfile2, index_col=0, header=None, names=col_names)
cash_flow_statement = pd.read_excel(inputfile3, index_col=0, header=None, names=col_names)

avg_tot_ass = [1, 1, 1, 1, 1, 1] # average amounts are inserted here.
avg_commstock = [1, 1, 1, 1, 1, 1] # average amounts are inserted here.
avg_tot_lia = [1, 1, 1, 1, 1, 1] # average amounts are inserted here.
avg_tot_curr_lia = [1, 1, 1, 1, 1, 1] # average amounts are inserted here.
lt_sh_eq = [1,1,1,1,1,1] #long term shareholders equity is entered here.
w_avg_sh = [1, 1, 1, 1, 1, 1] # average amounts are inserted here.

print("Creating excel files.....")
print("Please wait.....")

number = '#,##0.00'
percentage = '0%'

def create_excel_file(file_name, outputfile_name, sh_name='Sheet1', format_name=number):
	writer = pd.ExcelWriter("results//" + outputfile_name,
                        engine='xlsxwriter',)
	file_name.to_excel(writer, sheet_name=sh_name,)
	workbook  = writer.book
	worksheet = writer.sheets[sh_name]
	format1 = workbook.add_format({'num_format': format_name})
	# formats = workbook.add_format()
	# formats.set_align('left')
	worksheet.set_column('A:A', 23, )
	worksheet.set_column('B:G', 10, format1,)
	worksheet.write(0, 0, 'Items',)
	# worksheet.set_column('A:C',5, format)
	writer.close()

	return file_name

def create_excel_wsheets(inputfile_name, sh_name='Sheet1'):
	from openpyxl import load_workbook

	path = r"results//liquidity_ratios.xlsx"

	book = load_workbook(path)
	writer = pd.ExcelWriter(path, engine = 'openpyxl')
	writer.book = book

	df = inputfile_name

	df.to_excel(writer, sheet_name = sh_name)
	writer.save()
	writer.close()

def h_analysis(file_name):
	h_analysis_result = pd.DataFrame(file_name,)

	for year in col_names:
		h_analysis_result[year] = (((file_name[year] / file_name['2015'])) )

	return h_analysis_result

def v_analysis(file_name):
	# rev_names = ['Revenues', 'Net sales', 'Sales', 'Total sales']
	try:
		v_analysis_result = ((file_name.loc[:] / file_name.loc['Total assets']))
	except KeyError:
		v_analysis_result = ((file_name.loc[:] / file_name.loc['Net sales']))

	return v_analysis_result

def cash_ratio(balance_sheet):
    data = [balance_sheet.loc['Cash and cash equivalents'], balance_sheet.loc['Current liabilities']]
    cash_ratio_output = pd.DataFrame(columns=balance_sheet.columns, index=None, data=data)
    cash_ratio_output.loc['Cash ratio'] = (balance_sheet.loc['Cash and cash equivalents'] / balance_sheet.loc['Current liabilities'])

    return cash_ratio_output

def current_ratio(balance_sheet):
    data = [balance_sheet.loc['Current assets'], balance_sheet.loc['Current liabilities']]
    current_ratio_output = pd.DataFrame(columns=balance_sheet.columns, index=None, data=data)
    current_ratio_output.loc['Cash ratio'] = (balance_sheet.loc['Current assets'] / balance_sheet.loc['Current liabilities'])

    return current_ratio_output

def quick_ratio(balance_sheet):
    data = [balance_sheet.loc['Current assets'], balance_sheet.loc['Inventories'], balance_sheet.loc['Current liabilities']]
    quick_ratio_output = pd.DataFrame(columns=balance_sheet.columns, index=None, data=data)
    quick_ratio_output.loc['Quick ratio'] = ((balance_sheet.loc['Current assets']-balance_sheet.loc['Inventories']) / balance_sheet.loc['Current liabilities'])

    return quick_ratio_output

def op_act_cl_ratio(balance_sheet, cash_flow):

	data = [cash_flow.loc['Cash generated by operating activities'], balance_sheet.loc['Current liabilities']]
	op_act_cl_ratio_output = pd.DataFrame(columns=bal_sheet.columns, index=None, data=data)
	op_act_cl_ratio_output.loc['Average total current liabilities'] = avg_tot_curr_lia
	op_act_cl_ratio_output.loc['Cash flow from opetation to current liabilities ratio'] = (op_act_cl_ratio_output.loc['Cash generated by operating activities']
		/ op_act_cl_ratio_output.loc['Average total current liabilities'])

	return op_act_cl_ratio_output

def liabilities_asset_ratio(balance_sheet):
    data = [balance_sheet.loc['Total liabilities'], balance_sheet.loc['Total assets']]
    liabilities_asset_ratio_output = pd.DataFrame(columns=balance_sheet.columns, index=None, data=data)
    liabilities_asset_ratio_output.loc['Liabilities to assets ratio'] = (balance_sheet.loc['Total liabilities'] / balance_sheet.loc['Total assets'])

    return liabilities_asset_ratio_output

def liabilities_equity_ratio(balance_sheet):
    data = [balance_sheet.loc['Total liabilities'], balance_sheet.loc['Total assets']]
    liabilities_equity_ratio_output = pd.DataFrame(columns=balance_sheet.columns, index=None, data=data)
    liabilities_equity_ratio_output.loc['Liabilities to assets ratio'] = (balance_sheet.loc['Total liabilities'] / balance_sheet.loc['Total assets'])

    return liabilities_equity_ratio_output

def ltdb_lteq_ratio(balance_sheet):
    data = [balance_sheet.loc['Non-current portion of term debt']]
    ltdb_lteq_ratio_output = pd.DataFrame(columns=balance_sheet.columns, index=None, data=data)
    ltdb_lteq_ratio_output.loc['Long term shareholders’ equity'] = lt_sh_eq
    ltdb_lteq_ratio_output.loc['Long term debt to long term capital ratio'] = (balance_sheet.loc['Non-current portion of term debt'] / ltdb_lteq_ratio_output.loc['Long term shareholders’ equity'])

    return ltdb_lteq_ratio_output

def ltdb_eq_ratio(balance_sheet):
    data = [balance_sheet.loc['Non-current portion of term debt'], balance_sheet.loc['Shareholders’ equity']]
    ltdb_eq_ratio_output = pd.DataFrame(columns=balance_sheet.columns, index=None, data=data)
    ltdb_eq_ratio_output.loc['Long term debt to long term capital ratio'] = (balance_sheet.loc['Non-current portion of term debt'] / balance_sheet.loc['Shareholders’ equity'])

    return ltdb_eq_ratio_output

def int_coverage_ratio(income_stat):
    data = [income_stat.loc['Net income'], income_stat.loc['Interest expense'], income_stat.loc['Provision for income taxes'],
    income_stat.loc['Interest expense'], income_stat.loc['Non controlling interests']]
    int_coverage_ratio_output = pd.DataFrame(columns=income_stat.columns, index=None, data=data)
    int_coverage_ratio_output.loc['Interest coverage ratio'] = (income_stat.loc[''] / income_stat.loc[''])

    return int_coverage_ratio_output

def life_cycle_analysis(cash_flow):
    data = [cash_flow.loc['Net income'], cash_flow.loc['Cash generated by operating activities'],
    cash_flow.loc['Cash (used in) generated by investing activities'],
    cash_flow.loc['Cash used in financing activities']]
    lca_output = pd.DataFrame(columns=cash_flow.columns, index=None, data=data)
    lca_output['Average'] = ((lca_output['2020'] + lca_output['2019'] + lca_output['2018'] + lca_output['2017'] + lca_output['2016'] + lca_output['2015'])/
    (len(lca_output.columns)))
    # lca_output.plot()

    return lca_output

def roa(income_stat):
	data = [income_stat.loc['Net income']]
	roa_output = pd.DataFrame(columns=income_stat.columns, index=None, data=data)
	roa_output.loc['Average total assets'] = avg_tot_ass
	roa_output.loc['Return on assets'] = (income_stat.loc['Net income'] / roa_output.loc['Average total assets'])

	return roa_output

def npr(income_stat):
	data = [income_stat.loc['Net income'], income_stat.loc['Net sales']]
	npr_output = pd.DataFrame(columns=income_stat.columns, index=None, data=data)
	npr_output.loc['Return on assets'] = (income_stat.loc['Net income'] / income_stat.loc['Net sales'])

	return npr_output

def atr(income_stat):
	data = [income_stat.loc['Net sales']]
	atr_output = pd.DataFrame(columns=income_stat.columns, index=None, data=data)
	atr_output.loc['Average total assets'] = avg_tot_ass
	atr_output.loc['Return on assets'] = (atr_output.loc['Net sales'] / atr_output.loc['Average total assets'])

	return atr_output

def roce(income_stat):
	data = [income_stat.loc['Net income']]
	roce_output = pd.DataFrame(columns=income_stat.columns, index=None, data=data)
	roce_output.loc['Average common stockholders equity'] = avg_commstock
	roce_output.loc['Return on assets'] = (income_stat.loc['Net income'] / roce_output.loc['Average common stockholders equity'])

	return roce_output

def op_avg_tot_liabities(balance_sheet, cash_flow):
	data = [balance_sheet.loc['Current liabilities'], cash_flow.loc['Cash generated by operating activities']]
	op_avg_tot_liabities_output = pd.DataFrame(columns=bal_sheet.columns, index=None, data=data)
	op_avg_tot_liabities_output.loc['Average total liabilities'] = avg_tot_lia
	op_avg_tot_liabities_output.loc['Cash flow from opetation to average total liabilities ratio'] = (op_avg_tot_liabities_output.loc['Cash generated by operating activities']
		/ op_avg_tot_liabities_output.loc['Average total liabilities'])

	return op_avg_tot_liabities_output

def op_cash_div(balance_sheet, cash_flow):
	data = [cash_flow.loc['Cash generated by operating activities'], balance_sheet.loc['Cash dividends']]
	op_cash_div_output = pd.DataFrame(columns=bal_sheet.columns, index=None, data=data)
	op_cash_div_output.loc['Operating cash flow to cash dividends'] = (cash_flow.loc['Cash generated by operating activities']
		/ balance_sheet.loc['Cash dividends'])

	return op_cash_div_output

def op_cash_pershare(balance_sheet, cash_flow):
	data = [cash_flow.loc['Cash generated by operating activities']]
	op_cash_pershare_output = pd.DataFrame(columns=balance_sheet.columns, index=None, data=data)
	op_cash_pershare_output.loc['Weighted average shares Outstanding'] = w_avg_sh
	op_cash_pershare_output.loc['Operating cash flow per share'] = (cash_flow.loc['Cash generated by operating activities']
		/ op_cash_pershare_output.loc['Weighted average shares Outstanding'])

	return op_cash_pershare_output


# create_excel_file(int_coverage_ratio(bal_sheet), "int_coverage_ratio.xlsx")

create_excel_file(v_analysis(bal_sheet), "v_analysis_balance_sheet.xlsx", format_name=percentage)
create_excel_file(v_analysis(income_statement), "v_analysis_income_statement.xlsx", format_name=percentage)
create_excel_file(h_analysis(bal_sheet), "h_analysis_balance_sheet.xlsx", format_name=percentage)
create_excel_file(h_analysis(income_statement), "h_analysis_income_statement.xlsx", format_name=percentage)
create_excel_file(cash_ratio(bal_sheet), "cash_ratio.xlsx")
create_excel_file(current_ratio(bal_sheet), "current_ratio.xlsx")
create_excel_file(quick_ratio(bal_sheet), "quick_ratio.xlsx")
create_excel_file(op_act_cl_ratio(bal_sheet, cash_flow_statement), "op_act_cl_ratio.xlsx")
create_excel_file(liabilities_asset_ratio(bal_sheet), "liabilities_asset_ratio.xlsx")
create_excel_file(liabilities_equity_ratio(bal_sheet), "liabilities_equity_ratio.xlsx")
create_excel_file(ltdb_eq_ratio(bal_sheet), "ltdb_eq_ratio.xlsx")
create_excel_file(life_cycle_analysis(cash_flow_statement), "life_cycle_analysis.xlsx")
create_excel_file(roa(income_statement), "roa.xlsx")
create_excel_file(npr(income_statement), "npr.xlsx")
create_excel_file(atr(income_statement), "atr.xlsx")
create_excel_file(roce(income_statement), "roce.xlsx")
create_excel_file(op_avg_tot_liabities(bal_sheet, cash_flow_statement), "op_avg_tot_liabities.xlsx")
create_excel_file(op_cash_div(bal_sheet, cash_flow_statement), "op_cash_div.xlsx")
create_excel_file(op_cash_pershare(bal_sheet, cash_flow_statement), "op_cash_pershare.xlsx")

print("\nDone.")
print("Please check the excel files.")
