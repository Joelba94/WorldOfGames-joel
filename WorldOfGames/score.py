import utils
def add_score(diffculty):
    POINTS_OF_WINNING=int((diffculty*3)+5)
    read_file = open(utils.SCORES_FILE_NAME, 'r')
    for line in read_file.readlines():
        line=int(line)+POINTS_OF_WINNING
    read_file.close()
    read_file = open(utils.SCORES_FILE_NAME, 'w')
    read_file.write(str(line))
    read_file.close()

