import scipy.stats as stats

def distribution_type():
    while True:
        gen_distribution = input(f"Enter the general type of distribution you want: C - Continous; D - Discrete").upper()
        if gen_distribution == "C":
            return "continuous"
        elif gen_distribution == "D":
            return "discrete"
        else:
            print("Your input is invalid. Please enter 'C' for continuous or 'D' for Discrete")


