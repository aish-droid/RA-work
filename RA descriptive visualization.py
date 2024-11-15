#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Initialize-dataset" data-toc-modified-id="Initialize-dataset-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Initialize dataset</a></span></li><li><span><a href="#Initialize-all-dictionaries" data-toc-modified-id="Initialize-all-dictionaries-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Initialize all dictionaries</a></span></li><li><span><a href="#Vizualizations-samples" data-toc-modified-id="Vizualizations-samples-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Vizualizations samples</a></span><ul class="toc-item"><li><span><a href="#Female-occupations-vs-State-heatmap-for-2004-and-2011" data-toc-modified-id="Female-occupations-vs-State-heatmap-for-2004-and-2011-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Female occupations vs State heatmap for 2004 and 2011</a></span></li><li><span><a href="#Top-5-female-occupations-for-every-state-in-2004-and-2011" data-toc-modified-id="Top-5-female-occupations-for-every-state-in-2004-and-2011-3.2"><span class="toc-item-num">3.2&nbsp;&nbsp;</span>Top 5 female occupations for every state in 2004 and 2011</a></span></li><li><span><a href="#Top-5-female-occupations-for-every-state-in-2011,-compared-with-2004-proportions" data-toc-modified-id="Top-5-female-occupations-for-every-state-in-2011,-compared-with-2004-proportions-3.3"><span class="toc-item-num">3.3&nbsp;&nbsp;</span>Top 5 female occupations for every state in 2011, compared with 2004 proportions</a></span></li><li><span><a href="#Top-5-female-occupations-for-every-state-in-2004,-compared-with-2011-proportions" data-toc-modified-id="Top-5-female-occupations-for-every-state-in-2004,-compared-with-2011-proportions-3.4"><span class="toc-item-num">3.4&nbsp;&nbsp;</span>Top 5 female occupations for every state in 2004, compared with 2011 proportions</a></span></li><li><span><a href="#Top-20-occupations-that-females-work-in-across-India-for-2011-and-2004" data-toc-modified-id="Top-20-occupations-that-females-work-in-across-India-for-2011-and-2004-3.5"><span class="toc-item-num">3.5&nbsp;&nbsp;</span>Top 20 occupations that females work in across India for 2011 and 2004</a></span></li><li><span><a href="#Female-Industry-vs-State-heatmap-for-2004-and-2011" data-toc-modified-id="Female-Industry-vs-State-heatmap-for-2004-and-2011-3.6"><span class="toc-item-num">3.6&nbsp;&nbsp;</span>Female Industry vs State heatmap for 2004 and 2011</a></span></li><li><span><a href="#Top-5-female-industries-for-every-state-in-2004-and-2011" data-toc-modified-id="Top-5-female-industries-for-every-state-in-2004-and-2011-3.7"><span class="toc-item-num">3.7&nbsp;&nbsp;</span>Top 5 female industries for every state in 2004 and 2011</a></span></li><li><span><a href="#Top-5-female-industries-for-every-state-in-2011,-compared-with-2004-proportions" data-toc-modified-id="Top-5-female-industries-for-every-state-in-2011,-compared-with-2004-proportions-3.8"><span class="toc-item-num">3.8&nbsp;&nbsp;</span>Top 5 female industries for every state in 2011, compared with 2004 proportions</a></span></li><li><span><a href="#Top-5-female-industries-for-every-state-in-2004,-compared-with-2011-proportions" data-toc-modified-id="Top-5-female-industries-for-every-state-in-2004,-compared-with-2011-proportions-3.9"><span class="toc-item-num">3.9&nbsp;&nbsp;</span>Top 5 female industries for every state in 2004, compared with 2011 proportions</a></span></li><li><span><a href="#Top-20-industries-that-females-work-in-across-India-for-2011-and-2004" data-toc-modified-id="Top-20-industries-that-females-work-in-across-India-for-2011-and-2004-3.10"><span class="toc-item-num">3.10&nbsp;&nbsp;</span>Top 20 industries that females work in across India for 2011 and 2004</a></span></li><li><span><a href="#RELIGIONB-and-top-20-industries-females-work-in" data-toc-modified-id="RELIGIONB-and-top-20-industries-females-work-in-3.11"><span class="toc-item-num">3.11&nbsp;&nbsp;</span>RELIGIONB and top 20 industries females work in</a></span></li><li><span><a href="#RELIGIONA-and-top-20-industries-females-work-in" data-toc-modified-id="RELIGIONA-and-top-20-industries-females-work-in-3.12"><span class="toc-item-num">3.12&nbsp;&nbsp;</span>RELIGIONA and top 20 industries females work in</a></span></li></ul></li></ul></div>

# 
# # Descriptive visualization
# 

# ## Initialize dataset

# In[2]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data from the .dta file
data_path = r"C:\Users\Aishwarya Venkat\Documents\Yale\RA Work_Prof Ardina\Cleaned files_Aishwarya\all_obs_data.dta"
df = pd.read_stata(data_path,convert_categoricals=False) #set convert categoricals to false to avoid error


# ## Initialize all dictionaries

# In[7]:


#initialize all dictionaries

