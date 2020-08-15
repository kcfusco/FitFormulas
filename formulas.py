"""
Compilation of useful calculators for athletes.
Metric units used for input.
"""
from math import sqrt, log10

# Total Daily Energy Expenditure
def bmr(gender, weight, height, age, activity):
    """
    Basal Metabolic Rate, Harris-Benedict Equation
    :param gender: Male or female
    :param weight: Weight in kgs
    :param height: Height in cm
    :param age: Age in years
    :param activity: Sedentary, light, moderate, or active
    """
    c1 = c2 = c3 = c4 = 0

    if gender == 'm':
        c1 = 66.5
        c2 = 13.75
        c3 = 5.003
        c4 = 6.775
    elif gender == 'f':
        c1 = 655.1
        c2 = 9.563
        c3 = 1.850
        c4 = 4.676

    rate = c1 + (c2 * weight) + (c3 * height) - (c4 * age)

    if activity == 'sedentary':
        rate *= 1.2
    elif activity == 'light':
        rate *= 1.375
    elif activity == 'moderate':
        rate *= 1.55
    elif activity == 'active':
        rate *= 1.9
    return rate


# Body fat percentage
def bf_percentage(gender, height, waist, neck, hip=36):
    """
    Body fat percentage formula developed by the US Navy
    :param gender: Male or female
    :param height: Height in cm
    :param waist: Waist (at navel) in cm
    :param neck: Neck (at narrowest) in cm
    :param hip: Hip (at widest; for women only) in cm
    """
    bf = 0
    if gender == 'm':
        bf = 495 / (1.0324 - 0.19077 * log10(waist - neck) + 0.15456 * log10(height)) - 450
    elif gender == 'f':
        bf = 495 / (1.29579 - 0.35004 * log10(waist + hip - neck) + 0.22100 * log10(height)) - 450
    return bf


# Muscular potential models
# TODO: Double check these models work for women
def berkhan_model(height):
    """
    Also known as leangains model, created by Martin Berkhan
    The simplest formula here and thus the most prone to errors
    :param height: Height in cm
    :param imperial: If set to True, results are returned in lbs
    :return Max potential body weight for a stage-ready male bodybuilder at 5% body fat
            Max potential fat-free body weight (subtracts the 5% body fat)
    """
    weight = height - 100
    fat_free_mass = weight * 0.95


    return fat_free_mass


def fffmi_model(height, weight, bodyfat):
    """
    Fat Free Mass Index
    :param height: Height in m
    :param weight: Weight in kg
    :param bodyfat: The body fat percentage at which to predict maximum lean body mass
    :return Free Free Mass Index
            16 - 17: below average
            18 - 19: average
            20 - 21: above average
            22: excellent
            23 - 25: superior
            26 - 27: scores considered suspicious but still attainable naturally
            28 - 30: highly unlikely scores to be obtained naturally without steroid usage
    """
    fat_mass = bodyfat * weight
    lean_mass = weight - fat_mass
    ffmi = lean_mass / (height ** 2)
    ffmi_normalized = 6.1 * (1.8 - height)


def butts_model(height, wrist, ankle, bodyfat):
    """
    Developed by Dr. Casey Butt
    :param height: Height in cm
    :param wrist: Wrist circumference measured on the hand side of the styloid process (bony protrusion)
    :param ankle: Ankle circumference at the smallest point
    :param bodyfat: The body fat percentage at which to predict maximum lean body mass
                    Defaulted to 12 as this is the lowest reccomended bodyfat for powerlifters
    :return Max potential body weight at a given body fat %
            Max potential fat-free body weight at a given body fat %
    """
    max_lbm = ((height / 2.54) ** 1.5) * (sqrt((wrist / 2.54)) / 22.6670 + sqrt((ankle / 2.54)) / 17.0104) * \
              (bodyfat / 224 + 1)
    total_bw = (max_lbm / (100 - bodyfat)) * 100

    max_muscular_measurements = {'chest': (1.626 * wrist) + (1.3682 + ankle) + (0.3562 * height),
                                 'upper arm': (1.1709 * wrist) + (0.1350 * height),
                                 'forearm': (0.950 * wrist) + (0.1041 * height),
                                 'neck': (1.1875 * wrist) + (0.1301 * height),
                                 'thigh': (1.4737 * ankle) + (0.1918 * height),
                                 'calf': (0.9812 * ankle) + (0.1250 * height)
                                 }
    return total_bw / 2.205
