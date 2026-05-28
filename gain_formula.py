
import math

########### PARAMETERS #############
# specific stats parameters
OD_CHANCES={
    "XANAX": 1/33,
    "ECSTASY": 1/22,
}
PARAMS = {
    "str": {
        "A": 1600,
        "B": 1700, 
        "C": 700},
    "def": {
        "A": 2100,
        "B": -600, 
        "C": 1500},
    "dex": {
        "A": 1800,
        "B": 1500, 
        "C": 1000,
    },
    "spe": {
        "A": 1600,
        "B": 2000, 
        "C": 1350,
    }

}
BATTLESTAT_MAX = 50e6
# specific gym parameters
GYM = [
    {"name": "Premier Fitness", "e": 5, "unlock_e": 0, "str": 2.0, "spe": 2.0, "def": 2.0, "dex": 2.0, "e_spent": 0},
    {"name": "Average Joes", "e": 5, "unlock_e": 200, "str": 2.4, "spe": 2.4, "def": 2.8, "dex": 2.4, "e_spent": 0},
    {"name": "Woody's Workout", "e": 5, "unlock_e": 500, "str": 2.8, "spe": 3.2, "def": 3.0, "dex": 2.8, "e_spent": 0},
    {"name": "Beach Bods", "e": 5, "unlock_e": 1000, "str": 3.2, "spe": 3.2, "def": 3.2, "dex": 0.0, "e_spent": 0},
    {"name": "Silver Gym", "e": 5, "unlock_e": 2000, "str": 3.4, "spe": 3.6, "def": 3.4, "dex": 3.2, "e_spent": 0},
    {"name": "Pour Femme", "e": 5, "unlock_e": 2750, "str": 3.4, "spe": 3.6, "def": 3.6, "dex": 3.8, "e_spent": 0},
    {"name": "Davies Den", "e": 5, "unlock_e": 3000, "str": 3.7, "spe": 0.0, "def": 3.7, "dex": 3.7, "e_spent": 0},
    {"name": "Global Gym", "e": 5, "unlock_e": 3500, "str": 4.0, "spe": 4.0, "def": 4.0, "dex": 4.0, "e_spent": 0},
    {"name": "Knuckle Heads", "e": 10, "unlock_e": 4000, "str": 4.8, "spe": 4.4, "def": 4.0, "dex": 4.2, "e_spent": 0},
    {"name": "Pioneer Fitness", "e": 10, "unlock_e": 6000, "str": 4.4, "spe": 4.5, "def": 4.8, "dex": 4.4, "e_spent": 0},
    {"name": "Anabolic Anomalies", "e": 10, "unlock_e": 7000, "str": 5.0, "spe": 4.5, "def": 5.2, "dex": 4.5, "e_spent": 0},
    {"name": "Core", "e": 10, "unlock_e": 8000, "str": 5.0, "spe": 5.2, "def": 5.0, "dex": 5.0, "e_spent": 0},
    {"name": "Racing Fitness", "e": 10, "unlock_e": 11000, "str": 5.0, "spe": 5.4, "def": 4.8, "dex": 5.2, "e_spent": 0},
    {"name": "Complete Cardio", "e": 10, "unlock_e": 12420, "str": 5.5, "spe": 5.8, "def": 5.5, "dex": 5.2, "e_spent": 0},
    {"name": "Legs, Bums and Tums", "e": 10, "unlock_e": 18000, "str": 0.0, "spe": 5.6, "def": 5.6, "dex": 5.8, "e_spent": 0},
    {"name": "Deep Burn", "e": 10, "unlock_e": 18100, "str": 6.0, "spe": 6.0, "def": 6.0, "dex": 6.0, "e_spent": 0},
    {"name": "Apollo Gym", "e": 10, "unlock_e": 24140, "str": 6.0, "spe": 6.2, "def": 6.4, "dex": 6.2, "e_spent": 0},
    {"name": "Gun Shop", "e": 10, "unlock_e": 31260, "str": 6.6, "spe": 6.4, "def": 6.2, "dex": 6.2, "e_spent": 0},
    {"name": "Force Training", "e": 10, "unlock_e": 36610, "str": 6.4, "spe": 6.6, "def": 6.4, "dex": 6.8, "e_spent": 0},
    {"name": "Cha Cha's", "e": 10, "unlock_e": 46640, "str": 6.4, "spe": 6.4, "def": 6.8, "dex": 7.0, "e_spent": 0},
    {"name": "Atlas", "e": 10, "unlock_e": 56520, "str": 7.0, "spe": 6.4, "def": 6.4, "dex": 6.6, "e_spent": 0},
    {"name": "Last Round", "e": 10, "unlock_e": 67775, "str": 6.8, "spe": 6.6, "def": 7.0, "dex": 6.6, "e_spent": 0},
    {"name": "The Edge", "e": 10, "unlock_e": 84535, "str": 6.8, "spe": 7.0, "def": 7.0, "dex": 6.8, "e_spent": 0},
    {"name": "George's", "e": 10, "unlock_e": 106305, "str": 7.3, "spe": 7.3, "def": 7.3, "dex": 7.3, "e_spent": 0},

    {"name": "Balboas Gym", "e": 25, "unlock_e": None, "str": 0.0, "spe": 0.0, "def": 7.5, "dex": 7.5, "e_spent": 0},
    {"name": "Frontline Fitness", "e": 25, "unlock_e": None, "str": 7.5, "spe": 7.5, "def": 0.0, "dex": 0.0, "e_spent": 0},
    {"name": "Gym 3000", "e": 50, "unlock_e": None, "str": 8.0, "spe": 0.0, "def": 0.0, "dex": 0.0, "e_spent": 0},
    {"name": "Mr. Isoyamas", "e": 50, "unlock_e": None, "str": 0.0, "spe": 0.0, "def": 8.0, "dex": 0.0, "e_spent": 0},
    {"name": "Total Rebound", "e": 50, "unlock_e": None, "str": 0.0, "spe": 8.0, "def": 0.0, "dex": 0.0, "e_spent": 0},
    {"name": "Elites", "e": 50, "unlock_e": None, "str": 0.0, "spe": 0.0, "def": 0.0, "dex": 8.0, "e_spent": 0},
    {"name": "The Sports Science Lab", "e": 25, "unlock_e": None, "str": 9.0, "spe": 9.0, "def": 9.0, "dex": 9.0, "e_spent": 0},
    {"name": "Fight Club", "e": 10, "unlock_e": None, "str": 10.0, "spe": 10.0, "def": 10.0, "dex": 10.0, "e_spent": 0},

    {"name": "Crims Gym", "e": 5, "unlock_e": None, "str": 3.4, "spe": 3.4, "def": 4.5, "dex": 0.0, "e_spent": 0},
]

