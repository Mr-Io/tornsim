import copy
import matplotlib.pyplot as plt

from model import Player, BSS
from happy_func import f_happy, f_stat, BOOSTER_CD 

a = Player()
while(not a.unlocked_all):
    en += 50
    a.train(5, force_ratio=True)

print("player_a\n")
print(a)
print(a.en_spent)


########### DATA AND PLOTS ################
fig, ax = plt.subplots(figsize=(16, 8))
en_max =  550000

for bs in BSS:
    s= []
    h = []
    for s_value in range(0, stat_max+1, stat_max//20):
        h_value = f_happy(d, s_value)
        if h_value>99999:
            h_value=99999
            s_value= f_stat(d,99999)
            s.append(s_value)
            h.append(h_value)
            break
        s.append(s_value)
        h.append(h_value)
    y_max = 99999
    ax.plot(s, h, color="grey")
    ax.text(s_value, h_value, f"+{d:,.0f} days", color="grey", horizontalalignment="center", verticalalignment="bottom")

ax.grid(
    True,
    which='both',          # major and minor grid lines
    linestyle='-',
    linewidth=0.4,
    color='gray',
    alpha=0.7
)


# figure 1: happy needed to reach same gains than a jump
# 24h booster CD
happy_color = "black"#"#A79001"
gym_color = "#075300"
#fig.suptitle("3 XANAX/DAY")
#ax.set_title(f"gym bonus:   {2}%\n"
#             f"booster CD: {BOOSTER_CD}h ")
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_yticks([0, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 99999],["0", "10k", "20k","30k","40k","50k","60k","70k","80k","90k", "99.999"],
              color=happy_color)
ax.set_xlim(0, stat_max)
ax.set_ylim(0, y_max+10000)
#ax.grid(axis='y')
# 25h candy
color_99k = "#B68C03"
color_edvd = "#B91C1C"
hlines_values = [((4500+(BOOSTER_CD*2+1)*25)*2,  "green", "25h candy", 0.5),
                 ((4500+(BOOSTER_CD*2+1)*100)*2, "green", "50h candy", 1),
                 ((4500+(BOOSTER_CD/6+1)*2500)*2, color_edvd, "Erotic DVD", 0.5),
                 ((4500+(BOOSTER_CD/6+1)*5000)*2, color_edvd, "eDVD 10* Adult Nov.", 0.8),
                 (99999, color_99k , "99k jump", 1),
                ]
"""
xticks_x = []
xticks_s = []
for y, color, label, alpha in hlines_values:
    ax.axhline(y=y, color=color, alpha=alpha, label=label, linewidth=1) 
    ax.text(2e6-10000, y, f"{y:,.0f} happy", color=color, alpha=alpha, horizontalalignment="right", verticalalignment="bottom")
    for r in [2, 1]:
        x = f_stat(r, y, n_xanax=4)
        xticks_x.append(x)
        xticks_s.append(f"{int(x)/1000:,.0f}k" if x < 999999 else f"{int(x)/1e6:,.2f}M")
        ax.plot(x, y, marker="o", color="black", markersize=2)
        ax.vlines(x=x, ymin=0, ymax=y, linewidth=0.5, color="grey")

ax.set_xlim(0, 2.5e6)


ax.set_xticks(xticks_x) 
ax.set_xticklabels(xticks_s, rotation=60)#, color=gym_color, fontweight="bold", bbox=dict(
        #facecolor='white',   # fondo
        #edgecolor='black',   # borde
        #boxstyle='round,pad=0.3'
    #))

# label 
ax.set_xlabel("INITIAL STAT")



ls = ax.get_xticklabels()
ls[0].set_color("green")
ls[0].set_alpha(0.5)
ls[1].set_color("green")
ls[2].set_color(color_edvd)
ls[2].set_alpha(0.5)
ls[3].set_color(color_edvd)
ls[3].set_alpha(0.8)
ls[4].set_color(color_99k)
"""



#legend = ax.legend(ncol=3)
#for line in legend.get_lines():
#    line.set_linewidth(3)

fig.show()

###########