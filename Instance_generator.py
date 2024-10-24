#!/usr/bin/python
# -*- coding: latin-1 -*-
import numpy as np
import pandas as pd
import random


# Function to generate box distribution with additional box data
def generate_distribution(file_name, N, sheet_name, sort_articles=False, rand_art=False):
    # Read data (including box details such as weight, dimensions, etc.)
    df = pd.read_excel(file_name, sheet_name=sheet_name)
    quantities = [int(i) for i in df['Quantity']]
    articles = [int(i) for i in df["Box"]]
    all_box_data = pd.read_excel(file_name, sheet_name="Boxes")
    instance_name = "Orig"
    if sort_articles:
        articles = list(sorted(random.sample(range(len(all_box_data)), len(quantities))))
        instance_name = "Dist"
        if rand_art:
            articles = list(random.sample(range(len(all_box_data)), len(quantities)))
            instance_name = "Rand"
        df = all_box_data[all_box_data["Box"].isin(articles)]

    cumulative_dist = np.cumsum(quantities) / sum(quantities)
    new_dist = [[] for _ in range(len(quantities))]

    # Generate random values for the new distribution
    for _ in range(N):
        rand_val = random.random()
        for j, dist in enumerate(cumulative_dist):
            if rand_val <= dist:
                new_dist[j].append(1)
                break

    new_distribution = [sum(d) for d in new_dist]
    final_distribution = [i if i > 0 else 1 for i in new_distribution]

    # Include additional box data in the output: (Box, Weight, Length, Width, Height, Compression, Final Quantity)
    result = [
        ["Box", "Weight", "Length", "Width", "Height", "Compression", "Quantity"],
        articles,
        list(df['Weight']),
        list(df['Length']),
        list(df['Width']),
        list(df['Height']),
        list(df['Compression']),
        final_distribution,
        instance_name
    ]
    return result


# Function to create multiple instances of the problem with different box setups
def create_instances(file_name, n_min_box, n_max_box, box_step):
    instances = []
    for j in range(5):
        df_name = f"Instance{j+1}"
        for i in range(n_min_box, n_max_box, box_step):
            N = i + (-1) ** random.randint(1, 2) * random.randint(0, i // 10)
            instances.append(generate_distribution(file_name, N, df_name))  # Original
        for i in range(n_min_box, n_max_box, box_step):
            N = i + (-1) ** random.randint(1, 2) * random.randint(0, i // 10)
            instances.append(generate_distribution(file_name, N, df_name, True))  # Sorted
        for i in range(n_min_box, n_max_box, box_step):
            N = i + (-1) ** random.randint(1, 2) * random.randint(0, i // 10)
            instances.append(generate_distribution(file_name, N, df_name, True, True))  # Random
    return instances


# Function to save instances with box data to Excel
def create_and_save_to_excel(new_file_name, original_file_name, n_min_box, n_max_box, box_step):
    writer = pd.ExcelWriter(new_file_name, engine='openpyxl', mode='w')
    instances = create_instances(original_file_name, n_min_box, n_max_box, box_step)
    print("Generated instances count: ", len(instances))
    for i, inst in enumerate(instances):
        header = inst[0]
        columns = inst[1:-1]
        # Transpose the columns to match the format expected by pandas DataFrame
        transposed_data = list(map(list, zip(*columns)))
        # Create a DataFrame
        df = pd.DataFrame(transposed_data, columns=header)
        # Save to Excel
        sheet_name = f'Instance{i+1}.{inst[-1]}'
        df.to_excel(writer, sheet_name=sheet_name, index=False)
    writer._save()

# Parameters
n_min_box = 100
n_max_box = 500
box_step = 50

# Generate and save results
create_and_save_to_excel("New_instances.xlsx",'Original_dataset.xlsx', n_min_box, n_max_box, box_step)
