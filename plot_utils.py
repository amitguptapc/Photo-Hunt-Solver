import matplotlib.pyplot as plt
plt.style.use('seaborn')

def plotImage(img,t="Image"):
    plt.figure(figsize=(13,10))
    plt.title(t)
    plt.imshow(img)
    plt.axis("off")
    plt.show()