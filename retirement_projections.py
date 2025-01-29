#retirement_projections.py
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def monte_carlo_simulation(initial_balance, monthly_contribution, years, risk_profile):
    """Run Monte Carlo simulation for retirement projections"""
    n_simulations = 1000
    n_months = years * 12
    
    # Get portfolio metrics based on risk profile
    metrics = calculate_portfolio_metrics(risk_profile)
    monthly_return = metrics["expected_return"] / 12
    monthly_vol = metrics["volatility"] / np.sqrt(12)
    
    simulations = np.zeros((n_simulations, n_months))
    
    for sim in range(n_simulations):
        balance = initial_balance
        for month in range(n_months):
            # Generate random monthly return
            return_multiplier = np.random.normal(monthly_return, monthly_vol)
            balance = balance * (1 + return_multiplier) + monthly_contribution
            simulations[sim, month] = balance
    
    return {
        "median": np.percentile(simulations, 50, axis=0),
        "upper": np.percentile(simulations, 75, axis=0),
        "lower": np.percentile(simulations, 25, axis=0),
        "worst_case": np.percentile(simulations, 5, axis=0),
        "best_case": np.percentile(simulations, 95, axis=0)
    }

def create_projection_chart(simulation_results, years):
    """Create an interactive projection chart using plotly"""
    months = range(years * 12)
    
    fig = go.Figure()
    
    # Add projection lines
    fig.add_trace(go.Scatter(
        x=months, y=simulation_results["median"],
        name="Median Projection",
        line=dict(color="blue", width=2)
    ))
    
    # Add confidence intervals
    fig.add_trace(go.Scatter(
        x=months, y=simulation_results["upper"],
        name="75th Percentile",
        line=dict(color="lightblue", width=1)
    ))
    
    fig.add_trace(go.Scatter(
        x=months, y=simulation_results["lower"],
        name="25th Percentile",
        line=dict(color="lightblue", width=1),
        fill="tonexty"
    ))
    
    fig.update_layout(
        title="Retirement Portfolio Projection",
        xaxis_title="Months",
        yaxis_title="Portfolio Value ($)",
        showlegend=True
    )
    
    return fig
