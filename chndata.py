import pandas as pd
import streamlit as st
import io

buffer = io.BytesIO()
print('Hello')

st.title("Leco TruSpec CHN-Data")
df_chn = pd.DataFrame
uploaded_file = st.file_uploader("Choose a CHN Leco TruSpec Analysisdata file")
if uploaded_file is not None:
  df = pd.read_csv(uploaded_file, sep='\t',
                   usecols=['Analysis Date', 'Name', 'Carbon %', 'Hydrogen %', 'Nitrogen %'])
  # Der Index auf Datetime gesetzt
  df.index = df['Analysis Date']
  # Umordnen der Spalten
  cols = ['Name', 'Carbon %', 'Hydrogen %', 'Nitrogen %']
  df = df[cols]



  df_chn = df.groupby(['Name'], as_index=False).mean()


  st.write(df_chn)

  with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
    # Write each dataframe to a different worksheet.
    df_chn.to_excel(writer, sheet_name='Sheet1')

    # Close the Pandas Excel writer and output the Excel file to the buffer
    writer.save()

    st.download_button(
      label="Download Excel worksheets",
      data=buffer,
      file_name="pandas_multiple.xlsx",
      mime="application/vnd.ms-excel"
    )






