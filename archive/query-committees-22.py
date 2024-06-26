#!/usr/bin/env python3

"""Check finance records from CERS for MT political committees spending in 2022

run as: python3 query-committees-22.py
"""

from models.cers_interface import Interface

cers = Interface()

print('# Fetching committees')

# cers.list_2022_committees_with_spending()

# committees = cers.get_committee_by_name('Republican', fetchReports=False)
# Excludes ActBlue, which breaks script
committees = cers.get_2022_committees_with_spending()
committees.export('raw/committees')
