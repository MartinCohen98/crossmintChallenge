from src.models.map import Map
from src.services.crossmintChallengeService import CrossmintChallengeService


def main():

    solutionMap = Map(CrossmintChallengeService())

    solutionMap.sendAstralObjects()


if __name__ == "__main__":
    main()