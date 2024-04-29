import scipy.stats as stats
import plotly.graph_objects as go
import numpy as np

### Citations ###
# https://docs.scipy.org/doc/scipy/reference/stats.html
# https://www.techladder.in/article/pmf-pdf-and-cdf-and-its-implementation-python
# https://www.geeksforgeeks.org/args-kwargs-python/ 

def distribution_type():
    """
    This function asks starts off application by asking the user to enter the general type of distribution they would like to calculate: Continuous or Discrete.
    """
    while True:
        gen_distribution = input("Enter the general type of distribution you want: C - Continuous; D - Discrete: ").upper()
        if gen_distribution == "C":
            return "continuous"
        elif gen_distribution == "D":
            return "discrete"
        else:
            print("Your input is invalid. Please enter 'C' for continuous or 'D' for Discrete")

def continuous_dist():
    """
    This function is conditional if the user chooses they want to use a continuous distribution. It displays the options of continuous distributions that they can choose from and prompts them to select a specific distribution.
    """
    distributions_c = {
        1: "Beta",
        2: "Gamma",
        3: "Exponential",
        4: "Normal"
    }
    print("Please choose a continuous distribution:")
    
    for num, dist in distributions_c.items():
        print(f"{num}. {dist}")
    choice_c = int(input("Please enter the number corresponding to your distribution choice: "))
    return choice_c

def discrete_dist():
    """
    This function is conditional if the user chooses they want to use a discrete distribution. It displays the options of discrete distributions that they can choose from and prompts them to select a specific distribution.
    """
    distributions_d = {
        1: "Binomial",
        2: "Geometric",
        3: "Hypergeometric",
        4: "Poisson"
    }
    print("Please choose a discrete distribution:")
    
    for num, dist in distributions_d.items():
        print(f"{num}. {dist}")
    choice_d = int(input("Please enter the number corresponding to your distribution choice: "))
    return choice_d

def dist_parameters(distribution_type):
    """
    This function is based upon the selection made from the previous functions. Depending on the probability distribution selected, the user then inputs the x-value (the value they want to obtain information about), alongside the parameters for the distribution.
    """
    x = float(input("Please enter the value of x: "))

    if distribution_type == 'continuous':
        user_choice = continuous_dist()

        if user_choice == 1: #Beta
            alpha = float(input("Please enter the alpha parameter: "))
            beta = float(input("Please enter the beta parameter: "))
            return x, user_choice, alpha, beta
        elif user_choice == 2: #Gamma
            shape = float(input("Please enter the shape parameter: "))
            scale = float(input("Please enter the scale parameter: "))
            return x, user_choice, shape, scale
        elif user_choice == 3: #Exponential
            lambda_1 = float(input("Please enter the lambda parameter: "))
            return x, user_choice, lambda_1
        elif user_choice == 4: #Normal
            mean = float(input("Please enter the mean parameter: "))
            std_dev = float(input("Please enter the standard deviation parameter: "))
            return x, user_choice, mean, std_dev
        
    elif distribution_type == 'discrete':
        user_choice = discrete_dist()

        if user_choice == 1: #Binomial
            n = int(input("Please enter the number of trials (n): "))
            p = float(input("Please enter the probability of success for each trial: "))
            return x, user_choice, n, p
        elif user_choice == 2: #Geometric
            p = float(input("Please enter the probability of success for each trial: "))
            return x, user_choice, p
        elif user_choice == 3: #Hypergeometric
            cap_n = int(input("Please enter the population size (N): "))
            r = int(input("Please enter the number in the population with given characteristic (r): "))
            n = int(input("Please enter the sample size (n): "))
            return x, user_choice, cap_n, r, n
        elif user_choice == 4: #Poisson
            lambda_2 = float(input("Please enter the lambda parameter: "))
            return x, user_choice, lambda_2


def calculate_prob(distribution_type, choice, x, *parameters): 
    """
    This function conducts the calculation based on the selected distributions and its relevant parameters from the functions above. It then outputs the relevant information regarding the x-value inputted.

    For example: If the user selected a discrete binomial distribution and wanted to see what the probability of them making in 5 (x-value) basketball free throws from 8 (n) attempts, with the probability any free throw going in at 0.75. The output would tell you that the probability of making in exactly 5 shots is 0.2076, less than 5 shots is 0.1138, and more than 5 shots is 0.6785

    Note: Continuous distributions don't have an P(X = x) as there is no significance in this value.
    """
    
    results = {}

    if distribution_type == 'continuous':
        
        if choice == 1: #Beta
            alpha, beta = parameters
            results['P(X < x)'] = stats.beta.cdf(x, alpha, beta)
            results['P(X > x)'] = 1 - stats.beta.cdf(x, alpha, beta)
        elif choice == 2: #Gamma
            shape, scale = parameters
            results['P(X < x)'] = stats.gamma.cdf(x, shape, scale)
            results['P(X > x)'] = 1 - stats.gamma.cdf(x, shape, scale)
        elif choice == 3: #Exponential
            lambda_1, = parameters
            results['P(X < x)'] = stats.expon.cdf(x, lambda_1)
            results['P(X > x)'] = 1 - stats.expon.cdf(x, lambda_1)
        elif choice == 4: #Normal
            mean, std_dev = parameters
            results['P(X < x)'] = stats.norm.cdf(x, mean, std_dev)
            results['P(X > x)'] = 1 - stats.norm.cdf(x, mean, std_dev)

    elif distribution_type == 'discrete':
        
        if choice == 1: #Binomial
            n, p = parameters
            results['P(X = x)'] = stats.binom.pmf(x, n, p)
            results['P(X > x)'] = 1 - stats.binom.cdf(x, n, p)
            results['P(X < x)'] = stats.binom.cdf(x - 1, n, p)
        elif choice == 2: #Geometric
            p, = parameters
            results['P(X = x)'] = stats.geom.pmf(x, p)
            results['P(X > x)'] = 1 - stats.geom.cdf(x, p)
            results['P(X < x)'] = stats.geom.cdf(x - 1, p)
        elif choice == 3: #Hypergeometric
            cap_n, r, n = parameters
            results['P(X = x)'] = stats.hypergeom.pmf(x, cap_n, r, n)
            results['P(X > x)'] = 1 - stats.hypergeom.cdf(x, cap_n, r, n)
            results['P(X < x)'] = stats.hypergeom.cdf(x - 1, cap_n, r, n)
        elif choice == 4: #Poisson
            lambda_2, = parameters
            results['P(X = x)'] = stats.poisson.pmf(x, lambda_2)
            results['P(X > x)'] = 1 - stats.poisson.cdf(x, lambda_2)
            results['P(X < x)'] = stats.poisson.cdf(x - 1, lambda_2)
    return results

def main():
    """
    Main Function
    """
    dist = distribution_type()
    x, choice, *parameters = dist_parameters(dist)
    probabilities = calculate_prob(dist, choice, x, *parameters)
    for prob_type, value in probabilities.items():
        print(f"{prob_type}: {value:.4f}")
    
if __name__ == "__main__":
    main()
