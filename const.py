num_pixels_background = 63 * 4
num_pixels_honey = 18 * 2
num_pixels_salted = 21 * 2

# Starting index for the letters.
idx_honey_start = ((27 * 4) + 2)
idx_salted_start = num_pixels_honey + ((33 * 4) + 2)

# The number of NeoPixels
num_pixels = num_pixels_background + num_pixels_honey + num_pixels_salted

# Calculate total amperage
amperage_max = num_pixels * 80 / 1000
amperage_limit = 20
brightness = min(.2, amperage_limit / amperage_max)

print("Maximum Brightness: %.2f" % brightness)

