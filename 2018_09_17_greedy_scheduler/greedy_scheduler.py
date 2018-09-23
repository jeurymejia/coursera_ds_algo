from collections import namedtuple
from heap import Heap


Job = namedtuple('Job', ['weight', 'length', 'score'])


def main():
    with open('jobs.txt', 'r') as file:
        file.readline()  # Ignore top (header) line of file
        lines = file.readlines()
    lines = [tuple(line.split()) for line in lines]
    lines = [(int(x), int(y)) for x, y in lines]

    jobs = [
        Job(weight=weight, length=length, score=None)
        for weight, length in lines
    ]

    bad_schedule = build_schedule(jobs, calc_greedy_bad)
    # Correct answer is 69119377652
    print("Total weighted completion time using suboptimal algo: {}"
          .format(calc_weighted_completion(bad_schedule)))

    good_schedule = build_schedule(jobs, calc_greedy_good)
    # Correct answer is 67311454237
    print("Total weighted completion time using optimal algo: {}"
          .format(calc_weighted_completion(good_schedule)))


def calc_greedy_bad(weight, length):
    """Calculates *suboptimal* greedy score for scheduling problem.

    Greedy score is:

        ( (length - weight) * 1000 ) + weight

    Jobs are scheduled in decreasing order of the difference of
    length - weight, with the higher-weighted job going first
    if the difference of weight - length is a tie.
    """
    return ((weight - length) * 1000) + weight


def calc_greedy_good(weight, length):
    """Calculates optimal greedy score for scheduling problem.

    Greedy score is:

        weight/length

    Jobs are scheduled in decreasing order of the ratio with ties
    handled arbitrarily.
    """
    return weight / length


def build_schedule(jobs, greedy_criterion):
    jobs = [
        Job(weight, length, greedy_criterion(weight, length))
        for weight, length, score in jobs
    ]
    heap = Heap(jobs, key=lambda x: (x.score * -1))
    schedule = []
    for _ in range(len(jobs)):
        schedule.append(heap.extract_min())
    return schedule


def calc_weighted_completion(schedule):
    comp_time = 0
    total_weighted_comp_time = 0
    for job in schedule:
        # print("Cur job: {}".format(job))
        comp_time += job.length
        # print(comp_time)
        total_weighted_comp_time += comp_time * job.weight
    return total_weighted_comp_time


if __name__ == '__main__':
    main()
