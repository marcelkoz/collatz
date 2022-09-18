import matplotlib.patches as patches
import matplotlib.pyplot as plot

class CollatzConjecture:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current == 1:
            self.current = 0
            return 1

        if self.current > 0:
            current      = self.current
            next         = self.calculate()
            self.current = next
            return current
        else:
            raise StopIteration

    def calculate(self):
        if self.current % 2 == 0:
            return self.current // 2
        else:
            return 3 * self.current + 1

def label_axises(axises):
    axises.set_ylabel('Collatz Numbers')
    axises.set_xlabel('Number of Stops')

def label_legend(axises, biggest, stops):
    biggest_patch = patches.Patch(color='red', label=f'Highest Point: {biggest}')
    stops_patch = patches.Patch(color='red', label=f'Number of Stops: {stops}')
    axises.legend(handles=[biggest_patch, stops_patch])

def main():
    number = 27
    numbers = list(CollatzConjecture(number))
    biggest = max(numbers)
    stops = len(numbers)

    # x axis: stops
    # y axis: numbers

    figure, axises = plot.subplots()
    axises.set_title(f'Collatz Conjecture of {number}')
    label_axises(axises)
    label_legend(axises, biggest=biggest, stops=stops)
    axises.set_xticks(range(0, stops + 1, 10))
    axises.plot(range(1, stops + 1), numbers)
    plot.show()

if __name__ == '__main__':
    main()
