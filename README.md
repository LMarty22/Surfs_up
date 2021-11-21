# Surfs_up

## Overview of the Analysis

Analysis is performed to identify weather trends in Oahu, Hawaii for the months of June and December. 
Weather temperature trends will be used to determine if a surf and ice-cream shop business is sustainable year-round.

## Results

* The average temperature in the month of December is 3.90 degrees cooler than in June.
* The highest temperature difference between June and December is 2 degrees.
* The lowest temperature difference between June and December is 8 degrees. 

Please see statistical data below derived for months of June and December.

![Image June] 
![Image December]

##Summary

Based on the analysis conducted above, one can expect lower average temperatures in the month of December than June. If temperatures are a direct correlation of customer volume and frequency	 of visit to surf and ice cream shop, then in December the volume of customers will be less than in June. However, due to the slight drop in temperature, 3.90 degrees, this does not indicate severe weather change. Additional queries one should consider in order to determine impact of business between months of June vs December is the level or percipitation in each month. Precipitation would directly impact the surf shop business model as customers are less likely to go out surfing in inclement weather.

1.) june_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 6).all()

2.) dec_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date) == 12).all()


