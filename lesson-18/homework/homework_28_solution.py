
import pandas as pd

# -------- Homework 2: StackOverflow Data --------
df = pd.read_csv('task/stackoverflow_qa.csv')

# 1. Questions before 2014
q1 = df[pd.to_datetime(df['creationdate']) < '2014-01-01']

# 2. Score > 50
q2 = df[df['score'] > 50]

# 3. Score between 50 and 100
q3 = df[(df['score'] >= 50) & (df['score'] <= 100)]

# 4. Answered by Scott Boston
q4 = df[df['ans_name'] == 'Scott Boston']

# 5. Answered by specific users
users = ['Scott Boston', 'unutbu', 'Mike Pennington', 'Warren Weckesser', 'DSM']
q5 = df[df['ans_name'].isin(users)]

# 6. Questions created Mar–Oct 2014, answered by Unutbu, score < 5
df['creationdate'] = pd.to_datetime(df['creationdate'])
q6 = df[(df['creationdate'] >= '2014-03-01') & (df['creationdate'] <= '2014-10-31') &
        (df['ans_name'] == 'unutbu') & (df['score'] < 5)]

# 7. Score between 5–10 or viewcount > 10,000
q7 = df[((df['score'] >= 5) & (df['score'] <= 10)) | (df['viewcount'] > 10000)]

# 8. Not answered by Scott Boston
q8 = df[df['ans_name'] != 'Scott Boston']


# -------- Homework 3: Titanic Data --------
titanic_df = pd.read_csv('task/titanic.csv')

# 1. Female in Class 1 aged 20–30
t1 = titanic_df[(titanic_df['Sex'] == 'female') & (titanic_df['Pclass'] == 1) &
                (titanic_df['Age'].between(20, 30))]

# 2. Fare > 100
t2 = titanic_df[titanic_df['Fare'] > 100]

# 3. Survived & Alone (SibSp == 0 & Parch == 0)
t3 = titanic_df[(titanic_df['Survived'] == 1) & 
                (titanic_df['SibSp'] == 0) & (titanic_df['Parch'] == 0)]

# 4. Embarked 'C' & Fare > 50
t4 = titanic_df[(titanic_df['Embarked'] == 'C') & (titanic_df['Fare'] > 50)]

# 5. Had both SibSp and Parch > 0
t5 = titanic_df[(titanic_df['SibSp'] > 0) & (titanic_df['Parch'] > 0)]

# 6. Age <= 15 and didn't survive
t6 = titanic_df[(titanic_df['Age'] <= 15) & (titanic_df['Survived'] == 0)]

# 7. Known Cabin and Fare > 200
t7 = titanic_df[titanic_df['Cabin'].notna() & (titanic_df['Fare'] > 200)]

# 8. Odd PassengerId
t8 = titanic_df[titanic_df['PassengerId'] % 2 == 1]

# 9. Unique tickets
t9 = titanic_df[titanic_df.duplicated('Ticket') == False]

# 10. 'Miss' in Name and in Class 1
t10 = titanic_df[(titanic_df['Name'].str.contains('Miss')) & 
                 (titanic_df['Pclass'] == 1)]
