import pysurfline

sport_forecasts = pysurfline.get_spot_forecasts(
    spotId='5cbf8d85e7b15800014909e8',
    days=2,
    intervalHours=3
)

print(sport_forecasts.name)