en_unlock_cum = 0
for i in range(0, 24):
    en_unlock_cum += GYM[i]["unlock_e"]
    GYM[i]["unlock_en_cum"] = en_unlock_cum




############ GYM FORMULA ############
def _estimated_gains(happy, stat, battlestat, gym, perks: list):
    # !! HASTA QUE VALOR DE HAPPY ESTA FUNCION ES ESTRICTAMENTE CRECIENTE!??? -> hasta 45M de happy
    if stat > BATTLESTAT_MAX:
        stat = BATTLESTAT_MAX
    part_1 = stat*round(1 + 0.07* round(math.log(1+happy/250),4), 4)
    part_2 = 8 * pow(happy, 1.05) 
    part_3 = (1-pow(happy/99999, 2)) * PARAMS[battlestat]["A"]+ PARAMS[battlestat]["B"] 
    part_4 = (1/200000) * gym[battlestat] * gym["e"]

    part_perks = 1
    for p in perks:
        part_perks *= (1+p) 
    
    value = (part_1 + part_2 + part_3) * part_4 * part_perks
    random_part = PARAMS[battlestat]["C"] * part_4 * part_perks
    happy_loss = gym["e"]/2

    return {"value": value,
            "happy": -happy_loss,
            "var": random_part}

########## NORMALIZED GAINS ###################

def train(happy, stat, energy, battlestat, gym, perks:list):
    """try to do energy a multiple of 50"""
    while (energy >= gym["e"]):
        res = _estimated_gains(happy, stat, battlestat=battlestat, gym=gym, perks=perks)
        energy -= gym["e"]
        stat += res["value"]
        happy += res["happy"]
        if happy < 0:
            happy = 0
    if energy > 0:
        raise ValueError(f"{energy} energy left for train")
    
    return {"stat": stat, 
            "happy": happy}