import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

# Create output directory for graphs if it doesn't exist
if not os.path.exists('graphs'):
    os.makedirs('graphs')

# Sample data - replace with your actual data loading logic
def load_data(condition, protocol):
    """
    Load experimental data for a given network condition and protocol.
    In a real implementation, this would read from your log files.
    
    Args:
        condition: 'high-bandwidth' or 'low-bandwidth'
        protocol: 'cubic', 'bbr', or 'sprout'
    
    Returns:
        DataFrame with columns: time, throughput, rtt, loss
    """
    # This is placeholder data - replace with your actual data loading code
    # For example:
    # return pd.read_csv(f'data/{condition}_{protocol}.csv')
    
    # Generate sample data for demonstration
    np.random.seed(hash(f"{condition}_{protocol}") % 10000)
    
    time = np.arange(0, 60, 0.1)
    n = len(time)
    
    # Different behavior based on protocol and condition
    if protocol == 'cubic':
        base_throughput = 8.5 if condition == 'high-bandwidth' else 0.8
        throughput = base_throughput + np.sin(time/5) * 1.5 + np.random.normal(0, 0.5, n)
        rtt = 80 + np.random.normal(0, 10, n) if condition == 'high-bandwidth' else 220 + np.random.normal(0, 15, n)
        loss = 0.01 + 0.03 * np.abs(np.sin(time/10)) + np.random.normal(0, 0.005, n)
    
    elif protocol == 'bbr':
        base_throughput = 9.2 if condition == 'high-bandwidth' else 0.9
        throughput = base_throughput + np.sin(time/8) * 1.0 + np.random.normal(0, 0.3, n)
        rtt = 100 + np.random.normal(0, 8, n) if condition == 'high-bandwidth' else 240 + np.random.normal(0, 12, n)
        loss = 0.005 + 0.01 * np.abs(np.sin(time/12)) + np.random.normal(0, 0.002, n)
    
    else:  # sprout
        base_throughput = 6.0 if condition == 'high-bandwidth' else 0.6
        throughput = base_throughput + np.sin(time/6) * 2.0 + np.random.normal(0, 0.8, n)
        rtt = 120 + np.random.normal(0, 15, n) if condition == 'high-bandwidth' else 260 + np.random.normal(0, 20, n)
        loss = 0.03 + 0.04 * np.abs(np.sin(time/8)) + np.random.normal(0, 0.01, n)
    
    # Ensure non-negative values
    throughput = np.maximum(throughput, 0)
    rtt = np.maximum(rtt, 0)
    loss = np.maximum(loss, 0)
    
    return pd.DataFrame({
        'time': time,
        'throughput': throughput,
        'rtt': rtt,
        'loss': loss * 100  # Convert to percentage
    })

# Generate Figure 1 & 2: Time-series throughput plots
def generate_throughput_plots():
    """Generate throughput over time plots for both network conditions"""
    
    for condition in ['high-bandwidth', 'low-bandwidth']:
        plt.figure(figsize=(10, 6))
        
        for protocol, color in zip(['cubic', 'bbr', 'sprout'], ['blue', 'red', 'green']):
            data = load_data(condition, protocol)
            plt.plot(data['time'], data['throughput'], label=protocol.upper(), color=color)
        
        plt.title(f'Throughput Over Time ({condition.replace("-", " ").title()} Condition)')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Throughput (Mbps)')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        
        # Save the figure
        plt.savefig(f'graphs/throughput_{condition}.png', dpi=300)
        plt.close()
        
        print(f"Generated throughput plot for {condition}")

# Generate Figure 3 & 4: Time-series loss plots
def generate_loss_plots():
    """Generate loss over time plots for both network conditions"""
    
    for condition in ['high-bandwidth', 'low-bandwidth']:
        plt.figure(figsize=(10, 6))
        
        for protocol, color in zip(['cubic', 'bbr', 'sprout'], ['blue', 'red', 'green']):
            data = load_data(condition, protocol)
            plt.plot(data['time'], data['loss'], label=protocol.upper(), color=color)
        
        plt.title(f'Packet Loss Over Time ({condition.replace("-", " ").title()} Condition)')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Loss Rate (%)')
        plt.grid(True, alpha=0.3)
        plt.legend()
        plt.tight_layout()
        
        # Save the figure
        plt.savefig(f'graphs/loss_{condition}.png', dpi=300)
        plt.close()
        
        print(f"Generated loss plot for {condition}")

