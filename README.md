# What planes are flying around me?

## AKA How to use PiAware to capture flights around San Francisco August-September 2019

Using a RaspberryPi3 and a NooElec Software Defined Radio -- I've been collecting flights passing within ~100 mile of Potrero Hill, San Francisco, CA (37.75956, -122.39334) for the last few months.

[FlightAware](https://flightaware.com/) created the impressive ADS-B flight tracking software [PiAware](https://flightaware.com/adsb/piaware/) which -- combined with their own sensors enables FlightAware to have high quality information about flights around the world. Take a look at the data coming off my receiver at: 

https://flightaware.com/adsb/stats/user/wasauce#stats-106041



A quick look at the setup:

![piNooElec.png](/Users/wferrell/Documents/piNooElec.png)



---

## The Data

FlightAware & PiAware don't make it easy for you to keep a copy of all the flight data captured with your receiver. I wrote a little script to fetch the data every 10 seconds.

A single example files can be found here:

[`1567969448.9--DAL1390--a4366a51-6d59-48dc-b53c-1906202a7992.json`]([https://github.com/wasauce/piaware-flightdata/blob/master/1567969448.9--DAL1390--a4366a51-6d59-48dc-b53c-1906202a7992.json](https://github.com/wasauce/piaware-flightdata/blob/master/1567969448.9--DAL1390--a4366a51-6d59-48dc-b53c-1906202a7992.json))

I've included the key information in the filename

`1567969448.9` is the UTC timestamp of when the data was gathered

`DAL1390` is the flight information (Airline + flight number)

`a4366a51-6d59-48dc-b53c-1906202a7992` is just a random UUID I appended.



Take a look at what you will find inside the JSON file here:

```json
{
  "gva": 2,
  "gs": 398.5,
  "hex": "a448ba",
  "nac_v": 1,
  "seen": 0,
  "nav_altitude_mcp": 11008,
  "nac_p": 9,
  "category": "A3",
  "sil_type": "perhour",
  "lon": -122.701224,
  "alt_baro": 15900,
  "version": 2,
  "nav_qnh": 1016.8,
  "rc": 186,
  "nav_heading": 156.8,
  "alt_geom": 16600,
  "sil": 3,
  "squawk": "6063",
  "flight": "DAL1390",
  "emergency": "none",
  "track": 166.8,
  "nic": 8,
  "mlat": [],
  "sda": 2,
  "lat": 37.993842,
  "baro_rate": -2112,
  "tisb": [],
  "messages": 1730,
  "rssi": -16.3,
  "nic_baro": 1,
  "seen_pos": 0,
  "piaware-utctimestamp": 1567969448.9,
  "timeutc": "2019/09/08 19:04"
}
```

The full `clean` data following the above format is available in the [clean directory](https://github.com/wasauce/piaware-flightdata/tree/master/clean)



---

# Visualizing Flights around Potrero Hill, San Francisco, CA

## See the data on a map using Kepler.gl:

![Flights_Around_Potrero_Hill_Aug_Sept_2019.gif](https://github.com/wasauce/piaware-flightdata/blob/master/Flights_Around_Potrero_Hill_Aug_Sept_2019.gif)

Full video: [https://www.youtube.com/watch?v=4uYzdsCbLXQ](https://www.youtube.com/watch?v=4uYzdsCbLXQ)

## [Click to play with the data in Kepler](https://kepler.gl/demo/map?mapUrl=https://dl.dropboxusercontent.com/s/pqvrvdi9bpe92vt/keplergl_spv7qf.json)
