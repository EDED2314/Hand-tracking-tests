import matplotlib.pyplot as plt


def leaderboard():
    all = []
    scores = []
    with open("times.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            all.append(line.split(",")[1:])
    x = [pep for pep in all]
    with open("scores.txt", "r") as f:
        lines = f.readlines()
        if lines[0] != '0':
            for i in range(len(lines)):
                scores.append(int(lines[i].split(" ")[2].strip('\n')))
    y = [score for score in scores]

    plt.plot(x, y)
    plt.title('Score leaderboard')
    plt.xlabel('Time')
    plt.ylabel('Scores')
    plt.show()


leaderboard()