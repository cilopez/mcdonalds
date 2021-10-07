from sklearn.neighbors import BallTree

df_police = dataframe[dataframe['type']=='police']
# Construcción Ball Tree
ball_police = BallTree(df_police[["latitude_rad", "longitude_rad"]].values, metric='haversine')