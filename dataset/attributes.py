class Attributes:
    id = 'ID'
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

    def get_hover_data_for_weather(self):
        return [
            Attributes.id,
            Attributes.overall_weather_condition,
            Attributes.summarise_weather,
            Attributes.cloud_cover,
            Attributes.humidity,
            Attributes.visibility,
            Attributes.pressure,
        ]

    def get_hover_data_for_electric(self):
        return [
            Attributes.id,
            Attributes.dishwasher,
            Attributes.living_room,
            Attributes.furnace_1,
            Attributes.furnace_2,
            Attributes.microwave,
            Attributes.fridge,
            Attributes.wine_cellar,
            Attributes.well,
            Attributes.kitchen_1,
            Attributes.kitchen_2,
            Attributes.kitchen_3,
            Attributes.barn
        ]

    def get_hover_data_for_all(self):
        return [
            Attributes.id,
            Attributes.total_energy_consumption,
            Attributes.total_energy_generated,
            Attributes.overall_house_energy_consumption,
            Attributes.humidity,
            Attributes.summarise_weather
        ]

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

    def all_attributes(self):
        return self.get_weather_attributes()+self.get_appliance_attributes()

    def get_appliance_attributes(self):
        return [
            Attributes.dishwasher,
            Attributes.furnace_1,
            Attributes.furnace_2,
            Attributes.home_office,
            Attributes.fridge,
            Attributes.wine_cellar,
            Attributes.garage_door,
            Attributes.kitchen_1,
            Attributes.kitchen_2,
            Attributes.kitchen_3,
            Attributes.barn,
            Attributes.well,
            Attributes.microwave,
            Attributes.living_room
        ]

    def get_weather_attributes(self):
        return [
            Attributes.temperature,
            # Attributes.overall_weather_condition,
            Attributes.humidity,
            Attributes.visibility,
            # Attributes.summarise_weather,
            Attributes.apparent_temperature,
            Attributes.pressure,
            # Attributes.cloud_cover,
            Attributes.wind_bearing,
            Attributes.precipitation_intensity,
            Attributes.dew_point,
            Attributes.precipitation_probability

        ]

    def get_non_numeric_attributes(self):
        return [
            Attributes.overall_weather_condition,
            Attributes.summarise_weather,
            Attributes.cloud_cover
        ]

    def get_rolling_attributes(self):
        return [
            Attributes.total_energy_consumption,
            Attributes.total_energy_generated,
            Attributes.overall_house_energy_consumption,
            Attributes.dishwasher,
            Attributes.furnace_1,
            Attributes.furnace_2,
            Attributes.home_office,
            Attributes.fridge,
            Attributes.wine_cellar,
            Attributes.garage_door,
            Attributes.kitchen_1,
            Attributes.kitchen_2,
            Attributes.kitchen_3,
            Attributes.barn,
            Attributes.well,
            Attributes.microwave,
            Attributes.living_room,
            Attributes.solar_power_generation,
            Attributes.temperature,
            Attributes.humidity,
            Attributes.visibility,
            Attributes.apparent_temperature,
            Attributes.pressure,
            Attributes.wind_speed,
            Attributes.wind_bearing,
            Attributes.precipitation_intensity,
            Attributes.dew_point,
            Attributes.precipitation_probability
        ]

    def get_numeric_attributes(self):
        return [
            Attributes.day,
            Attributes.hour,
            Attributes.minute,
            Attributes.total_energy_consumption,
            Attributes.total_energy_generated,
            Attributes.overall_house_energy_consumption,
            Attributes.dishwasher,
            Attributes.furnace_1,
            Attributes.furnace_2,
            Attributes.home_office,
            Attributes.fridge,
            Attributes.wine_cellar,
            Attributes.garage_door,
            Attributes.kitchen_1,
            Attributes.kitchen_2,
            Attributes.kitchen_3,
            Attributes.barn,
            Attributes.well,
            Attributes.microwave,
            Attributes.living_room,
            Attributes.solar_power_generation,
            Attributes.temperature,
            Attributes.humidity,
            Attributes.visibility,
            Attributes.apparent_temperature,
            Attributes.pressure,
            Attributes.wind_speed,
            Attributes.wind_bearing,
            Attributes.precipitation_intensity,
            Attributes.dew_point,
            Attributes.precipitation_probability
        ]

    def get_attr_list(self):
        return [
            Attributes.day,
            Attributes.hour,
            Attributes.minute,
            Attributes.total_energy_consumption,
            Attributes.total_energy_generated,
            Attributes.overall_house_energy_consumption,
            Attributes.dishwasher,
            Attributes.furnace_1,
            Attributes.furnace_2,
            Attributes.home_office,
            Attributes.fridge,
            Attributes.wine_cellar,
            Attributes.garage_door,
            Attributes.kitchen_1,
            Attributes.kitchen_2,
            Attributes.kitchen_3,
            Attributes.barn,
            Attributes.well,
            Attributes.microwave,
            Attributes.living_room,
            Attributes.solar_power_generation,
            Attributes.temperature,
            Attributes.overall_weather_condition,
            Attributes.humidity,
            Attributes.visibility,
            Attributes.summarise_weather,
            Attributes.apparent_temperature,
            Attributes.pressure,
            Attributes.wind_speed,
            Attributes.cloud_cover,
            Attributes.wind_bearing,
            Attributes.precipitation_intensity,
            Attributes.dew_point,
            Attributes.precipitation_probability
        ]
