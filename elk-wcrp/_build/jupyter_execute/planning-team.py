#!/usr/bin/env python
# coding: utf-8

# # Planning Team and Key Actors
# 
# Test {ref}`Table 1 <team_tbl>` reference.

# In[1]:


import pandas as pd
from myst_nb import glue
team_tbl = pd.read_csv("./tables/planning-team.csv")
team_tbl = team_tbl.style.hide_index()
team_tbl = team_tbl.set_caption("Table 1. Elk River WCRP Planning Team")    .set_table_styles([{
        'selector': 'caption',
        'props': 'caption-side: top;'
    }],overwrite=False)
glue("team_tbl", team_tbl)
#team_tbl


# ```{glue:figure} team_tbl
# :name: "team_tbl"
# ```
