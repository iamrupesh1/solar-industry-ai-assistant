from pvlib.iotools import get_pvgis_hourly
import requests

def get_pvgis_irradiance(lat, lon):
    # Choose PVGIS database according to location coverage
    if 24 <= lat <= 50 and -125 <= lon <= -66:
        raddatabase = 'PVGIS-NSRDB'
    elif -60 <= lat <= 65 and -25 <= lon <= 45:
        raddatabase = 'PVGIS-SARAH'
    else:
        raddatabase = 'PVGIS-ERA5'  # fallback global

    try:
        data, meta = get_pvgis_hourly(
            latitude=lat,
            longitude=lon,
            start=2015,
            end=2015,
            raddatabase=raddatabase,
            surface_tilt=35,
            surface_azimuth=180,
            pvcalculation=True,
            peakpower=1,
            pvtechchoice='crystSi',
            mountingplace='free',
            loss=14,
            trackingtype=0,
            optimal_surface_tilt=False,
            optimalangles=False,
            url='https://re.jrc.ec.europa.eu/api/v5_2/'
        )

        if 'poa_global' in data.columns:
            irradiance = data['poa_global'].sum()
        elif 'E' in data.columns:
            irradiance = data['E'].sum()
        else:
            irradiance = data.select_dtypes(include='number').sum().max()

        annual_irradiance_kwh = irradiance / 1000  # Wh to kWh
        return annual_irradiance_kwh

    except requests.HTTPError as e:
        print(f"PVGIS API error: {e}")
        return None