# full occupation mapping - Occ or WS4 - 100 values 
occupation_dict = { 0: 'Physical scientists', 1: 'Physical sci tech', 2: 'Engineers', 3: 'Eng. tech', 7: 'Physicians', 8: 'Nursing', 9: 'Other scientific', 11: 'Economists', 12: 'Accountants', 13: 'Social scientists', 14: 'Lawyers', 15: 'Teachers', 16: 'Journalists', 17: 'Artists', 18: 'Performers', 19: 'Professional nec', 20: 'Elected officials', 21: 'Govt officials', 22: 'Mgr Whsl/retail', 23: 'Mgr finance', 24: 'Mgr manf', 25: 'Mgr transp/commun', 26: 'Mgr service', 29: 'Managerial nec', 30: 'Clerical supe', 31: 'Village officials', 32: 'Typists', 33: 'Book-keepers', 34: 'Computing op', 35: 'Clerical nec', 36: 'Transp/commun supe', 37: 'Transp conductors', 38: 'Mail distributors', 39: 'Telephone op', 40: 'Shopkeepers', 41: 'Manuf agents', 42: 'Technical sales', 43: 'Sales, shop', 44: 'FIRE sales', 45: 'Money lenders', 49: 'Sales, nec', 50: 'Hotel/restaurant', 51: 'House keepers', 52: 'Cooks/waiters', 53: 'Maids', 54: 'Sweepers', 55: 'Launderers', 56: 'Barbers', 57: 'Police', 59: 'Service nec', 60: 'Farm manager', 61: 'Cultivators', 62: 'Other farmers', 63: 'Ag labour', 64: 'Plantation lab', 65: 'Other farm', 66: 'Forestry', 67: 'Hunters', 68: 'Fishermen', 71: 'Miners', 72: 'Metal workers', 73: 'Wood/paper', 74: 'Chemical', 75: 'Textile', 76: 'Tanners', 77: 'Food', 78: 'Tobacco', 79: 'Tailors', 80: 'Shoe makers', 81: 'Carpenters', 82: 'Stone cutters', 83: 'Machine tool op', 84: 'Assemblers', 85: 'Electrical', 86: 'Cinema op', 87: 'Plumbers/welders', 88: 'Jewellery', 89: 'Potters', 90: 'Rubber/plastic', 91: 'Paper', 92: 'Printing', 93: 'Painters', 94: 'Production nec', 95: 'Construction', 96: 'Boilermen', 97: 'Loaders', 98: 'Drivers', 99: 'Labour nec' }

# full state mapping - STATEID - 34 values 
state_dict = { 1: 'Jammu & Kashmir', 2: 'Himachal Pradesh', 3: 'Punjab', 4: 'Chandigarh', 5: 'Uttaranchal', 6: 'Haryana', 7: 'Delhi', 8: 'Rajasthan', 9: 'Uttar Pradesh', 10: 'Bihar', 11: 'Sikkim', 12: 'Arunachal Pradesh', 13: 'Nagaland', 14: 'Manipur', 15: 'Mizoram', 16: 'Tripura', 17: 'Meghalaya', 18: 'Assam', 19: 'West Bengal', 20: 'Jharkhand', 21: 'Orissa', 22: 'Chhattisgarh', 23: 'Madhya Pradesh', 24: 'Gujarat', 25: 'Daman & Diu', 26: 'Dadra+Nagar Haveli', 27: 'Maharashtra', 28: 'Andhra Pradesh', 29: 'Karnataka', 30: 'Goa', 32: 'Kerala', 33: 'Tamil Nadu', 34: 'Pondicherry' }

#full industry mapping - industry or WS5 - 99 values, check for -6 values
industry_dict = { 0: 'Agriculture', 1: 'Plantations', 2: 'Livestock', 3: 'Ag services', 4: 'Hunting', 5: 'Forestry', 6: 'Fishing', 10: 'Coal mining', 11: 'Petroleum extract', 12: 'Iron mining', 13: 'Other metal mining', 14: 'Uranium mining', 15: 'Nonmetal mining', 19: 'Mining services', 20: 'Manf food products', 22: 'Manf bev/tobacco', 23: 'Manf cotton textiles', 24: 'Manf wool/silk/etc', 25: 'Manf jute', 26: 'Manf apparel', 27: 'Manf wood/furniture', 28: 'Manf paper/publish', 29: 'Manf leather', 30: 'Manf chemicals', 31: 'Manf rubber/plastic', 32: 'Manf mineral', 33: 'Manf basic metal', 34: 'Manf metal products', 35: 'Manf machinery', 37: 'Manf transport equip', 38: 'Manf other', 39: 'Repair capital goods', 40: 'Electricity', 41: 'Gas/steam', 42: 'Water works', 43: 'Other energy', 50: 'Construction', 51: 'Allied construction', 60: 'Whsl ag/textiles', 61: 'Whsl basic goods', 62: 'Whsl machinery', 63: 'Whsl nec', 64: 'Manf agents', 65: 'Retail food', 66: 'Retail textiles', 67: 'Retail household', 68: 'Retail nec', 69: 'Restaurants/hotels', 70: 'Land transport', 71: 'Water transport', 72: 'Air transport', 73: 'Transport nec', 74: 'Storage', 75: 'Communication', 80: 'Banking', 81: 'Insurance', 82: 'Real estate', 83: 'Legal', 84: 'Lotteries', 85: 'Renting', 89: 'Business services', 90: 'Public admin', 91: 'Sanitary', 92: 'Education', 93: 'Medical', 94: 'Community', 95: 'Rec/culture', 96: 'Personal services', 97: 'Repair services', 98: 'International', 99: 'Services nec' }

#RELIGIONB mapping
religionb_dict = {1: "Hindu",2: "Muslim",3: "Christian",4: "Sikh",5: "Buddhist",6: "Jain",7: "Tribal",8: "Others", 9: "None"}

#RELIGIONA mapping
religiona_dict = {1: "Brahmin", 2: "Forward caste", 3: "Other Backward Castes (OBC)", 4: "Dalit", 5: "Adivasi", 6: "Muslim", 7: "Christian, Sikh, Jain"}


# ## Vizualizations samples 

# ### Female occupations vs State heatmap for 2004 and 2011

# In[107]:


