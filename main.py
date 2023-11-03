from src.services.crossmintChallengeService import CrossmintChallengeService
from src.models.map import Map

def main():

    solutionMap = Map(CrossmintChallengeService().getSolution())

    solutionMap.sendPolyanets()

if __name__ == "__main__":
    main()