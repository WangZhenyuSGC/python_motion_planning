"""
@file: global_example.py
@breif: global planner application examples
@author: Winter
@update: 2023.3.2
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../")
from python_motion_planning.utils import Grid, Map, SearchFactory


if __name__ == '__main__':
    '''
    path searcher constructor
    '''
    search_factory = SearchFactory()

    '''
    graph search
    '''
    # build environment
    # start = (5, 5)
    # goal = (45, 5)
    # env = Grid(51, 31)

    field_width = 82
    field_height = 144
    start = (20, 70)
    goal = (20, 20)
    env = Grid(field_width, field_height)

    obstacles = set()
    for i in range(field_width):
        obstacles.add((i, 0))
        obstacles.add((i, field_height - 1))
    for i in range(field_height):
        obstacles.add((0, i))
        obstacles.add((field_width - 1, i))
    for i in range(0, 30):
        obstacles.add((i, 40))
        obstacles.add((field_width - i, 40))
    
    env.update(obstacles)
    # creat planner
    # planner = search_factory("a_star", start=start, goal=goal, env=env)
    # planner = search_factory("dijkstra", start=start, goal=goal, env=env)
    # planner = search_factory("gbfs", start=start, goal=goal, env=env)
    planner = search_factory("theta_star", start=start, goal=goal, env=env)
    # planner = search_factory("lazy_theta_star", start=start, goal=goal, env=env)
    # planner = search_factory("s_theta_star", start=start, goal=goal, env=env)
    # planner = search_factory("jps", start=start, goal=goal, env=env)
    # planner = search_factory("d_star", start=start, goal=goal, env=env)
    # planner = search_factory("lpa_star", start=start, goal=goal, env=env)
    # planner = search_factory("d_star_lite", start=start, goal=goal, env=env)
    # planner = search_factory("voronoi", start=start, goal=goal, env=env, n_knn=4,
    #                             max_edge_len=10.0, inflation_r=1.0)

    # animation
    planner.run()

    # ========================================================

    '''
    sample search
    '''
    # # build environment
    # start = (18, 8)
    # goal = (37, 18)
    # env = Map(51, 31)

    # # creat planner
    # planner = search_factory("rrt", start=start, goal=goal, env=env)
    # planner = search_factory("rrt_connect", start=start, goal=goal, env=env)
    # planner = search_factory("rrt_star", start=start, goal=goal, env=env)
    # planner = search_factory("informed_rrt", start=start, goal=goal, env=env)

    # # animation
    # planner.run()

    # ========================================================

    '''
    evolutionary search
    '''
    # planner = search_factory("aco", start=start, goal=goal, env=env)
    # planner = search_factory("pso", start=start, goal=goal, env=env)
    # planner.run()
