import random

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    balls = ['red', 'red', 'red', 'green', 'green', 'green']
    allEqualCount = 0.0
    
    for i in range(numTrials):
        ballsSet = balls[:]
        ballsPicks = []
        for i in range(3):
            choice = ballsSet[random.randrange(len(ballsSet))]
            ballsPicks.append(choice)
            ballsSet.remove(choice)

        if ballsPicks[0] == ballsPicks[1] and ballsPicks[0] == ballsPicks[2]:
            allEqualCount += 1

    return allEqualCount / numTrials
print noReplacementSimulation(5000)