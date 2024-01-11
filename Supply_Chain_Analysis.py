#!/usr/bin/env python
# coding: utf-8

# # Supply Chain Analysis:
# The supply Chain is the network of production and logistics involved in producing and delivering goods to customers. And Supply Chain Analysis means analyzing various components of a Supply Chain to understand how to improve the effectiveness of the Supply Chain to create more value for customers.
# # Summary
# Supply Chain Analysis means analyzing various components of a Supply Chain to understand how to improve the effectiveness of the Supply Chain to create more value for customers.

# # What is supply chain analysis?
# Supply chain analysis is the process of evaluating every stage of a supply chain starting from the time the business acquires raw materials or supplies from its suppliers to the delivery of final products to the customers.
# 
# The purpose of the analysis is to determine which part of the supply chain can be improved or shortened to deliver the product more quickly and efficiently to the customers.

# # What are supply chain analytics and it's different types?
# Each of these supply chain analytics can increase the overall efficiency of business operations, which can lead to sizable cost savings.
# Descriptive Analytics focuses on understanding what happened in the past by analyzing historical data. It can provide insights on key performance metrics, such as inventory levels, lead times, and delivery performance. Descriptive analytics can help identify patterns and trends in past supply chain operations, allowing organizations to make informed decisions about future strategies.
# 
# Diagnostic Analytics goes beyond descriptive analytics by identifying the root causes of supply chain issues. By analyzing data from different sources, such as suppliers, logistics providers, and customers, organizations can identify the factors that contribute to delays, disruptions, or quality issues in their supply chain. This can help them take corrective actions to prevent similar problems from happening in the future.
# 
# Predictive Analytics uses statistical models and machine learning algorithms to forecast future supply chain events. By analyzing historical data, organizations can identify patterns and trends that can help predict demand, inventory levels, and delivery performance. This can help organizations optimize their supply chain operations, reduce costs, and improve customer satisfaction.
# 
# Prescriptive Analytics takes predictive analytics one step further by providing recommendations on how to optimize supply chain operations. By using optimization algorithms and simulations, prescriptive analytics can help organizations identify the best course of action to improve supply chain performance. This can help organizations make better decisions and improve their overall supply chain efficiency.

# # How to conduct supply chain analysis?
# 
# The above analytics should be used when conducting supply chain analysis. The basic steps of an analysis are:
# 
# Define your objectives.
# Research the market.
# Conduct in-depth supplier analysis.
# Identify key market indicators
# Pull together your findings and outline final suggestions - I'd recommend taking a look at using SharpCloud as a visual presentation tool.

# # DataSet:
# Here is a dataset we collected from a Fashion and Beauty startup. The dataset is based on the supply chain of Makeup products. Below are all the features in the dataset:
# 
# Product Type
# SKU
# Price
# Availability
# Number of products sold
# Revenue generated
# Customer demographics
# Stock levels
# Lead times
# Order quantities
# Shipping times
# Shipping carriers
# Shipping costs
# Supplier name
# Location
# Lead time
# Production volumes
# Manufacturing lead time
# Manufacturing costs
# Inspection results
# Defect rates
# Transportation modes
# Routes
# Costs

# In[44]:


import pandas as pd
import plotly.express as px
import plotly.io as pio
import plotly.graph_objects as go
import matplotlib.pyplot as plt
pio.templates.default = "plotly_white"


# In[2]:


data =pd.read_csv("supply_chain_data.csv")


# In[3]:


data


# In[7]:


print(data.head())


# In[9]:


print(data.describe())


# In[27]:


data['Transportation modes'].unique()


# In[28]:


data['Routes'].unique()


# In[10]:


print(data.info())


# In[29]:


data['Customer demographics'].unique()


# In[49]:


cols = ['Product type', 'SKU', 'Price', 'Availability', 'Number of products sold', 
        'Revenue generated', 'Customer demographics', 'Stock levels', 'Lead times', 
        'Order quantities', 'Shipping times', 'Shipping carriers', 'Shipping costs', 
        'Supplier name', 'Location', 'Lead time', 'Production volumes', 
        'Manufacturing lead time', 'Manufacturing costs', 'Inspection results', 
        'Defect rates', 'Transportation modes', 'Routes', 'Costs']


# In[50]:


# Plot univariate distributions of selected variables
for col in cols:
    if data[col].dtype != 'object':  # Ignore non-numeric columns
        sns.histplot(data[col], kde=False)
        plt.title(col)
        plt.show()


# In[11]:


# Product type and Price
# analyzing the Supply Chain by looking at the relationship between the price of the products and the revenue generated by them:
fig = px.scatter(data, x='Price', 
                 y='Revenue generated', 
                 color='Product type', 
                 hover_data=['Number of products sold'], 
                 trendline="ols")
fig.show()


# In[35]:


# HeatMap Analysis
import seaborn as sns
heatmap_1 = pd.pivot_table(
    data=data,
    index = 'Customer demographics',
    columns='Product type',
    values='Order quantities',
    aggfunc='sum'
)

sns.heatmap(heatmap_1)


# In[38]:


heatmap_2 = pd.pivot_table(
    data=data,
    index = 'Transportation modes',
    columns='Routes',
    values='Shipping costs',
    aggfunc='sum'
)

sns.heatmap(heatmap_2)


# # Sales by Product Type
# The company derives more revenue from skincare products, and the higher the price of skincare products, the more revenue they generate. Now let’s have a look at the sales by product type:

# In[16]:


sales_data = data.groupby('Product type')['Number of products sold'].sum().reset_index()

pie_chart = px.pie(sales_data, values='Number of products sold', names='Product type', 
                   title='Sales by Product Type', 
                   hover_data=['Number of products sold'],
                   hole=0.5,
                   color_discrete_sequence=px.colors.qualitative.Pastel)
                   
