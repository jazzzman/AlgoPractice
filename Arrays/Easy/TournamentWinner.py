"""
  DESCRIPTION

  There's an algorithms tournament taking place in which teams of programmers
  compete against each other to solve algorithmic problems as fast as possible.
  Teams compete in a round robin, where each team faces off against all other
  teams. Only two teams compete against each other at a time, and for each
  competition, one team is designated the home team, while the other team is the
  away team. In each competition there's always one winner and one loser; there
  are no ties. A team receives 3 points if it wins and 0 points if it loses. The
  winner of the tournament is the team that receives the most amount of points.

  Given an array of pairs representing the teams that have competed against each
  other and an array containing the results of each competition, write a
  function that returns the winner of the tournament. The input arrays are named
  <span>competitions</span> and <span>results</span>, respectively. The
  <span>competitions</span> array has elements in the form of
  <span>[homeTeam, awayTeam]</span>, where each team is a string of at most 30
  characters representing the name of the team. The <span>results</span> array
  contains information about the winner of each corresponding competition in the
  <span>competitions</span> array. Specifically, <span>results[i]</span> denotes
  the winner of <span>competitions[i]</span>, where a <span>1</span> in the
  <span>results</span> array means that the home team in the corresponding
  competition won and a <span>0</span> means that the away team won.

  It's guaranteed that exactly one team will win the tournament and that each
  team will compete against all other teams exactly once. It's also guaranteed
  that the tournament will always have at least two teams.

  Time complexity O(n) n-length of  competitions
  Space complexity O(v) v-count commands
"""
import pytest


def tournamentWinner(competitions, results):
    command_points = {}
    for result,(home,away) in zip(results,competitions):
        winner = home if result==1 else away
        if winner in command_points:
            command_points[winner]+=3
        else:
            command_points[winner]=3
    return max(command_points, key=command_points.get)


cases = [
    [[['HTML', 'C#'], ['C#', 'Python'], ['Python', 'HTML']], [0, 0, 1], 'Python'],
    [[['HTML', 'Java'], ['Java', 'Python'], ['Python', 'HTML']], [0, 1, 1], 'Java'],
    [[['HTML', 'Java'], ['Java', 'Python'], ['Python', 'HTML'], ['C#', 'Python'], ['Java', 'C#'], ['C#', 'HTML']], [0, 1, 1, 1, 0, 1], 'C#'],
    [[['HTML', 'Java'], ['Java', 'Python'], ['Python', 'HTML'], ['C#', 'Python'], ['Java', 'C#'], ['C#', 'HTML'], ['SQL', 'C#'], ['HTML', 'SQL'], ['SQL', 'Python'], ['SQL', 'Java']], [0, 1, 1, 1, 0, 1, 0, 1, 1, 0], 'C#'],
    [[['Bulls', 'Eagles']], [1], 'Bulls'],
    [[['Bulls', 'Eagles'], ['Bulls', 'Bears'], ['Bears', 'Eagles']], [0, 0, 0], 'Eagles'],
    [[['Bulls', 'Eagles'], ['Bulls', 'Bears'], ['Bulls', 'Monkeys'], ['Eagles', 'Bears'], ['Eagles', 'Monkeys'], ['Bears', 'Monkeys']], [1, 1, 1, 1, 1, 1], 'Bulls'],
    [[['AlgoMasters', 'FrontPage Freebirds'], ['Runtime Terror', 'Static Startup'], ['WeC#', 'Hypertext Assassins'], ['AlgoMasters', 'WeC#'], ['Static Startup', 'Hypertext Assassins'], ['Runtime Terror', 'FrontPage Freebirds'], ['AlgoMasters', 'Runtime Terror'], ['Hypertext Assassins', 'FrontPage Freebirds'], ['Static Startup', 'WeC#'], ['AlgoMasters', 'Static Startup'], ['FrontPage Freebirds', 'WeC#'], ['Hyp ertext Assassins', 'Runtime Terror'], ['AlgoMasters', 'Hypertext Assassins'], ['WeC#', 'Runtime Terror'], ['FrontPage Freebirds', 'Static Startup']], [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0], 'AlgoMasters'], [[['HTML', 'Java'], ['Java', 'Python'], ['Python', 'HTML'], ['C#', 'Python'], ['Java', 'C#'], ['C#', 'HTML'], ['SQL', 'C#'], ['HTML', 'SQL'], ['SQL', 'Python'], ['SQL', 'Java']], [0, 0, 0, 0, 0, 0, 1, 0, 1, 1], 'SQL'],
    [[['A', 'B']], [0], 'B']
]

@pytest.mark.parametrize("competition, results, expected",cases)
def test_tournamentWinner(competition, results, expected):
    assert tournamentWinner(competition, results)==expected