""" Occupation vs State heatmap for 2004 and 2011
Note that proportions DO NOT account for missing data and that about 80% of observations have occupation as empty """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to create occupation vs state heatmap for a specific year
def plot_occupation_heatmap(year_data, year_label):
    # Group by STATEID and Occ to get counts of each occupation per state
    occupation_counts = year_data.groupby(['STATEID', 'Occ']).size().unstack(fill_value=0)

    # Update the columns with occupation names
    occupation_counts.columns = [occupation_dict.get(i, f"Occupation {i}") for i in occupation_counts.columns]

    # Update the index with state names
    occupation_counts.index = [state_dict.get(i, f"State {i}") for i in occupation_counts.index]

    # Plot heatmap to visualize occupation distribution across states
    plt.figure(figsize=(20, 15))  # Increased figure size to accommodate all labels
    sns.heatmap(occupation_counts, cmap='viridis', cbar_kws={'label': 'Number of Females'},
                xticklabels=occupation_counts.columns, yticklabels=occupation_counts.index,
                linewidths=0.5, annot=False)

    # Customize plot labels and title
    plt.title(f'Distribution of Occupations of Females by State in India - {year_label}')
    plt.xlabel('Occupation')
    plt.ylabel('State')

    # Rotate the tick labels for better readability
    plt.xticks(rotation=90, fontsize=8)  # Rotate x-axis labels and reduce font size
    plt.yticks(rotation=0, fontsize=8)   # Keep y-axis labels horizontal and reduce font size

    plt.tight_layout()  # Ensures everything fits within the figure
    plt.show()

# Filter for females (SEX == 2) for each year
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Generate heatmaps for 2004 and 2011
plot_occupation_heatmap(female_data_2004, '2004')
plot_occupation_heatmap(female_data_2011, '2011')


# ### Top 5 female occupations for every state in 2004 and 2011

# In[109]:


""" Top 5 occupations for every state in 2004 and 2011.
Note that proportions on the x-axis account for missing data and that about 80% of observations have 'Occ' as empty """

from matplotlib.ticker import FuncFormatter
import seaborn as sns
import matplotlib.pyplot as plt

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Function to plot top 5 occupations for each state for a specific year
def plot_top_occupations_by_state(year_data, year_label):
    # Calculate the total number of females in each state
    total_females_per_state = year_data.groupby('STATEID').size()

    # Group by STATEID and Occ to get counts of each occupation per state
    occupation_counts = year_data.groupby(['STATEID', 'Occ']).size().unstack(fill_value=0)

    # Calculate the proportion of each occupation within each state
    occupation_proportions = occupation_counts.div(total_females_per_state, axis=0)

    # Update the columns with occupation names
    occupation_proportions.columns = [occupation_dict.get(i, f"Occupation {i}") for i in occupation_proportions.columns]

    # Update the index with state names
    occupation_proportions.index = [state_dict.get(i, f"State {i}") for i in occupation_proportions.index]

    # Set up a grid of plots
    fig, axes = plt.subplots(6, 6, figsize=(20, 20))  # Create a 6x6 grid for 34 states
    axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

    # Loop through states and plot top 5 occupations for each
    for i, state in enumerate(occupation_proportions.index):
        # Get the top 5 occupations by proportion for the current state
        top_occupations = occupation_proportions.loc[state].sort_values(ascending=False).head(5)

        # Plot the top 5 occupations for the state
        sns.barplot(x=top_occupations.values, y=top_occupations.index, ax=axes[i], palette="viridis", hue=top_occupations.index)

        axes[i].set_title(f"Top 5 in {state} ({year_label})")
        axes[i].set_xlabel('Proportion of Females')
        axes[i].set_ylabel('Occupation')

        # Apply the percentage formatter to the x-axis
        axes[i].xaxis.set_major_formatter(FuncFormatter(percentage_formatter))

    # Adjust the layout to make it compact and readable
    plt.tight_layout()
    plt.show()

# Filter for females (SEX == 2) for each year
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Generate top occupations plots for 2004 and 2011
plot_top_occupations_by_state(female_data_2004, '2004')
plot_top_occupations_by_state(female_data_2011, '2011')


# ### Top 5 female occupations for every state in 2011, compared with 2004 proportions

# In[123]:


""" Top 5 occupations for every state in 2011, compared with 2004 proportions.
The top 5 occupations are selected from 2011 data, with 2004 data for those same occupations shown for comparison """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Calculate total females per state for 2004 and 2011 separately
total_females_per_state_2004 = female_data_2004.groupby('STATEID').size()
total_females_per_state_2011 = female_data_2011.groupby('STATEID').size()

# Group by STATEID and Occ to get counts of each occupation per state for 2004 and 2011
occupation_counts_2004 = female_data_2004.groupby(['STATEID', 'Occ']).size().unstack(fill_value=0)
occupation_counts_2011 = female_data_2011.groupby(['STATEID', 'Occ']).size().unstack(fill_value=0)

# Calculate proportions for each occupation within each state
occupation_proportions_2004 = occupation_counts_2004.div(total_females_per_state_2004, axis=0)
occupation_proportions_2011 = occupation_counts_2011.div(total_females_per_state_2011, axis=0)

# Update the columns with occupation names
occupation_proportions_2004.columns = [occupation_dict.get(i, f"Occupation {i}") for i in occupation_proportions_2004.columns]
occupation_proportions_2011.columns = [occupation_dict.get(i, f"Occupation {i}") for i in occupation_proportions_2011.columns]

# Update the index with state names
occupation_proportions_2004.index = [state_dict.get(i, f"State {i}") for i in occupation_proportions_2004.index]
occupation_proportions_2011.index = [state_dict.get(i, f"State {i}") for i in occupation_proportions_2011.index]

# Set up a grid of plots
fig, axes = plt.subplots(6, 6, figsize=(20, 20))  # Create a 6x6 grid for 34 states
axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

