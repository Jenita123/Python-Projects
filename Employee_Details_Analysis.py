#!/usr/bin/env python
# coding: utf-8

# # Analysis the Employee DATA
# 
# Do data analysis of employees data based on their historical data.

# In[24]:


import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split 
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import joblib


# In[2]:


df= pd.read_csv("Employee.csv")


# In[4]:


df.head()


# In[5]:


df.info


# In[6]:


df.shape


# In[7]:


df.describe()


# In[8]:


df.isna().sum()


# In[9]:


df.duplicated().sum()


# In[10]:


df[df.duplicated(keep=False)]


# In[11]:


sorted(df["JoiningYear"].unique())


# In[13]:


sorted(df['Gender'].unique())


# In[14]:


df["City"].unique()


# In[15]:


df["EverBenched"].unique()


# In[16]:


# EDA (Exploratory Data Analysis)
df["LeaveOrNot"].value_counts()


# In[18]:


df['EverBenched'].value_counts()


# In[19]:


df["LeaveOrNot"].value_counts().plot(kind='pie')


# In[20]:


sns.countplot(data=df, x='Education', hue="LeaveOrNot")


# In[21]:


sns.countplot(data=df, x='Gender', hue="LeaveOrNot")


# In[22]:


sns.countplot(data=df, x='City', hue="LeaveOrNot")


# In[23]:


sns.set_style('whitegrid')
sns.countplot(y='Age',data=df, hue='LeaveOrNot')


# # Modeling

# In[25]:


le=LabelEncoder()
df["Education"]= le.fit_transform(df["Education"])
df["City"]=le.fit_transform(df["City"])
df["Gender"]=le.fit_transform(df["Gender"])
df["EverBenched"]=le.fit_transform(df["EverBenched"])


# In[26]:


X= df.drop(columns='LeaveOrNot')
y=df['LeaveOrNot'] 

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1234, test_size=0.25) 


# In[27]:


X_train


# In[28]:


y_train


# In[29]:


model = KNeighborsClassifier(n_neighbors=5)


# In[30]:


model.fit(X_train, y_train)


# In[31]:


y_pred = model.predict(X_test)


# In[32]:


conf_matrix = confusion_matrix(y_test, y_pred)
print(conf_matrix)


# In[33]:


accuracy = accuracy_score(y_test, y_pred)
print(accuracy)


# In[34]:


classification_rep = classification_report(y_test, y_pred)
print(classification_rep)


# In[35]:


import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


# In[36]:


X, y = make_classification(random_state=0)
X_train, X_test, y_train, y_test = train_test_split(
         X, y, random_state=0)
clf = SVC(random_state=0)
clf.fit(X_train, y_train)
SVC(random_state=0)
y_pred = clf.predict(X_test)
ConfusionMatrixDisplay.from_predictions(y_test, y_pred)
plt.show()


# # Conclsuion
# 1. Male employees are leaving more as compared to female employees.
# 2. Bachelors males are leaving more as compared to other degree's employees.
# 3. Branch Bangolore employees are leaving more as compared to other city.
