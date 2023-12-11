# %%
# Import Libraries and Dependencies
import pandas as pd

# %% [markdown]
# ### 1. Combine and Clean the Data (15 pts - done)
# #### Import CSVs

# %%
# Read the CSV files into DataFrames.  
sales_2020 = "Resources/athletic_sales_2020.csv"
sales2020_df = pd.read_csv(sales_2020) 
sales_2021 = "Resources/athletic_sales_2021.csv"
sales2021_df = pd.read_csv(sales_2021)

# %%
# Display the 2020 sales DataFrame
sales2020_df.head()

# %%
# Display the 2021 sales DataFrame
sales2021_df.head()

# %% [markdown]
# #### Check the data types of each DataFrame

# %%
# Check the 2020 sales data types.
print(sales2020_df.dtypes)

# %%
# Check the 2021 sales data types.
print(sales2021_df.dtypes)


# %% [markdown]
# #### Combine the sales data by rows.

# %%
# Combine the 2020 and 2021 sales DataFrames on the rows (using inner join) and reset the index.
joined_20_21_sales_df = pd.concat([sales2020_df,sales2021_df], axis=0, join='inner')
joined_20_21_sales_df = joined_20_21_sales_df.reset_index(drop=True)
joined_20_21_sales_df.head(20)


# %%
# Check if any values are null.
joined_20_21_sales_df.count()


# %%
# Check the data type of each column
print(joined_20_21_sales_df.dtypes)

# %%
# Convert the "invoice_date" to a datetime datatype
joined_20_21_sales_df['invoice_date'] = pd.to_datetime(joined_20_21_sales_df['invoice_date'], errors='coerce')

# %%
# Confirm that the "invoice_date" data type has been changed.
print(joined_20_21_sales_df.dtypes)

# %% [markdown]
# ### 2. Determine which Region Sold the Most Products (15pts-done)

# %% [markdown]
# #### Using `groupby`

# %%
# Show the number products sold for region, state, and city.
grouped_region_df = pd.DataFrame(joined_20_21_sales_df) 
grouped_region_df = joined_20_21_sales_df.groupby(['region', 'state', 'city'])['units_sold'].sum()
grouped_region_df = grouped_region_df.reset_index()
grouped_region_df.head()

#Rename the sum to "Total_Products_Sold".
grouped_region_df = grouped_region_df.rename(columns={'units_sold':'Total_Products_Sold'})

# Show the top 5 results.
grouped_df_sorted = grouped_region_df.sort_values(by='Total_Products_Sold', ascending=False)    
grouped_df_sorted.head()                 

# %% [markdown]
# #### Using `pivot_table`

# %%
# Show the number products sold for region, state, and city.
pv_grouped_df_sum = pd.pivot_table(joined_20_21_sales_df,
                                   index=['region','state','city'],
                                   values='units_sold',
                                   aggfunc='sum')

# Rename the "units_sold" column to "Total_Products_Sold"
pv_grouped_df_sum = pv_grouped_df_sum.rename(columns={'units_sold':'Total_Products_Sold'})

# Show the top 5 results.
pv_grouped_df_sorted = pv_grouped_df_sum.sort_values(by='Total_Products_Sold', ascending=False)
#grouped_df_sorted = grouped_region_df.sort_values(by='Total_Products_Sold', ascending=False)    
pv_grouped_df_sorted.head()

# %% [markdown]
# ### 3. Determine which Region had the Most Sales (15 pts - done)

# %% [markdown]
# #### Using `groupby`

# %%
# Show the total sales for the products sold for each region, state, and city.
grouped_df_sales = joined_20_21_sales_df.groupby(['region', 'state', 'city'])['total_sales'].sum()
grouped_df_sales = grouped_df_sales.reset_index()
grouped_df_sales.head()

# Rename the "total_sales" column to "Total Sales"
grouped_df_sales = grouped_df_sales.rename(columns={'total_sales':'Total Sales'})
grouped_df_sales.head()

# Show the top 5 results.
grouped_df_sales_sorted = grouped_df_sales.sort_values(by='Total Sales', ascending=False)    
grouped_df_sales_sorted.head() 


# %% [markdown]
# #### Using `pivot_table`

# %%
# Show the total sales for the products sold for each region, state, and city.
pv_sales_df_sum = pd.pivot_table(joined_20_21_sales_df,
                                   index=['region','state','city'],
                                   values='total_sales',
                                   aggfunc='sum')

# Optional: Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.
pv_sales_df_sorted = pv_sales_df_sum.sort_values(by='total_sales',ascending=False)
pv_sales_df_sorted.head()

# %% [markdown]
# ### 4. Determine which Retailer had the Most Sales (15 pts - done)

# %% [markdown]
# #### Using `groupby`

