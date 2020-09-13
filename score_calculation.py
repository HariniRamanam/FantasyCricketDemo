#Evaluator is Ui_WindowEval object
def calculate(Evaluator,db):
    total_points = 0
    team_name = Evaluator.team_eval.currentText()
    players = db.get_match_details(team_name)
    for player in players:
        player_info = {"Player":player[0], "Scored":player[1], "Faced":player[2],
        "Fours":player[3], "Sixes":player[4], "Bowled":player[5],
        "Maiden":player[6], "Given":player[7], "Wkts":player[8],
        "Catches":player[9], "Stumping":player[10], "RO*":player[11]}
        points = batting_points(player_info)
        points += bowling_points(player_info)
        points += feilding_points(player_info)
        Evaluator.listWidget_4.addItem(player[0] + (' '*10) + str(points))
        total_points += points
        Evaluator.label_7.setText(str(total_points))
    return total_points
        
def feilding_points(d):
    points = 0
    points = d['Catches'] * 10
    points += d['Stumping'] * 10
    points += d['RO*'] * 10
    return points

def batting_points(d):
    points = 0
    points = d['Scored']//2
    if d['Scored'] >= 50:
        points += 5
    if d['Scored'] >= 100:
        points += 10
    faced = d['Faced'] * 100
    if faced > 0:
        strk = d['Scored'] / d['Faced'] * 100
    else:
        strk = d["Scored"]
    if strk >= 80 and strk <= 100:
        points += 2
    if strk > 100:
        points += 4
    points = points + d['Fours'] + d['Sixes'] * 2
    return points
    
def bowling_points(d):
    points = 0
    if d['Bowled'] != 0:
        points = d['Wkts'] * 10
        if d['Wkts'] >= 3:
            points += 5
        if d['Wkts'] >= 5:
            points += 10
        overs = d['Bowled'] / 6
        if overs > 0:
            ecr = d['Given'] / overs
        else:
            ecr = d['Given']
        if ecr >= 3.5 and ecr <= 4.5:
            points+=4
        elif ecr >= 2 and ecr < 3.5:
            points += 7
        elif ecr < 2:
            points += 10
    return points