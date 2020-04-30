#Lab 11
#Author: Kyle Leslie

#Instructions:
#1. Make function to determine province based on input
#2. Determine whether urban or rural based on input
#3. Display error message if invalid character used
        # Second # indicates Rural or urban. 0 = rural
        # Invalid Letters D, F, I, O, Q, U W, Z

postal_code_map = {
    'A': 'Newfoundland',
    'B': 'Nova Scotia',
    'C': 'Prince Edward Island',
    'E': 'New Brunswick',
    'G': 'Quebec',
    'H': 'Quebec',
    'J': 'Quebec',
    'K': 'Ontario',
    'L': 'Ontario',
    'M': 'Ontario',
    'N': 'Ontario',
    'P': 'Ontario',
    'R': 'Manitoba',
    'S': 'Sasketchwan',
    'T': 'Alberta',
    'V': 'British Columbia',
    'X': 'Nunavut or Northwest Territories',
    'Y': 'Yukon'
}

postalString = input("Please input your postal code using capital letters>")

def parsePostal(d):
    extractedLetter = d[:1]
    extractedNumber = d[1:2]

    if extractedLetter in postal_code_map:
        province = "in " + postal_code_map[extractedLetter] + "!"

        if extractedNumber is '0':
            place = "This postal code is from a rural residence "
        else:
            place = "This postal code is from a non-rural residence "

        finalOutput = place + province

        return finalOutput

    else:
        error = "You have not entered a legitimate Canadian postal code! Try again."

    return error

parsePostal(postalString)
print(parsePostal(postalString))




