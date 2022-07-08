import pandas as pd

extract_file ="C:\Psuedo D Drive\RAF Extracts Validation\HNET_payment_extract_110_risk_20220125080149_2021\HNET_payment_extract_110_risk_20220125080149_2021.txt"
df=pd.read_csv(extract_file,delimiter= '|')

# filename=str(service_year)+str(lob) + "Cohort All Data "+".csv"
# all_data.to_csv(filename,index=False)


print("Number of rows ",df.shape[0])
print("Number of  cols ",df.shape[1])
number_of_rows_list=["Number of rows ",df.shape[0]]
number_of_cols_list=["Number of cols ",df.shape[1]]

print(df['COZEVA ID'])