# Loop through states and plot top 5 occupations for each
for i, state in enumerate(occupation_proportions_2011.index):
    # Get the top 5 occupations by proportion for the current state in 2011
    top_occupations_2011 = occupation_proportions_2011.loc[state].sort_values(ascending=False).head(5)
    occupations_to_compare = top_occupations_2011.index

    # Get the corresponding proportions for 2004 and fill missing occupations with zero
    top_occupations_2004 = occupation_proportions_2004.reindex(index=occupation_proportions_2011.index, columns=occupations_to_compare, fill_value=0).loc[state, occupations_to_compare]

    # Create a DataFrame to hold both years' data
    comparison_df = pd.DataFrame({
        '2011': top_occupations_2011.values,
        '2004': top_occupations_2004.values
    }, index=occupations_to_compare)

    # Plot the side-by-side bars for each occupation
    comparison_df.plot(kind='bar', ax=axes[i], color=['#007acc', '#ffae42'], width=0.8)
    axes[i].set_title(f"Top 5 in {state} (2011 vs 04)")
    axes[i].set_xlabel('Occupation')
    axes[i].set_ylabel('Proportion of Females')

    # Apply the percentage formatter to the y-axis
    axes[i].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


# ### Top 5 female occupations for every state in 2004, compared with 2011 proportions 

# In[121]:


""" Top 5 occupations for every state in 2004, compared with 2011 proportions.
The top 5 occupations are selected from 2004 data, with 2011 data for those same occupations shown for comparison """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Calculate total females per state for 2004 and 2011 separately
total_females_per_state_2004 = female_data_2004.groupby('STATEID').size()
total_females_per_state_2011 = female_data_2011.groupby('STATEID').size()

# Group by STATEID and Occ to get counts of each occupation per state for 2004 and 2011
occupation_counts_2004 = female_data_2004.groupby(['STATEID', 'Occ']).size().unstack(fill_value=0)
occupation_counts_2011 = female_data_2011.groupby(['STATEID', 'Occ']).size().unstack(fill_value=0)

# Calculate proportions for each occupation within each state
occupation_proportions_2004 = occupation_counts_2004.div(total_females_per_state_2004, axis=0)
occupation_proportions_2011 = occupation_counts_2011.div(total_females_per_state_2011, axis=0)

# Update the columns with occupation names
occupation_proportions_2004.columns = [occupation_dict.get(i, f"Occupation {i}") for i in occupation_proportions_2004.columns]
occupation_proportions_2011.columns = [occupation_dict.get(i, f"Occupation {i}") for i in occupation_proportions_2011.columns]

# Update the index with state names
occupation_proportions_2004.index = [state_dict.get(i, f"State {i}") for i in occupation_proportions_2004.index]
occupation_proportions_2011.index = [state_dict.get(i, f"State {i}") for i in occupation_proportions_2011.index]

# Set up a grid of plots
fig, axes = plt.subplots(6, 6, figsize=(20, 20))  # Create a 6x6 grid for 34 states
axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

# Loop through states and plot top 5 occupations for each
for i, state in enumerate(occupation_proportions_2004.index):
    # Get the top 5 occupations by proportion for the current state in 2004
    top_occupations_2004 = occupation_proportions_2004.loc[state].sort_values(ascending=False).head(5)
    occupations_to_compare = top_occupations_2004.index

    # Get the corresponding proportions for 2011 and fill missing occupations with zero
    top_occupations_2011 = occupation_proportions_2011.reindex(index=occupation_proportions_2004.index, columns=occupations_to_compare, fill_value=0).loc[state, occupations_to_compare]

    # Create a DataFrame to hold both years' data
    comparison_df = pd.DataFrame({
        '2004': top_occupations_2004.values,
        '2011': top_occupations_2011.values
    }, index=occupations_to_compare)

    # Plot the side-by-side bars for each occupation
    comparison_df.plot(kind='bar', ax=axes[i], color=['#ffae42', '#007acc'], width=0.8)
    axes[i].set_title(f"Top 5 in {state} (2004 vs 11)")
    axes[i].set_xlabel('Occupation')
    axes[i].set_ylabel('Proportion of Females')

    # Apply the percentage formatter to the y-axis
    axes[i].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


# ### Top 20 occupations that females work in across India for 2011 and 2004

# In[143]:


""" Top 20 occupations that females work in across India for 2011 and 2004 (other year shown alongside for comparison in both cases). 
Note that proportions on x axis account for missing data and that about 80% of observations have occupation as empty """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Calculate total females for 2004 and 2011, including missing 'Occ'
total_females_2004 = len(female_data_2004)
total_females_2011 = len(female_data_2011)

# Calculate occupation counts and proportions for 2004 and 2011
occupation_counts_2004 = female_data_2004['Occ'].value_counts()
occupation_counts_2011 = female_data_2011['Occ'].value_counts()

# Calculate proportions for each occupation
occupation_proportions_2004 = occupation_counts_2004 / total_females_2004
occupation_proportions_2011 = occupation_counts_2011 / total_females_2011

# Update the occupation names based on a dictionary
occupation_proportions_2004.index = [occupation_dict.get(i, f"Occupation {i}") for i in occupation_proportions_2004.index]
occupation_proportions_2011.index = [occupation_dict.get(i, f"Occupation {i}") for i in occupation_proportions_2011.index]

# Get the top 20 occupations by proportion in 2011
top_20_occupations_2011 = occupation_proportions_2011.sort_values(ascending=False).head(20)

# Ensure the same occupations are included from 2004 for comparison
occupation_proportions_2004_top20 = occupation_proportions_2004.reindex(index=top_20_occupations_2011.index, fill_value=0)

