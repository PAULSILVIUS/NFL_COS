from data import data
from team import Team
import networkx as nx
import matplotlib.pyplot as plt


def main():
    gameset = [('ARI', 'CIN'), ('ARI', 'ATL'), ('ARI', 'NYG'), ('ARI', 'CLE'), ('ARI', 'SEA'), ('ATL', 'PHI'), ('ATL', 'NO'), ('ATL', 'CAR'), ('ATL', 'SF'), ('ATL', 'JAX'), ('ATL', 'TB'), ('BAL', 'MIA'), ('BAL', 'ARI'), ('BAL', 'PIT'), ('BAL', 'CIN'), ('BAL', 'SEA'), ('BAL', 'NE'), ('BAL', 'HOU'), ('BAL', 'LA'), ('BAL', 'SF'), ('BAL', 'BUF'), ('BAL', 'NYJ'), ('BAL', 'CLE'), ('BUF', 'NYJ'), ('BUF', 'NYG'), ('BUF', 'CIN'), ('BUF', 'TEN'), ('BUF', 'MIA'), ('BUF', 'WAS'), ('BUF', 'DEN'), ('BUF', 'DAL'), ('BUF', 'PIT'), ('CAR', 'ARI'), ('CAR', 'HOU'), ('CAR', 'JAX'), ('CAR', 'TB'), ('CAR', 'TEN'), ('CHI', 'DEN'), ('CHI', 'WAS'), ('CHI', 'MIN'), ('CHI', 'DET'), ('CHI', 'NYG'), ('CHI', 'DAL'), ('CIN', 'NYJ'), ('CIN', 'CLE'), ('CLE', 'NYJ'), ('CLE', 'BAL'), ('CLE', 'BUF'), ('CLE', 'PIT'), ('CLE', 'MIA'), ('CLE', 'CIN'), ('DAL', 'NYG'), ('DAL', 'WAS'), ('DAL', 'MIA'), ('DAL', 'PHI'), ('DAL', 'DET'), ('DAL', 'LA'), ('DEN', 'LAC'), ('DEN', 'TEN'), ('DEN', 'CLE'), ('DEN', 'HOU'), ('DEN', 'DET'), ('DEN', 'OAK'), ('DET', 'LAC'), ('DET', 'PHI'), ('DET', 'NYG'), ('GB', 'CHI'), ('GB', 'MIN'), ('GB', 'DEN'), ('GB', 'DAL'), ('GB', 'DET'), ('GB', 'OAK'), ('GB', 'KC'), ('GB', 'CAR'), ('GB', 'NYG'), ('GB', 'WAS'), ('GB', 'SEA'), ('HOU', 'JAX'), ('HOU', 'LAC'), ('HOU', 'ATL'), ('HOU', 'KC'), ('HOU', 'OAK'), ('HOU', 'IND'), ('HOU', 'NE'), ('HOU', 'TEN'), ('HOU', 'TB'), ('HOU', 'BUF'), ('IND', 'TEN'), ('IND', 'ATL'), ('IND', 'KC'), ('IND', 'HOU'), ('IND', 'DEN'), ('IND', 'JAX'), ('IND', 'CAR'), ('JAX', 'TEN'), ('JAX', 'DEN'), ('JAX', 'CIN'), ('JAX', 'NYJ'), ('JAX', 'OAK'), ('JAX', 'IND'), ('KC', 'JAX'), ('KC', 'OAK'), ('KC', 'BAL'), ('KC', 'DET'), ('KC', 'DEN'), ('KC', 'MIN'), ('KC', 'LAC'), ('KC', 'NE'), ('KC', 'CHI'), ('KC', 'HOU'), ('KC', 'TEN'), ('KC', 'SF'), ('LA', 'CAR'), ('LA', 'NO'), ('LA', 'CLE'), ('LA', 'ATL'), ('LA', 'CIN'), ('LA', 'CHI'), ('LA', 'ARI'), ('LA', 'SEA'), ('LAC', 'IND'), ('LAC', 'MIA'), ('LAC', 'CHI'), ('LAC', 'GB'), ('LAC', 'JAX'), ('MIA', 'NYJ'), ('MIA', 'IND'), ('MIA', 'PHI'), ('MIA', 'CIN'), ('MIA', 'NE'), ('MIN', 'ATL'), ('MIN', 'OAK'), ('MIN', 'NYG'), ('MIN', 'PHI'), ('MIN', 'DET'), ('MIN', 'WAS'), ('MIN', 'DAL'), ('MIN', 'DEN'), ('MIN', 'LAC'), ('MIN', 'NO'), ('NE', 'PIT'), ('NE', 'MIA'), ('NE', 'NYJ'), ('NE', 'BUF'), ('NE', 'WAS'), ('NE', 'NYG'), ('NE', 'CLE'), ('NE', 'PHI'), ('NE', 'DAL'), ('NE', 'CIN'), ('NO', 'HOU'), ('NO', 'SEA'), ('NO', 'DAL'), ('NO', 'TB'), ('NO', 'JAX'), ('NO', 'CHI'), ('NO', 'ARI'), ('NO', 'CAR'), ('NO', 'ATL'), ('NO', 'IND'), ('NO', 'TEN'), ('NYG', 'TB'), ('NYG', 'WAS'), ('NYG', 'MIA'), ('NYJ', 'DAL'), ('NYJ', 'NYG'), ('NYJ', 'WAS'), ('NYJ', 'OAK'), ('NYJ', 'MIA'), ('NYJ', 'PIT'), ('NYJ', 'BUF'), ('OAK', 'DEN'), ('OAK', 'IND'), ('OAK', 'CHI'), ('OAK', 'DET'), ('OAK', 'LAC'), ('OAK', 'CIN'), ('PHI', 'WAS'), ('PHI', 'GB'), ('PHI', 'NYJ'), ('PHI', 'BUF'), ('PHI', 'CHI'), ('PHI', 'NYG'), ('PHI', 'DAL'), ('PIT', 'CIN'), ('PIT', 'LAC'), ('PIT', 'MIA'), ('PIT', 'IND'), ('PIT', 'LA'), ('PIT', 'CLE'), ('PIT', 'ARI'), ('SEA', 'CIN'), ('SEA', 'PIT'), ('SEA', 'ARI'), ('SEA', 'LA'), ('SEA', 'CLE'), ('SEA', 'ATL'), ('SEA', 'TB'), ('SEA', 'SF'), ('SEA', 'PHI'), ('SEA', 'MIN'), ('SEA', 'CAR'), ('SF', 'TB'), ('SF', 'CIN'), ('SF', 'PIT'), ('SF', 'CLE'), ('SF', 'LA'), ('SF', 'WAS'), ('SF', 'CAR'), ('SF', 'ARI'), ('SF', 'GB'), ('SF', 'NO'), ('SF', 'SEA'), ('SF', 'MIN'), ('TB', 'CAR'), ('TB', 'LA'), ('TB', 'ARI'), ('TB', 'ATL'), ('TB', 'JAX'), ('TB', 'IND'), ('TB', 'DET'), ('TEN', 'CLE'), ('TEN', 'ATL'), ('TEN', 'LAC'), ('TEN', 'TB'), ('TEN', 'KC'), ('TEN', 'JAX'), ('TEN', 'IND'), ('TEN', 'OAK'), ('TEN', 'HOU'), ('TEN', 'NE'), ('TEN', 'BAL'), ('WAS', 'MIA'), ('WAS', 'DET'), ('WAS', 'CAR')]
    
    print(gameset[2][0])

    list = data(gameset)


    result_list = list.get_team_wins('BAL')
    #used_team_list = list.get_team_wins('MIA')

    all_teams = list.get_all_teams()
    oneTeam = all_teams[0]
    circle_list = []


    for x in all_teams:
        result_list = list.get_team_wins(x)
        team_object = Team(x, result_list)
        circle_list.append(team_object)
        # Team.print_data(x, result_list)
        
    for team in circle_list:
        print(f'''
            {team.getName()},
            {team.getDefeatedTeams()}''')
    i = 0
    while i < 100:
        i = i+1
        for team, next_team in zip(circle_list, circle_list[1:] + [circle_list[0]]):
            result = Team.compare(team, next_team)
            print(result)
            #print(team.name)
           #print(next_team.name)
            
            #Team.print_data(x, result_list)

    print(' ')
    print(' ')
    print(' ')
    print(' ')
    for team in circle_list:
        print(f'''
            {team.getName()},
            {team.getDefeatedTeams()}''')
    
    
    G = nx.Graph()
    G.add_nodes_from(all_teams)
    G.add_edges_from(gameset)
    
     # Perform DFS and obtain topological sort
    topological_sort = result_list(nx.dfs_preorder_nodes(G, source=0))

# Print the topological sort
    print("Topological Sort:")
    print(topological_sort)
    
    # draw the graph
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=500)
    nx.draw_networkx_edges(G, pos, arrowsize=10)
    nx.draw_networkx_labels(G, pos, font_size=10, font_family="sans-serif")
    plt.show()
    
    # Perform DFS and obtain topological sort
    topological_sort = all_teams(nx.dfs_preorder_nodes(G))

# Print the topological sort
    print("Topological Sort:")
    print(topological_sort)
main()
    






#circle_list = TeamList()
#circle_list.save_team(result_list)
#print(all_teams)
#print(result_list)

#circle_list.print_teams()