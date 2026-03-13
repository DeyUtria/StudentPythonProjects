import pandas as pd


ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(5))

views_per_platform = ad_clicks.groupby('utm_source').count().reset_index()

ad_clicks['is_click'] = ad_clicks.apply(lambda row: True if pd.notnull(row.ad_click_timestamp) else False, axis = 1)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()

clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] +
    clicks_pivot[False])

a_b_test = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(a_b_test)

percent = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
a_b_test_pivot = percent.pivot(columns='is_click', index='experimental_group', values='user_id').reset_index()
print(a_b_test_pivot)

a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
b_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

percentage_1 = a_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
percentage_1_pivot = percentage_1.pivot(columns='is_click', index='day', values='user_id').reset_index()
percentage_1_pivot['percent_clicked'] = \
   percentage_1_pivot[True] / \
   (percentage_1_pivot[True] +
    percentage_1_pivot[False])
print(percentage_1_pivot)


percentage_2 = b_clicks.groupby(['is_click', 'day']).user_id.count().reset_index()
percentage_2_pivot = percentage_2.pivot(columns='is_click', index='day', values='user_id').reset_index()
percentage_2_pivot['percent_clicked'] = \
   percentage_2_pivot[True] / \
   (percentage_2_pivot[True] +
    percentage_2_pivot[False])
print(percentage_2_pivot)