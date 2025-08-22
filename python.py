import matplotlib.pyplot as plt
import pandas as pd

# Correct file path for Excel
file_path = 'Zr6CoTe2.Im.xlsx'

# Read the Excel file (first sheet assumed)
df = pd.read_excel(file_path)

# Set global font to Times New Roman and size for ticks/legend
plt.rcParams['font.family'] = 'Times New Roman'
plt.rcParams['font.size'] = 20  # for ticks, legend, etc.

# Rename columns if needed
df.columns = ['energy', 'epsr_x', 'epsr_y', 'epsr_z']

# Ensure numeric types
df = df.apply(pd.to_numeric, errors='coerce')
df.dropna(inplace=True)

# Identify plasmonic regions (where Re[ε] < 0)
plasmonic_df = df[(df['epsr_x'] < 0) | (df['epsr_y'] < 0) | (df['epsr_z'] < 0)]

# Plotting
plt.figure(figsize=(6, 6))
plt.plot(df['energy'], df['epsr_x'], label='ε₁(x)', color='blue', linewidth=2.5)
plt.plot(df['energy'], df['epsr_y'], label='ε₁(y)', color='green', linewidth=2.5)
plt.plot(df['energy'], df['epsr_z'], label='ε₁(z)', color='red', linewidth=2.5)

# Add dashed horizontal line at y=0
plt.axhline(y=0, color='black', linestyle='--', linewidth=2)

# Labels and formatting
plt.title('(a) Zr₆CoTe₂', fontsize=32, pad=12)
plt.xlabel('Photon Energy (eV)', fontsize=32, labelpad=12)
plt.ylabel('ε₂(ω)', fontsize=32, labelpad=12)
plt.tick_params(axis='both', which='major', pad=10, labelsize=20)
plt.legend(loc='upper right')
plt.ylim(-10, 110)
plt.xlim(0,8)
plt.tight_layout()

# Save the figure
plt.savefig("Zr6CoTe2.Im.png", dpi=300)
plt.show()
