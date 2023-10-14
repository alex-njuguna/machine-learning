from matplotlib import pyplot


def create_chart(x, y, filename):
    fig = pyplot.figure()
    pyplot.scatter(x, y, alpha=0.5)
    fig.savefig(f"{filename}.png")