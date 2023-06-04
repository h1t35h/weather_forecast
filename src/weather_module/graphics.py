import pytermgui as ptg

def get_temp_string(temprature):
    color_prefix = "[bold lightgreen]"
    if temprature > 30:
        color_prefix = "[bold orange]"
    elif temprature < 10:
        color_prefix = "[bold cyan]"
    return f"{color_prefix} {temprature}°C"

def display_weather(weather_data):
    with ptg.WindowManager() as manager:
        manager.layout.add_slot("Body")

        container = ptg.Container(
            f"[bold aquamarine] Weather for {weather_data['name']}",
            "",
            {f"Actual temperature: {get_temp_string(weather_data['main']['temp'])}": 
            f"Feels like: {get_temp_string(weather_data['main']['feels_like'])}"},
            f"humidity is at {weather_data['main']['humidity']}",
            "",
            (f"cloudiness: {weather_data['clouds']['all']}" ),
            "",
            ptg.Button("Exit", lambda *_ : manager.stop())
        )
        window = ptg.Window("Weather Forecaster", container)
        manager.add(window)