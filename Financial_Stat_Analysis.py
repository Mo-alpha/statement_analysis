import pandas as pd

col_names = ['2020', '2019',  '2018', '2017',  '2016', '2015']
bal_sheet = pd.read_excel("data\\Balance-Sheet.xlsx", index_col=0, header=None, names=col_names,)
income_statement = pd.read_excel("data\\Income-Statement.xlsx", index_col=0, header=None, names=col_names)
cash_flow_statement = pd.read_excel("data\\Statement-of-Cash-Flows.xlsx", index_col=0, header=None, names=col_names)

def create_excel_file(file_name, outputfile_name, sh_name='Sheet1'):
	# print("\nCreating an excel file.....")
	writer = pd.ExcelWriter("results//" + outputfile_name,
                        engine='xlsxwriter',)

	file_name.to_excel(writer, sheet_name=sh_name, float_format="%0.2f")
	writer.close()

	# print("\nPlease check the excel file.")
	print(" ")

	return file_name

def create_excel_wsheets(file_name, outputfile_name, sh_name='Sheet1'):
	writer = pd.ExcelWriter(outputfile_name, engine='xlsxwriter')
	file_name.to_excel(writer, sheet_name=sh_name)

	writer.save()

def h_analysis(file_name):
	h_analysis_result = pd.DataFrame(file_name,)
	years = ['2020', '2019',  '2018', '2017',  '2016', '2015']

	for year in years:
		h_analysis_result[year] = (((file_name[year] / file_name['2015'])*100) )

	return h_analysis_result

def v_analysis(file_name):
	rev_names = ['Revenues', 'Net sales', 'Sales', 'Total sales']
	try:
		v_analysis_result = ((file_name.loc[:] / file_name.loc['Total assets'])*100)
	except KeyError:
		v_analysis_result = ((file_name.loc[:] / file_name.loc['Net sales'])*100)

	return v_analysis_result

def cash_ratio(file_name):
	data = [file_name.loc['Cash and cash equivalents'], file_name.loc['Current liabilities']]
	cash_ratio_output = pd.DataFrame(columns=file_name.columns, index=None, data=data)
	cash_ratio_output.loc['Cash ratio'] = (file_name.loc['Cash and cash equivalents'] / file_name.loc['Current liabilities'])

	return cash_ratio_output

def current_ratio(file_name):
	data = [file_name.loc['Current assets'], file_name.loc['Current liabilities']]
	current_ratio_output = pd.DataFrame(columns=file_name.columns, index=None, data=data)
	current_ratio_output.loc['Cash ratio'] = (file_name.loc['Current assets'] / file_name.loc['Current liabilities'])

	return current_ratio_output

def quick_ratio(file_name):
	data = [file_name.loc['Current assets'], file_name.loc['Inventories'], file_name.loc['Current liabilities']]
	quick_ratio_output = pd.DataFrame(columns=file_name.columns, index=None, data=data)
	quick_ratio_output.loc['Quick ratio'] = ((file_name.loc['Current assets']-file_name.loc['Inventories']) / file_name.loc['Current liabilities'])

	return quick_ratio_output

def liabilities_asset_ratio(file_name):
	data = [file_name.loc['Total liabilities'], file_name.loc['Total assets']]
	liabilities_asset_ratio_output = pd.DataFrame(columns=file_name.columns, index=None, data=data)
	liabilities_asset_ratio_output.loc['Liabilities to assets ratio'] = (file_name.loc['Total liabilities'] / file_name.loc['Total assets'])

	return liabilities_asset_ratio_output

def liabilities_equity_ratio(file_name):
	data = [file_name.loc['Total liabilities'], file_name.loc['Total assets']]
	liabilities_equity_ratio_output = pd.DataFrame(columns=file_name.columns, index=None, data=data)
	liabilities_equity_ratio_output.loc['Liabilities to assets ratio'] = (file_name.loc['Total liabilities'] / file_name.loc['Total assets'])

	return liabilities_equity_ratio_output

def ltdb_eq_ratio(file_name):
	data = [file_name.loc['Non-current portion of term debt'], file_name.loc['Shareholders’ equity']]
	ltdb_eq_ratio_output = pd.DataFrame(columns=file_name.columns, index=None, data=data)
	ltdb_eq_ratio_output.loc['Long term debt to long term capital ratio'] = (file_name.loc['Non-current portion of term debt'] / file_name.loc['Shareholders’ equity'])

	return ltdb_eq_ratio_output

def int_coverage_ratio(file_name):
	data = [file_name.loc[''], file_name.loc[''], file_name.loc[''], file_name.loc[''], file_name.loc['']]
	int_coverage_ratio_output = pd.DataFrame(columns=file_name.columns, index=None, data=data)
	int_coverage_ratio_output.loc['Interest coverage ratio'] = (file_name.loc[''] / file_name.loc[''])

	return int_coverage_ratio_output

def life_cycle_analysis(file_name):
	data = [file_name.loc['Net income'], file_name.loc['Cash generated by operating activities'],
	file_name.loc['Cash (used in) generated by investing activities'],
	file_name.loc['Cash used in financing activities']]
	lca_output = pd.DataFrame(columns=file_name.columns, index=None, data=data)
	lca_output['Average'] = ((lca_output['2020'] + lca_output['2019'] + lca_output['2018'] + lca_output['2017'] + lca_output['2016'] + lca_output['2015'])/
	(len(lca_output.columns)))
	# lca_output.plot()

	return lca_output

# create_excel_file(int_coverage_ratio(bal_sheet), "int_coverage_ratio.xlsx")

create_excel_file(v_analysis(bal_sheet), "v_analysis_balance_sheet.xlsx")
create_excel_file(v_analysis(income_statement), "v_analysis_income_statement.xlsx")
create_excel_file(h_analysis(bal_sheet), "h_analysis_balance_sheet.xlsx")
create_excel_file(h_analysis(income_statement), "h_analysis_income_statement.xlsx")
create_excel_file(cash_ratio(bal_sheet), "cash_ratio.xlsx")
create_excel_file(current_ratio(bal_sheet), "current_ratio.xlsx")
create_excel_file (quick_ratio(bal_sheet), "quick_ratio.xlsx")
create_excel_file(liabilities_asset_ratio(bal_sheet), "liabilities_asset_ratio.xlsx")
create_excel_file(liabilities_equity_ratio(bal_sheet), "liabilities_equity_ratio.xlsx")
create_excel_file(ltdb_eq_ratio(bal_sheet), "ltdb_eq_ratio.xlsx")
create_excel_file(life_cycle_analysis(cash_flow_statement), "life_cycle_analysis.xlsx")


print("\nDone.")
