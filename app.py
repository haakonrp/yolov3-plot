import os
from matplotlib import image, patches, pyplot as plt
from matplotlib.ticker import MultipleLocator

files_dir = "files/"
iterations = []
mapPercents = []
avgIous = []
for f in sorted(os.listdir(files_dir)):
    if ".TXT" in f or ".txt" in f:
        with open(files_dir + f, 'rt') as file:
            contents = file.read()
        iteration = f.split("_")[2].split(".")[0]
        mapPercent = round(float(contents.split("mean average precision (mAP@0.50) =")[1].split(",")[0])*100, 2)
        avgIou = float(contents.split("average IoU = ")[1].split(" ")[0])
        #print(contents)
        print("Iteration: " + str(iteration))
        print("mAP %: " + str(mapPercent))
        print("IOU %: " + str(avgIou))

        iterations.append(iteration)
        mapPercents.append(mapPercent)
        avgIous.append(avgIou)

fig, ax = plt.subplots()
# set area we focus on
ax.set_ylim(0, 100)

# draw values
for i in range(len(iterations)):
    plt.text(i, mapPercents[i]+1, str(mapPercents[i]), horizontalalignment='center', verticalalignment='bottom', color='red')
    plt.text(i, avgIous[i]-1, str(avgIous[i]), horizontalalignment='center', verticalalignment='top', color='blue')

plt.plot(iterations, mapPercents, 'r-s', lw=0.75, ms=5)
plt.plot(iterations, avgIous, 'b-s', lw=0.75, ms=5)
plt.grid(b=True, which='major', color='#666666', linestyle='-')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='-', alpha=0.2)
plt.title('mAP & IoU % pr. Iteration')
plt.xlabel('Iteration')
plt.ylabel('%')
plt.legend(['mAP', 'IoU'])

plt.tight_layout()

# saved as svg
plt.savefig("out.svg", dpi=300, format="svg")
plt.show()
