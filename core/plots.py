from matplotlib import pyplot as plt


class PlotWriter:
    bar_limit = 12
    x_min, x_max = 0, 2000
    y_min, y_max = -1, bar_limit

    def __init__(self, filename):
        self._filename = filename + ".svg"
        self._fig, self._ax = plt.subplots(figsize=(10, 0.5 * self.bar_limit), frameon=False, tight_layout=True)
        self.ax_init()
        self._ax.set_yticks([])
        plt.savefig(self._filename)
        self._colorOk = ['blue', 'green']
        self._colorError = ['red', 'black']
        self._height = [0.6, 0.8]
        self._coordMsg = [1400, 20]

    def ax_init(self):
        self._ax = plt.gca()
        self._ax.set_title(self._filename, size=14, loc='left')
        self._ax.set_xlabel('time, ms')
        self._ax.set_xlim(self.x_min, self.x_max)
        self._ax.set_xticks(list(range(self.x_min, self.x_max + 50, 50)), minor=True)
        self._ax.xaxis.grid(True)
        self._ax.set_ylim(self.y_min, self.y_max)
        self._ax.invert_yaxis()

    def ax_refresh(self):
        plt.delaxes()
        self.ax_init()
        p = plt.barh(0, 0, height=0.6, color='blue')
        l = plt.barh(0, 0, height=0.6, color='green')
        plt.legend((p, l), ('loading time', 'latency'), loc=4)

    def update(self, monitor_data, probe, tests_count):
        status_msg = "test " + str(probe + 1) + " has passed, tests remain: " + str(tests_count - probe - 1)
        self.ax_refresh()
        plt.text(self.x_max, self.y_min-0.5, status_msg, va='top', ha='right')
        for record in monitor_data:
            clock = record[0].value()
            index = 0
            for item in record[1:]:
                color = self._colorOk[index] if not item.msg() else self._colorError[index]
                self._ax.barh(clock, item.checked_value(), color=color, height=self._height[index])
                plt.text(self._coordMsg[index], clock, item.msg(), fontsize='small', va='baseline')
                index += 1

        self._fig.canvas.draw()
        plt.savefig(self._filename)