pie_chart.update_traces(textposition='inside', textinfo='percent+label')
pie_chart.show()


# In[ ]:


# So 45% of the business comes from skincare products, 29.5% from haircare, and 25.5% from cosmetics.


# # Total Revenue by Shipping Carrier

# In[17]:


total_revenue = data.groupby('Shipping carriers')['Revenue generated'].sum().reset_index()
fig = go.Figure()
fig.add_trace(go.Bar(x=total_revenue['Shipping carriers'], 
                     y=total_revenue['Revenue generated']))
fig.update_layout(title='Total Revenue by Shipping Carrier', 
                  xaxis_title='Shipping Carrier', 
                  yaxis_title='Revenue Generated')
fig.show()


# In[ ]:


# Product type
The company is using three carriers for transportation, and Carrier B helps the company in generating more revenue. Now let’s have a look at the Average lead time and Average Manufacturing Costs for all products of the company:


# In[18]:


avg_lead_time = data.groupby('Product type')['Lead time'].mean().reset_index()
avg_manufacturing_costs = data.groupby('Product type')['Manufacturing costs'].mean().reset_index()
result = pd.merge(avg_lead_time, avg_manufacturing_costs, on='Product type')
result.rename(columns={'Lead time': 'Average Lead Time', 'Manufacturing costs': 'Average Manufacturing Costs'}, inplace=True)
print(result)


# In[ ]:


# Analyzing SKUs
There’s a column in the dataset as SKUs. You must have heard it for the very first time. So, SKU stands for Stock Keeping Units. They’re like special codes that help companies keep track of all the different things they have for sale. Imagine you have a large toy store with lots of toys. Each toy is different and has its name and price, but when you want to know how many you have left, you need a way to identify them. So you give each toy a unique code, like a secret number only the store knows. This secret number is called SKU.


# # Revenue Generated by SKU
# 

# In[19]:


revenue_chart = px.line(data, x='SKU', 
                        y='Revenue generated', 
                        title='Revenue Generated by SKU')
revenue_chart.show()


# In[ ]:


# Stock Levels by SKU¶
Stock levels refer to the number of products a store or business has in its inventory. Now let’s have a look at the stock levels of each SKU:


# # Order Quantity by SKU

# In[20]:


order_quantity_chart = px.bar(data, x='SKU', 
                              y='Order quantities', 
                              title='Order Quantity by SKU')
order_quantity_chart.show()


# # Shipping Cost by Carrier

# In[21]:


shipping_cost_chart = px.bar(data, x='Shipping carriers', 
                             y='Shipping costs', 
                             title='Shipping Costs by Carrier')
shipping_cost_chart.show()


# In[ ]:


# In one of the above visualizations, we discovered that Carrier B helps the company in more revenue. It is also the most costly Carrier among the three


# # Cost Distribution by Transportation

# In[22]:


transportation_chart = px.pie(data, 
                              values='Costs', 
                              names='Transportation modes', 
                              title='Cost Distribution by Transportation Mode',
                              hole=0.5,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()


# In[ ]:


# So the company spends more on Road and Rail modes of transportation for the transportation of Goods.


# # Analyzing Defect Rate
# The defect rate in the supply chain refers to the percentage of products that have something wrong or are found broken after shipping.

# In[23]:


defect_rates_by_product = data.groupby('Product type')['Defect rates'].mean().reset_index()

fig = px.bar(defect_rates_by_product, x='Product type', y='Defect rates',
             title='Average Defect Rates by Product Type')
fig.show()


# In[ ]:


# So defect rates hair product is higher


# # Defects rates by Transportation Mode

# In[24]:


pivot_table = pd.pivot_table(data, values='Defect rates', 
                             index=['Transportation modes'], 
                             aggfunc='mean')

transportation_chart = px.pie(values=pivot_table["Defect rates"], 
                              names=pivot_table.index, 
                              title='Defect Rates by Transportation Mode',
                              hole=0.5,
                              color_discrete_sequence=px.colors.qualitative.Pastel)
transportation_chart.show()


# In[ ]:


# Road transportation results in a higher defect rate, and Air transportation has the lowest defect rates.


# In[26]:


pie_customer_demographics_revenue = px.pie(data, values='Revenue generated', names='Customer demographics', \
    title='Revenue generated by customer demographics', hole=0.5,color_discrete_sequence=px.colors.qualitative.Pastel)
pie_customer_demographics_revenue.update_traces(textposition='inside', textinfo='percent+label')
pie_customer_demographics_revenue.show()


# In[ ]:


# Most of revenue generated by Female


# # Chi-square analysis

# In[64]:


# Is there any relationship between Number of products sold with Revenue generated?
from scipy.stats import chi2_contingency
relation_1 = pd.pivot_table(
    data=data,
    index = 'Number of products sold',
    columns='Revenue generated',
    values='SKU',
    aggfunc='count'
)

# Calculating

stat, p, dof, expected = chi2_contingency(relation_1)

alpha = 0.05

if p<= alpha:
  print("Reject H0: Number of products sold has relation with revenue generated")
else:
  print("H0 is Accepted: Number of products sold has no relation with revenue generated")


# # Conclusion
# 1. Based on Product_type, the organization selling more on Skincare products. As for the Customer demographics is Unknown.
# 2. Carrier B is the courrier that delivers most of the organization goods. And based on the transportation mode, Sea is the least preferrable one by any of the Carriers.
# 3. If we're talking about stocks, then most of them is still categorized as A and could deliver normally. But there is no relationship between manufacturing volume with it, so even though the stock is still save, organization still manufactured it with a pretty huge volume.
