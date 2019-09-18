COLOUR_HEX_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
                    "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                    "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74",
                    "azure1": "f0ffff"}

colour_name = input("Enter a name (names are case sensitive): ")
while colour_name != "":
    if colour_name not in COLOUR_HEX_CODES:
        print("Invalid name")
    else:
        print("The Hex code for", colour_name, "is", COLOUR_HEX_CODES.get(colour_name))
    colour_name = input("Enter a name: ")
