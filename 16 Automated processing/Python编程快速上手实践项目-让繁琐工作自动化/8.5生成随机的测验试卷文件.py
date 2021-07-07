import random
import os

# new 为当前工作目录里的文件夹，此句是为了在当前工作目录里创建生成的文件
os.chdir(os.path.join(os.getcwd(), 'new'))


# import quiz data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton',
            'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia',
            'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate 35 quiz files.
for quizNum in range(1, 36):
    # TODO: Create the quiz and answer key files.
    quizfile = open('quizfile%02d.txt' % (quizNum), 'w')
    quizans = open('quiznum%02d.txt' % (quizNum), 'w')

    # TODO: Write out the header for the quiz.
    quizfile.write('Name:\n\nDate:\n\n')
    quizfile.write(('State Capital Quiz form-%02d' % (quizNum)).rjust(50))
    quizfile.write('\n\n')
    quizans.write('Answers for quiz form-%02d:\n' % (quizNum))

    # TODO: Shuffle the order of the states.
    state_list = list(capitals.keys())
    random.shuffle(state_list)

    # TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(len(capitals)):
        quizfile.write("%d. What's the capital of %s?\n" % (questionNum+1,
                                                            state_list[questionNum]))
# Write the question and the answer options to the quiz file.
        ans_sheet = []
        wrong_ans = list(capitals.values())
        wrong_ans.remove(capitals[state_list[questionNum]])
        ans_sheet = random.sample(wrong_ans, 3)
        ans_sheet.append(capitals[state_list[questionNum]])
        random.shuffle(ans_sheet)
        for i in range(4):
            quizfile.write("    %s. %s\n" % ('ABCD'[i], ans_sheet[i]))
        quizfile.write('\n')
# Write the answer key to a file.
        quizans.write('%d. %s(%s)\n' % (questionNum+1,
                                        'ABCD'[ans_sheet.index(
                                            capitals[state_list[questionNum]])],
                                        capitals[state_list[questionNum]]))

    quizfile.close()
    quizans.close()
