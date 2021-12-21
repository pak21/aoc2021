#!/usr/bin/env python3

import collections
import json
import sys

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

with open(sys.argv[1]) as f:
    data = json.load(f)

members = data['members'].values()
stars = []
for v in members:
    d = {'id': v['id']}
    for k2, v2 in v['completion_day_level'].items():
        for k3, v3 in v2.items():
            n = 2 * int(k2) + int(k3) - 3
            d[f'star{n}'] = v3['get_star_ts']
    stars.append(d)

df = pd.DataFrame(members).set_index('id').drop(['global_score', 'completion_day_level'], axis='columns')
stars_df = pd.DataFrame(stars).set_index('id')

for star in range(42):
    col_name = f'star{star}'
    foo = stars_df[[col_name]].sort_values(col_name).reset_index()
    foo['points'] = len(foo) + 1
    foo['points'] -= foo.index
    foo.loc[foo[col_name].isna(),'points'] = 0
    foo = foo.set_index('id')
    stars_df[f'points{star}'] = foo['points']

to_drop = filter(lambda s: s.startswith('star'), stars_df.columns)

stars_df = stars_df.drop(to_drop, axis='columns')

fig = plt.figure()
ax = plt.subplot(111)

for i in stars_df.index:
    if np.any(stars_df.loc[i].values):
        ax.plot(stars_df.loc[i].values, label=df.loc[i]['name'])

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()