# Generate Figure 5: RTT comparison (average and 95th percentile)
def generate_rtt_comparison():
    """Generate bar chart of average and 95th percentile RTT"""
    
    # Collect RTT statistics
    stats = []
    
    for condition in ['high-bandwidth', 'low-bandwidth']:
        for protocol in ['cubic', 'bbr', 'sprout']:
            data = load_data(condition, protocol)
            avg_rtt = data['rtt'].mean()
            percentile_95_rtt = np.percentile(data['rtt'], 95)
            
            stats.append({
                'condition': condition.replace('-bandwidth', '').title(),
                'protocol': protocol.upper(),
                'avg_rtt': avg_rtt,
                'percentile_95_rtt': percentile_95_rtt
            })
    
    # Convert to DataFrame for easier plotting
    stats_df = pd.DataFrame(stats)
    
    # Setup plot
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Set position of bars on X axis
    protocols = ['CUBIC', 'BBR', 'SPROUT']
    conditions = ['High', 'Low']
    bar_width = 0.2
    index = np.arange(len(protocols))
    
    # Plot bars
    for i, condition in enumerate(conditions):
        avg_rtts = stats_df[stats_df['condition'] == condition]['avg_rtt']
        p95_rtts = stats_df[stats_df['condition'] == condition]['percentile_95_rtt']
        
        pos1 = index + i*2*bar_width - 1.5*bar_width
        pos2 = index + i*2*bar_width - 0.5*bar_width
        
        ax.bar(pos1, avg_rtts, bar_width, label=f'{condition} BW - Avg RTT', 
               alpha=0.7, color=['blue', 'red', 'green'][i % 3])
        ax.bar(pos2, p95_rtts, bar_width, label=f'{condition} BW - 95th% RTT',
               alpha=0.9, color=['blue', 'red', 'green'][i % 3], hatch='//')
    
    # Add labels and legend
    ax.set_xlabel('Protocol')
    ax.set_ylabel('RTT (ms)')
    ax.set_title('RTT Comparison: Average vs 95th Percentile')
    ax.set_xticks(index)
    ax.set_xticklabels(protocols)
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('graphs/rtt_comparison.png', dpi=300)
    plt.close()
    
    print("Generated RTT comparison plot")

# Generate Figure 6: Comparative performance analysis
def generate_performance_comparison():
    """Generate graph with RTT on x-axis and throughput on y-axis"""
    
    # Collect average performance stats
    performance = []
    
    for protocol in ['cubic', 'bbr', 'sprout']:
        # Use high-bandwidth condition for comparison
        data = load_data('high-bandwidth', protocol)
        avg_throughput = data['throughput'].mean()
        avg_rtt = data['rtt'].mean()
        
        performance.append({
            'protocol': protocol.upper(),
            'throughput': avg_throughput,
            'rtt': avg_rtt
        })
    
    # Convert to DataFrame
    perf_df = pd.DataFrame(performance)
    
    # Create plot
    plt.figure(figsize=(8, 8))
    
    # Note: For this plot, higher RTT should be closer to origin
    # So we use negative RTT values for plotting
    for i, row in perf_df.iterrows():
        plt.scatter(-row['rtt'], row['throughput'], s=100, 
                   color=['blue', 'red', 'green'][i])
        plt.annotate(row['protocol'], (-row['rtt'], row['throughput']), 
                    xytext=(10, 5), textcoords='offset points', fontsize=12)
    
    # Add labels and guidelines
    plt.axhline(y=perf_df['throughput'].mean(), color='gray', linestyle='--', alpha=0.3)
    plt.axvline(x=-perf_df['rtt'].mean(), color='gray', linestyle='--', alpha=0.3)
    
    plt.title('Protocol Performance Comparison')
    plt.xlabel('RTT (ms) - Lower is better →')
    plt.ylabel('Throughput (Mbps)')
    plt.xlim(-max(perf_df['rtt'])*1.2, -min(perf_df['rtt'])*0.8)
    plt.ylim(min(perf_df['throughput'])*0.8, max(perf_df['throughput'])*1.2)
    
    # Invert x-axis to show higher RTT closer to origin
    plt.gca().invert_xaxis()
    
    # Add grid
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    
    plt.savefig('graphs/performance_comparison.png', dpi=300)
    plt.close()
    
    print("Generated performance comparison plot")

# Generate all plots
if __name__ == "__main__":
    print("Generating all plots for Pantheon analysis...")
    
    generate_throughput_plots()
    generate_loss_plots()
    generate_rtt_comparison()
    generate_performance_comparison()
    
    print("All plots generated successfully!")