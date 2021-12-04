import pandas as pd

db = pd.read_csv(r"adult.data.csv")
#LINK DO TESTE COM O RESULTADO: https://replit.com/@LuizSinx/boilerplate-demographic-data-analyzer-1#demographic_data_analyzer.py

def educationsalary(salary, educationhigh=True):
    education = db['education'].isin(['Bachelors', 'Masters', 'Doctorate']) \
        if educationhigh == True else ~db['education'].isin(['Bachelors', 'Masters', 'Doctorate'])

    salaryhigh_educationhigh = db['education'][(db['salary'] == f"{salary.upper()}") & (education)].count()

    return f"{salaryhigh_educationhigh / db['education'][education].count() * 100:.1f}"


# How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
race_count = db['race'].value_counts()

# What is the average age of men?
average_age_men = float(f"{db['age'][db['sex'] == 'Male'].mean():.1f}")

# What is the percentage of people who have a Bachelor's degree?
percentage_bachelors = float(f"{(db['education'].value_counts('Bachelors') * 100)['Bachelors']:.1f}")

# What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
# What percentage of people without advanced education make more than 50K?

# with and without `Bachelors`, `Masters`, or `Doctorate`
higher_education = db['education'][db['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()

lower_education = db['education'][~db['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].count()

# percentage with salary >50K
higher_education_rich = float(educationsalary('>50k'))
lower_education_rich = float(educationsalary('>50k', educationhigh=False))

# What is the minimum number of hours a person works per week (hours-per-week feature)?
min_work_hours = db['hours-per-week'].min()

# What percentage of the people who work the minimum number of hours per week have a salary of >50K?
num_min_workers = db['salary'][db['hours-per-week'] == db['hours-per-week'].min()].count()

rich_percentage = float(
    db['salary'][db['hours-per-week'] == db['hours-per-week'].min() & (db['salary'] == ">50K")].count() / db['salary'][
        db['hours-per-week'] == db['hours-per-week'].min()].count() * 100)

# What country has the highest percentage of people that earn >50K?
resultado = (db['native-country'][db['salary'] == '>50K'].value_counts() / db[
    'native-country'].value_counts() * 100).sort_values(ascending=False)

highest_earning_country = resultado.index[0]
highest_earning_country_percentage = float(f'{resultado[0]:.1f}')

# Identify the most popular occupation for those who earn >50K in India.
top_IN_occupation = \
(db['occupation'][(db['native-country'] == 'India') & (db['salary'] == ">50K")].value_counts()).index[0]




