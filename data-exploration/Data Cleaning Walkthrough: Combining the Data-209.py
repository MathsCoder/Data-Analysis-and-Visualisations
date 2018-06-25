## 3. Condensing the Class Size Data Set ##


class_size = data["class_size"]
class_size = class_size[class_size["GRADE "] == "09-12"]
class_size = class_size[class_size["PROGRAM TYPE"] == "GEN ED"]
print(class_size.head())

## 5. Computing Average Class Sizes ##

import numpy as np

class_size = (class_size.groupby("DBN") ).agg(np.mean )
#print(class_size)
class_size.reset_index("DBN")
data["class_size"] = class_size

## 7. Condensing the Demographics Data Set ##

data["demographics"] = data["demographics"][data["demographics"]["schoolyear"] == 20112012]
print(data["demographics"].head() )

## 9. Condensing the Graduation Data Set ##

data["graduation"] = data["graduation"][data["graduation"]["Cohort"] == "2006"]
data["graduation"] = data["graduation"][data["graduation"]["Demographic"] == "Total Cohort"]

## 10. Converting AP Test Scores ##

cols = ['AP Test Takers ', 'Total Exams Taken', 'Number of Exams with scores 3 4 or 5']
for col in cols:
    data["ap_2010"][col] = pd.to_numeric(data["ap_2010"][col], errors="coerce")

    
print(data["ap_2010"].dtypes)

## 12. Performing the Left Joins ##

combined = data["sat_results"]
ap_2010 = data["ap_2010"]
combined = combined.merge(ap_2010, on="DBN", how="left")
graduation = data["graduation"]
combined = combined.merge(graduation, on="DBN", how="left" )
print(combined.head())
print(combined.shape)

## 13. Performing the Inner Joins ##


df_to_merge = ["class_size", "demographics", "survey", "hs_directory"]

for df in df_to_merge:
    combined = combined.merge(data[df], on="DBN", how="inner")
print(combined.head())
print(combined.shape)

## 15. Filling in Missing Values ##

combined = combined.fillna(combined.mean())
combined = combined.fillna(0)
print(combined.head())

## 16. Adding a School District Column for Mapping ##

def extract_2_char(string):
    char_2 = string[0:2]
    return char_2

combined["school_dist"] = combined["DBN"].apply(extract_2_char)
print(combined["school_dist"].head())
    