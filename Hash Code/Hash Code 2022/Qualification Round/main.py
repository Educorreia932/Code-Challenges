from __future__ import annotations

from typing import List, Tuple, TextIO
from math import sqrt


class Contributor:
    def __init__(self, name: str, skills: dict):
        self.name = name
        self.skills = skills
        self.projects = dict()

    def upgrade_skill(self, name):
        self.skills[name] += 1

    @staticmethod
    def from_file(file: TextIO) -> Contributor:
        l = file.readline().split()
        name = l[0]
        n_skills = int(l[1])

        skills = dict()

        for _ in range(n_skills):
            l = file.readline().split()
            skills[l[0]] = int(l[1])

        return Contributor(name, skills)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Project:
    def __init__(self, name: str, duration: int, score: int, best_before: int, roles: List[List[str, int, Contributor]]):
        self.name = name
        self.duration = duration
        self.score = score
        self.best_before = best_before
        self.roles = roles
        self.started = -1

    def get_score_at_day(self, day: int):
        return self.score - max(0, day - self.best_before)

    @staticmethod
    def from_file(file: TextIO) -> Project:
        l = file.readline().split()
        name = l[0]
        duration, score, best_before, n_roles = [int(val) for val in l[1:]]

        roles = []

        for _ in range(n_roles):
            l = file.readline().split()
            roles.append([l[0], int(l[1]), None])

        return Project(name, duration, score, best_before, roles)

    def evaluate(self, cur_day: int = 0) -> float:
        return max(0, self.score- (self.best_before - cur_day))

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Problem:
    def __init__(self, contributors: List[Contributor], projects: List[Project]):
        self.contributors = contributors
        self.projects = projects

    @property
    def score(self):
        return sum((project.evaluate() for project in self.projects))


class Solution:
    def __init__(self, problem: Problem):
        self.problem = problem
        current_day = 0

        projects = sorted(problem.projects, key=lambda x: x.evaluate())

        for project in projects:
            for role in project.roles:
                for contributor in self.problem.contributors:
                    role_level = role[1]
                    role_name = role[0]

                    if role[2] == None and project.name not in contributor.projects:
                        collab_level = contributor.skills[role_name] if (role_name in contributor.skills) else 0

                        # No mentoring
                        if collab_level >= role_level:
                            role[2] = contributor
                            contributor.projects[project.name] = role_name

                        # Can find mentor?
                        elif collab_level == role_level - 1:
                            # POSSIBLE HILL CLIMB:
                            # Later we could iterate through all collaborators to check if someone could be reassigned to mentor the project
                            for mentor in project.roles:
                                mentor_level = contributor.skills[role_name] if (role_name in contributor.skills) else 0

                                if mentor_level >= role_level:
                                    role[2] = contributor
                                    contributor.projects[project.name] = role_name
                                    break

                # Guarantee that project is doable, that is, collaborators for each role
                if not any([x[2] == None for x in project.roles]):
                    project.started = current_day

                    # Upgrade skills when possible
                    for role in project.roles:
                        if (role[2].skills[role[0]] <= role[1]):
                            role[2].upgrade_skill(role[0])

            current_day += project.duration

    def __str__(self):
        projects = list(filter(lambda x: x.started != -1, sorted(self.problem.projects, key=lambda x: x.started)))
        result = f"{len(projects)}\n"

        for project in projects:
            result += f"{project}\n"
            result += f"{' '.join(str(x[2]) for x in project.roles)}\n"

        return result


def read_input(filename: str) -> Problem:
    with open(filename) as input_file:
        line = input_file.readline()
        number_contributors, number_projects = [int(x) for x in line.split()]
        contributors = list()
        projects = list()

        for _ in range(number_contributors):
            contributors.append(Contributor.from_file(input_file))

        for _ in range(number_projects):
            projects.append(Project.from_file(input_file))

        problem = Problem(contributors, projects)

        return problem


def main():
    datasets = [
        "a_an_example",
        "b_better_start_small",
        "c_collaboration",
        "d_dense_schedule",
        "e_exceptional_skills",
        "f_find_great_mentors"
    ]

    for dataset in datasets[:3]:
        problem = read_input(f"datasets/{dataset}.in")
        solution = Solution(problem)

        out_file = open(f"{dataset}.out", "w")

        out_file.write(str(solution))


if __name__ == "__main__":
    main()