# Create a DataFrame for plotting with both years
comparison_df = pd.DataFrame({
    '2011': top_20_occupations_2011.values,
    '2004': occupation_proportions_2004_top20.values
}, index=top_20_occupations_2011.index)

# Sort the DataFrame in descending order by the 2011 proportions
comparison_df = comparison_df.sort_values(by='2011', ascending=True)

# Create side-by-side subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot for 2011 vs 2004 (Proportions of Females)
comparison_df.plot(kind='bar', ax=axes[0], color=['#007acc', '#ffae42'])
axes[0].set_title("Top 20 Occupations of Females in India in 2011")
axes[0].set_xlabel("Occupation")
axes[0].set_ylabel("Proportion of Females")
axes[0].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))  # Format y-axis as percentages
axes[0].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for clarity

# For the second graph (2004 vs 2011), adjust as needed
occupation_proportions_2004_top20_sorted = occupation_proportions_2004.sort_values(ascending=False).head(20)
occupation_proportions_2011_top20_sorted = occupation_proportions_2011.reindex(index=occupation_proportions_2004_top20_sorted.index, fill_value=0)

# Plot for 2004 vs 2011 (Proportions of Females)
comparison_df_sorted = pd.DataFrame({
    '2004': occupation_proportions_2004_top20_sorted.values,
    '2011': occupation_proportions_2011_top20_sorted.values
}, index=occupation_proportions_2004_top20_sorted.index).sort_values(by='2004', ascending=True)

comparison_df_sorted.plot(kind='bar', ax=axes[1], color=['#007acc', '#ffae42'])
axes[1].set_title("Top 20 Occupations of Females in India in 2004")
axes[1].set_xlabel("Occupation")
axes[1].set_ylabel("Proportion of Females")
axes[1].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))  # Format y-axis as percentages
axes[1].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for clarity

# Adjust layout for better fit
plt.tight_layout()
plt.show()




# ### Female Industry vs State heatmap for 2004 and 2011

# In[147]:


