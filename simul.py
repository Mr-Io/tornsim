import math
import copy
import matplotlib.pyplot as plt

import numpy as np

from tqdm import tqdm

from model import Player, BSS, GYM



BALANCED_R = {"str": 1,
              "spe": 1,
              "def": 1,
              "dex": 1,}

HANK_R_DEF = {"str": 4,
              "spe": 4,
              "def": 5.2,
              "dex": 1,}

HANK_R_DEX = {"str": 4,
              "spe": 4,
              "def": 1,
              "dex": 5.2,}

BALD_R_DEF = {"str": 72,
              "spe": 72,
              "def": 80,
              "dex": 105,}

BALD_R_DEX = {"str": 72,
              "spe": 72,
              "def": 80,
              "dex": 105,}

BALD_R_STR = {"str": 72,
              "spe": 72,
              "def": 80,
              "dex": 105,}

BALD_R_SPE = {"str": 72,
              "spe": 72,
              "def": 80,
              "dex": 105,}

NO_DEX_RAT = {"str": 1,
              "spe": 1,
              "def": 1.5, #1.25 to 1.6
              "dex": 0}

NO_DEF_RAT = {"str": 1,
              "spe": 1,
              "def": 0, #1.25 to 1.6
              "dex": 1.5,}

PERKS_PI = {"str": [0.02],
            "spe": [0.02],
            "def": [0.02],
            "dex": [0.02],}

PERKS_PI_05 = {"str": [0.02, 0.05],
               "spe": [0.02, 0.05],
               "def": [0.02, 0.05],
               "dex": [0.02, 0.05],}

PERKS_PI_10 = {"str": [0.02, 0.1],
               "spe": [0.02, 0.1],
               "def": [0.02, 0.1],
               "dex": [0.02, 0.1],}

PERKS_PI_15 = {"str": [0.02, 0.15],
               "spe": [0.02, 0.15],
               "def": [0.02, 0.15],
               "dex": [0.02, 0.15],}

def simul(total_energy, training_energy, player, force_ratio=False):
    en = total_energy
    et = training_energy
    for _ in tqdm(range(0, en, et), desc=f"training player {player.name}"):
        if force_ratio:
            player.train(et, ratio=player.ratio)
        else:
            player.train(et)

""""
# player example
bal_forc = Player("bal_forc", ratio=BALANCED_R)
bal_musi = Player("balanced", ratio=BALANCED_R, music_store=True)
balanced = Player("balanced", ratio=BALANCED_R)
hank_def = Player("hank_def", ratio=HANK_R_DEF)
hank_dex = Player("hank_dex", ratio=HANK_R_DEX)
bald_def = Player("bald_def", ratio=BALD_R_DEF)
bald_dex = Player("bald_dex", ratio=BALD_R_DEX)
bald_str = Player("bald_str", ratio=BALD_R_STR)
bald_spe = Player("bald_spe", ratio=BALD_R_SPE)
no_dex   = Player("no_dex", ratio=NO_DEX_RAT, notrain=["dex"])
no_def   = Player("no_def", ratio=NO_DEF_RAT, notrain=["def"])



for p in (bal_musi, balanced, hank_def, hank_dex, bald_def, bald_dex, bald_str, bald_spe, no_dex, no_def):
    if p.gym_index < 19:
        simul(int(1500*365*10), 100, p)
    else:
        simul(int(1500*365*10), 100, p, force_ratio=True)
        
"""