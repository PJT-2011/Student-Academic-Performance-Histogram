import pandas as pd
import matplotlib.pyplot as plt

def create_histogram():
    # 1. Load the dataset
    file_name = 'student_performance.csv'
    
    try:
        df = pd.read_csv(file_name)
        
        # 2. Define the column you want to plot
        # CHANGE 'math_score' TO YOUR ACTUAL COLUMN NAME (e.g., 'Grade', 'Score')
        column_to_plot = 'final_score'
        
        if column_to_plot in df.columns:
            # 3. Create the histogram
            plt.figure(figsize=(10, 6))
            plt.hist(df[column_to_plot].dropna(), bins=15, color='skyblue', edgecolor='black')
            
            # Add clear labels and title
            plt.title(f'Histogram of {column_to_plot}')
            plt.xlabel('Scores')
            plt.ylabel('Frequency')
            plt.grid(axis='y', alpha=0.75)
            
            # 4. Save the output as an image file
            output_filename = 'histogram_output.png'
            plt.savefig(output_filename)
            print(f"Success! Histogram saved to your folder as '{output_filename}'")
            
            # 5. Display the plot
            plt.show()
            
        else:
            print(f"Error: Column '{column_to_plot}' not found in the dataset.")
            print("Available columns are:", df.columns.tolist())
            
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found in the current directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    create_histogram()