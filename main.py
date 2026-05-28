from matplotlib.ticker import FuncFormatter, MaxNLocator

from simul import *

# AÑADIR EN LA X CUANDO SE DESBLOQUE CADA GIMNASIO (PONER VALOR DE LA E TOTAL TB)

PARAM = {
    "str": {
        "color": None,
        "linestyle": "-.",
    },
    "spe": {
        "color": None,
        "linestyle": ":",
    },
    "def": {
        "color": None,
        "linestyle": "-"
    },
    "dex": {
        "color": None,
        "linestyle": "--"
    },
}



# first 1-2 month of training, with perks (PI), bs following balanced 

# first 1-2 month of training, with perks (PI + Faction), bs following balanced 

# first 1-2 month of training, with perks (PI + Faction), bs following best-gym

# first 1-2 month of training, with perks (PI + Faction), bs following best-gym, music store

# first 1-2 month of training, with perks (PI + Faction), specific bs, happy jumps

# plot training in the best gym
fig, ax = plt.subplots(figsize=(16, 8))
df = bal_forc.log
df = df[df.gym_i <= 20]
ax.plot(df["en"],df["str"], label=f"balanced", color="blue")
for bs in BSS:
    for p in [balanced,]:
        df = p.log
        df = df[df.gym_i <= 20]
        ax.plot(df["en"], df[bs], label=f"best-gym:{bs}", linestyle=PARAM[bs]["linestyle"], color="red")
        #ax.text(s_value, h_value, f"+{d:,.0f} days", color="grey", horizontalalignment="center", verticalalignment="bottom")
        #ax.set_ylim(0, 500000)

ax.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x:,.0f}")
)
ax.set_xticks([0] + list(g["unlock_en_cum"] for g in GYM[10:22]), ["start"] + list(f'{g["name"]}' for g in GYM[10:22]), rotation=90)
ax.grid(axis='x')
ax.grid(axis='y')
ax.legend()
fig.show()

# plot music store 
fig, ax = plt.subplots(figsize=(16, 8))
for bs in BSS:
    df = balanced.log
    df = df[df.en <= 350000]
    ax.plot(df["en"], df[bs], label=f"normal job :{bs}", linestyle=PARAM[bs]["linestyle"], color="blue")
for bs in BSS:
    df = bal_musi.log
    df = df[df.en <= 350000]
    ax.plot(df["en"], df[bs], label=f"music store:{bs}", linestyle=PARAM[bs]["linestyle"], color="red")

ax.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x:,.0f}")
)
ax.set_xticks([0] + list(g["unlock_en_cum"] for g in GYM[10:22]), ["start"] + list(f'{g["name"]}' for g in GYM[10:22]), rotation=90)
ax.grid(axis='x')
ax.grid(axis='y')
ax.legend()
fig.show()


# plot ratios with gym unlocking for lightweight gyms
fig, ax = plt.subplots(figsize=(16, 8))
max_x = 1500*60
for bs in BSS:
    df = no_dex.log
    df = df[df["en"] <= max_x]
    ax.plot(df["en"], df[bs], label=f"0-dex:{bs}", linestyle=PARAM[bs]["linestyle"], color="red")
for bs in BSS:
    df = bald_dex.log
    df = df[df["en"] <= max_x]
    ax.plot(df["en"], df[bs], label=f"bald-dex:{bs}", linestyle=PARAM[bs]["linestyle"], color="blue")
for bs in BSS:
    df = hank_def.log
    df = df[df["en"] <= max_x]
    ax.plot(df["en"], df[bs], label=f"hank-dex:{bs}", linestyle=PARAM[bs]["linestyle"], color="green")
for bs in BSS:
    df = balanced.log
    df = df[df["en"] <= max_x]
    ax.plot(df["en"], df[bs], label=f"balanced:{bs}", linestyle=PARAM[bs]["linestyle"], color="grey")
#ax.axhline(y=50_000_000, linestyle='-', linewidth=1, color="grey")
#ax.text(ax.get_xlim()[1], 50_000_000, '50,000,000', va='bottom', ha='right')

ax.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x:,.0f}")
)
ax.set_xticks(list(g["unlock_en_cum"] for g in GYM[0:9]), list(f'{g["name"]}' for g in GYM[0:9]), rotation=90)
ax.grid(axis='x')
#ax.grid(axis='y')
ax.legend()
fig.show()

# plot ratios with gym unlocking for lightweight gyms
fig, ax = plt.subplots(figsize=(16, 8))
max_x = 800000
for bs in BSS:
    df = no_dex.log
    df = df[df["en"] <= max_x]
    ax.plot(df["en"], df[bs], label=f"0-dex:{bs}", linestyle=PARAM[bs]["linestyle"], color="red")
for bs in BSS:
    df = bald_dex.log
    df = df[df["en"] <= max_x]
    ax.plot(df["en"], df[bs], label=f"bald-dex:{bs}", linestyle=PARAM[bs]["linestyle"], color="blue")
for bs in BSS:
    df = hank_def.log
    df = df[df["en"] <= max_x]
    ax.plot(df["en"], df[bs], label=f"hank-dex:{bs}", linestyle=PARAM[bs]["linestyle"], color="green")
for bs in BSS:
    df = balanced.log
    df = df[df["en"] <= max_x]
    ax.plot(df["en"], df[bs], label=f"balanced:{bs}", linestyle=PARAM[bs]["linestyle"], color="grey")
ax.axhline(y=50_000_000, linestyle='-', linewidth=1, color="grey")
ax.text(ax.get_xlim()[1], 50_000_000, '50,000,000', va='bottom', ha='right')

ax.yaxis.set_major_formatter(
    FuncFormatter(lambda x, pos: f"{x:,.0f}")
)
ax.set_xticks([0] + list(g["unlock_en_cum"] for g in GYM[10:24]), ["start"] + list(f'{g["name"]}' for g in GYM[10:24]), rotation=90)
ax.grid(axis='x')
#ax.grid(axis='y')
ax.legend()
fig.show()

"""
########### DATA AND PLOTS ################

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
# 25h candy
color_99k = "#B68C03"
color_edvd = "#B91C1C"
hlines_values = [((4500+(BOOSTER_CD*2+1)*25)*2,  "green", "25h candy", 0.5),
                 ((4500+(BOOSTER_CD*2+1)*100)*2, "green", "50h candy", 1),
                 ((4500+(BOOSTER_CD/6+1)*2500)*2, color_edvd, "Erotic DVD", 0.5),
                 ((4500+(BOOSTER_CD/6+1)*5000)*2, color_edvd, "eDVD 10* Adult Nov.", 0.8),
                 (99999, color_99k , "99k jump", 1),
                ]
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



#legend = ax.legend(ncol=3)
#for line in legend.get_lines():
#    line.set_linewidth(3)

fig.show()

###########
"""