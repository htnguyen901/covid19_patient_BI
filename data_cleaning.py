import pandas as pd

  
df = pd.read_csv("D:/CODING/Projects/DataScience/Covid19_Patients/patient_information_vi_encoded.csv", encoding = 'utf-8', sep= ',')

# 1. patient info parsing

#create column status for patient's current status
df['status'] = df['Tình trạng'].apply(lambda x: 1 if x == 'Đang điều trị' else 0 if x == "Khỏi" else 2)

#create column to see each patient's gender
df['gender'] = df['Giới tính'].apply(lambda x: 1 if x == 'Nam' else 0 if x == "Nữ" else 2)

#create column to see patients in age range
df['age_range'] = df['Tuổi'].apply(lambda x: 1 if x <65 else 0)

#create column to see whether patient's nationality
df['nationality'] = df['Quốc tịch'].apply(lambda x: 1 if x == 'Việt Nam' else 0)

#create column for HCM number of patients
df['in_HCM'] = df['Địa điểm'].apply(lambda x: 1 if x == 'Hồ Chí Minh' else 0)
df["in_HCM"].value_counts()

df_out = df.drop(['Bệnh nhân'], axis = 1)

df_out.to_csv('D:/CODING/Projects/DataScience/Covid19_Patients/patient_information_vi_cleaned.csv', index = False)

pd.read_csv('patient_information_vi_cleaned.csv')