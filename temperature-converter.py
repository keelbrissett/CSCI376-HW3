from nicegui import ui

ui.colors(
      primary='#808080',
      secondary='#f59300',
      accent='#FFFFFF',
      positive='#009e1d',
      negative='#a80014',
      info='#1d1d1d',
      warning='#F2C037'
)

def convert():
    try: 
        temp = float(input_field.value)
        if conversion_type.value == "Celsius to Fahrenheit":
            result_label.set_text(f"{temp}°C = {temp * 9/5 + 32:.2f}°F")
        else:
            result_label.set_text(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")
        result_label.classes("text-lg font-semibold text-positive mt-4")
        # text-positive: Changes the color of the text to green
    except ValueError:
        result_label.set_text("Please enter a valid number.")
        result_label.classes("text-lg font-semibold text-negative mt-4")
        # text-negative: Changes the color of the text to red
with ui.row().classes("mx-auto"):
    with ui.card().classes("bg-gradient-to-b from-blue-400 to-transparent p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        # w-100: Set element width to be fixed at 100
        # p-6: Indicates the padding around text within a box
        # shadow-xl: Drop shadow of a box
        # mx-auto: Affects the horizontal alignments/centering of an item/text
        # mt-10: Affects the vertical alignments/centering of an item/text
        # rounded-xl: Rounds the corners of a container
        ui.label("Temperature Converter").classes("text-2xl font-bold text-accent mb-4")
        # text-2xl: Used to change the size of the text
        # font-bold: Makes the font bold
        # text-accent: Used to change the accent color of text
        # mb-4: Affects the margin below the text/box/container
        input_field = ui.input("Enter Temperature").props('type="number"').classes("w-full mb-4 p-2 text-lg border rounded shadow-xl bg-gray-100")
        # w-full: Set elemetn width to be the full width
        # border: Specifications for the border of the container
        # rounded: Rounds the corners of the box
        conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("text-white mb-4")
        convert_button = ui.button("Convert", on_click=convert).classes("delay-75 duration-100 transform hover:scale-110 transition ease-linear text-white font-bold py-2 px-4 rounded")
        # text-white: Makes the text white
        # py-2: Changes the top and bottom margins of the container
        # px-4: Changes the left and right margins of the container
        result_label = ui.label("").classes("text-lg mt-4")

    with ui.card().classes("bg-gradient-to-b from-green-600 to-transparent p-6 shadow-xl mx-auto mt-10 rounded-xl"):
        ui.label("New Temperature Converter").classes("text-2xl font-bold text-accent mb-4")

        number_input = ui.number(label="Enter Temperature", value=0, min=-50, max=100).classes("w-full mb-4 p-2 text-lg border rounded shadow-xl bg-gray-100")
        new_conversion_type = ui.radio(["Celsius to Fahrenheit", "Fahrenheit to Celsius"], value="Celsius to Fahrenheit").classes("text-white mb-4")
        new_result_label = ui.label("").classes("text-lg mt-4")

        # Converting temperature
        def convert_from_number_input():
            value = number_input.value  # Update Input
            if value is None:
                return
            if new_conversion_type.value == "Celsius to Fahrenheit":
                converted = (value * 9/5) + 32
                new_result_label.set_text(f"Converted: {converted:.2f}°F")
            else:
                converted = (value - 32) * 5/9
                new_result_label.set_text(f"Converted: {converted:.2f}°C")

        # Trigger conversion when input or radio changes
        number_input.on("update:modelValue", lambda _: convert_from_number_input())
        new_conversion_type.on("update:modelValue", lambda _: convert_from_number_input())


ui.run()