# %%
# Show the total sales for the products sold for each retailer, region, state, and city.
grouped_df_retailers = joined_20_21_sales_df.groupby(['retailer','region', 'state', 'city'])['total_sales'].sum()
grouped_df_retailers = grouped_df_retailers.reset_index()
grouped_df_retailers.head()

# Rename the "total_sales" column to "Total Sales"
grouped_df_retailers = grouped_df_retailers.rename(columns={'total_sales':'Total Sales'})
grouped_df_retailers.head()

# Show the top 5 results.
grouped_df_retailers_sorted = grouped_df_retailers.sort_values(by='Total Sales', ascending=False)    
grouped_df_retailers_sorted.head()




# %% [markdown]
# #### Using `pivot_table`

# %%
# Show the total sales for the products sold for each retailer, region, state, and city.
pv_grouped_df_retailers = pd.pivot_table(joined_20_21_sales_df,
                                        index=['retailer','region','state','city'],
                                        values='total_sales',
                                        aggfunc='sum')

# Optional: Rename the "total_sales" column to "Total Sales"


# Show the top 5 results.
pv_grouped_df_retailers_sorted = pv_grouped_df_retailers.sort_values(by='total_sales',ascending=False)
pv_grouped_df_retailers_sorted.head()

# %% [markdown]
# ### 5. Determine which Retailer Sold the Most Women's Athletic Footwear (20pts - done)

# %%
# Filter the sales data to get the women's athletic footwear sales data.
w_ath_footwear_df = joined_20_21_sales_df.loc[(joined_20_21_sales_df["product"]=="Women's Athletic Footwear")]
w_ath_footwear_df

# %% [markdown]
# #### Using `groupby`

# %%
# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
ttl_w_ath_footwear_df = w_ath_footwear_df.groupby(['retailer','region', 'state', 'city'])['units_sold'].sum()
ttl_w_ath_footwear_df = ttl_w_ath_footwear_df.reset_index()
ttl_w_ath_footwear_df.head()

# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
ttl_w_ath_footwear_df = ttl_w_ath_footwear_df.rename(columns={'units_sold':'Womens_Footwear_Units_Sold'})
ttl_w_ath_footwear_df.head()

# Show the top 5 results.
ttl_w_ath_footwear_sorted_df = ttl_w_ath_footwear_df.sort_values(by='Womens_Footwear_Units_Sold', ascending=False)    
ttl_w_ath_footwear_sorted_df.head()



# %% [markdown]
# #### Using `pivot_table`

# %%
# Show the total number of women's athletic footwear sold for each retailer, region, state, and city.
pv_ttl_foot = pd.pivot_table(w_ath_footwear_df,
                                        index=['retailer','region','state','city'],
                                        values='units_sold',
                                        aggfunc='sum')

# Rename the "units_sold" column to "Womens_Footwear_Units_Sold"
pv_ttl_foot = pv_ttl_foot.rename(columns={'units_sold':'Womens_Footwear_Units_Sold'})
# Show the top 5 results.
pv_ttl_foot_sorted = pv_ttl_foot.sort_values(by='Womens_Footwear_Units_Sold', ascending=False)
pv_ttl_foot_sorted.head()

# %% [markdown]
# ### 5(6)  . Determine the Day with the Most Women's Athletic Footwear Sales (15pts - done)

# %%
# Create a pivot table with the 'invoice_date' column is the index, and the "total_sales" as the values.
w_ath_footwear_df['invoice_date'] = pd.to_datetime(w_ath_footwear_df['invoice_date'], errors='coerce')
most_waf_sales_df = w_ath_footwear_df.pivot_table(index='invoice_date',
                                                values='total_sales',
                                                aggfunc='sum')

# Optional: Rename the "total_sales" column to "Total Sales"
most_waf_sales_df = most_waf_sales_df.rename(columns={'total_sales':'Total Sales'})

# Resample the pivot table into daily bins, and get the total sales for each day.
daily_ttl_sales = most_waf_sales_df.resample('D').sum()

# Sort the resampled pivot table in ascending order on "Total Sales".
daily_ttl_sales_sorted_df = daily_ttl_sales.sort_values(by='Total Sales', ascending=False)    


# Show the table.
daily_ttl_sales_sorted_df.head(10)

# %% [markdown]
# ### 6(7).  Determine the Week with the Most Women's Athletic Footwear Sales (5 pts - done)

# %%
# Resample the pivot table into weekly bins, and get the total sales for each week.
weekly_ttl_sales = most_waf_sales_df.resample('W').sum()

# Sort the resampled pivot table in ascending order on "Total Sales".
weekly_ttl_sales_sorted = weekly_ttl_sales.sort_values(by='Total Sales', ascending=False)
weekly_ttl_sales_sorted.head(10)