""" Industry vs State heatmap 
Note that proportions DO NOT account for missing data and that about 80% of observations have industry as empty"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Group by STATEID and industry to get counts of each industry per state for 2004
industry_counts_2004 = female_data_2004.groupby(['STATEID', 'industry']).size().unstack(fill_value=0)

# Update the columns with industry names for 2004
industry_counts_2004.columns = [industry_dict.get(i, f"Industry {i}") for i in industry_counts_2004.columns]

# Update the index with state names for 2004
industry_counts_2004.index = [state_dict.get(i, f"State {i}") for i in industry_counts_2004.index]

# Group by STATEID and industry to get counts of each industry per state for 2011
industry_counts_2011 = female_data_2011.groupby(['STATEID', 'industry']).size().unstack(fill_value=0)

# Update the columns with industry names for 2011
industry_counts_2011.columns = [industry_dict.get(i, f"Industry {i}") for i in industry_counts_2011.columns]

# Update the index with state names for 2011
industry_counts_2011.index = [state_dict.get(i, f"State {i}") for i in industry_counts_2011.index]

# Create subplots one below another (2 rows, 1 column)
fig, axes = plt.subplots(2, 1, figsize=(20, 30))

# Plot heatmap for 2004
sns.heatmap(industry_counts_2004, cmap='viridis', cbar_kws={'label': 'Number of Females'},
            xticklabels=industry_counts_2004.columns, yticklabels=industry_counts_2004.index,
            linewidths=0.5, annot=False, ax=axes[0])

axes[0].set_title('Distribution of Industries of Females by State in 2004')
axes[0].set_xlabel('Industry')
axes[0].set_ylabel('State')

# Plot heatmap for 2011
sns.heatmap(industry_counts_2011, cmap='viridis', cbar_kws={'label': 'Number of Females'},
            xticklabels=industry_counts_2011.columns, yticklabels=industry_counts_2011.index,
            linewidths=0.5, annot=False, ax=axes[1])

axes[1].set_title('Distribution of Industries of Females by State in 2011')
axes[1].set_xlabel('Industry')
axes[1].set_ylabel('State')

# Rotate the tick labels for better readability
axes[0].tick_params(axis='x', rotation=90, labelsize=8)  # Rotate x-axis labels for 2004
axes[0].tick_params(axis='y', labelsize=8)  # Adjust y-axis labels for 2004

axes[1].tick_params(axis='x', rotation=90, labelsize=8)  # Rotate x-axis labels for 2011
axes[1].tick_params(axis='y', labelsize=8)  # Adjust y-axis labels for 2011

# Adjust layout for better fit
plt.tight_layout()
plt.show()



# ### Top 5 female industries for every state in 2004 and 2011

# In[149]:


""" Top 5 industries for every state in 2004 and 2011.
Note that proportions on the x-axis account for missing data and that about 80% of observations have 'industry' as empty """

from matplotlib.ticker import FuncFormatter
import seaborn as sns
import matplotlib.pyplot as plt

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Function to plot top 5 industries for each state for a specific year
def plot_top_industries_by_state(year_data, year_label):
    # Calculate the total number of females in each state
    total_females_per_state = year_data.groupby('STATEID').size()

    # Group by STATEID and industry to get counts of each industry per state
    industry_counts = year_data.groupby(['STATEID', 'industry']).size().unstack(fill_value=0)

    # Calculate the proportion of each industry within each state
    industry_proportions = industry_counts.div(total_females_per_state, axis=0)

    # Update the columns with industry names
    industry_proportions.columns = [industry_dict.get(i, f"Industry {i}") for i in industry_proportions.columns]

    # Update the index with state names
    industry_proportions.index = [state_dict.get(i, f"State {i}") for i in industry_proportions.index]

    # Set up a grid of plots
    fig, axes = plt.subplots(6, 6, figsize=(20, 20))  # Create a 6x6 grid for 34 states
    axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

    # Loop through states and plot top 5 industries for each
    for i, state in enumerate(industry_proportions.index):
        # Get the top 5 industries by proportion for the current state
        top_industries = industry_proportions.loc[state].sort_values(ascending=False).head(5)

        # Plot the top 5 industries for the state
        sns.barplot(x=top_industries.values, y=top_industries.index, ax=axes[i], palette="viridis", hue=top_industries.index)

        axes[i].set_title(f"Top 5 in {state} ({year_label})")
        axes[i].set_xlabel('Proportion of Females')
        axes[i].set_ylabel('Industry')

        # Apply the percentage formatter to the x-axis
        axes[i].xaxis.set_major_formatter(FuncFormatter(percentage_formatter))

    # Adjust the layout to make it compact and readable
    plt.tight_layout()
    plt.show()

# Filter for females (SEX == 2) for each year
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Generate top industries plots for 2004 and 2011
plot_top_industries_by_state(female_data_2004, '2004')
plot_top_industries_by_state(female_data_2011, '2011')


# ### Top 5 female industries for every state in 2011, compared with 2004 proportions

# In[151]:


""" Top 5 industries for every state in 2011, compared with 2004 proportions.
The top 5 industries are selected from 2011 data, with 2004 data for those same industries shown for comparison """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Calculate total females per state for 2004 and 2011 separately
total_females_per_state_2004 = female_data_2004.groupby('STATEID').size()
total_females_per_state_2011 = female_data_2011.groupby('STATEID').size()

# Group by STATEID and industry to get counts of each industry per state for 2004 and 2011
industry_counts_2004 = female_data_2004.groupby(['STATEID', 'industry']).size().unstack(fill_value=0)
industry_counts_2011 = female_data_2011.groupby(['STATEID', 'industry']).size().unstack(fill_value=0)

# Calculate proportions for each industry within each state
industry_proportions_2004 = industry_counts_2004.div(total_females_per_state_2004, axis=0)
industry_proportions_2011 = industry_counts_2011.div(total_females_per_state_2011, axis=0)

# Update the columns with industry names
industry_proportions_2004.columns = [industry_dict.get(i, f"Industry {i}") for i in industry_proportions_2004.columns]
industry_proportions_2011.columns = [industry_dict.get(i, f"Industry {i}") for i in industry_proportions_2011.columns]

# Update the index with state names
industry_proportions_2004.index = [state_dict.get(i, f"State {i}") for i in industry_proportions_2004.index]
industry_proportions_2011.index = [state_dict.get(i, f"State {i}") for i in industry_proportions_2011.index]

# Set up a grid of plots
fig, axes = plt.subplots(6, 6, figsize=(20, 20))  # Create a 6x6 grid for 34 states
axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

# Loop through states and plot top 5 industries for each
for i, state in enumerate(industry_proportions_2011.index):
    # Get the top 5 industries by proportion for the current state in 2011
    top_industries_2011 = industry_proportions_2011.loc[state].sort_values(ascending=False).head(5)
    industries_to_compare = top_industries_2011.index

    # Get the corresponding proportions for 2004 and fill missing industries with zero
    top_industries_2004 = industry_proportions_2004.reindex(index=industry_proportions_2011.index, columns=industries_to_compare, fill_value=0).loc[state, industries_to_compare]

    # Create a DataFrame to hold both years' data
    comparison_df = pd.DataFrame({
        '2011': top_industries_2011.values,
        '2004': top_industries_2004.values
    }, index=industries_to_compare)

    # Plot the side-by-side bars for each industry
    comparison_df.plot(kind='bar', ax=axes[i], color=['#007acc', '#ffae42'], width=0.8)
    axes[i].set_title(f"Top 5 in {state} (2011 vs 04)")
    axes[i].set_xlabel('Industry')
    axes[i].set_ylabel('Proportion of Females')

    # Apply the percentage formatter to the y-axis
    axes[i].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


# ### Top 5 female industries for every state in 2004, compared with 2011 proportions

# In[162]:


""" Top 5 industries for every state in 2004, compared with 2011 proportions.
The top 5 industries are selected from 2004 data, with 2011 data for those same industries shown for comparison """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Calculate total females per state for 2004 and 2011 separately
total_females_per_state_2004 = female_data_2004.groupby('STATEID').size()
total_females_per_state_2011 = female_data_2011.groupby('STATEID').size()

# Group by STATEID and industry to get counts of each industry per state for 2004 and 2011
industry_counts_2004 = female_data_2004.groupby(['STATEID', 'industry']).size().unstack(fill_value=0)
industry_counts_2011 = female_data_2011.groupby(['STATEID', 'industry']).size().unstack(fill_value=0)

# Calculate proportions for each industry within each state
industry_proportions_2004 = industry_counts_2004.div(total_females_per_state_2004, axis=0)
industry_proportions_2011 = industry_counts_2011.div(total_females_per_state_2011, axis=0)

# Update the columns with industry names
industry_proportions_2004.columns = [industry_dict.get(i, f"Industry {i}") for i in industry_proportions_2004.columns]
industry_proportions_2011.columns = [industry_dict.get(i, f"Industry {i}") for i in industry_proportions_2011.columns]

# Update the index with state names
industry_proportions_2004.index = [state_dict.get(i, f"State {i}") for i in industry_proportions_2004.index]
industry_proportions_2011.index = [state_dict.get(i, f"State {i}") for i in industry_proportions_2011.index]

# Set up a grid of plots
fig, axes = plt.subplots(6, 6, figsize=(20, 20))  # Create a 6x6 grid for 34 states
axes = axes.flatten()  # Flatten the 2D array of axes for easy iteration

# Loop through states and plot top 5 industries for each
for i, state in enumerate(industry_proportions_2004.index):
    # Get the top 5 industries by proportion for the current state in 2004
    top_industries_2004 = industry_proportions_2004.loc[state].sort_values(ascending=False).head(5)
    industries_to_compare = top_industries_2004.index

    # Get the corresponding proportions for 2011 and fill missing industries with zero
    top_industries_2011 = industry_proportions_2011.reindex(index=industry_proportions_2004.index, columns=industries_to_compare, fill_value=0).loc[state, industries_to_compare]

    # Create a DataFrame to hold both years' data
    comparison_df = pd.DataFrame({
        '2004': top_industries_2004.values,
        '2011': top_industries_2011.values
    }, index=industries_to_compare)

    # Plot the side-by-side bars for each industry
    comparison_df.plot(kind='bar', ax=axes[i], color=['#ffae42', '#007acc'], width=0.8)
    axes[i].set_title(f"Top 5 in {state} (2004 vs 11)")
    axes[i].set_xlabel('Industry')
    axes[i].set_ylabel('Proportion of Females')

    # Apply the percentage formatter to the y-axis
    axes[i].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))

# Adjust layout and display the plot
plt.tight_layout()
plt.show()


# ### Top 20 industries that females work in across India for 2011 and 2004

# In[5]:


""" Top 20 industries that females work in across India for 2011 and 2004 (other year shown alongside for comparison in both cases).
Note that proportions on x-axis account for missing data and that about 80% of observations have industry as empty """

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Calculate total females for 2004 and 2011, including missing 'industry'
total_females_2004 = len(female_data_2004)
total_females_2011 = len(female_data_2011)

# Calculate industry counts and proportions for 2004 and 2011
industry_counts_2004 = female_data_2004['industry'].value_counts()
industry_counts_2011 = female_data_2011['industry'].value_counts()

# Calculate proportions for each industry
industry_proportions_2004 = industry_counts_2004 / total_females_2004
industry_proportions_2011 = industry_counts_2011 / total_females_2011

# Update the industry names based on a dictionary
industry_proportions_2004.index = [industry_dict.get(i, f"Industry {i}") for i in industry_proportions_2004.index]
industry_proportions_2011.index = [industry_dict.get(i, f"Industry {i}") for i in industry_proportions_2011.index]

# Get the top 20 industries by proportion in 2011
top_20_industries_2011 = industry_proportions_2011.sort_values(ascending=False).head(20)

# Ensure the same industries are included from 2004 for comparison
industry_proportions_2004_top20 = industry_proportions_2004.reindex(index=top_20_industries_2011.index, fill_value=0)

# Create a DataFrame for plotting with both years
comparison_df = pd.DataFrame({
    '2011': top_20_industries_2011.values,
    '2004': industry_proportions_2004_top20.values
}, index=top_20_industries_2011.index)

# Sort the DataFrame in descending order by the 2011 proportions
comparison_df = comparison_df.sort_values(by='2011', ascending=True)

# Create side-by-side subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot for 2011 vs 2004 (Proportions of Females in Industries)
comparison_df.plot(kind='bar', ax=axes[0], color=['#007acc', '#ffae42'])
axes[0].set_title("Top 20 Industries of Females in India in 2011")
axes[0].set_xlabel("Industry")
axes[0].set_ylabel("Proportion of Females")
axes[0].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))  # Format y-axis as percentages
axes[0].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for clarity

# For the second graph (2004 vs 2011), adjust as needed
industry_proportions_2004_top20_sorted = industry_proportions_2004.sort_values(ascending=False).head(20)
industry_proportions_2011_top20_sorted = industry_proportions_2011.reindex(index=industry_proportions_2004_top20_sorted.index, fill_value=0)

# Plot for 2004 vs 2011 (Proportions of Females in Industries)
comparison_df_sorted = pd.DataFrame({
    '2004': industry_proportions_2004_top20_sorted.values,
    '2011': industry_proportions_2011_top20_sorted.values
}, index=industry_proportions_2004_top20_sorted.index).sort_values(by='2004', ascending=True)

comparison_df_sorted.plot(kind='bar', ax=axes[1], color=['#007acc', '#ffae42'])
axes[1].set_title("Top 20 Industries of Females in India in 2004")
axes[1].set_xlabel("Industry")
axes[1].set_ylabel("Proportion of Females")
axes[1].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))  # Format y-axis as percentages
axes[1].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for clarity

# Adjust layout for better fit
plt.tight_layout()
plt.show()


# ### RELIGIONB and top 20 industries females work in

# In[8]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Calculate industry counts and religion counts for 2004 and 2011
industry_religion_counts_2004 = female_data_2004.groupby(['industry', 'RELIGIONB']).size().unstack(fill_value=0)
industry_religion_counts_2011 = female_data_2011.groupby(['industry', 'RELIGIONB']).size().unstack(fill_value=0)

# Calculate proportions for each religion within each industry
industry_religion_proportions_2004 = industry_religion_counts_2004.div(industry_religion_counts_2004.sum(axis=1), axis=0)
industry_religion_proportions_2011 = industry_religion_counts_2011.div(industry_religion_counts_2011.sum(axis=1), axis=0)

# Get the top 20 industries by total female proportion for 2011
top_20_industries_2011 = industry_religion_proportions_2011.sum(axis=1).sort_values(ascending=False).head(20)

# Ensure the same industries are included from 2004 for comparison
industry_religion_proportions_2004_top20 = industry_religion_proportions_2004.loc[top_20_industries_2011.index]

# Create a DataFrame for plotting with both years
comparison_df = pd.DataFrame(index=top_20_industries_2011.index)

# Stack and add both years' proportions as columns
for year, data in zip([2004, 2011], [industry_religion_proportions_2004_top20, industry_religion_proportions_2011]):
    comparison_df[year] = data.loc[top_20_industries_2011.index].values.tolist()

# Now sort the DataFrame in descending order by the 2011 proportions
comparison_df = comparison_df.sort_values(by=2011, ascending=True)

# Create side-by-side subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot for 2011 vs 2004 (Proportions of Females in Industries)
industry_religion_proportions_2011.loc[top_20_industries_2011.index].plot(kind='bar', stacked=True, ax=axes[0],
                                                                           color=[plt.cm.Paired(i) for i in range(9)], width=0.8)
axes[0].set_title("Top 20 Industries of Females in India in 2011 by religion")
axes[0].set_xlabel("Industry")
axes[0].set_ylabel("Proportion of Females")
axes[0].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))  # Format y-axis as percentages
axes[0].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for clarity
axes[0].set_xticklabels([industry_dict[i] for i in top_20_industries_2011.index], rotation=90)  # Use industry_dict for x-axis labels
axes[0].legend(title="Religion", labels=[religionb_dict[i] for i in range(1, 10)], bbox_to_anchor=(1.05, 1), loc='upper left')

# Plot for 2004 vs 2011 (Proportions of Females in Industries)
industry_religion_proportions_2004_top20.plot(kind='bar', stacked=True, ax=axes[1],
                                              color=[plt.cm.Paired(i) for i in range(9)], width=0.8)
axes[1].set_title("Top 20 Industries of Females in India in 2004 by religion")
axes[1].set_xlabel("Industry")
axes[1].set_ylabel("Proportion of Females")
axes[1].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))  # Format y-axis as percentages
axes[1].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for clarity
axes[1].set_xticklabels([industry_dict[i] for i in top_20_industries_2011.index], rotation=90)  # Use industry_dict for x-axis labels
axes[1].legend(title="Religion", labels=[religionb_dict[i] for i in range(1, 10)], bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout for better fit
plt.tight_layout()
plt.show()


# ### RELIGIONA and top 20 industries females work in

# In[10]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Function to format the y-axis labels as percentages without decimals
def percentage_formatter(x, pos):
    return f'{x*100:.0f}%'

# Filter for females (SEX == 2) for both 2004 and 2011
female_data_2004 = df[(df['SEX'] == 2) & (df['wave'] == 2004)]
female_data_2011 = df[(df['SEX'] == 2) & (df['wave'] == 2011)]

# Calculate industry counts and religion counts for 2004 and 2011
industry_religion_counts_2004 = female_data_2004.groupby(['industry', 'RELIGIONA']).size().unstack(fill_value=0)
industry_religion_counts_2011 = female_data_2011.groupby(['industry', 'RELIGIONA']).size().unstack(fill_value=0)

# Calculate proportions for each religion within each industry
industry_religion_proportions_2004 = industry_religion_counts_2004.div(industry_religion_counts_2004.sum(axis=1), axis=0)
industry_religion_proportions_2011 = industry_religion_counts_2011.div(industry_religion_counts_2011.sum(axis=1), axis=0)

# Get the top 20 industries by total female proportion for 2011
top_20_industries_2011 = industry_religion_proportions_2011.sum(axis=1).sort_values(ascending=False).head(20)

# Ensure the same industries are included from 2004 for comparison
industry_religion_proportions_2004_top20 = industry_religion_proportions_2004.loc[top_20_industries_2011.index]

# Create a DataFrame for plotting with both years
comparison_df = pd.DataFrame(index=top_20_industries_2011.index)

# Stack and add both years' proportions as columns
for year, data in zip([2004, 2011], [industry_religion_proportions_2004_top20, industry_religion_proportions_2011]):
    comparison_df[year] = data.loc[top_20_industries_2011.index].values.tolist()

# Now sort the DataFrame in descending order by the 2011 proportions
comparison_df = comparison_df.sort_values(by=2011, ascending=True)

# Create side-by-side subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# Plot for 2011 vs 2004 (Proportions of Females in Industries)
industry_religion_proportions_2011.loc[top_20_industries_2011.index].plot(kind='bar', stacked=True, ax=axes[0],
                                                                           color=[plt.cm.Paired(i) for i in range(9)], width=0.8)
axes[0].set_title("Top 20 Industries of Females in India in 2011 by religion")
axes[0].set_xlabel("Industry")
axes[0].set_ylabel("Proportion of Females")
axes[0].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))  # Format y-axis as percentages
axes[0].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for clarity
axes[0].set_xticklabels([industry_dict[i] for i in top_20_industries_2011.index], rotation=90)  # Use industry_dict for x-axis labels
axes[0].legend(title="Religion", labels=[religiona_dict[i] for i in range(1, 8)], bbox_to_anchor=(1.05, 1), loc='upper left')

# Plot for 2004 vs 2011 (Proportions of Females in Industries)
industry_religion_proportions_2004_top20.plot(kind='bar', stacked=True, ax=axes[1],
                                              color=[plt.cm.Paired(i) for i in range(9)], width=0.8)
axes[1].set_title("Top 20 Industries of Females in India in 2004 by religion")
axes[1].set_xlabel("Industry")
axes[1].set_ylabel("Proportion of Females")
axes[1].yaxis.set_major_formatter(FuncFormatter(percentage_formatter))  # Format y-axis as percentages
axes[1].tick_params(axis='x', rotation=90)  # Rotate x-axis labels for clarity
axes[1].set_xticklabels([industry_dict[i] for i in top_20_industries_2011.index], rotation=90)  # Use industry_dict for x-axis labels
axes[1].legend(title="Religion", labels=[religiona_dict[i] for i in range(1, 8)], bbox_to_anchor=(1.05, 1), loc='upper left')

# Adjust layout for better fit
plt.tight_layout()
plt.show()


# In[ ]:




