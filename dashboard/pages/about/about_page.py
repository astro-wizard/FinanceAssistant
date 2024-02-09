# -*- coding: utf-8 -*-

"""
FinanceAssistant.dashboard.pages.about.about_page.py
---------


Created : 28 December 2023
Last Modified : 28 December 2023
"""


import dash
from dash import dcc
dash.register_page(__name__, path='/about')


layout = dcc.Markdown('''
## **Prabhat Tiwari**

Finance was developed by Prabhat Tiwari in 2023 for the LLM App Building Challenge.  

''')
