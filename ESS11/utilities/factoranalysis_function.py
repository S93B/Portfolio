from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
import numpy as np
import pandas as pd

def factor_analysis(data, n_factors):
    # Check Data Suitability
    df_numeric = data.select_dtypes(include=[np.number])

    # Check KMO Measure
    kmo_all, kmo_model = calculate_kmo(df_numeric)
    print(f"KMO Measure: {kmo_model} (> 0.6 is acceptable")

    # Perform Bartlett’s Test of Sphericity
    chi_square_value, p_value = calculate_bartlett_sphericity(df_numeric)
    print(f"Bartlett’s test: chi_square({chi_square_value}), p_value({p_value})")

    # Perform Factor Analysis
    fa = FactorAnalyzer(n_factors=n_factors, rotation='varimax')
    fa.fit(df_numeric)

    # Extract and print factors
    loadings = fa.loadings_
    loadings_df = pd.DataFrame(loadings, index=df_numeric.columns, columns=['Factor 1', 'Factor 2', 'Factor 3'])
    print("Factor Loadings:\n", loadings_df)

    # Plot the scree plot
    import matplotlib.pyplot as plt

    ev, v = fa.get_eigenvalues()
    plt.scatter(range(1, df_numeric.shape[1] + 1), ev)
    plt.plot(range(1, df_numeric.shape[1] + 1), ev)
    plt.title('Scree Plot')
    plt.xlabel('Factors')
    plt.ylabel('Eigenvalue')
    plt.grid()
    plt.show()