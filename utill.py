import pandas as pd
df = pd.read_csv("/Users/junyuwu/Largest Company/components/babyNamesUSYOB-full.csv")

def get_all_sex():
    bysex = df.groupby("Sex")[["Number"]].sum()
    return bysex

def get_male_top10():
    male_top10 = df[df["Sex"] == "M"].groupby("Name")[["Number"]].sum()
    male_top10.sort_values("Number",ascending=False, inplace = True)
    male_top10 = male_top10[:10]
    return male_top10

def get_female_top10():
    female_top10 = df[df["Sex"] == "F"].groupby("Name")[["Number"]].sum()
    female_top10.sort_values("Number",ascending=False, inplace = True)
    female_top10 = female_top10[:10]
    return female_top10

def get_19_sex():
    before_1900 = df[df["YearOfBirth"]<1900]
    bysex1900 = before_1900.groupby("Sex")[["Number"]].sum()
    return bysex1900

def get_19male_top10():
    before_1900 = df[df["YearOfBirth"]<1900]
    male_name = before_1900[before_1900["Sex"]=="M"].groupby("Name")[["Number"]].sum()
    male_name.sort_values("Number",ascending=False, inplace = True)
    male_name = male_name[:10]
    return male_name

def get_19female_top10():
    before_1900 = df[df["YearOfBirth"]<1900]
    female_name = before_1900[before_1900["Sex"]=="F"].groupby("Name")[["Number"]].sum()
    female_name.sort_values("Number",ascending=False, inplace = True)
    female_name = female_name[:10]
    return female_name

def get_50_sex():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_50 = df.query('1900 <= YearOfBirth < 1950')
    before_50 = before_50.groupby("Sex")[["Number"]].sum()
    return before_50

def get_50male_top10():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_50 = df.query('1900 <= YearOfBirth < 1950')
    male_50 = before_50[before_50["Sex"] == "M"].groupby("Name")[["Number"]].sum()
    male_50.sort_values("Number",ascending=False, inplace = True)
    male_50 = male_50[:10]
    return male_50

def get_50female_top10():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_50 = df.query('1900 <= YearOfBirth < 1950')
    female_50 = before_50[before_50["Sex"] == "F"].groupby("Name")[["Number"]].sum()
    female_50.sort_values("Number",ascending=False, inplace = True)
    female_50 = female_50[:10]
    return female_50

def get_00_sex():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_00 = df.query('1950 <= YearOfBirth < 2000')
    before_00 = before_00.groupby("Sex")[["Number"]].sum()
    return before_00

def get_00male_top10():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_00 = df.query('1950 <= YearOfBirth < 2000')
    male_00 = before_00[before_00["Sex"] == "M"].groupby("Name")[["Number"]].sum()
    male_00.sort_values("Number",ascending=False, inplace = True)
    male_00 = male_00[:10]
    return male_00

def get_00female_top10():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_00 = df.query('1950 <= YearOfBirth < 2000')
    female_00 = before_00[before_00["Sex"] == "F"].groupby("Name")[["Number"]].sum()
    female_00.sort_values("Number",ascending=False, inplace = True)
    female_00 = female_00[:10]
    return female_00

def get_15_sex():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_15 = df.query('2000 <= YearOfBirth < 2015')
    before_15 = before_15.groupby("Sex")[["Number"]].sum()
    return before_15

def get_15male_top10():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_15 = df.query('2000 <= YearOfBirth < 2015')
    male_15 = before_15[before_15["Sex"] == "M"].groupby("Name")[["Number"]].sum()
    male_15.sort_values("Number",ascending=False, inplace = True)
    male_15 = male_15[:10]
    return male_15

def get_15female_top10():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_15 = df.query('2000 <= YearOfBirth < 2015')
    female_15 = before_15[before_15["Sex"] == "F"].groupby("Name")[["Number"]].sum()
    female_15.sort_values("Number",ascending=False, inplace = True)
    female_15 = female_15[:10]
    return female_15

def get_malelist():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_15 = df.query('2000 <= YearOfBirth < 2015')
    male_15 = before_15[before_15["Sex"] == "M"].groupby("Name")[["Number"]].sum()
    male_15.sort_values("Number",ascending=False, inplace = True)
    male_15 = male_15[:10]
    list_male = sorted(list(set(male_15.index.tolist())))
    return list_male

def get_femalelist():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_15 = df.query('2000 <= YearOfBirth < 2015')
    female_15 = before_15[before_15["Sex"] == "F"].groupby("Name")[["Number"]].sum()
    female_15.sort_values("Number",ascending=False, inplace = True)
    female_15 = female_15[:10]
    list_female = sorted(list(set(female_15.index.tolist())))
    return list_female

def get_15male_bar():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_15 = df.query('2000 <= YearOfBirth < 2015')
    male_15 = before_15[before_15["Sex"] == "M"].groupby("Name")[["Number"]].sum()
    male_15.sort_values("Number",ascending=False, inplace = True)
    male_15 = male_15[:10]
    male_15.reset_index(inplace=True)
    return male_15

def get_15female_bar():
    df["YearOfBirth"] = df["YearOfBirth"].astype(int)
    before_15 = df.query('2000 <= YearOfBirth < 2015')
    female_15 = before_15[before_15["Sex"] == "F"].groupby("Name")[["Number"]].sum()
    female_15.sort_values("Number",ascending=False, inplace = True)
    female_15 = female_15[:10]
    female_15.reset_index(inplace=True)
    return female_15