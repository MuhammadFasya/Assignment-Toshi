def konversi_suhu(celcius):
    try:
      c = float(celcius)
      fahrenheit = (c * 9/5) + 32
      kelvin = c + 273.15

      return f"Fahrenheit: {fahrenheit:.2f}\nKelvin: {kelvin:.2f}"
    
    except ValueError:
        return "Error: Invalid input."