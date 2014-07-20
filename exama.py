import random
import pylab
def sampleQuizzes(): 
	numTrials = 10000
	count = 0.0
	for __ in range(numTrials): 
		midterm1 = random.randrange(50,80)
		midterm2 = random.randrange(60,90)
		finals = random.randrange(55,95)
		totalScore = 0.25*midterm2 + 0.25*midterm1 + 0.5*finals
		if totalScore>=70 and totalScore <= 75:
			count+=1

	return count/numTrials

def generateScores(numTrials):
    """
    Runs numTrials trials of score-generation for each of
    three exams (Midterm 1, Midterm 2, and Final Exam).
    Generates uniformly distributed scores for each of 
    the three exams, then calculates the final score and
    appends it to a list of scores.
    
    Returns: A list of numTrials scores.
    """
    listScores = [] 
    for __ in range(numTrials): 
		midterm1 = random.randrange(50,80)
		midterm2 = random.randrange(60,90)
		finals = random.randrange(55,95)
		totalScore = 0.25*midterm2 + 0.25*midterm1 + 0.5*finals
		listScores.append(totalScore)
    
    return listScores


def plotQuizzes(): 
	numTrials = 10000
	pylab.hist(generateScores(numTrials), 7)
	pylab.title('Distribution of Scores')
	pylab.xlabel('Final Score')
	pylab.ylabel('Number of Trials')
	pylab.show()

plotQuizzes()