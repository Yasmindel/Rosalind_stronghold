def calculate_dominant_phenotype_probability(k, m, n):
    """
    This function calculates the probability that two randomly selected mating organisms 
    will produce an individual possessing a dominant allele, given a population with k 
    homozygous dominant, m heterozygous, and n homozygous recessive individuals.

    Args:
    k (int): Number of homozygous dominant individuals.
    m (int): Number of heterozygous individuals.
    n (int): Number of homozygous recessive individuals.

    Returns:
    float: Probability of producing an offspring with a dominant phenotype.
    """
    
    total_population = k + m + n
    total_combinations = total_population * (total_population - 1)
    
    # Calculate probabilities of recessive-recessive, hetero-recessive, and hetero-hetero matings
    recessive_recessive = (n / total_population) * ((n - 1) / (total_population - 1))
    hetero_recessive = 2 * (m / total_population) * (n / (total_population - 1))
    hetero_hetero = (m / total_population) * ((m - 1) / (total_population - 1)) * 0.25
    
    # Calculate probability of not having a dominant phenotype
    no_dominant_phenotype = recessive_recessive + hetero_recessive + hetero_hetero
    
    # Return the complement to get the probability of having a dominant phenotype
    return 1 - no_dominant_phenotype

# Example usage with the sample dataset
k, m, n = 2, 2, 2
print(calculate_dominant_phenotype_probability(k, m, n))
