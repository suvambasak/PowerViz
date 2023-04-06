class Attributes:
    day = 'day'
    hour = 'hour'
    minute = 'minute'
    total_energy_consumption = 'use [kW]'
    total_energy_generated = 'gen [kW]'
    overall_house_energy_consumption = 'House overall [kW]'
    dishwasher = 'Dishwasher [kW]'
    furnace_1 = 'Furnace 1 [kW]'
    furnace_2 = 'Furnace 2 [kW]'
    home_office = 'Home office [kW]'
    fridge = 'Fridge [kW]'
    wine_cellar = 'Wine cellar [kW]'
    garage_door = 'Garage door [kW]'
    kitchen_1 = 'Kitchen 12 [kW]'
    kitchen_2 = 'Kitchen 14 [kW]'
    kitchen_3 = 'Kitchen 38 [kW]'
    barn = 'Barn [kW]'
    well = 'Well [kW]'
    microwave = 'Microwave [kW]'
    living_room = 'Living room [kW]'
    solar_power_generation = 'Solar [kW]'
    temperature = 'temperature'
    overall_weather_condition = 'icon'
    humidity = 'humidity'
    visibility = 'visibility'
    summarise_weather = 'summary'
    apparent_temperature = 'apparentTemperature'
    pressure = 'pressure'
    wind_speed = 'windSpeed'
    cloud_cover = 'cloudCover'
    wind_bearing = 'windBearing'
    precipitation_intensity = 'precipIntensity'
    dew_point = 'dewPoint'
    precipitation_probability = 'precipProbability'

    def build_labels(self):
        return {
            Attributes.day: 'day',
            Attributes.hour: 'hour',
            Attributes.minute: 'minute',
            Attributes.total_energy_consumption: 'Total energy use [kW]',
            Attributes.total_energy_generated: 'Total energy generated [kW]',
            Attributes.overall_house_energy_consumption: 'House overall consumption  [kW]',
            Attributes.dishwasher: 'Dish washer [kW]',
            Attributes.furnace_1: 'Furnace 1 [kW]',
            Attributes.furnace_2: 'Furnace 2 [kW]',
            Attributes.home_office: 'Home office [kW]',
            Attributes.fridge: 'Fridge [kW]',
            Attributes.wine_cellar: 'Wine cellar [kW]',
            Attributes.garage_door: 'Garage door [kW]',
            Attributes.kitchen_1: 'Kitchen 1 [kW]',
            Attributes.kitchen_2: 'Kitchen 1 [kW]',
            Attributes.kitchen_3: 'Kitchen 3 [kW]',
            Attributes.barn: 'Barn [kW]',
            Attributes.well: 'Well [kW]',
            Attributes.microwave: 'Microwave [kW]',
            Attributes.living_room: 'Living room [kW]',
            Attributes.solar_power_generation: 'Solar [kW]',
            Attributes.temperature: 'Temperature',
            Attributes.overall_weather_condition: 'Overall weather condition',
            Attributes.humidity: 'Humidity',
            Attributes.visibility: 'Visibility',
            Attributes.summarise_weather: 'Summary',
            Attributes.apparent_temperature: 'Apparent temperature',
            Attributes.pressure: 'Pressure',
            Attributes.wind_speed: 'Wind speed',
            Attributes.cloud_cover: 'Cloud cover',
            Attributes.wind_bearing: 'Wind bearing',
            Attributes.precipitation_intensity: 'Precipitation intensity',
            Attributes.dew_point: 'Dew point',
            Attributes.precipitation_probability: 'Precipitation Probability'

        }

    def get_attr_list(self):
        labels = self.build_labels()
        attr_list = []
        for attr in labels.keys():
            attr_list.append(labels[attr])
        return attr_list
