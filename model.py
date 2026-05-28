
import copy
import math

import pandas as pd

from gain_formula import train, GYM

HAPPY = 5025
PERKS = {"str": [0.02, 0.1],
         "spe": [0.02, 0.1],
         "def": [0.02, 0.1],
         "dex": [0.02, 0.1],}
BSS = ["str", "spe", "def", "dex"]
class Player:
    def __init__(self, name, gym_index:int=0, happy:int=HAPPY, bstats={}, ratio={}, notrain=None, perks={}, music_store=False):
        self.name = name
        # player bars
        self.en = 0 
        self.en_spent = 0
        self.happy = happy
        # battlestats
        self.bstats = copy.deepcopy(bstats) 
        for bs in BSS:
            if not bs in self.bstats:
                self.bstats[bs] = 10.0
        # player % extra gains
        self.perks = copy.deepcopy(perks)
        for bs in BSS:
            if not bs in self.perks.keys():
                self.perks[bs] = PERKS[bs]
        # player training logic 
        self.ratio = copy.deepcopy(ratio)
        for bstat in BSS:
            if not bstat in self.ratio:
                self.ratio[bstat] = 1
        # gym modeling
        if not notrain:
            notrain = []
        self.notrain = notrain
        self.gyms = copy.deepcopy(GYM)
        self.gym_index = gym_index
        self.en_unlock = 0 # energy for unblocking next gym
        self.music_store = music_store
        self._unlock_gym(0)
        # logging history
        self._log = []
    
    # need for speed
    @property
    def log(self):
        return pd.DataFrame(self._log)

    @property
    def tot_bstats(self):
        res = 0
        for bs in BSS:
            res += self.bstats[bs]
        return res

    @property
    def ff_bstats(self):
        res = 0
        for bs in BSS:
            res += math.sqrt(self.bstats[bs])
        return res
    
    @property
    def gym(self):
        return self.gyms[self.gym_index]

    @property
    def unlocked_all(self):
        if self.gym_index >= 23:
            return True
        else:
            return False
    
    def _unlock_gym(self, en):
        if self.unlocked_all:
            return
        if self.music_store:
            en *= 1.3
        next_gym_en = self.gyms[self.gym_index + 1]["unlock_e"]
        self.en_unlock += en
        if next_gym_en <= self.en_unlock:
            self.gym_index += 1
            self.en_unlock -= next_gym_en
            #print(f"{self.gym['name']} gym unlocked")
    
    def _is_25_higher(self, bstat):
        value = self.bstats[bstat] 
        for bs in BSS:
            if bs != bstat:
                if value < (1.25*self.bstats[bs]):
                    return False
        return True

    def _gym_for(self, bstat):
        if self.unlocked_all:
            if bstat == "str" and self._is_25_higher("str"): 
                return self.gyms[26] # Elites
            if bstat == "def" and self._is_25_higher("def"): 
                return self.gyms[27] # Elites
            if bstat == "spe" and self._is_25_higher("spe"): 
                return self.gyms[28] # Elites
            if bstat == "dex" and self._is_25_higher("dex"): 
                return self.gyms[29] # Elites
        if self.gym_index >= 19:
            if bstat in ["def", "dex"]:
                if (self.bstats["def"] + self.bstats["dex"]) >= 1.25*(self.bstats["str"] + self.bstats["spe"]):
                    return self.gyms[24] # Balboas Gym
            if bstat in ["str", "spe"]:
                if (self.bstats["str"] + self.bstats["spe"]) >= 1.25*(self.bstats["def"] + self.bstats["dex"]):
                    return self.gyms[25] # Frontline Fitness
        gym = self.gyms[self.gym_index]
        if gym[bstat] == 0 & self.gym_index <24:
            gym = self.gyms[self.gym_index - 1]
        if gym[bstat] == 0:
            ValueError(f"You were going to train {bstat} in {gym["name"]} gym, wich has {gym[bstat]} as multiplicator!")
        return gym

    def _train_bstat(self, en, bstat, happy=None):
        if not happy:
            happy = self.happy
        #train
        gym = self._gym_for(bstat)
        res = train(happy, self.bstats[bstat], en, bstat, gym, self.perks[bstat])
        self.en_spent += en
        # log the train
        self._log.append({"en": self.en_spent,
                          "en_used": en,
                          "happy": happy,
                          "str": self.bstats["str"],
                          "spe": self.bstats["spe"],
                          "def": self.bstats["def"],
                          "dex": self.bstats["dex"],
                          "bs": bstat,
                          "gym": gym["name"],
                          "gym_i": self.gym_index,
                          "tot_bs": self.tot_bstats,
                          "ff_bs": self.ff_bstats,
                          "perks": self.perks[bstat],
                          })
        # compute gains
        gains = res["stat"] - self.bstats[bstat]
        self.bstats[bstat] = res["stat"]
        #print(f"you trained in {GYM[gym]["name"]} using {en} energy for {gains} {bstat} increasing it to {self.bstats[bstat]}")
        gym["e_spent"] += en
        self._unlock_gym(en)
    
    def _which_bs(self, allowed):
        # train the stat which has better gym ratio from the battlestats allowed
        x = 0
        stat_value = 0
        for bs in allowed:
            gym = self._gym_for(bs)
            if gym[bs] > x:
                x = gym[bs]
                res = bs
                stat_value = self.bstats[bs]
            elif gym[bs] == x and self.bstats[bs] < stat_value:
                res = bs
                stat_value = self.bstats[bs]
        return res
                 

    def _train(self, en, allowed, happy=None):
        # get the battlestat to train and gym to use
        bstat = self._which_bs(allowed)
        gym = self._gym_for(bstat)
        # get the exact energy to be trained, leave the rest for next train
        en_total = self.en + en
        en_left = en_total % gym["e"]
        en_train = en_total - en_left
        self.en = en_left
        # if en_train > 0, train
        if en_train > 0:
            self._train_bstat(en_train, bstat, happy)
        return
    
    def train(self, en, happy=None, ratio=None, notrain=None):
        if notrain is None:
            notrain = []
        if not ratio:
            allowed = copy.deepcopy(BSS)
        else:
            allowed = []
            sum_ra = 0
            for bs in BSS:
                sum_ra += ratio[bs] 
            worst_diff = 1e-6
            for bs in BSS:
                bs_diff = self.bstats[bs]/self.tot_bstats - ratio[bs]/sum_ra
                if bs_diff < worst_diff: 
                    worst_bs = bs
                    worst_diff = bs_diff
            allowed.append(worst_bs)
        for vbs in notrain:
            if vbs in allowed:
                allowed.remove(vbs)
        return self._train(en, allowed, happy)
    
    def en_to_reach(self, player):
        """ arreglar """
        iplayer = copy.deepcopy(self)
        oplayer = copy.deepcopy(player)
        en = 0
        for key in iplayer.bstats.keys():
            while (iplayer.bstats[key] < oplayer.bstats[key]):
                en_trained = iplayer._gym_for(key)["e"]
                en += en_trained
                iplayer._train_bstat(en_trained, key)
            while (oplayer.bstats[key] < iplayer.bstats[key]):
                en_trained = oplayer._gym_for(key)["e"]
                en -= en_trained
                oplayer._train_bstat(en_trained, key)
        return en
    
    def __str__(self):
        res = self.__repr__()
        # get e spent on every gym
        res += "\n"
        # get gyms energy used
        res += self.log.groupby("gym")["en_used"].sum().sort_values().__str__()
        return res


    def __repr__(self):
        res = ""
        ff = 0
        for bstat in self.bstats.keys():
            res += f"{bstat}:{self.bstats[bstat]:>32,.0f}\n"
        res += f"TOTAL BSS: {self.tot_bstats:>25,.0f}\n"
        res += f"FF RATIO: {self.ff_bstats:>26,.0f}\n"

        return res

        
